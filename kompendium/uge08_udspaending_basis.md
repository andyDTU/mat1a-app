# Uge 8: Udspænding, ordnet basis og koordinater

## Linearkombination

En **linearkombination** af vektorer $\mathbf{v}_1, \ldots, \mathbf{v}_k$ er:

$$\alpha_1 \mathbf{v}_1 + \alpha_2 \mathbf{v}_2 + \cdots + \alpha_k \mathbf{v}_k$$

hvor $\alpha_1, \ldots, \alpha_k$ er skalarer.

---

## Udspænding (span)

**Udspændingen** af vektorerne $\mathbf{v}_1, \ldots, \mathbf{v}_k$ er mængden af **alle** linearkombinationer:

$$\text{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\} = \{\alpha_1 \mathbf{v}_1 + \cdots + \alpha_k \mathbf{v}_k \mid \alpha_i \in \mathbb{R}\}$$

### Tjek om $\mathbf{w}$ ligger i udspændingen

**Spørgsmål:** Er $\mathbf{w} \in \text{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$?

**Metode:** Løs ligningssystemet $\alpha_1\mathbf{v}_1 + \cdots + \alpha_k\mathbf{v}_k = \mathbf{w}$ med Gauss elimination. Hvis systemet har en løsning, er svaret ja.

---

## Lineær uafhængighed

Vektorer $\mathbf{v}_1, \ldots, \mathbf{v}_k$ er **lineært uafhængige** hvis:

$$\alpha_1 \mathbf{v}_1 + \cdots + \alpha_k \mathbf{v}_k = \mathbf{0} \implies \alpha_1 = \cdots = \alpha_k = 0$$

Dvs. den eneste linearkombination der giver nulvektoren er den trivielle (alle $\alpha_i = 0$).

**Lineært afhængige** = mindst én vektor kan skrives som linearkombination af de andre.

### Opskrift: Tjek lineær uafhængighed

1. Opskriv vektorerne som søjler i en matrix $\mathbf{A}$
2. Reducér til trappeform med Gauss elimination
3. **Lineært uafhængige** $\iff$ ingen frie variable $\iff$ hver søjle har et pivot

---

## Basis

En **ordnet basis** for et underrum $V$ er en ordnet mængde vektorer $(\mathbf{v}_1, \ldots, \mathbf{v}_n)$ som:

1. **Udspænder** $V$: $\text{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_n\} = V$
2. Er **lineært uafhængige**

### Standardbasis for $\mathbb{R}^n$

$$\mathbf{e}_1 = \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix}, \quad \mathbf{e}_2 = \begin{bmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{bmatrix}, \quad \ldots, \quad \mathbf{e}_n = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix}$$

---

## Dimension

**Dimensionen** af et underrum $V$ er antallet af vektorer i en basis for $V$.

$$\dim(V) = \text{antal basisvektorer}$$

Alle baser for det samme underrum har **samme antal** vektorer.

---

## Nulrum og søjlerum

### Nulrum

$$\text{nul}(\mathbf{A}) = \{\mathbf{x} \in \mathbb{R}^n \mid \mathbf{A}\mathbf{x} = \mathbf{0}\}$$

Nulrummet er mængden af alle løsninger til det homogene system. Det er et underrum af $\mathbb{R}^n$.

**Opskrift:** Løs $\mathbf{A}\mathbf{x} = \mathbf{0}$ med Gauss elimination. De frie variable giver basisvektorer for nulrummet.

### Søjlerum

$$\text{søjle}(\mathbf{A}) = \text{span}\{\text{søjlerne i } \mathbf{A}\}$$

Det er et underrum af $\mathbb{R}^m$ (for en $m \times n$ matrix).

**Opskrift:** Reducér $\mathbf{A}$ til trappeform. Pivotsøjlerne i den **originale** matrix $\mathbf{A}$ er en basis for søjlerummet.

### Dimensionssætningen

$$\dim(\text{søjle}(\mathbf{A})) + \dim(\text{nul}(\mathbf{A})) = n$$

$$\text{rang}(\mathbf{A}) + \text{nullitet}(\mathbf{A}) = n$$

---

## Koordinater mht. en ordnet basis

Lad $\mathcal{B} = (\mathbf{v}_1, \ldots, \mathbf{v}_n)$ være en ordnet basis for $V$.

Da kan ethvert $\mathbf{w} \in V$ skrives **entydigt** som:

$$\mathbf{w} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n$$

Vektoren $[\mathbf{w}]_{\mathcal{B}} = \begin{bmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{bmatrix}$ er **koordinatvektoren** for $\mathbf{w}$ mht. $\mathcal{B}$.

### Opskrift: Find koordinater

1. Opstil ligningen $c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n = \mathbf{w}$
2. Løs for $c_1, \ldots, c_n$ med Gauss elimination

### Gennemregnet eksempel

Lad $\mathcal{B} = \left(\begin{bmatrix} 1 \\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\ -1 \end{bmatrix}\right)$ og $\mathbf{w} = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$.

Løs $c_1\begin{bmatrix} 1 \\ 1 \end{bmatrix} + c_2\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$:

$$\begin{cases} c_1 + c_2 = 3 \\ c_1 - c_2 = 1 \end{cases}$$

Lægger vi de to ligninger sammen: $2c_1 = 4$, så $c_1 = 2$ og $c_2 = 1$.

$$[\mathbf{w}]_{\mathcal{B}} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$$

---

## Typiske fejl at undgå

1. **Forveksler lineær uafhængighed og udspænding** – de er to forskellige egenskaber
2. **Bruger den reducerede matrix som basis for søjlerummet** – brug søjlerne fra den **originale** matrix!
3. **Glemmer at nulrummet altid indeholder $\mathbf{0}$** – det er et underrum
4. **Forveksler koordinatvektoren med vektoren selv** – $[\mathbf{w}]_\mathcal{B} \neq \mathbf{w}$ generelt
5. **Rækkefølgen i en ordnet basis betyder noget** – $(\mathbf{v}_1, \mathbf{v}_2) \neq (\mathbf{v}_2, \mathbf{v}_1)$ giver forskellige koordinater!
