# Uge 7: Matrixalgebra og determinanter

## Matrixoperationer

### Matrixaddition

To matricer $\mathbf{A}$ og $\mathbf{B}$ af **samme dimension** $m \times n$ lægges sammen elementvist:

$$(\mathbf{A} + \mathbf{B})_{ij} = a_{ij} + b_{ij}$$

### Skalarmultiplikation

$$(\alpha \mathbf{A})_{ij} = \alpha \cdot a_{ij}$$

### Matrixmultiplikation

For $\mathbf{A}$ ($m \times p$) og $\mathbf{B}$ ($p \times n$): Produktet $\mathbf{A}\mathbf{B}$ er en $m \times n$ matrix.

$$(\mathbf{A}\mathbf{B})_{ij} = \sum_{k=1}^{p} a_{ik} \cdot b_{kj}$$

**Huskemåde:** "Række gange søjle" – element $(i,j)$ i produktet er prikproduktet af $i$'te **række** i $\mathbf{A}$ med $j$'te **søjle** i $\mathbf{B}$.

### Gennemregnet eksempel

$$\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 1\cdot5 + 2\cdot7 & 1\cdot6 + 2\cdot8 \\ 3\cdot5 + 4\cdot7 & 3\cdot6 + 4\cdot8 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}$$

⚠️ **Vigtigt:** Matrixmultiplikation er **IKKE kommutativ**: $\mathbf{AB} \neq \mathbf{BA}$ generelt!

### Vigtige regneregler

- $\mathbf{A}(\mathbf{B} + \mathbf{C}) = \mathbf{AB} + \mathbf{AC}$ (distributiv)
- $\mathbf{A}(\mathbf{BC}) = (\mathbf{AB})\mathbf{C}$ (associativ)
- $\mathbf{AI} = \mathbf{IA} = \mathbf{A}$ (identitetsmatrix)
- $(\mathbf{AB})^T = \mathbf{B}^T \mathbf{A}^T$ (rækkefølgen bytter!)

---

## Transponering

Den **transponerede** $\mathbf{A}^T$ fås ved at bytte rækker og søjler:

$$(\mathbf{A}^T)_{ij} = a_{ji}$$

**Eksempel:**
$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}^T = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}$$

---

## Invers matrix

### Definition

$\mathbf{A}^{-1}$ er den **inverse** af $\mathbf{A}$ hvis:

$$\mathbf{A} \mathbf{A}^{-1} = \mathbf{A}^{-1} \mathbf{A} = \mathbf{I}$$

Kun **kvadratiske** matricer kan have en invers, og ikke alle har det.

$\mathbf{A}$ er **invertibel** (regulær) $\iff$ $\det(\mathbf{A}) \neq 0$.

### Opskrift: Find $\mathbf{A}^{-1}$ med Gauss-Jordan

1. Opskriv $[\mathbf{A} | \mathbf{I}]$
2. Reducér venstresiden til $\mathbf{I}$ med rækkeoperationer
3. Højresiden er nu $\mathbf{A}^{-1}$: $[\mathbf{I} | \mathbf{A}^{-1}]$

### For $2 \times 2$ matricer (hurtig formel):

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix}^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

(kun hvis $ad - bc \neq 0$)

### Gennemregnet eksempel

Find inversen af $\mathbf{A} = \begin{bmatrix} 2 & 1 \\ 5 & 3 \end{bmatrix}$:

$\det(\mathbf{A}) = 2 \cdot 3 - 1 \cdot 5 = 1 \neq 0$ ✓

$$\mathbf{A}^{-1} = \frac{1}{1} \begin{bmatrix} 3 & -1 \\ -5 & 2 \end{bmatrix} = \begin{bmatrix} 3 & -1 \\ -5 & 2 \end{bmatrix}$$

---

## Determinanter

### Definition for $2 \times 2$

$$\det\begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc$$

### Definition for $3 \times 3$ (kofaktorudvikling langs 1. række)

$$\det\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} = a\det\begin{bmatrix} e & f \\ h & i \end{bmatrix} - b\det\begin{bmatrix} d & f \\ g & i \end{bmatrix} + c\det\begin{bmatrix} d & e \\ g & h \end{bmatrix}$$

$$= a(ei-fh) - b(di-fg) + c(dh-eg)$$

### Huskemåde for fortegn (skaktavlemønster)

$$\begin{bmatrix} + & - & + \\ - & + & - \\ + & - & + \end{bmatrix}$$

### Vigtige egenskaber af determinanter

- $\det(\mathbf{I}) = 1$
- $\det(\mathbf{AB}) = \det(\mathbf{A}) \cdot \det(\mathbf{B})$
- $\det(\mathbf{A}^T) = \det(\mathbf{A})$
- $\det(\alpha \mathbf{A}) = \alpha^n \det(\mathbf{A})$ for $n \times n$ matrix
- $\det(\mathbf{A}^{-1}) = \frac{1}{\det(\mathbf{A})}$
- Bytning af to rækker: ændrer fortegn på determinanten
- Lægge multiplum af én række til en anden: ændrer **ikke** determinanten
- En række af nuller: $\det = 0$
- To identiske rækker: $\det = 0$

### Gennemregnet eksempel ($3\times3$)

$$\det\begin{bmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{bmatrix} = 1 \cdot 4 \cdot 6 = 24$$

For **trekantsmatricer** (øvre eller nedre) er determinanten = produktet af diagonalelementerne!

---

## Sammenhæng: Invertibilitet

Følgende er ækvivalente for en $n \times n$ matrix $\mathbf{A}$:

- $\mathbf{A}$ er invertibel
- $\det(\mathbf{A}) \neq 0$
- $\text{rang}(\mathbf{A}) = n$
- Systemet $\mathbf{Ax} = \mathbf{b}$ har en entydig løsning for ethvert $\mathbf{b}$
- $\mathbf{A}$ kan reduceres til $\mathbf{I}$ via rækkeoperationer

---

## Typiske fejl at undgå

1. **$\mathbf{AB} \neq \mathbf{BA}$** – matrixmultiplikation er IKKE kommutativ!
2. **Dimensioner skal passe:** $\mathbf{A}$ ($m \times p$) gange $\mathbf{B}$ ($p \times n$) – antallet af søjler i $\mathbf{A}$ skal matche antallet af rækker i $\mathbf{B}$
3. **$(\mathbf{AB})^T = \mathbf{B}^T\mathbf{A}^T$** – rækkefølgen bytter!
4. **Fortegnsfejl i kofaktorudvikling** – brug skaktavlemønsteret
5. **$\det(\mathbf{A}+\mathbf{B}) \neq \det(\mathbf{A}) + \det(\mathbf{B})$** – determinanten er IKKE lineær i matricer!
