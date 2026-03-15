# Uge 2: Mængder og funktioner

## Mængder

En **mængde** er en samling af objekter (kaldet **elementer**). Vi skriver $a \in A$ for "$a$ er et element i mængden $A$".

### Notation

**Listeform:** $A = \{1, 4, 9, 16, 25\}$

**Beskrivelseform:** $A = \{n \in \mathbb{N} \mid n = m^2 \text{ hvor } m \in \{1,2,3,4,5\}\}$

### Vigtige talmængder

| Symbol | Navn | Indhold |
|:---:|:---|:---|
| $\mathbb{N}$ | Naturlige tal | $\{0, 1, 2, 3, \ldots\}$ (pas på: inkluderer 0 i dette kursus) |
| $\mathbb{Z}$ | Hele tal | $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$ |
| $\mathbb{Q}$ | Rationale tal | Brøker $\frac{p}{q}$ hvor $p, q \in \mathbb{Z}$, $q \neq 0$ |
| $\mathbb{R}$ | Reelle tal | Hele tallinjen |

**Delmængde:** $A \subseteq B$ betyder at ethvert element i $A$ også er i $B$.

---

## Mængdeoperationer

### Fællesmængde (snit): $A \cap B$

$$A \cap B = \{x \mid x \in A \wedge x \in B\}$$

Elementer der er i **begge** mængder.

### Foreningsmængde: $A \cup B$

$$A \cup B = \{x \mid x \in A \vee x \in B\}$$

Elementer der er i **mindst én** af mængderne.

### Mængdedifferens: $A \setminus B$

$$A \setminus B = \{x \mid x \in A \wedge x \notin B\}$$

Elementer der er i $A$ men **ikke** i $B$.

### Gennemregnet eksempel

Lad $A = \{1, 4, 9, 16, 25\}$ og $B = \{1, 3, 5, 7, 9\}$.

- $A \cap B = \{1, 9\}$ (de fælles elementer)
- $A \cup B = \{1, 3, 4, 5, 7, 9, 16, 25\}$ (alle elementer samlet)
- $A \setminus B = \{4, 16, 25\}$ (i $A$ men ikke i $B$)
- $B \setminus A = \{3, 5, 7\}$ (i $B$ men ikke i $A$)

### Kardinalitetsformlen

For endelige mængder:

$$|A \cup B| = |A| + |B| - |A \cap B|$$

Vi trækker $|A \cap B|$ fra, fordi de fælles elementer ellers tælles dobbelt.

### Vigtige regneregler (Sætning 2.1.2)

**De Morgans love for mængder:**
- $(A \cup B)^c = A^c \cap B^c$
- $(A \cap B)^c = A^c \cup B^c$

**Distributive love:**
- $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
- $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$

---

## Funktioner

En **funktion** $f: A \to B$ er en regel, der til hvert element $x \in A$ knytter præcis ét element $f(x) \in B$.

### Vigtige begreber

| Begreb | Symbol/notation | Forklaring |
|:---|:---|:---|
| **Definitionsmængde** | $A$ (i $f: A \to B$) | Mængden af mulige input |
| **Dispositionsmængde** | $B$ (i $f: A \to B$) | Mængden hvor output *kan* ligge |
| **Værdimængde** (billedmængde) | $f(A)$ | Mængden af *faktiske* output: $\{f(x) \mid x \in A\}$ |
| **Funktionsforskrift** | $f(x) = \ldots$ | Reglen der bestemmer output |

⚠️ **Vigtigt:** Værdimængden er altid en delmængde af dispositionsmængden: $f(A) \subseteq B$. De behøver ikke være ens!

---

## Injektiv, surjektiv og bijektiv

### Injektiv (en-til-en)

$f$ er **injektiv** hvis forskellige input altid giver forskellige output:

$$f(x_1) = f(x_2) \Rightarrow x_1 = x_2$$

**Huskemåde:** Ingen to pile rammer det samme mål. Hvert element i $B$ rammes af **højst ét** element fra $A$.

**Tjek-metode:** Antag $f(x_1) = f(x_2)$ og vis at $x_1 = x_2$, ELLER find et modeksempel (to forskellige $x$-værdier der giver samme $f$-værdi).

### Surjektiv (på)

$f$ er **surjektiv** hvis ethvert element i $B$ rammes:

$$\forall b \in B \, \exists a \in A: f(a) = b$$

**Huskemåde:** Værdimængden er lig dispositionsmængden: $f(A) = B$.

**Tjek-metode:** For vilkårligt $b \in B$, vis at ligningen $f(x) = b$ har mindst én løsning $x \in A$.

### Bijektiv

$f$ er **bijektiv** hvis den er **både injektiv og surjektiv**.

**Huskemåde:** Hvert element i $B$ rammes af **præcis ét** element fra $A$.

### Gennemregnet eksempel

Lad $A = \{1,2,3,4,5,6,7\}$, $B = \{1,4,9,16,25,36,49\}$ og $f: A \to B$ med $f(x) = x^2$.

- **Injektiv?** Ja – alle $x \in A$ er positive, så $x_1^2 = x_2^2 \Rightarrow x_1 = x_2$.
- **Surjektiv?** Ja – hvert element i $B$ er $m^2$ for et $m \in A$.
- **Bijektiv?** Ja – den er begge dele.

Lad nu $D = \{x \in \mathbb{Z} \mid -7 \leq x \leq 7, x \neq 0\}$ og $g: D \to B$ med $g(x) = x^2$.

- **Injektiv?** Nej – f.eks. $g(3) = g(-3) = 9$.
- **Surjektiv?** Ja – hvert element i $B$ rammes.

---

## Sammensatte funktioner

Givet $f: A \to B$ og $g: B \to C$ er den **sammensatte funktion** $g \circ f: A \to C$ defineret ved:

$$(g \circ f)(x) = g(f(x))$$

⚠️ **Vigtigt:** $g \circ f$ læses "g efter f" – man udfører $f$ **først**, derefter $g$.

⚠️ **Bemærk:** $g \circ f$ er kun defineret når $f$'s dispositionsmængde er lig $g$'s definitionsmængde.

### Gennemregnet eksempel

Lad $A = \{0, 1, 2\}$, $f: A \to A$ med $f(x) = 2-x$, og $g: A \to \mathbb{R}$ med $g(x) = 2x + e^x$.

**Er $f \circ g$ defineret?** Nej! $g$'s dispositionsmængde er $\mathbb{R}$, men $f$'s definitionsmængde er $A$.

**Er $g \circ f$ defineret?** Ja! $f$'s dispositionsmængde er $A = g$'s definitionsmængde.

**Beregning:** $(g \circ f)(x) = g(f(x)) = g(2-x) = 2(2-x) + e^{2-x} = 4 - 2x + e^{2-x}$

- $(g \circ f)(0) = 4 + e^2$
- $(g \circ f)(1) = 2 + e$
- $(g \circ f)(2) = 0 + e^0 = 1$

---

## Inverse funktioner

Hvis $f: A \to B$ er **bijektiv**, eksisterer den **inverse funktion** $f^{-1}: B \to A$ hvor:

$$f^{-1}(y) = x \iff f(x) = y$$

### Opskrift til at finde $f^{-1}$:

1. Skriv $y = f(x)$
2. Isolér $x$ som funktion af $y$
3. Det giver dig $x = f^{-1}(y)$
4. (Evt. ombyt $x$ og $y$ for at skrive $f^{-1}(x) = \ldots$)

### Gennemregnet eksempel

Find den inverse til $h_1(x) = 2x^2 - 20x + 57$ for $x \geq 5$ (med dispositionsmængde $\mathbb{R}_{\geq 7}$).

1. Sæt $y = 2x^2 - 20x + 57$
2. Kvadratkompleter: $y = 2(x-5)^2 + 7$
3. Isolér: $y - 7 = 2(x-5)^2$, så $(x-5)^2 = \frac{y-7}{2}$
4. $x - 5 = \sqrt{\frac{y-7}{2}}$ (positiv rod, da $x \geq 5$)
5. $x = 5 + \sqrt{\frac{y-7}{2}}$

Altså: $h_1^{-1}(y) = 5 + \sqrt{\frac{y-7}{2}}$ med definitionsmængde $\mathbb{R}_{\geq 7}$.

---

## Rekursivt definerede funktioner og sumtegnet

### Rekursion

En funktion defineres **rekursivt** ved:
1. En **startværdi** (basistilfælde), f.eks. $a_0 = 1$
2. En **rekursionsregel**, f.eks. $a_{n+1} = 2 \cdot a_n + 1$

### Sumtegnet

$$\sum_{k=m}^{n} f(k) = f(m) + f(m+1) + \cdots + f(n)$$

**Eksempel:** $\sum_{k=1}^{4} k^2 = 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = 30$

---

## Typiske fejl at undgå

1. **Forveksler dispositionsmængde og værdimængde:** Dispositionsmængden er "hvad output *kan* være", værdimængden er "hvad output *faktisk* er"
2. **Glemmer at tjekke definitionsmængden** ved sammensatte funktioner
3. **Rækkefølge i sammensætning:** $(g \circ f)(x) = g(f(x))$ – $f$ først!
4. **Kun én retning ved injektivitet:** Du skal vise at $f(x_1)=f(x_2) \Rightarrow x_1=x_2$, ikke omvendt
5. **Glemmer at funktionen skal være bijektiv** for at have en invers
