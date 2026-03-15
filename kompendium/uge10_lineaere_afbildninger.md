# Uge 10: Lineære afbildninger

## Definition

En funktion $T: V \to W$ mellem vektorrum er en **lineær afbildning** hvis:

1. $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ for alle $\mathbf{u}, \mathbf{v} \in V$
2. $T(\alpha\mathbf{v}) = \alpha T(\mathbf{v})$ for alle $\alpha \in \mathbb{R}$, $\mathbf{v} \in V$

Ækvivalent (begge på én gang):

$$T(\alpha\mathbf{u} + \beta\mathbf{v}) = \alpha T(\mathbf{u}) + \beta T(\mathbf{v})$$

### Vigtig konsekvens

$$T(\mathbf{0}) = \mathbf{0}$$

⚠️ Hvis $T(\mathbf{0}) \neq \mathbf{0}$, er $T$ **ikke** lineær! (Hurtig test.)

### Tjek om en afbildning er lineær

**Metode 1:** Vis de to egenskaber direkte.

**Metode 2:** Vis at $T(\alpha\mathbf{u} + \beta\mathbf{v}) = \alpha T(\mathbf{u}) + \beta T(\mathbf{v})$ for vilkårlige $\alpha, \beta, \mathbf{u}, \mathbf{v}$.

### Gennemregnet eksempel

Er $T: \mathbb{R}^2 \to \mathbb{R}^2$ givet ved $T(x, y) = (2x + y, x - 3y)$ lineær?

$T(\alpha(x_1, y_1) + \beta(x_2, y_2)) = T(\alpha x_1 + \beta x_2, \alpha y_1 + \beta y_2)$
$= (2(\alpha x_1 + \beta x_2) + (\alpha y_1 + \beta y_2), (\alpha x_1 + \beta x_2) - 3(\alpha y_1 + \beta y_2))$
$= \alpha(2x_1 + y_1, x_1 - 3y_1) + \beta(2x_2 + y_2, x_2 - 3y_2)$
$= \alpha T(x_1, y_1) + \beta T(x_2, y_2)$ ✓

**Ikke-eksempel:** $T(x, y) = (x + 1, y)$ er **ikke** lineær, fordi $T(0, 0) = (1, 0) \neq (0, 0)$.

---

## Kerne og billedrum

### Kernen

$$\ker(T) = \{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}\}$$

Kernen er et **underrum** af $V$ (domænet).

**Betydning:** Kernen måler "hvor meget information $T$ mister."

- $\ker(T) = \{\mathbf{0}\}$ $\iff$ $T$ er **injektiv**

### Billedrummet

$$\text{im}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in V\} = \text{mængden af alle output}$$

Billedrummet er et **underrum** af $W$ (kodomænet).

- $\text{im}(T) = W$ $\iff$ $T$ er **surjektiv**

### Opskrift: Find kerne og billedrum

**Kerne:** Løs $T(\mathbf{v}) = \mathbf{0}$ (homogent system via afbildningsmatricen).

**Billedrum:** Find søjlerummet af afbildningsmatricen.

---

## Dimensionssætningen for lineære afbildninger

$$\dim(\ker(T)) + \dim(\text{im}(T)) = \dim(V)$$

**Eksempel:** Hvis $T: \mathbb{R}^5 \to \mathbb{R}^3$ og $\dim(\ker(T)) = 2$, så $\dim(\text{im}(T)) = 5 - 2 = 3$.

---

## Afbildningsmatrix

### Idéen

Givet ordnede baser $\mathcal{B}$ for $V$ og $\mathcal{C}$ for $W$, kan enhver lineær afbildning $T: V \to W$ repræsenteres som en matrix $\mathbf{A}$ der opfylder:

$$[T(\mathbf{v})]_\mathcal{C} = \mathbf{A} \cdot [\mathbf{v}]_\mathcal{B}$$

### Opskrift: Find afbildningsmatricen

1. Lad $\mathcal{B} = (\mathbf{v}_1, \ldots, \mathbf{v}_n)$ være basis for $V$
2. Beregn $T(\mathbf{v}_1), T(\mathbf{v}_2), \ldots, T(\mathbf{v}_n)$
3. Find koordinaterne af hvert $T(\mathbf{v}_j)$ mht. basis $\mathcal{C}$ for $W$
4. Disse koordinatvektorer er **søjlerne** i afbildningsmatricen:

$$\mathbf{A} = \Big[ [T(\mathbf{v}_1)]_\mathcal{C} \;\Big|\; [T(\mathbf{v}_2)]_\mathcal{C} \;\Big|\; \cdots \;\Big|\; [T(\mathbf{v}_n)]_\mathcal{C} \Big]$$

### Gennemregnet eksempel

$T: \mathbb{R}^2 \to \mathbb{R}^2$ med $T(x, y) = (2x + y, x - 3y)$ og standardbaser.

$T(\mathbf{e}_1) = T(1, 0) = (2, 1)$ og $T(\mathbf{e}_2) = T(0, 1) = (1, -3)$.

$$\mathbf{A} = \begin{bmatrix} 2 & 1 \\ 1 & -3 \end{bmatrix}$$

Tjek: $\mathbf{A}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2x + y \\ x - 3y \end{bmatrix}$ ✓

---

## Basisskiftmatrix

### Problem

Du har koordinaterne $[\mathbf{v}]_\mathcal{B}$ mht. basis $\mathcal{B}$ og vil finde $[\mathbf{v}]_\mathcal{C}$ mht. basis $\mathcal{C}$.

### Opskrift

**Basisskiftmatricen** $\mathbf{P}_{\mathcal{B} \to \mathcal{C}}$ opfylder:

$$[\mathbf{v}]_\mathcal{C} = \mathbf{P}_{\mathcal{B} \to \mathcal{C}} \cdot [\mathbf{v}]_\mathcal{B}$$

Søjlerne i $\mathbf{P}_{\mathcal{B} \to \mathcal{C}}$ er koordinaterne af $\mathcal{B}$-basisvektorerne udtrykt i $\mathcal{C}$-basen.

### Beregning med Gauss

Reducér $[\mathcal{C} | \mathcal{B}]$ til $[\mathbf{I} | \mathbf{P}_{\mathcal{B} \to \mathcal{C}}]$.

---

## Sammenhæng: Afbildningsmatrix ved basisskift

Hvis $\mathbf{A}$ er afbildningsmatricen for $T$ mht. basis $\mathcal{B}$, og vi skifter til basis $\mathcal{C}$:

$$\mathbf{A}_\mathcal{C} = \mathbf{P}^{-1} \mathbf{A} \mathbf{P}$$

hvor $\mathbf{P} = \mathbf{P}_{\mathcal{C} \to \mathcal{B}}$ er basisskiftmatricen.

---

## Typiske fejl at undgå

1. **Glemmer at tjekke $T(\mathbf{0}) = \mathbf{0}$** – hurtig test for linearitet
2. **Forveksler kerne og billedrum:** Kernen er i $V$ (domænet), billedrummet er i $W$ (kodomænet)
3. **Forkert rækkefølge i søjlerne:** Søjle $j$ i afbildningsmatricen svarer til $T(\mathbf{v}_j)$
4. **Glemmer at angive baserne** – afbildningsmatricen afhænger af valg af baser!
5. **Forveksler $\mathbf{P}_{\mathcal{B} \to \mathcal{C}}$ med $\mathbf{P}_{\mathcal{C} \to \mathcal{B}}$** – retningen betyder noget!
