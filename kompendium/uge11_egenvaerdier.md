# Uge 11: Egenværdier, egenvektorer og diagonalisering

## Egenværdier og egenvektorer

### Definition

Lad $\mathbf{A}$ være en $n \times n$ matrix. En skalar $\lambda$ er en **egenværdi** for $\mathbf{A}$ hvis der findes en **ikke-nul** vektor $\mathbf{v}$ så:

$$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$$

Vektoren $\mathbf{v} \neq \mathbf{0}$ kaldes en **egenvektor** hørende til $\lambda$.

**Geometrisk:** En egenvektor er en vektor, som $\mathbf{A}$ blot skalerer (strækker/komprimerer/vender), men ikke ændrer retningen af.

⚠️ **Vigtigt:** Nulvektoren $\mathbf{0}$ er **aldrig** en egenvektor (selvom $\mathbf{A}\mathbf{0} = \lambda\mathbf{0}$ altid gælder).

### Tjek om en vektor er en egenvektor

**Opskrift:** Beregn $\mathbf{A}\mathbf{v}$ og se om resultatet er et skalarmultiplum af $\mathbf{v}$.

**Gennemregnet eksempel:**

$\mathbf{A} = \begin{bmatrix} -5 & 10 \\ 1 & 4 \end{bmatrix}$, er $\mathbf{v} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ en egenvektor?

$\mathbf{A}\mathbf{v} = \begin{bmatrix} -5+10 \\ 1+4 \end{bmatrix} = \begin{bmatrix} 5 \\ 5 \end{bmatrix} = 5\begin{bmatrix} 1 \\ 1 \end{bmatrix} = 5\mathbf{v}$

Ja! Egenvektor med egenværdi $\lambda = 5$. ✓

---

## Det karakteristiske polynomium

### Opskrift: Find alle egenværdier

$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$ kan omskrives til:

$$(\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$$

Denne ligning har en ikke-triviel løsning $\mathbf{v} \neq \mathbf{0}$ præcis når:

$$\det(\mathbf{A} - \lambda\mathbf{I}) = 0$$

Polynomiet $p(\lambda) = \det(\mathbf{A} - \lambda\mathbf{I})$ kaldes det **karakteristiske polynomium**.

### Gennemregnet eksempel ($2 \times 2$)

Find egenværdierne for $\mathbf{A} = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$:

$$\det(\mathbf{A} - \lambda\mathbf{I}) = \det\begin{bmatrix} 3-\lambda & 1 \\ 0 & 2-\lambda \end{bmatrix} = (3-\lambda)(2-\lambda) - 0 = 0$$

$$\lambda^2 - 5\lambda + 6 = 0 \implies (\lambda - 3)(\lambda - 2) = 0$$

**Egenværdier:** $\lambda_1 = 3$ og $\lambda_2 = 2$.

### Gennemregnet eksempel ($3 \times 3$)

Find egenværdierne for $\mathbf{A} = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix}$:

$$\det(\mathbf{A} - \lambda\mathbf{I}) = (2-\lambda)(2-\lambda)(3-\lambda) = 0$$

**Egenværdier:** $\lambda_1 = 2$ (med algebraisk multiplicitet 2) og $\lambda_2 = 3$ (med algebraisk multiplicitet 1).

---

## Egenrum

**Egenrummet** hørende til egenværdien $\lambda$ er:

$$E_\lambda = \ker(\mathbf{A} - \lambda\mathbf{I}) = \{\mathbf{v} \mid (\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}\}$$

### Opskrift: Find egenvektorer

1. Find egenværdierne fra det karakteristiske polynomium
2. For hver egenværdi $\lambda$: Løs $(\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$ med Gauss elimination
3. De frie variable giver basisvektorer for egenrummet

### Gennemregnet eksempel (fortsat)

For $\mathbf{A} = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$ med $\lambda_1 = 3$:

$$(\mathbf{A} - 3\mathbf{I})\mathbf{v} = \begin{bmatrix} 0 & 1 \\ 0 & -1 \end{bmatrix}\mathbf{v} = \mathbf{0}$$

Gauss: $v_2 = 0$, $v_1$ fri. Egenrum: $E_3 = \text{span}\left\{\begin{bmatrix} 1 \\ 0 \end{bmatrix}\right\}$.

For $\lambda_2 = 2$:

$$(\mathbf{A} - 2\mathbf{I})\mathbf{v} = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}\mathbf{v} = \mathbf{0}$$

$v_1 + v_2 = 0$, så $v_1 = -v_2$. Egenrum: $E_2 = \text{span}\left\{\begin{bmatrix} -1 \\ 1 \end{bmatrix}\right\}$.

---

## Algebraisk og geometrisk multiplicitet

- **Algebraisk multiplicitet** af $\lambda$: Multipliciteten af $\lambda$ som rod i det karakteristiske polynomium.
- **Geometrisk multiplicitet** af $\lambda$: $\dim(E_\lambda)$ = antal lineært uafhængige egenvektorer.

**Altid:** $1 \leq \text{geo. mult.} \leq \text{alg. mult.}$

---

## Diagonalisering

### Hvornår er en matrix diagonaliserbar?

$\mathbf{A}$ er **diagonaliserbar** $\iff$ der findes en basis for hele rummet bestående af egenvektorer.

Ækvivalent: den geometriske multiplicitet er lig den algebraiske for **alle** egenværdier.

### Opskrift: Diagonalisér $\mathbf{A}$

1. Find alle egenværdier $\lambda_1, \ldots, \lambda_k$
2. Find en basis for hvert egenrum $E_{\lambda_i}$
3. Tjek at det samlede antal lineært uafhængige egenvektorer = $n$
4. Lad $\mathbf{P}$ = matricen med egenvektorerne som søjler
5. Lad $\mathbf{D}$ = diagonalmatrix med egenværdierne på diagonalen
6. Så gælder: $\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$ (eller $\mathbf{D} = \mathbf{P}^{-1}\mathbf{A}\mathbf{P}$)

### Gennemregnet eksempel (fortsat)

$\mathbf{P} = \begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}$, $\mathbf{D} = \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}$

Tjek: $\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$ ✓

### Hvornår er $\mathbf{A}$ IKKE diagonaliserbar?

Hvis der for en egenværdi gælder: geometrisk multiplicitet $<$ algebraisk multiplicitet.

**Eksempel:** $\mathbf{A} = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}$ har $\lambda = 2$ med alg. mult. 2, men geo. mult. 1 → **ikke diagonaliserbar**.

---

## Komplekse egenværdier

For en **reel** matrix: komplekse egenværdier optræder altid i **konjugerede par** $\lambda$ og $\bar{\lambda}$.

De tilhørende egenvektorer er også konjugerede: $\mathbf{v}$ og $\bar{\mathbf{v}}$.

### Gennemregnet eksempel

$\mathbf{A} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ (rotation $90°$)

$\det(\mathbf{A} - \lambda\mathbf{I}) = \lambda^2 + 1 = 0 \implies \lambda = \pm i$

For $\lambda = i$: $\begin{bmatrix} -i & -1 \\ 1 & -i \end{bmatrix}\mathbf{v} = \mathbf{0}$, giver $\mathbf{v} = \begin{bmatrix} i \\ 1 \end{bmatrix}$.

For $\lambda = -i$: $\mathbf{v} = \begin{bmatrix} -i \\ 1 \end{bmatrix} = \overline{\begin{bmatrix} i \\ 1 \end{bmatrix}}$ ✓

---

## Nyttige egenskaber

- Summen af egenværdierne = sporet ($\text{tr}(\mathbf{A})$ = summen af diagonalelementerne)
- Produktet af egenværdierne = $\det(\mathbf{A})$
- Egenvektorer hørende til **forskellige** egenværdier er altid lineært uafhængige
- Trekantsmatricers egenværdier = diagonalelementerne

---

## Typiske fejl at undgå

1. **$\mathbf{0}$ er aldrig en egenvektor!** Men $\lambda = 0$ kan godt være en egenværdi
2. **Glemmer at finde ALLE egenvektorer** – løs det homogene system fuldstændigt
3. **Rækkefølgen i $\mathbf{P}$ og $\mathbf{D}$:** Søjle $j$ i $\mathbf{P}$ skal svare til diagonalelement $j$ i $\mathbf{D}$
4. **Antager at alle matricer er diagonaliserbare** – tjek altid multipliciteterne!
5. **Fortegnsfejl** i $\mathbf{A} - \lambda\mathbf{I}$ – det er $\mathbf{A}$ minus $\lambda$ gange identiteten
