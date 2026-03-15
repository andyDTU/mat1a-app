# Uge 6: Lineære ligningssystemer og Gauss elimination

## Hvad er et lineært ligningssystem?

Et system af $m$ ligninger med $n$ ubekendte:

$$\begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\ \vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m \end{cases}$$

**Homogent:** Alle $b_i = 0$. **Inhomogent:** Mindst ét $b_i \neq 0$.

---

## Matricer og totalmatrix

### Koefficientmatrix

$$\mathbf{A} = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & & & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}$$

### Totalmatrix (udvidet matrix)

$$[\mathbf{A} | \mathbf{b}] = \left[\begin{array}{cccc|c} a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\ a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\ \vdots & & & \vdots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} & b_m \end{array}\right]$$

---

## Gauss elimination

### De tre tilladte rækkeoperationer

1. **Ombytning:** Byt to rækker
2. **Skalering:** Gang en række med en konstant $\neq 0$
3. **Addition:** Læg et multiplum af én række til en anden

### Opskrift: Gauss elimination

**Mål:** Bring totalmatricen på (reduceret) trappeform.

1. Find det første **pivotelement** (første ikke-nul element i en kolonne)
2. Brug rækkeoperationer til at gøre alle elementer **under** pivotelementet til 0
3. Gå til næste kolonne og gentag
4. For **reduceret** trappeform: Gør også alle elementer **over** pivotelementerne til 0 og skalér pivoterne til 1

### Gennemregnet eksempel

Løs systemet:
$$\begin{cases} x + 2y - z = 3 \\ 2x + 5y + z = 7 \\ x + 3y + 2z = 4 \end{cases}$$

**Totalmatrix:**
$$\left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 2 & 5 & 1 & 7 \\ 1 & 3 & 2 & 4 \end{array}\right]$$

**Trin 1:** $R_2 \leftarrow R_2 - 2R_1$ og $R_3 \leftarrow R_3 - R_1$:

$$\left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 1 & 3 & 1 \\ 0 & 1 & 3 & 1 \end{array}\right]$$

**Trin 2:** $R_3 \leftarrow R_3 - R_2$:

$$\left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 1 & 3 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right]$$

**Trin 3:** Reduceret trappeform: $R_1 \leftarrow R_1 - 2R_2$:

$$\left[\begin{array}{ccc|c} 1 & 0 & -7 & 1 \\ 0 & 1 & 3 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right]$$

**Aflæsning:** $x = 1 + 7z$ og $y = 1 - 3z$, hvor $z = t$ er en **fri variabel**.

**Fuldstændig løsning:** $(x, y, z) = (1, 1, 0) + t(7, -3, 1)$, $t \in \mathbb{R}$.

---

## Trappeform og reduceret trappeform

### Trappeform (echelon form)

- Alle nulrækker er i bunden
- Det ledende element (pivot) i hver række er til højre for pivotet i rækken ovenover

### Reduceret trappeform (reduced row echelon form)

- Alle pivoter = 1
- Alle elementer over og under pivoterne = 0

---

## Rang

**Rangen** af en matrix $\mathbf{A}$ er antallet af pivoter i trappeformen.

$$\text{rang}(\mathbf{A}) = \text{antal pivoter}$$

### Rang og løsninger

For et $m \times n$ system $\mathbf{A}\mathbf{x} = \mathbf{b}$:

- **Ingen løsning:** Hvis $\text{rang}([\mathbf{A}|\mathbf{b}]) > \text{rang}(\mathbf{A})$ (en "modstridsligning" som $0 = 1$ opstår)
- **Præcis én løsning:** Hvis $\text{rang}(\mathbf{A}) = n$ (antal ubekendte = antal pivoter, ingen frie variable)
- **Uendeligt mange løsninger:** Hvis $\text{rang}(\mathbf{A}) < n$ (der er frie variable)
  - Antal frie variable $= n - \text{rang}(\mathbf{A})$

---

## Partikulær og fuldstændig løsning

### Sætning (superpositionsprincippet)

Hvis $\mathbf{x}_p$ er en **partikulær løsning** til $\mathbf{A}\mathbf{x} = \mathbf{b}$ (inhomogent), og $\mathbf{x}_h$ er den **fuldstændige løsning** til $\mathbf{A}\mathbf{x} = \mathbf{0}$ (homogent), så er:

$$\text{Fuldstændig løsning til } \mathbf{A}\mathbf{x} = \mathbf{b}: \quad \mathbf{x} = \mathbf{x}_p + \mathbf{x}_h$$

### Opskrift:

1. **Find en partikulær løsning** $\mathbf{x}_p$ til det inhomogene system (sæt frie variable = 0)
2. **Løs det homogene system** $\mathbf{A}\mathbf{x} = \mathbf{0}$ (sæt højresiden = 0)
3. **Kombiner:** Den fuldstændige løsning er $\mathbf{x} = \mathbf{x}_p + \mathbf{x}_h$

### Fra eksemplet ovenfor:

- Partikulær løsning: $(1, 1, 0)$ (sæt $z = 0$)
- Homogen løsning: $t(7, -3, 1)$ for $t \in \mathbb{R}$
- Fuldstændig: $(x, y, z) = (1, 1, 0) + t(7, -3, 1)$

---

## Typiske fejl at undgå

1. **Glemmer at tjekke for modstridsligninger** ($0 = k$ med $k \neq 0$) → ingen løsning
2. **Glemmer frie variable** – enhver kolonne uden pivot giver en fri variabel
3. **Forkert rækkeoperationer** – skriv altid hvad du gør (f.eks. $R_2 \leftarrow R_2 - 3R_1$)
4. **Glemmer det homogene system** ved fuldstændig løsning
5. **Forveksler rang af $\mathbf{A}$ og rang af totalmatricen** – de kan være forskellige!
