# Uge 9: Generelle vektorrum

## Hvad er et vektorrum?

Et **vektorrum** $V$ over $\mathbb{R}$ er en mængde med to operationer (addition og skalarmultiplikation) der opfylder 8 aksiomer:

1. $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ (kommutativ)
2. $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$ (associativ)
3. Der findes en **nulvektor** $\mathbf{0}$ så $\mathbf{v} + \mathbf{0} = \mathbf{v}$
4. Til enhver $\mathbf{v}$ findes $-\mathbf{v}$ så $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$
5. $\alpha(\mathbf{u} + \mathbf{v}) = \alpha\mathbf{u} + \alpha\mathbf{v}$
6. $(\alpha + \beta)\mathbf{v} = \alpha\mathbf{v} + \beta\mathbf{v}$
7. $(\alpha\beta)\mathbf{v} = \alpha(\beta\mathbf{v})$
8. $1 \cdot \mathbf{v} = \mathbf{v}$

### Vigtige eksempler på vektorrum

| Vektorrum | Elementer | Nulvektor |
|:---|:---|:---|
| $\mathbb{R}^n$ | $n$-tupler af reelle tal | $(0, 0, \ldots, 0)$ |
| $\mathbb{R}^{m \times n}$ | $m \times n$ matricer | Nulmatricen |
| $P_n$ | Polynomier af grad $\leq n$ | Nulpolynomiet $0$ |
| $C(\mathbb{R})$ | Kontinuerte funktioner $\mathbb{R} \to \mathbb{R}$ | Funktionen $f(x) = 0$ |

⚠️ **Vigtigt:** Vektorrum er ikke kun "pile i rummet"! Polynomier, matricer og funktioner kan også være vektorer.

---

## Underrum

Et **underrum** $W$ af et vektorrum $V$ er en delmængde $W \subseteq V$ der selv er et vektorrum med de arvede operationer.

### Underrumskriteriet (opskrift til at tjekke)

$W$ er et underrum af $V$ hvis og kun hvis:

1. **Ikke-tomt:** $\mathbf{0} \in W$ (eller bare: $W \neq \emptyset$)
2. **Lukket under addition:** $\mathbf{u}, \mathbf{v} \in W \Rightarrow \mathbf{u} + \mathbf{v} \in W$
3. **Lukket under skalarmultiplikation:** $\mathbf{v} \in W, \alpha \in \mathbb{R} \Rightarrow \alpha\mathbf{v} \in W$

**Tip:** Punkt 2 og 3 kan kombineres: Tjek at $\alpha\mathbf{u} + \beta\mathbf{v} \in W$ for alle $\mathbf{u}, \mathbf{v} \in W$ og $\alpha, \beta \in \mathbb{R}$.

### Gennemregnet eksempel

Vis at $W = \{(x, y, z) \in \mathbb{R}^3 \mid x + 2y - z = 0\}$ er et underrum af $\mathbb{R}^3$.

1. **$\mathbf{0} \in W$?** $(0, 0, 0)$: $0 + 0 - 0 = 0$ ✓
2. **Lukket under addition?** Lad $(x_1, y_1, z_1), (x_2, y_2, z_2) \in W$. Da $x_1 + 2y_1 - z_1 = 0$ og $x_2 + 2y_2 - z_2 = 0$. Summen: $(x_1+x_2) + 2(y_1+y_2) - (z_1+z_2) = 0$ ✓
3. **Lukket under skalering?** $\alpha(x_1 + 2y_1 - z_1) = \alpha \cdot 0 = 0$ ✓

**Ikke-eksempel:** $W = \{(x, y) \in \mathbb{R}^2 \mid x + y = 1\}$ er **ikke** et underrum, fordi $(0,0) \notin W$.

---

## Lineær uafhængighed i generelle vektorrum

Definitionen er den samme som i $\mathbb{R}^n$:

Vektorer $\mathbf{v}_1, \ldots, \mathbf{v}_k \in V$ er **lineært uafhængige** hvis:

$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0} \implies c_1 = c_2 = \cdots = c_k = 0$$

### Eksempel med polynomier

Er $p_1(x) = 1$, $p_2(x) = x$, $p_3(x) = x^2$ lineært uafhængige i $P_2$?

Antag $c_1 \cdot 1 + c_2 \cdot x + c_3 \cdot x^2 = 0$ for alle $x$.

Sæt $x = 0$: $c_1 = 0$. Sæt $x = 1$: $c_2 + c_3 = 0$. Sæt $x = -1$: $-c_2 + c_3 = 0$.

Altså $c_2 = c_3 = 0$. De er lineært uafhængige ✓.

---

## Basis og dimension i generelle vektorrum

### Basis

En **basis** for $V$ er en lineært uafhængig mængde der udspænder hele $V$.

### Dimension

$\dim(V)$ = antal vektorer i en basis.

| Vektorrum | Standardbasis | Dimension |
|:---|:---|:---:|
| $\mathbb{R}^n$ | $\mathbf{e}_1, \ldots, \mathbf{e}_n$ | $n$ |
| $P_n$ (polynomier af grad $\leq n$) | $1, x, x^2, \ldots, x^n$ | $n+1$ |
| $\mathbb{R}^{m \times n}$ (matricer) | De $mn$ matricer med ét 1-tal | $m \cdot n$ |

### Opskrift: Find en basis for et underrum

1. Beskriv underrummet parametrisk (med frie variable)
2. Skriv den generelle vektor som en linearkombination af "basisvektorer"
3. Disse vektorer er en basis

### Gennemregnet eksempel

Find en basis for $W = \{(x, y, z) \in \mathbb{R}^3 \mid x + 2y - z = 0\}$.

Parameterisér: $x = -2y + z$, så $(x, y, z) = (-2y + z, y, z) = y(-2, 1, 0) + z(1, 0, 1)$.

**Basis:** $\{(-2, 1, 0), (1, 0, 1)\}$ og $\dim(W) = 2$.

---

## Koordinater og basisskift

### Koordinatvektor

Hvis $\mathcal{B} = (\mathbf{v}_1, \ldots, \mathbf{v}_n)$ er en ordnet basis for $V$ og $\mathbf{w} = c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n$, så er:

$$[\mathbf{w}]_\mathcal{B} = \begin{bmatrix} c_1 \\ \vdots \\ c_n \end{bmatrix}$$

### Eksempel med polynomier

Lad $\mathcal{B} = (1, x, x^2)$ være standardbasen for $P_2$ og $p(x) = 3 - 2x + 5x^2$.

$$[p]_\mathcal{B} = \begin{bmatrix} 3 \\ -2 \\ 5 \end{bmatrix}$$

---

## Typiske fejl at undgå

1. **"Vektorer er pile"** – nej! Polynomier, funktioner og matricer kan også være vektorer
2. **Glemmer at tjekke nulvektoren** ved underrumskriteriet
3. **Forveksler $P_n$ og $P_{n+1}$** – polynomier af grad $\leq n$ har dimension $n+1$
4. **Antager at ethvert delmængde er et underrum** – det skal tjekkes med de tre kriterier
5. **Glemmer "for alle $x$"** ved lineær uafhængighed af funktioner/polynomier
