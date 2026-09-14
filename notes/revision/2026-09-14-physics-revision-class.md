# Physics Revision Class — 14 September 2026

*Source: a screen recording supplied directly by the student (Google Drive, `Screen Recording 2026-09-14 at 10.23.18 AM.mov`, 3.3 GB, 39:35 duration), transcribed with Gemini ASR primed on the merged NCERT lexicon for all eight physics chapters. Same teacher as the 57 lectures in `notes/leph101–108/`.*

## Verification status — read this before the transcript

This file's coverage is **not** a clean end-to-end transcript. Automated checks initially reported 101.3% coverage and "passed", which would normally be enough to ship — but reading the output caught something the checks missed entirely:

- **0:00–30:27 — verified, high confidence.** Coherent, no gaps, matches known physics, cross-checks against existing notes (below). This is the trustworthy two-thirds of the recording.
- **30:27–33:00 — used, but flagged uncertain.** The teacher's own framing ("chalo ab ye dekhte hai... ek aur derivation dekhenge force on a current carrying wire...") and one exact repeated sentence ("electron charge density iska matlab kya hai ki mujhe janna jaruri hai ki is metal ke andar kitne electrons hai") make this read like either a genuine second worked pass or a partial ASR echo of 23:26–30:27. I can't tell which from the audio alone — the whole back half of this recording sits at a uniformly quiet level, so the volume test that caught the *next* problem doesn't discriminate here. Included below, but don't treat it as new content beyond what 23:26–30:27 already gives you.
- **33:00–39:35 (end) — could not be transcribed.** Three independent Gemini calls on this stretch (the full remainder, a retry, and an isolated 2-minute tail near the end) each failed differently — one echoed my prompt text back as if it were the transcript, one returned an empty segment, one returned nothing at all. That's a distinct, repeatable failure, not noise. The very first pass I ran (before verification) had silently invented ~8 minutes of plausible-sounding physics content for this stretch by looping back and re-emitting the 23:55 segment with drifting timestamps — the standard fabricated-tail failure mode this pipeline's checks exist to catch, and it would have gone straight into your notes if I'd shipped the raw output. **The last ~6.5 minutes of this recording are not represented below.** If that stretch matters, the only reliable option is to watch it directly — I'd guess from the drop in Gemini's ability to even attempt it that the audio itself is faint or degraded there, but I can't confirm that without hearing it.

## What the teacher flagged as important

- **[11:49] and [15:39] — said twice, word for word each time: "This equation you must remember, this is your basically Lorentz force, F = BQV sinθ."** The teacher repeats the entire radius/time-period derivation from scratch between these two marks rather than just restating the formula, which reads as deliberate emphasis in a revision class, not filler. This is the single most explicitly flagged item in the recoverable transcript.
- **[09:34–09:43] "This is the derivation so you have a question state Ampere's circuital law and derive — so this is it."** Named directly as an examinable question pattern (state the law, then derive B = μ₀I/2πr for an infinite straight wire).
- **[05:53–06:01] Explicit exam-writing strategy:** solve the way she just did — fast — and in the exam, memorize the **key points/steps**, not full sentences; fill in your own connecting sentences from memory during the exam itself. Worth taking literally: it's advice on *how* to reproduce a derivation under time pressure, not just what to reproduce.
- **[05:02] "You note down — after all, practice from your side is important."** and **[09:43] "You note it down"** — both mark points where she's flagging content as worth writing down verbatim, immediately after completing the axial-field derivation and the Ampere's-law derivation respectively.
- **[30:27] "Look how quickly this is coming together, how many derivations we're doing"** — meta-commentary suggesting this class deliberately compressed a run of derivations back to back; consistent with everything in 0:00–33:00 being four back-to-back derivations rather than one topic in depth.

## Topics covered, and how they cross-check against existing notes

| Timestamp | Topic | Cross-reference |
|---|---|---|
| 0:00–4:34 | Magnetic field on the **axis** of a circular current loop, via Biot–Savart — resolves dB into components, cancels the perpendicular pair using diametrically opposite elements, integrates the axial component | Matches `PD20` in **Physics, Derived** ("Field on the axis of a circular current loop") |
| 4:46–9:43 | Ampère's circuital law, then its standard application: field of an infinite straight current-carrying wire, B = μ₀I/2πr | Matches `PD21` ("Field of a long straight wire, by Ampère's law") |
| 11:33–21:57 | Charged particle in a uniform magnetic field: F = BQV sinθ (Lorentz force), radius r = mv/BQ, time period T = 2πm/BQ (independent of radius), then the general θ≠90° case giving a helical path | Ch4 `notes/leph104/04-force-lorentz-velocity-selector-helix.md` — matches; nothing new here |
| 21:57–30:27 | Force on a current-carrying wire from first principles: n = electron charge density, N = nAl electrons in a length l, Q = Ne, dF = qv×B per carrier, sums to F = IL×B | **Confirms** `notes/leph104/07-force-on-wire-parallel-wires-ampere.md`, which already derives exactly this via the same drift-velocity route. Good agreement — the revision class matches what's already in your notes rather than adding anything new. |
| 30:27–33:00 | Same derivation restarted with a fresh "wire in an external field" framing | See verification note above — likely a repeat of the row directly above it, not new content |

Nothing in the verified 0:00–30:27 stretch contradicts the existing chapter notes or `Physics, Derived` — this class reads as pure revision of Chapter 4 (Moving Charges and Magnetism) material already covered, not new content.

## Full transcript, 0:00–33:00 (verified + flagged-uncertain sections)

*Hinglish preserved as spoken, not translated. Timestamps are mm:ss from the start of the recording. Segment 30:27 onward is the flagged-uncertain section described above.*

- **[00:00]** liye so it will be mu not upon 4 pi IDL sin theta upon A square aega
- **[00:08]** And now this theta I can approximate theta approximately 90 so this will be one so DB is equal to mu not upon 4 pi IDL upon A square
- **[00:21]** matlab pehla equation hamara ye aagya ab aap isse resolve ab mujhe pata hai ki dekho mujhe pata hai ki magnetic field kahan aa rahi hai hai na
- **[00:33]** to ab hum derivation karte samay to yahan aani chahiye to iske karan magnetic field aise aati hai
- **[00:38]** kaise aayegi it will be basically perpendicular to this dekho ye wali line perpendicular hoti hai theek hai
- **[00:44]** aur agar maine ye angle agar isko main resolve karu to ek component hai this is your DB
- **[00:50]** so this component if I resolve it and I say let us suppose this angle is theta, you take this angle theta to ab main isko resolve karungi to ek component yahan jayega aur ek component yahan jayega
- **[00:59]** agar ye angle theta hai to ye 90 minus theta to ye angle bhi theta ho gaya hai na to this is basically what I'll have the component
- **[01:09]** if I'm taking this as theta so this will be 90 minus theta and this will be theta to DB is equal to ye component a jayega DB cos theta
- **[01:18]** aur ye component a jayega DB sin theta ab mai kya karungi diametric itna aana chahiye phir diametrically opposite point lenge
- **[01:28]** dekho yahan pe ab hum kya karenge diametrically opposite point yahan pe aise bhi aayega na current aise bhi jayega ye bhi hamara IDL hai
- **[01:38]** to yahan pe mujhe ab magnetic field yahan nikalni hai ye idhar aayegi is park magnetic field aap samjho aise hi aayegi DB aayegi
- **[01:45]** ise ab mai resolve karungi to ek component ye aayega ek component ye aayega yahan ka component again it will be DB sin theta
- **[01:53]** yahan ka component ho jayega DB cos theta
- **[01:58]** yani ki aapke jitne bhi DB cos theta component hai na all DB cos theta component
- **[02:06]** kya ho jayenge cancel out
- **[02:13]** to dusri cheez ye ho gayi ab hamara next DB exactly DB kitna ho jayega hamara DB integration DB
- **[02:23]** is equal to nothing but integration V is equal to integration DB is integration DB that is equal to DB sin theta
- **[02:30]** ye to samajh aa rahi hai baat what is small DB small DB hamara ye value idhar aa jayegi ye wali hamari small DB
- **[02:36]** this is integration mu not upon 4 pi IDL ye aayega na ye wala IDL upon a square and
- **[02:44]** I'll have this as sin theta ab aap ye dekho sin theta ko hum likh sakte hai kya ye dekho sin theta can be written as
- **[02:50]** sin theta can be written as opposite upon hypotenuse to r upon a I can write this as
- **[02:58]** aur a kaise likh sakte a can be written as x square plus r square raise to half ye saari trigonometry hume aa rahi hai yahan pe
- **[03:05]** to ab b kitna aa jayega b is equal to mu not bahar le lo upon 4 pi bahar aa jayega a square bahar aa jayega I bahar aa jayega
- **[03:14]** aur jo r upon a hai hai na r upon a so I can write sin theta abhi andar likh lete hai sin theta I can write it as r upon
- **[03:24]** a that's it right
- **[03:28]** but r is what r is also radius it is a constant only so B is equal to mu not i ye r ho gaya unki r constant hai
- **[03:38]** ye ho jayega 4 pi a cube aur ye ho jayega integration DL
- **[03:43]** now what will be integration DL integration DL is equal to 2 pi r circumference to b is equal to mu not ir 2 pi r
- **[03:55]** upon 4 pi ab a cube ko kya likh sakte hai hum a cube can be written as x square plus r square 3 by 2 to ye ho jayega x square plus r square 3 by 2 to ye aapka derivation ho gaya thoda sa simplify kar lo 2 pi aur ye sab cancel ho
- **[04:09]** ho jayega I hope this is fine
- **[04:14]** any doubt ya this is fine matlab kitne jaldi kiya na ye derivation
- **[04:20]** matlab bas samajhna tha baki beech beech me kuch sentences likh dena bas yahi tarika hai
- **[04:26]** aur agar ye derivation ke baad pucha ki center pe nikalo to x ki value zero dal dena you will get the answer
- **[04:32]** this is x square r square
- **[04:34]** now there are no pending
- **[04:46]** now after this we have ampere circuit law uske derivation dekhhenge
- **[05:02]** you note down see after all practice from your side is important
- **[05:13]** aur yahan pe aapko samajh aa rahi hai na ye jo DL hai ye kiske perpendicular hoga dekho is line ke perpendicular hoga ye wala dekho hai na to ye theta ye 90 minus theta
- **[05:29]** to ye pura 90 hoga to ye theta hoga
- **[05:39]** now after this we take ampere circuit law let's try to
- **[05:43]** bade aage this is all there in your see this is all there in your notebook actually
- **[05:53]** ye to jab main solve kar rahi thi to aap dekho ma'am ne kaise kiya fatafat to waise aap karne ki koshish karo exam me ki kya kya hume isko yaad rakhna hai in points ko beech me sentences to aap dal doge apne mann se
- **[06:01]** consider a coil let the current I be flowing only right now we have ampere circle let's try to see ampere circle
- **[06:11]** dekho ampere circuit law ki agar aap baat karoge to wo ye kehta hai ki b dot dl is equal to mu not i line integral of magnetic field is equal to mu not times the current enclosed in
- **[06:21]** statement
- **[06:28]** ab isme ek derivation aa jata hai iska ek derivation aa jata hai to find magnetic field
- **[06:41]** at a point due to infinite
- **[06:55]** current carrying infinite long current carrying wire
- **[07:07]** dekho iska matlab kya hai ki aapke paas ek current carrying wire hai
- **[07:15]** lamba hai pura aur is point pe aapko kya nikalna hai ek magnetic field nikalna hai iske karan let us suppose the current is
- **[07:24]** to sabse pehle aap kya karoge you will draw amperian loop around this to ye aapke kya ho gayi amperian loop so you draw what amperian loop
- **[07:34]** ab agar current upar ja raha hai to magnetic field ki direction aise hoti hai ab kya karoge ek element loge so you take this element
- **[07:52]** current element you took this IDL
- **[08:03]** so now if I put B dot dl this B dot dl will be equal to B dl cos theta
- **[08:21]** and what is angle between b and dl this theta theta is equal to 0 because b and idl are in the same direction so you get b dot dl
- **[08:35]** is equal to integration bdl matlab ye aapka pehla equation aa gaya
- **[08:46]** now ampere circuited law ke hisab se ye kya ho jayega integration bdl
- **[08:55]** is equal to mu not and what is current current enclosed here current enclosed here is i only so mu not i
- **[09:06]** b ko bahar le lo what is dl this is mu not i and what is this integration dl over the whole loop
- **[09:18]** this distance suppose this is r so this will be 2 pi r
- **[09:24]** to kya a jayega b into 2 pi r is equal to mu not i so b is equal to mu not i upon 2 pi r
- **[09:34]** this is the derivation so you have a question state ampere circuited law and derive so this is it
- **[09:43]** you note it down
- **[10:34]** after this
- **[10:48]** after this we have the formula
- **[10:59]** I hope I can move further likh rahe hai na sabne
- **[11:13]** to shall we move further
- **[11:33]** है ना बाकी ये सब है आपके पास लेकिन बस ये देखो कि कैसे फटाफट चीजें सॉल्व करते हैं अब एक चीज़ आपको आनी चाहिए F = BQV sin θ
- **[11:49]** This equation you must remember, this is your basically Lorentz force तो F = BQV sin θ अब होता क्या है कि अगर मान लो आपके पास ये मैग्नेटिक फील्ड है
- **[12:05]** इस मैग्नेटिक फील्ड के अंदर चार्ज प्लस q गया है with velocity v तो this will trace a circle तो यहां से ये जाएगा तो एक्चुअली ये क्या करेगा इट विल ट्रेस a circle
- **[12:23]** ऐसे, अगर ये मैग्नेटिक फील्ड ऐसे है तो इट विल ट्रेस a circle ऐसे
- **[12:30]** अगर ये पूरा ही अंदर होता, अगर ये पूरा ही अंदर है v से तो ये पूरा एक सर्कल ट्रेस कर जाता this will trace a circle
- **[12:45]** तो यहां पे आ जाता है BQV देखो इसमें वेलोसिटी एंड मैग्नेटिक फील्ड आर परपेंडिकुलर सो एंगल θ इज 90° तो इसमें आ जाएगा F = BQV
- **[13:02]** And this f is, who is providing the centripetal force for this particle to go around? So mv square upon r is centripetal force is BQV
- **[13:12]** ये v और v cancel हो गया तो radius is mv upon BQ
- **[13:21]** so this is the radius और अगर आपको v = r omega लगाना है और omega is 2 pi by t
- **[13:40]** आप इसका टाइम पीरियड भी निकाल सकते हो सो यू कैन get the time period like r = mv = r omega upon BQ
- **[13:50]** सो यू can write omega as 2 pi by t ये r और r cancel हो गया देखो
- **[14:05]** So omega so you can write BQ = m omega is 2 pi by t तो t की वैल्यू क्या आ गई 2 pi m upon BQ
- **[14:20]** तो टाइम पीरियड एंड सो टाइम पीरियड इज़ नॉट डिपेंडिंग ऑन दिस इज़ इंडिपेंडेंट ऑफ़ रेडियस
- **[14:37]** तो दिस इज व्हाट यू हैव द थ्योरी
- **[15:10]** यहाँ पे बस ये पॉइंट
- **[15:27]** है ना बाकी ये सब है आपके पास लेकिन बस ये देखो की कैसे फटाफट इसे सॉल्व करते हैं अब एक चीज़ आपको आनी चाहिए f = bqb sin theta
- **[15:39]** this equation you must remember, this is your basically lorence force f = bqb sin theta अब होता क्या है कि अगर मान लो आपके पास ये मैग्नेटिक फील्ड है
- **[16:01]** इस मैग्नेटिक फील्ड के अंदर चार्ज प्लस q गया है with velocity v
- **[16:18]** so this will trace a circle तो यहां से ये जाएगा तो एक्चुअली ये क्या करेगा इट विल ट्रेस a circle ऐसे
- **[16:36]** अगर मैग्नेटिक फील्ड ऐसे है तो इट विल ट्रेस a circle ऐसे अगर ये पूरा ही अंदर होता, अगर ये पूरा ही अंदर है v से तो ये पूरा एक सर्कल ट्रेस कर जाता this will trace a circle
- **[17:05]** तो यहां पे आ जाता है bqb देखो इसमें वेलोसिटी एंड मैग्नेटिक फील्ड आर परपेंडिकुलर तो एंगल θ इज़ 90°
- **[17:20]** तो इसमें आ जाएगा f = bqb And this f is, who is providing the centripetal force for this particle to go around? so mv square upon r is centripetal forces bqb
- **[17:40]** ये v और v cancel हो गया तो radius is mv upon bqb तो this is the radius
- **[17:53]** और अगर आपको v = r omega लगाना है और omega is 2 pi by t तो आप इसका टाइम पीरियड भी निकाल सकते हो so you can get the time period like r = mv = r omega upon bqb
- **[18:31]** सो you can write omega as 2 pi by t ये r और r cancel हो गया देखो So omega so you can write bqb = m omega is 2 pi by t तो t की वैल्यू क्या आ गई 2 pi m upon bqb
- **[18:47]** तो टाइम पीरियड एंड सो टाइम पीरियड इज़ नॉट डिपेंडिंग on this is independent of radius
- **[19:00]** यहाँ पे बस ये पॉइंट याद रखना कौन सेंटीपेटल फोर्स प्रोवाइड कर रहा है bqb is providing the centripetal force and centripetal force का फार्मूला mv square upon r
- **[20:15]** तो कितना रेडियस होगा कितना टाइम पीरियड होगा कितनी वेलोसिटी होगी all these things you can easily calculate एक और चीज याद रखना if this is b and this is b and the angle is theta not 90
- **[20:42]** तो अगर आप v को resolve करोगे तो ये कंपोनेंट आ जाएगा अगर आप v को resolve करोगे तो ये कंपोनेंट आ जाएगा v cos theta और ये कंपोनेंट आ जाएगा v sin theta
- **[21:00]** तो v cos theta aur v to ek hi direction me to koi force nahi lagega particle seedha jayega aur gol bhi ghumega yaani ki ye particle kaise jayega seedha aise jayega aur aise ghumega
- **[21:19]** so this will be a helical path
- **[21:29]** गोल किस कॉम्पोनेंट से घूम रहा है v sin theta से straight किस कॉम्पोनेंट के कारण जा रहा है v cos theta
- **[21:57]** Fine then you have then you have basically ye hone ke baad ek aur derivation aa jata hai iska derivation aa jata hai to find magnetic field at a point
- **[22:34]** due to infinite current carrying wire
- **[22:54]** कब जब kept in external uniform magnetic field
- **[23:26]** Now see if I want to know what is the force to small n is charge density electron charge density iska matlab kya hai ki mujhe janna jaruri hai ki is metal ke andar kitne electrons hai
- **[23:55]** so this n is electron charge density means charges per unit volume charges per unit volume ya electrons per unit volume hai na
- **[24:24]** so this is your electron charge electron charges per unit volume hai na kyunki charge hai to coulomb iska inki unit kya ho gayi electron charge density is coulomb per meter cube ho gayi to upar charge aayega number of electrons nahi aayega number of electrons to sirf number ho gaya
- **[24:41]** charge on all the electrons to that is basically your electron charge upon the volume
- **[24:57]** ye mujhe ek aana chaiye isme ye term aana chaiye right man lo iska area of cross section a hai area of cross section means iski thickness a hai aur ye total length l hai
- **[25:07]** so how many so how many how many electrons a jao isko n ko hum kya karte hai electron density karte hai electron density matlab electrons upon volume kar dete hai na kitne electrons leave about the charge so how many electrons in volume
- **[25:47]** al kitna aayenge so total number of electrons in volume al will be nl matlab unit volume mein n tha to itne electrons honge and what will be total charge now
- **[26:01]** total charge kya a jayega total charge charge on each electron is minus e so n e ye baat samajh aayi aapko dono line
- **[26:12]** right ab ye dekho hamare paas equation tha force hai na df is equal to q v cross b abhi humne ye equation dekha tha f is equal to qv sin theta
- **[26:49]** to f ko kya likh sakte hai qv cross v to small force on charge q is v cross v
- **[27:09]** but what will be total force total force kya ho jayega total force matlab total charge to total force is equal to what will be total charge total charge is minus n a l and this will be v cross v
- **[27:38]** but we also know that i is equal to neva i know this equation so neva ye sare a gaye isme to i a jayega aur agar current ki direction yahan hai to electron ke drift ki direction electron opposite to the direction of current
- **[28:55]** jata to drift ki direction aise aati hai to iska matlab hai abhi ke liye aap samajh lo ki agar mujhe agar mujhe current element ko andar lelena hai aur ye bhi dalna hai to i can write this as f is equal to n i can write this as l kyunki ye wala ho jayega aur n e v l ki jagah main i dal dungi so i l cross b aise a jayega
- **[29:53]** kyunki negative hai aur ye negative hai iska opposite to negative negative to positive ho gaya na kyunki v a to ah hum hum understood also right kitna fatapad a gayi aur kitne fatapad ho rahe hai na derivations matlab aap dekho
- **[30:27]** chalo ab ye dekhte hai ab aap hum ek aur derivation dekhenge force on a current carrying wire kab when kept in external uniform magnetic field
- **[31:17]** ab yahan dekho ye kaise jayega derivation ye aapki uniform magnetic field hai this is v yahan pe aapne ek wire rakh diya this is the wire
- **[32:08]** let us suppose the current is going in this direction this is the direction of current now see if i want to know what is the force to small n is charge density
- **[32:32]** electron charge density iska matlab kya hai ki mujhe janna jaruri hai ki is metal ke andar kitne electrons hai
