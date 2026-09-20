import wave, struct, math, os, json, shutil

SR=44100
PICK = {
 # voice          source file                        role gain  max dur
 'bass':        ('wav3/pp_bass.wav',                 1.00, 0.85),
 'tone_1':      ('wav2/inf_djembe_hit4_wav.wav',     0.72, 0.55),
 'tone_2':      ('wav2/inf_djembe_hit6_rim_wav.wav', 0.72, 0.55),
 'tone_3':      ('wav2/inf_djembe_hit9_rim_wav.wav', 0.72, 0.55),
 'tone_4':      ('wav2/inf_djembe_hit11_wav.wav',    0.72, 0.55),
 'slap':        ('wav3/cc_slap.wav',                 0.80, 0.45),
 'sangban_O':   ('wav/sangban_open.wav',             0.92, 1.30),
 'sangban_M':   ('wav/sangban_mute.wav',             0.78, 0.40),
 'kenkeni_T':   ('wav/kenkeni.wav',                  0.72, 0.80),
 'doundounba_T':('wav/doundounba.wav',               1.00, 1.40),
 'bell':        ('wav/bell_agogo1.wav',              0.42, 0.55),
}

def load(p):
    w=wave.open(p); n=w.getnframes(); d=w.readframes(n); sr=w.getframerate(); w.close()
    s=[v/32768.0 for v in struct.unpack('<%dh'%(len(d)//2), d)]
    return s, sr

def process(s, sr, gain, maxdur):
    # DC removal
    m=sum(s)/len(s); s=[v-m for v in s]
    peak=max(abs(v) for v in s) or 1e-9
    # trim to 3 ms before the attack
    start=next((i for i,v in enumerate(s) if abs(v)>peak*0.04), 0)
    start=max(0, start-int(sr*0.003))
    s=s[start:]
    # cap the length, fade the tail so nothing clicks
    n=min(len(s), int(sr*maxdur)); s=s[:n]
    fade=min(int(sr*0.03), n//4)
    for i in range(fade): s[n-fade+i]*= (fade-i)/fade
    for i in range(min(32,n)): s[i]*= i/32          # kill any pre-attack step
    peak=max(abs(v) for v in s) or 1e-9
    k=gain/peak
    return [max(-1,min(1,v*k)) for v in s]

os.makedirs('pack', exist_ok=True)
man={}
for name,(src,gain,maxdur) in PICK.items():
    s,sr=load(src)
    assert sr==SR, (src,sr)
    o=process(s,sr,gain,maxdur)
    out=os.path.join('pack', name+'.wav')
    with wave.open(out,'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(b''.join(struct.pack('<h', int(v*32767)) for v in o))
    man[name]=dict(src=src, dur=round(len(o)/SR,3), bytes=os.path.getsize(out))
    print(f"  {name:14s} {len(o)/SR:5.2f}s  {os.path.getsize(out)/1024:6.1f} kB   <- {os.path.basename(src)}")
json.dump(man, open('pack/manifest.json','w'), indent=1)
print('\ntotal', sum(v['bytes'] for v in man.values())/1024, 'kB')
