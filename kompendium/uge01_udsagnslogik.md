# Uge 1: Udsagnslogik

## Hvad er et udsagn?

Et **udsagn** (eller en **proposition**) er en sætning, som enten er **sand (T)** eller **falsk (F)** – aldrig begge dele og aldrig "halvt sandt". 

**Eksempler på udsagn:**
- "6 er et lige tal" → T (sand)
- "3 > 7" → F (falsk)
- "$\pi$ er et rationalt tal" → F (falsk)

**Ikke udsagn:**
- "Hvad er klokken?" (spørgsmål)
- "Luk døren!" (opfordring)
- "$x > 5$" (afhænger af $x$ – ikke entydigt sandt/falsk)

Vi bruger typisk store bogstaver som $P$, $Q$, $R$ til at betegne udsagn.

---

## De logiske operatorer

### Negation: $\neg P$ ("ikke P")

Negationen vender sandhedsværdien:

| $P$ | $\neg P$ |
|:---:|:---:|
| T | F |
| F | T |

**Eksempel:** Hvis $P$ = "Solen skinner", så er $\neg P$ = "Solen skinner ikke."

### Konjunktion: $P \wedge Q$ ("P og Q")

Sandt kun når **begge** udsagn er sande:

| $P$ | $Q$ | $P \wedge Q$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

### Disjunktion: $P \vee Q$ ("P eller Q")

Sandt når **mindst ét** af udsagnene er sandt:

| $P$ | $Q$ | $P \vee Q$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

⚠️ **Vigtigt:** I matematik er "eller" **inklusivt** – det udelukker **ikke** at begge kan være sande! I daglig tale bruges "eller" ofte eksklusivt (enten det ene eller det andet, men ikke begge).

### Implikation: $P \Rightarrow Q$ ("P medfører Q" / "hvis P, så Q")

| $P$ | $Q$ | $P \Rightarrow Q$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

⚠️ **Vigtigt:** Implikationen er kun **falsk** når $P$ er sand og $Q$ er falsk. Hvis $P$ er falsk, er implikationen **altid sand** – uanset $Q$. Det kaldes "ex falso quodlibet" (fra noget falsk følger hvad som helst).

**Huskemåde:** "En løgner lyver kun, hvis han siger noget, og det viser sig at være forkert."

### Biimplikation: $P \Leftrightarrow Q$ ("P hvis og kun hvis Q")

| $P$ | $Q$ | $P \Leftrightarrow Q$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

Biimplikation er sand, når begge udsagn har **samme** sandhedsværdi.

$P \Leftrightarrow Q$ er logisk ækvivalent med $(P \Rightarrow Q) \wedge (Q \Rightarrow P)$.

---

## Sådan laver du en sandhedstabel

### Opskrift:

1. **Identificér de atomiske udsagn** ($P$, $Q$, evt. $R$)
2. **Skriv alle kombinationer af T/F:**
   - Med 2 udsagn: $2^2 = 4$ rækker
   - Med 3 udsagn: $2^3 = 8$ rækker
3. **Byg udtrykket op indefra og ud** – beregn delresultater
4. **Udfyld den endelige kolonne**

### Gennemregnet eksempel:

Lav sandhedstabel for $(P \vee Q) \wedge \neg(P \wedge Q)$:

| $P$ | $Q$ | $P \vee Q$ | $P \wedge Q$ | $\neg(P \wedge Q)$ | $(P \vee Q) \wedge \neg(P \wedge Q)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | F | **F** |
| T | F | T | F | T | **T** |
| F | T | T | F | T | **T** |
| F | F | F | F | T | **F** |

Bemærk: Dette udtryk er "eksklusiv eller" (XOR) – sandt netop når **præcis ét** af udsagnene er sandt.

---

## Logisk ækvivalens

To logiske udtryk er **logisk ækvivalente** hvis de har **identiske sandhedstabeller** (dvs. identiske kolonner i den endelige kolonne).

### De vigtigste ækvivalenser:

**De Morgans love** (ekstremt vigtige!):
- $\neg(P \wedge Q) \equiv \neg P \vee \neg Q$
- $\neg(P \vee Q) \equiv \neg P \wedge \neg Q$

**Huskemåde:** Negation "vender" både operatoren ($\wedge \leftrightarrow \vee$) og udsagnene.

**Kontraposition:**
- $P \Rightarrow Q \equiv \neg Q \Rightarrow \neg P$

**Andre nyttige:**
- $P \Rightarrow Q \equiv \neg P \vee Q$
- $\neg(\neg P) \equiv P$ (dobbelt negation)
- $P \wedge (Q \vee R) \equiv (P \wedge Q) \vee (P \wedge R)$ (distributiv lov)

### Sådan viser du logisk ækvivalens:

**Metode:** Lav sandhedstabeller for begge udtryk og sammenlign kolonnerne.

**Eksempel:** Vis at $\neg(P \wedge Q) \equiv \neg P \vee \neg Q$ (De Morgans lov):

| $P$ | $Q$ | $P \wedge Q$ | $\neg(P \wedge Q)$ | $\neg P$ | $\neg Q$ | $\neg P \vee \neg Q$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | **F** | F | F | **F** |
| T | F | F | **T** | F | T | **T** |
| F | T | F | **T** | T | F | **T** |
| F | F | F | **T** | T | T | **T** |

Kolonne 4 og 7 er identiske ✓ → de er logisk ækvivalente.

---

## Tautologier

En **tautologi** er et logisk udtryk, der **altid er sandt**, uanset sandhedsværdierne af de indgående udsagn.

**Eksempler:**
- $P \vee \neg P$ (udsagnet er sandt, eller det er ikke sandt – altid sandt!)
- $(P \vee Q) \vee (\neg P \wedge \neg Q)$ (enten mindst ét er sandt, eller ingen er sande – altid sandt!)
- $(P \Rightarrow Q) \vee (Q \Rightarrow P)$ (altid sandt – tjek med sandhedstabel!)

**Metode:** Lav sandhedstabellen og kontrollér at **alle rækker giver T**.

---

## Bevistyper

### Direkte bevis

Du vil vise $P \Rightarrow Q$:
1. **Antag** at $P$ er sandt
2. **Udled** logisk at $Q$ også er sandt
3. **Konklusion:** $P \Rightarrow Q$ er vist

### Kontrapositionsbevis

Du vil vise $P \Rightarrow Q$, men viser i stedet $\neg Q \Rightarrow \neg P$ (som er logisk ækvivalent):
1. **Antag** at $Q$ er falsk ($\neg Q$ er sandt)
2. **Udled** at $P$ også er falsk ($\neg P$ er sandt)
3. **Konklusion:** $P \Rightarrow Q$ er vist (via kontraposition)

**Gennemregnet eksempel:** Vis at "hvis $a^2$ er lige, så er $a$ lige" for heltal $a$.

Vi viser kontrapositivt: "Hvis $a$ er ulige, så er $a^2$ ulige."

Antag at $a$ er ulige. Så $a = 1 + 2c$ for et heltal $c$.

$$a^2 = (1+2c)^2 = 1 + 4c + 4c^2 = 1 + 2(2c + 2c^2)$$

Da $2c + 2c^2$ er et heltal, er $a^2$ på formen $1 + 2k$, dvs. $a^2$ er ulige. ✓

### Modstridsbevis (bevis ved modstrid)

Du vil vise $P$:
1. **Antag** at $P$ er falsk ($\neg P$ er sandt)
2. **Udled** en **modstrid** (noget der er selvmodsigende, f.eks. $0 = 1$)
3. **Konklusion:** $\neg P$ kan ikke være sandt, så $P$ er sandt

**Gennemregnet eksempel:** Vis at diskriminanten $D = b^2 - 4c$ aldrig kan være lig 2 for $b, c \in \mathbb{Z}$.

Antag at $D = 2$, dvs. $b^2 - 4c = 2$, altså $b^2 = 2 + 4c = 2(1 + 2c)$.

Så $b^2$ er lige, og dermed er $b$ lige (vist ovenfor). Skriv $b = 2k$.

Så $4k^2 = 2 + 4c$, dvs. $4k^2 - 4c = 2$, altså $2(2k^2 - 2c) = 2$, dvs. $2k^2 - 2c = 1$.

Men venstresiden er lige og højresiden er ulige – **modstrid!** ✓

---

## NAND-operatoren (bonusstof)

NAND ($\uparrow$) er "not and": $A \uparrow B \equiv \neg(A \wedge B)$

| $A$ | $B$ | $A \uparrow B$ |
|:---:|:---:|:---:|
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | T |

**Vigtige egenskaber:**
- $A \uparrow A \equiv \neg A$ (NAND med sig selv giver negation)
- $(A \uparrow B) \uparrow (A \uparrow B) \equiv A \wedge B$ (dobbelt NAND giver AND)
- Alle logiske operatorer kan bygges fra NAND alene

---

## Typiske fejl at undgå

1. **Forveksling af $\vee$ og XOR:** Matematisk "eller" inkluderer "begge sande"
2. **Implikation med falsk præmis:** $F \Rightarrow Q$ er altid sand!
3. **Glemmer at tjekke alle rækker** i sandhedstabellen
4. **Forveksler $P \Rightarrow Q$ med $Q \Rightarrow P$:** De er IKKE logisk ækvivalente (den omvendte er konversen)
5. **Kontraposition vs. konvers:** $P \Rightarrow Q \equiv \neg Q \Rightarrow \neg P$ (kontraposition, ækvivalent), men $P \Rightarrow Q \not\equiv Q \Rightarrow P$ (konvers, IKKE ækvivalent)
