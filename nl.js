/* Dutch text for dundun-trainer.html.

   The English stays in the page itself; this file only overlays it. Keys follow
   the page: `ui` matches the data-i18n attributes in the markup plus the labels
   the script builds, `rhythms` follows RHYTHMS (ladder steps in the same order,
   parts by key). Anything missing here falls back to English, and the browser
   console names what is missing.

   Terms used throughout, so they stay consistent:
     tone toon · slap slap · bass bas · open/closed/muted open/dicht/gedempt
     bell bel · drum trom · call signaal · part partij · beat tel · bar maat
     slot vakje · cycle cyclus · straight eighths rechte achtsten
     both hands together samen (SAMEN in the spoken composites)
     count 1 e en a, and 1 la li in 12/8 · galop stays galop               */

window.NL_TEXT = {
  ui: {
    play: "Speel", stop: "Stop",
    callBtn: "Speel het signaal", clickBtn: "Metronoom", handsBtn: "Handen", tempo: "Tempo",
    bar: "maat", beat: "tel", barWord: "maat", beatWord: "tel", and: "en",
    countHands: "tel / handen", useCall: "via „speel het signaal”",
    begins: "begint", ends: "eindigt",
    drum: "TROM", bell: "BEL", playLane: "SPEEL", solo: "SOLO",
    drumLabel: "Trom", bellLabel: "Bel", playLabel: "Speel", soloLabel: "Solo",
    beginTitle: "hier begint de eigen cyclus van deze partij",
    eindeTitle: "Einde — het stuk eindigt op deze slag",
    loadOnPlay: "geluid laadt bij afspelen", real: "echte instrumenten",
    partial: "{ok}/{total} opgenomen", synth: "gesynthetiseerd",
    chooseRhythm: "Kies een ritme", language: "Taal",
    partsNote: "Het kleine label onder de naam van elke partij zegt hoe lang de herhaling is. Kortere partijen herhalen zich binnen de cyclus, zodat het rooster de langste partij precies één keer laat zien.",

    lgBass: "bas", lgTone: "toon", lgSlap: "slap", lgOpen: "open dundun-toon",
    lgMuted: "gedempte dundun-toon", lgBell: "bel", lgBoth: "beide handen tegelijk",
    lgEnd: "waar het stuk eindigt", lgHand: "welke hand — alleen bij de djembé-partijen",

    h2Ladder: "De dunduns leren, de makkelijkste eerst",
    h2Drill: "Zo oefen je het",
    h2Parts: "Hoe elke partij in elkaar zit",
    drillIntro: "De valkuil is om vanaf het begin beide handen tegelijk te oefenen en te hopen dat ze vanzelf loskomen. Dat gebeurt niet — je houdt twee half geleerde partijen over. De bel moet <b>eerst</b> automatisch gaan, want tijdens het spelen is dat de partij die nooit stopt.",
    drillSteps: `
  <li><b>Alleen de bel, tot het saai wordt.</b> Zet hierboven de trom uit en speel alleen de bel,
  minutenlang, tot je er een gesprek overheen kunt voeren.</li>
  <li><b>Zing de trompartij erover.</b> Blijf de bel spelen en <b>zeg</b> alleen de tromslagen hardop.
  Zo leer je hoe de twee lijnen samenhangen, zonder dat je handen iets nieuws hoeven te doen.</li>
  <li><b>Voeg de tromhand eerst alleen toe waar ze samenvallen.</b> Elke kolom met een okergele streep
  eronder is een slag waarbij beide handen tegelijk bewegen. Twee handen die als één bewegen is nog geen
  onafhankelijkheid, en het is veel makkelijker dan het lijkt.</li>
  <li><b>Vul de rest in.</b> Wat overblijft is alleen bel — dat hoort dus bij de belhand, en die heb je
  in stap 1 al automatisch gemaakt.</li>
  <li><b>Zet het tempo veel lager dan nodig lijkt.</b> Schuif naar 40–55. Coördinatie leer je op de
  snelheid waarop je elke slag bewust kunt plaatsen; de snelheid komt vanzelf.</li>
  <li><b>Oefen ook zonder trom.</b> Belhand op de ene knie, tromhand op de andere. Het meeste hiervan
  zit in je hoofd, niet in je handen.</li>
`,
    drillHands: "De meeste spelers geven de bel aan de zwakkere hand en de stok aan de sterkere, omdat de tromslagen de dynamiek dragen — maar doe wat je docent doet, want later omschakelen is echt vervelend.",
    footer: `Ritmes onderwezen en genoteerd door <a href="https://agbodo.nl" style="color:var(--accent)">Michael Agbodo</a>;
traditioneel West-Afrikaans repertoire, overgenomen uit zijn partituren — zes of zeven notenbalken per ritme, op een raster van zestienden
(de 12/8-ritmes — Gidamba, Sorsornet, Garangedon — op een raster van drieën). De handzetting volgt de positie: elk even vakje is de rechterhand,
elk oneven vakje de linker, zoals de bladen het boven de djembé-balken afdrukken. De geluiden zijn opnames van echte instrumenten van Freesound,
bijgesneden en op gelijk volume gebracht; de drie dunduns komen uit één opnamesessie, de djembéslagen van drie verschillende trommen.
Grotendeels CC0 — djembé-slapsample door klemmy via Freesound, CC&nbsp;BY&nbsp;3.0.`,
  },

  // row labels inside the pattern lines; "bel" is padded to keep the columns aligned with "trom"
  pat: { drum: "trom", bell: "bel&nbsp;", bar: "maat" },

  names: { "Signal": "Signaal", "Entrance": "Inzet" },
  subs: {
    "call": "oproep", "one beat": "één tel", "two beats": "twee tellen", "half bar": "halve maat",
    "one bar": "één maat", "two bars": "twee maten", "four bars": "vier maten", "entry, bar 1": "inzet, maat 1",
  },

  // the call the Djolé family shares
  call: { blurb: "Het signaal. Tonen in de eerste helft, dan drie slaps om de break aan te kondigen. Elke maat begint met een <b>galop</b> — een voorslag vlak voor tel 1 en de toon op de tel, heel snel gespeeld, links en dan rechts." },

  rhythms: {
    djole: {
      origin: "Guinee · 4/4 · cyclus van twee maten",
      standfirst: "Elke partij van het blad op een raster van zestienden. De dundun-partijen zijn gesplitst in twee banen — <b>trom</b> en <b>bel</b> — zodat je één hand kunt uitzetten en de andere tegen het hele ensemble kunt oefenen. De okergele streep markeert de kolommen waar <b>beide handen tegelijk slaan</b>; dat zijn de ankerpunten waar je de partij omheen bouwt.",
      parts: {
        djembe1: { blurb: "Een bas op elke kwart, dan een paar op de <b>en</b> en de <b>a</b>: tonen op tel 1 en 3, slaps op tel 2 en 4. Die afwisseling is de hele partij." },
        djembe2: { blurb: "De enige partij die echt beide maten nodig heeft. Maat 1 begint met een <b>bas</b> en eindigt met vier tonen achter elkaar; maat 2 begint met een <b>toon</b> en eindigt met één." },
        sangban: { blurb: "Open toon op 1, <b>gedempte</b> toon op 2. De bel speelt rechte achtsten, dus de trom valt op elke tweede belslag." },
        kenkeni: { blurb: "Trom en bel <b>precies samen</b>, en niets op de tel zelf — het paar zit op de <b>en</b> en de <b>a</b>. De makkelijkste plek om te beginnen." },
        doundounba: { blurb: "Eén diepe open toon per halve maat. De bel doet al het andere alleen — en dat maakt dit de moeilijkste van de drie." },
      },
      ladder: [
        { tag: "geen onafhankelijkheid nodig", body: "Trom en bel spelen <b>precies samen</b> — elke slag, beide handen, altijd. Het enige lastige is de plaatsing: niets valt op de tel.",
          say: ["tel mee", "rust, rust, <b>samen</b>, <b>samen</b>"] },
        { tag: "twee belslagen per tromslag", body: "De bel speelt rechte achtsten en de trom valt op <b>elke tweede</b>. De tromhand slaat nooit alleen. Voeg het <b>dempen</b> als laatste toe — tel 1 klinkt door, tel 2 is gedempt.",
          say: ["zeg het hardop", "<b>SAMEN</b> &nbsp; bel &nbsp; <b>SAMEN</b> &nbsp; bel"] },
        { tag: "de echt moeilijke", body: "De bel speelt een gesyncopeerde figuur van vijf slagen, de trom speelt <b>één keer</b> per halve maat. Vier van de vijf belslagen zijn alleen bel.",
          say: ["zeg het hardop", "<b>SAMEN</b> &nbsp; – &nbsp; ka &nbsp; ka &nbsp; – &nbsp; ka &nbsp; ka &nbsp; –"] },
      ],
      note: "De drie dundun-partijen zijn niet even moeilijk, en het blad laat zien waarom: het hangt af van <b>hoe vaak de twee handen samenvallen</b>.",
      partsnote: "Alleen Djembé&nbsp;2 gebruikt de volle twee maten. Al het andere is een kortere herhaling binnen de cyclus.",
    },

    fankani: {
      origin: "4/4 · cyclus van twee maten · gedreven door slaps",
      standfirst: "Waar Djole draait om een bas op elke kwart, <b>draait Fankani om slaps</b> — beide djembé-partijen beginnen met een slap en keren er steeds naar terug. De dundun-banen zijn weer gesplitst in <b>trom</b> en <b>bel</b>, en de okergele streep markeert waar beide handen tegelijk slaan. Bij Fankani is dat <b>elke tromslag</b>.",
      parts: {
        djembe1: { blurb: "Een slap op elke kwart. Tel 1–2 antwoorden met een <b>bas op de en</b>; tel 3–4 met <b>twee tonen</b>, en dan weer een bas. De slap op de <b>a</b> van tel 1 is waar mensen over struikelen." },
        djembe2: { blurb: "Hetzelfde begin als Djembé 1, maar deze komt elke halve maat uit op <b>twee tonen</b> in plaats van af te wisselen. De kortste partij op het blad — begin hier." },
        sangban: { blurb: "Het blad zet <b>Begin</b> op de en van maat 2, tel 3 — daar begint de eigen cyclus van de sangban. De twee maten zijn bijna gelijk; maat 1 heeft één dichte toon extra." },
        kenkeni: { blurb: "Twee dichte tonen op <b>1</b> en de <b>e</b>, dan de <b>open</b> toon op 2. Onder elke tromslag zit een belslag." },
        doundounba: { blurb: "Maar <b>drie</b> tromslagen in de hele cyclus, allemaal op de <b>en</b>. Let op het gat — geen slag op de en van maat 1, tel 2, terwijl de rest elke halve maat herhaalt. Zo staat het op het blad." },
      },
      ladder: [
        { tag: "12 tromslagen, 8 alleen bel", body: "De drukste trompartij van de drie, en elke slag wordt gedragen door de bel. Twee dichte tonen en dan de open — zorg dat dat contrast helder is voordat je je druk maakt om de bel.",
          say: ["tel mee", "<b>samen samen</b> &nbsp; ka &nbsp; <b>samen</b> &nbsp; – &nbsp; ka &nbsp; –"] },
        { tag: "9 tromslagen, 11 alleen bel", body: "Een volledige frase van twee maten in plaats van een herhaling, dus tel de cyclus in plaats van hem te voelen. Het <b>Begin</b>-teken staat in maat 2 — de partij begint niet waar het blad begint.",
          say: ["de drukke maat", "maat 1 tel 3: <b>T . T T</b> — de enige plek waar de tromhand het druk krijgt"] },
        { tag: "3 tromslagen, 17 alleen bel", body: "Het moeilijkst om dezelfde reden als bij Djole: de belhand staat bijna de hele cyclus alleen, en de drie tromslagen liggen ver uit elkaar. Puur uithoudingsvermogen op de bel.",
          say: ["zeg het hardop", "<b>SAMEN</b> &nbsp; – &nbsp; ka &nbsp; ka &nbsp; – &nbsp; ka &nbsp; ka &nbsp; –"] },
      ],
      note: "Bij Fankani <b>valt elke tromslag op een belslag</b>, in alle drie de partijen — de tromhand beweegt nooit alleen. De hele moeilijkheid is de bel vasthouden terwijl de tromhand rust.",
      partsnote: "Beide trompartijen van de dunduns zijn volledige frases van twee maten met hun eigen <b>Begin</b>-teken, als klein pijltje in het rooster. De djembé-partijen zijn korte herhalingen.",
    },

    "djole-guinee": {
      origin: "Guinee · 4/4 · cyclus van twee maten · drie djembé-partijen",
      standfirst: "De Guineese versie van Djolé, met <b>drie</b> djembé-partijen in plaats van twee. Djembé&nbsp;2 is noot voor noot de Djembé&nbsp;1 van het andere Djolé-blad, dus als je die kent heb je hier al een partij. De zwarte driehoekjes markeren <b>Einde</b> — waar het stuk eindigt.",
      parts: {
        djembe1: { blurb: "Slaps rond een gat, dan <b>twee tonen</b> aan het eind van elke halve maat. Vol — vijf slagen op acht — en het paar slaps op de <b>en</b> en de <b>a</b> is het lastige stuk." },
        djembe2: { blurb: "<b>Precies de Djembé 1 van het andere Djolé-blad</b> — bas op de kwart, dan een paar op de <b>en</b> en de <b>a</b>, eerst tonen, dan slaps. Gratis als je die al kent." },
        djembe3: { blurb: "De partij die het meest naar een solo neigt. Vier losse <b>open slaps</b> — op het blad onderstreept, dus laat ze doorklinken — en dan opent maat 2 in een reeks van zes tonen achter elkaar. Eerst spaarzaam, dan ineens niet meer." },
        sangban: { blurb: "Drie slagen per maat tegen een bel in rechte achtsten. Het paar op tel 4 — <b>op de tel en op de en</b> — is de figuur om vast te leggen." },
        kenkeni: { blurb: "<b>Gelijk aan de kenkeni van de andere Djolé</b> — trom en bel precies samen op de <b>en</b> en de <b>a</b>, niets op de tel." },
        doundounba: { blurb: "<b>Dezelfde vorm als de sangban, een tel eerder</b> — een slag op 1, dan het paar op tel 3. Zie je dat eenmaal, dan zijn de twee partijen één idee." },
      },
      ladder: [
        { tag: "precies samen — geen onafhankelijkheid nodig", body: "Trom en bel samen op elke slag, net als bij de andere Djolé. Niets op de tel; het paar zit op de <b>en</b> en de <b>a</b>.",
          say: ["tel mee", "rust, rust, <b>samen</b>, <b>samen</b>"] },
        { tag: "6 tromslagen, 10 alleen bel", body: "Bel in rechte achtsten, trom op 1 en dan het paar op tel 3. Elke tromslag valt op een belslag, dus de handen gaan nooit uit elkaar — je houdt alleen de bel vast door de gaten heen.",
          say: ["zeg het hardop", "<b>SAMEN</b> &nbsp; bel &nbsp; <b>SAMEN</b> &nbsp; <b>SAMEN</b> &nbsp; bel &nbsp; bel"] },
        { tag: "hetzelfde, een tel later", body: "Precies dezelfde figuur als de doundounba, één tel opgeschoven. Leer eerst de doundounba en dit is bijna gratis — maar ze tegen elkaar in spelen is het moeilijke deel, want juist die verschuiving voel je.",
          say: ["het verband", "sangban = doundounba, een tel later"] },
      ],
      note: "Zowel de sangban als de doundounba spelen tegen een <b>bel in rechte achtsten</b>, en elke tromslag valt op een belslag — dus geen hand beweegt ooit alleen. Het addertje is dat de twee partijen dezelfde figuur zijn, een tel uit elkaar: makkelijk te spelen, moeilijk te horen.",
    },

    gidamba: {
      origin: "12/8 · ternair · cyclus van vier maten",
      standfirst: "Het eerste <b>ternaire</b> ritme hier — drie onderverdelingen per tel in plaats van vier, geteld als <b>1 la li</b>. De doundounba speelt een echte <b>frase van vier maten</b> terwijl elke andere partij een korte herhaling is, dus het rooster is vier maten lang en de meeste rijen herhalen zich daarbinnen.",
      parts: {
        signal: { blurb: "Een reeks tonen, ingezet met twee voorslagen, die over de maat dunner wordt: drie, dan twee, dan twee, dan één." },
        djembe1: { blurb: "De simpelste partij op het blad — <b>slap, toon, slap</b> over twee tellen, dan een rust. Zes vakjes en je hebt hem." },
        djembe2: { blurb: "Drie slaps naar <b>twee tonen</b>. De slap op de <b>li</b> van tel 1 die direct doorloopt in de slap op tel 2 is het stuk om schoon te krijgen." },
        sangban: { blurb: "Eén slag per tel, afwisselend <b>open</b> en <b>dicht</b>. De bel is de simpelste van al deze bladen: twee slagen en dan een gat, elke tel." },
        kenkeni: { blurb: "Elke tromslag valt op een belslag; de bel voegt er twee aan toe. Een herhaling van één maat, en de makkelijkste van de drie om vast te houden." },
        doundounba: { blurb: "De enige partij hier die een echte frase is in plaats van een herhaling. Maat 1–2 zijn spaarzaam — drie slagen per maat. <b>Maat 3 loopt helemaal vol en de bel speelt precies met de trom mee</b>, daarna wordt maat 4 weer dunner." },
      },
      ladder: [
        { tag: "20 trom, 8 alleen bel", body: "Een herhaling van één maat waarin de trom een deel van de bel is — onder elke tromslag zit een belslag en de bel voegt er maar twee aan toe. De drukste trompartij en het minste coördinatiewerk.",
          say: ["tel mee", "<b>samen</b> la <b>samen</b> &nbsp; li <b>samen</b> li &nbsp; ka <b>samen</b> li &nbsp; <b>samen</b> la ka"] },
        { tag: "16 trom, 16 alleen bel", body: "Meer slagen met alleen bel dan wat dan ook hier, maar de bel is heel regelmatig — <b>twee en dan een gat</b>, elke tel — en de trom speelt één slag per tel, afwisselend open en dicht. Makkelijk vast te houden zodra het dempen schoon is.",
          say: ["zeg het hardop", "<b>SAMEN</b> &nbsp; bel &nbsp; – &nbsp;│&nbsp; <b>SAMEN</b> &nbsp; bel &nbsp; –"] },
        { tag: "een frase van vier maten", body: "Het moeilijkst, niet door de handen maar door het <b>geheugen</b> — het is de enige partij die niet elke maat of twee herhaalt. Leer maat 3 eerst: trom en bel spelen die hele maat precies samen, dus dat is de ene maat zonder enige onafhankelijkheid.",
          say: ["de vorm", "spaarzaam · spaarzaam · <b>vol</b> · dun"] },
      ],
      note: "Gidamba staat in <b>12/8</b>, dus tel <b>1 la li</b> in plaats van <b>1 e en a</b>. Elke tromslag in alle drie de dundun-partijen valt op een belslag, dus geen hand beweegt ooit alleen — het werk is de bel vasthouden door de gaten heen, en de frase van de doundounba onthouden.",
    },

    gumbe: {
      origin: "4/4 · cyclus van twee maten · twee sangban-partijen",
      standfirst: "Het enige blad hier met <b>twee sangban-partijen</b>, die tegen elkaar in spelen op verschillende bellen. Ook het signaal is anders — alleen tonen, geen slaps, anders dan het signaal dat de Djolé-familie deelt. De djembé-partijen zijn korte herhalingen; de doundounba gebruikt de volle twee maten.",
      parts: {
        signal: { blurb: "Een ander signaal dan bij de Djolé-familie — <b>alleen tonen, geen slaps</b>. Het wordt over de maat dunner: drie slagen, dan twee, dan twee, dan één." },
        djembe1: { blurb: "Twee tonen naar een slap, twee keer, waarbij de slap de eerste keer op de <b>a</b> valt en de tweede keer op de <b>en</b>. Die verschuiving is de hele partij." },
        djembe2: { blurb: "Bas, twee tonen, dan één slap op de <b>en</b> van tel 2. De kaalste djembé-partij van al deze bladen." },
        sangban: { blurb: "Open toon op 1, dan een paar dichte tonen op tel 2. Bel in rechte achtsten — en <b>maar vier belslagen per cyclus hebben geen tromslag eronder</b>, het minst van alle partijen hier." },
        sangban2: { blurb: "De tweede sangban antwoordt op de eerste: <b>twee dichte tonen op de tel</b>, dan de open op 2 — waar Sangban 1 hem op 1 heeft. Ook de bel is anders." },
        kenkeni: { blurb: "Eén slag op elke tel tegen een bel in rechte achtsten. De simpelste partij op het blad en de logische plek om te beginnen." },
        doundounba: { blurb: "Twee <b>open</b> tonen een gepunteerde tel uit elkaar, dan drie dichte, dan een hele tel rust. Let op: de bel verandert halverwege de maat — twee tellen gesyncopeerd, dan rechte achtsten." },
      },
      ladder: [
        { tag: "8 alleen bel", body: "Eén tromslag per tel, bel op de achtsten. Onder elke tromslag zit een belslag en de gaten zijn steeds één slag. Begin hier.",
          say: ["tel mee", "<b>SAMEN</b> &nbsp; bel &nbsp; <b>SAMEN</b> &nbsp; bel"] },
        { tag: "4 alleen bel — het minst hier", body: "Bijna elke belslag heeft een tromslag, dus er is nauwelijks onafhankelijkheid op te bouwen. Het werk zit in het contrast <b>open-dan-dicht</b>, niet in de coördinatie.",
          say: ["zeg het hardop", "<b>SAMEN</b> &nbsp; bel &nbsp; <b>SAMEN</b> &nbsp; <b>SAMEN</b>"] },
        { tag: "10 alleen bel, en een bel die verandert", body: "De moeilijkste van de vier, omdat <b>de bel zelf halverwege de maat verandert</b> — twee tellen gesyncopeerd, dan rechte achtsten. Krijg eerst de bel alleen door die wissel heen voordat je de tromhand toevoegt.",
          say: ["alleen de bel", "✕ . ✕ ✕ &nbsp; . ✕ ✕ . &nbsp;│&nbsp; ✕ . ✕ . &nbsp; ✕ . ✕ ."] },
      ],
      note: "Twee sangban-partijen betekent twee verschillende bellen tegelijk — als je er één leert, zet de andere uit tot die van jou stevig staat, anders drijf je af naar de andere bel.",
    },

    "soli-lent": {
      origin: "4/4 · cyclus van twee maten · langzaam",
      standfirst: "Langzaam, en gebouwd op <b>djembé-frases van een hele maat</b> in plaats van korte herhalingen — beide djembé-partijen lopen alle zestien vakjes af voordat ze herhalen. De doundounba is de kaalste van al deze bladen: <b>drie slagen in de hele cyclus</b>.",
      parts: {
        signal: { blurb: "Het signaal dat de Djolé-familie deelt — tonen, dan drie slaps." },
        djembe1: { blurb: "Een hele maat voordat hij herhaalt. Bas, twee tonen, dan een reeks <b>slap-toon-toon</b> over tel 2–3 naar een tweede bas. De drukste partij op het blad." },
        djembe2: { blurb: "Een slap op elke tel, beantwoord door <b>twee tonen</b> op tel 2 en 4. De bas op tel 3 is het enige verschil tussen de twee helften." },
        sangban: { blurb: "Een dichte toon op elke tel, met één <b>open</b> toon op de en van tel 3 — de enige kleur in de partij. Bel in rechte achtsten." },
        kenkeni: { blurb: "Twee slagen per halve maat — op de tel en op de <b>en</b> van de volgende — tegen de gesyncopeerde bel." },
        doundounba: { blurb: "<b>Drie slagen in de hele cyclus van twee maten</b> — één in maat 1, twee in maat 2. Bijna puur uithoudingsvermogen op de bel; de tromhand wacht bijna de hele tijd." },
      },
      ladder: [
        { tag: "8 alleen bel", body: "Een slag op elke tel tegen rechte achtsten — de bel vult gewoon de gaten. Voeg de enkele <b>open</b> toon op de en van tel 3 toe zodra de rest automatisch gaat.",
          say: ["zeg het hardop", "<b>SAMEN</b> &nbsp; bel &nbsp; <b>SAMEN</b> &nbsp; bel"] },
        { tag: "12 alleen bel", body: "Maar twee tromslagen per halve maat, en de tweede valt op de <b>en</b> — naast de tel, tegen een bel die ook gesyncopeerd is. Hier begint de onafhankelijkheid echt.",
          say: ["het geheel", "<b>SAMEN</b> &nbsp; ka &nbsp; ka &nbsp; – &nbsp; ka &nbsp; <b>SAMEN</b> &nbsp; –"] },
        { tag: "17 alleen bel — drie tromslagen in totaal", body: "De kaalste dundun-partij van al deze bladen. Er is geen coördinatiepatroon te leren, alleen het vermogen om de bel twee maten door te laten lopen en daarbinnen drie slagen precies te plaatsen.",
          say: ["de vorm", "maat 1: één slag &nbsp;│&nbsp; maat 2: twee"] },
      ],
      note: "Soli Lent is langzaam, en dat maakt het minder vergevingsgezind — er is tijd om elke slag te vroeg of te laat te horen vallen. Zet het tempo <b>omlaag</b>, niet omhoog.",
    },

    sunun: {
      origin: "4/4 · cyclus van twee maten",
      standfirst: "Djembé-partijen vol slaps boven de drukste doundounba van al deze bladen — en ongebruikelijk genoeg is die doundounba de <b>makkelijkste</b> dundun-partij hier, omdat de bel bijna elke slag meespeelt.",
      parts: {
        signal: { blurb: "Het signaal dat de Djolé-familie deelt." },
        djembe1: { blurb: "Een toon en dan <b>twee slaps</b>, twee keer, waarbij de tweede keer een bas de plaats van de toon inneemt. Negen slagen per maat — de drukste djembé-partij hier." },
        djembe2: { blurb: "<b>Dezelfde partij als Djembé 2 van Fankani</b> — slap, slap op de <b>a</b>, slap op 2, dan twee tonen. Gratis als je die kent." },
        sangban: { blurb: "Twee slagen per halve maat tegen de gesyncopeerde bel — op de tel, dan op de <b>en</b> van de volgende." },
        kenkeni: { blurb: "Eén slag op elke tel, bel in rechte achtsten. Simpeler wordt het niet." },
        doundounba: { blurb: "Zeven slagen per maat, een mix van dichte en <b>open</b> tonen — en de bel speelt ze allemaal mee. Druk om te spelen, maar er zit bijna geen onafhankelijkheid in." },
      },
      ladder: [
        { tag: "maar 6 alleen bel", body: "Tegen je gevoel in de <b>makkelijkste</b> hier. Het is de drukste trompartij op het blad, maar de bel speelt bijna elke slag mee, dus de handen bewegen bijna steeds samen. Leer het contrast open/dicht, niet de onafhankelijkheid.",
          say: ["zeg het hardop", "<b>SAMEN</b> &nbsp; ka &nbsp; <b>SAMEN</b> &nbsp; <b>SAMEN</b>"] },
        { tag: "8 alleen bel", body: "Eén slag per tel tegen de achtsten. Eenvoudig, en een goede rustpauze voor je hoofd na de doundounba.",
          say: ["tel mee", "<b>SAMEN</b> &nbsp; bel &nbsp; <b>SAMEN</b> &nbsp; bel"] },
        { tag: "12 alleen bel", body: "De moeilijkste van de drie, ook al is hij het kaalst: twee tromslagen per halve maat, de tweede naast de tel, tegen een gesyncopeerde bel. De bel moet eerst helemaal automatisch gaan.",
          say: ["het geheel", "<b>SAMEN</b> &nbsp; ka &nbsp; ka &nbsp; – &nbsp; ka &nbsp; <b>SAMEN</b> &nbsp; –"] },
      ],
      note: "Een handige omkering hier: <b>drukker betekent niet moeilijker</b>. De doundounba van Sunun heeft meer dan twee keer zoveel slagen als de sangban en is veel makkelijker, omdat de bel de trom meespeelt.",
    },

    toro: {
      origin: "4/4 · cyclus van twee maten · met een inzet",
      standfirst: "Het enige blad met een uitgeschreven <b>inzet</b> — een figuur van één maat met slaps die het ensemble binnenhaalt en dan wegvalt. Beide dundun-partijen zijn echte frases van twee maten: de sangban verandert zijn einde en de doundounba valt in maat 2 bijna stil.",
      parts: {
        signal: { blurb: "Het signaal dat de Djolé-familie deelt." },
        entrance: { blurb: "<b>Eén keer</b> gespeeld om iedereen binnen te halen, daarna stil. Slaps op de tel met een paar op de en — het is de aftel van het blad, geen partij die je herhaalt." },
        djembe1: { blurb: "Twee tonen naar een bas, en de rest slaps. De tweede bas, op de <b>a</b> van tel 3, is degene die mensen verrast." },
        djembe2: { blurb: "<b>Weer de Djembé 2 van Fankani en Sunun</b> — dezelfde acht vakjes komen op drie verschillende bladen terug." },
        sangban: { blurb: "Een echte frase van twee maten: drie tellen gelijk, dan eindigt maat 1 op <b>dichte</b> tonen en maat 2 op <b>open</b>. Dat einde is het enige verschil — en je mist het makkelijk." },
        kenkeni: { blurb: "Niets op de tel — twee dichte tonen op de <b>en</b> en de <b>a</b>, dan de <b>open</b> op de en van de volgende tel." },
        doundounba: { blurb: "Maat 1 beantwoordt het openingspaar met een reeks over tel 3–4; <b>maat 2 speelt het openingspaar en dan helemaal niets</b>. De bel verandert mee." },
      },
      ladder: [
        { tag: "maar 4 alleen bel", body: "Bijna elke belslag heeft een tromslag, dus er is weinig onafhankelijkheid op te bouwen. De hele moeilijkheid is <b>onthouden in welke maat je zit</b> — ze verschillen alleen in hun laatste tel.",
          say: ["het verschil", "maat 1 eindigt <b>dicht</b> · maat 2 eindigt <b>open</b>"] },
        { tag: "8 alleen bel", body: "Er valt niets op de tel, en dat is het enige lastige eraan. Beide tromslagen van het paar vallen op belslagen.",
          say: ["tel mee", "– &nbsp; ka &nbsp; <b>samen</b> &nbsp; <b>samen</b>"] },
        { tag: "11 alleen bel, over twee maten", body: "Maat 2 is bijna helemaal alleen bel — de tromhand speelt twee slagen en wacht dan anderhalve maat. De bel stabiel houden door die leegte heen is de eigenlijke vaardigheid.",
          say: ["de vorm", "maat 1: <b>vol</b> &nbsp;│&nbsp; maat 2: twee slagen, dan niets"] },
      ],
      note: "De <b>inzet</b>-rij van Toro speel je één keer om het ensemble binnen te halen, daarna valt hij weg — het is geen partij om te herhalen. Zet hem uit zodra je speelt.",
    },

    sorsornet: {
      origin: "12/8 · ternair · cyclus van twee maten",
      standfirst: "Weer ternair — tel <b>1 la li</b>. Wat Sorsornet bijzonder maakt is de <b>sangban-bel</b>: die slaat op elk tweede vakje tegen een raster van drieën, dus hij valt nooit vast op de tel zoals de andere bellen. Drie belslagen op elke twee tellen. De dundun-banen zijn gesplitst in <b>trom</b> en <b>bel</b>, en de okergele streep markeert waar beide handen tegelijk slaan — hier is dat <b>elke tromslag</b>, in alle drie de partijen.",
      parts: {
        signal: { blurb: "Tonen in paren over drie tellen, dan één alleen om af te sluiten. Elke maat begint met een <b>galop</b> — de voorslag en de tel als twee heel snelle slagen, links en dan rechts." },
        djembe1: { blurb: "Slap, toon, slap — dezelfde cel van twee tellen als de eerste djembé van Gidamba. Zes vakjes en je hebt de hele partij." },
        djembe2: { blurb: "Een slap op elke tel, met <b>twee tonen</b> die de tweede opvullen. Het gat na de eerste slap geeft hem zijn karakter." },
        djembe3: { blurb: "De volste partij op het blad — elk vakje klinkt. Drie slaps achter elkaar door tel 1, dan een slap en <b>twee tonen</b> op tel 2." },
        sangban: { blurb: "De bel slaat op <b>elk tweede vakje</b> tegen een tel van drie, dus hij valt op de tel, dan op de <b>li</b>, dan op de <b>la</b> — een drie-tegen-twee waar je even aan moet wennen. Beide tromslagen vallen op een belslag: <b>open</b> op tel 1, <b>dicht</b> op de <b>la</b> van tel 2." },
        kenkeni: { blurb: "Eén tel lang en elke tel hetzelfde: bel op de tel, dan <b>trom en bel samen</b> op de <b>li</b>. De plek om te beginnen." },
        doundounba: { blurb: "Een echte frase, geen herhaling. Tel 1 van elke maat is <b>drie slagen trom en bel precies samen</b>, dan antwoordt maat 1 over tel 3–4 en valt de trom in maat 2 helemaal stil. Negen tromslagen op vierentwintig vakjes, en <b>allemaal meegespeeld door de bel</b>." },
      },
      ladder: [
        { tag: "één tel, niets te onthouden", body: "Eén tel, acht keer herhaald. De bel markeert de tel, de trom komt erbij op de <b>li</b>. Onder elke tromslag zit een belslag en er is geen frase om te onthouden.",
          say: ["tel mee", "bel &nbsp; – &nbsp; <b>SAMEN</b>"] },
        { tag: "de drie-tegen-twee-bel", body: "Maar vier slagen met alleen bel — minder dan wat dan ook hier — maar de bel loopt in <b>tweeën tegen een tel van drie</b>, dus hij kruist de telling en valt elke tel op een andere plek. Leer de bel alleen tot hij geen aandacht meer vraagt, en voeg dan de trom toe.",
          say: ["zeg het hardop", "<b>SAMEN</b> &nbsp; – &nbsp; bel &nbsp;│&nbsp; – &nbsp; <b>SAMEN</b> &nbsp; –"] },
        { tag: "twee maten om te onthouden", body: "De handen zijn makkelijk — trom en bel spelen bij elke tromslag precies samen. Het werk is <b>geheugen</b>: het is een frase van twee maten, en in de hele tweede helft zit na tel 1 geen trom meer.",
          say: ["de vorm", "<b>vol</b> · rust · antwoord &nbsp;│&nbsp; <b>vol</b> · rust · rust"] },
      ],
      note: "Elke tromslag in alle drie de dundun-partijen valt op een belslag, dus geen hand beweegt ooit alleen. De moeilijkheid zit in de <b>bel van de sangban</b>, die drie slagen op elke twee tellen speelt en daardoor elke ronde op een andere plek zit.",
    },

    garangedon: {
      origin: "12/8 · ternair · cyclus van twee maten",
      standfirst: "Het vriendelijkste blad hier voor een dundunspeler: <b>alle drie de partijen delen precies dezelfde bel</b> — op de tel en op de <b>li</b>, elke tel, de hele weg door. Leer die ene bel en hij draagt de sangban, de kenkeni en de doundounba alle drie, zodat je van partij kunt wisselen zonder de belhand opnieuw te leren. De okergele streep markeert waar beide handen tegelijk slaan, en ook hier is dat <b>elke tromslag</b>.",
      parts: {
        signal: { blurb: "Bijna hetzelfde signaal in beide maten, maar net niet — maat 2 laat de slag op tel 3 weg en antwoordt in plaats daarvan op de <b>li</b>. Elke maat begint met een <b>galop</b>: de voorslag en de tel als twee heel snelle slagen, links en dan rechts." },
        djembe1: { blurb: "Een <b>slap op de li van elke tel</b>, zonder uitzondering — dat is de ruggengraat. Maat 1 begint met een bas en voegt verder niets toe; maat 2 vult tel 2 en 3 met <b>twee tonen</b> vóór de slap." },
        djembe2: { blurb: "Slap, toon, slap over twee tellen — dezelfde cel als de eerste djembé van Sorsornet, en de snelste manier om erin te komen." },
        djembe3: { blurb: "Een slap op elke tel, <b>twee tonen</b> om de tweede af te sluiten. Tegen Djembé 2 vallen de twee partijen samen op de tellen en vullen ze de gaten elk anders." },
        sangban: { blurb: "De enige partij die <b>beide</b> dundun-tonen gebruikt: dicht op tel 1, dan <b>open</b> op de li, en weer open op de li van tel 3. Tien slagen in de cyclus en elke slag op een belslag." },
        kenkeni: { blurb: "Twee tromslagen <b>direct achter elkaar over de tel heen</b> — de <b>li</b> van de ene tel en de tel die volgt — en dan een tel rust. Beide zijn belslagen, dus het is de bel die het paar bij elkaar houdt." },
        doundounba: { blurb: "Druk in maat 1, dan in maat 2 <b>twee hele tellen alleen bel</b> voordat één slag de cyclus weer rond maakt. Die twee stille tellen zijn de partij — de rest is eenvoudig." },
      },
      ladder: [
        { tag: "8 trom, 8 alleen bel", body: "De bel is dezelfde als die van iedereen. De trom speelt een <b>paar over de tel heen</b> — li, dan de volgende tel — en rust dan een hele tel. Kort, herhalend, en beide slagen zijn belslagen.",
          say: ["tel mee", "bel &nbsp; – &nbsp; <b>SAMEN</b> &nbsp;│&nbsp; <b>SAMEN</b> &nbsp; – &nbsp; bel"] },
        { tag: "10 trom, 6 alleen bel", body: "De volste trompartij en de <b>minste slagen met alleen bel</b> op het blad, en daardoor makkelijker vast te houden dan hij lijkt. Het echte werk zijn de <b>open en dichte</b> tonen: tel 1 dicht, de li erna open.",
          say: ["zeg het hardop", "<b>SAMEN</b> &nbsp; – &nbsp; <b>SAMEN</b> &nbsp;│&nbsp; bel &nbsp; – &nbsp; <b>SAMEN</b>"] },
        { tag: "de twee stille tellen", body: "Alleen moeilijk in maat 2, waar de trom <b>twee hele tellen</b> stopt terwijl de bel gewoon doorgaat. Tel hardop door het gat heen — de verleiding is om te vroeg terug te komen.",
          say: ["de vorm", "druk &nbsp;│&nbsp; slag · <b>rust · rust</b> · slag"] },
      ],
      note: "<b>Alle drie de dundun-partijen spelen dezelfde bel</b> — op de tel en op de <b>li</b>, elke tel. Dat is ongebruikelijk op deze bladen, en het maakt Garangedon het beste ritme om de belhand op te leren: leg hem één keer vast en je kunt tussen alle drie de partijen wisselen.",
    },
  },
};
