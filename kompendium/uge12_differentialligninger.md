# Uge 12: Differentialligninger og systemer

## Hvad er en differentialligning?

En **differentialligning** (ODE) er en ligning, der involverer en ukendt funktion og dens afledede.

**Førsteordens lineær ODE:**

$$y'(t) = a \cdot y(t) + f(t)$$

**Homogen** ($f(t) = 0$): $y' = ay$

**Inhomogen** ($f(t) \neq 0$): $y' = ay + f(t)$

---

## Den simple homogene ODE: $y' = ay$

### Løsningen

$$y(t) = Ce^{at}$$

hvor $C$ er en vilkårlig konstant.

**Med begyndelsesbetingelse** $y(0) = y_0$: $C = y_0$, så:

$$y(t) = y_0 \cdot e^{at}$$

### Gennemregnet eksempel

Løs $y' = 3y$ med $y(0) = 2$:

$$y(t) = 2e^{3t}$$

**Tjek:** $y'(t) = 6e^{3t} = 3 \cdot 2e^{3t} = 3y(t)$ ✓ og $y(0) = 2$ ✓

---

## Systemer af differentialligninger

### Systemet

$$\mathbf{y}'(t) = \mathbf{A}\mathbf{y}(t)$$

hvor $\mathbf{y}(t) = \begin{bmatrix} y_1(t) \\ \vdots \\ y_n(t) \end{bmatrix}$ og $\mathbf{A}$ er en $n \times n$ matrix.

### Løsning via egenværdier (det diagonaliserbare tilfælde)

**Opskrift:**

1. Find egenværdierne $\lambda_1, \ldots, \lambda_n$ og egenvektorer $\mathbf{v}_1, \ldots, \mathbf{v}_n$ for $\mathbf{A}$
2. Den fuldstændige løsning er:

$$\mathbf{y}(t) = c_1 e^{\lambda_1 t}\mathbf{v}_1 + c_2 e^{\lambda_2 t}\mathbf{v}_2 + \cdots + c_n e^{\lambda_n t}\mathbf{v}_n$$

3. Bestem konstanterne $c_1, \ldots, c_n$ fra begyndelsesbetingelsen $\mathbf{y}(0) = \mathbf{y}_0$

### Hvorfor virker det?

Hvis $\mathbf{v}$ er egenvektor med egenværdi $\lambda$, så er $\mathbf{y}(t) = e^{\lambda t}\mathbf{v}$ en løsning:

$$\mathbf{y}'(t) = \lambda e^{\lambda t}\mathbf{v} = e^{\lambda t}(\lambda\mathbf{v}) = e^{\lambda t}\mathbf{A}\mathbf{v} = \mathbf{A}(e^{\lambda t}\mathbf{v}) = \mathbf{A}\mathbf{y}(t) \checkmark$$

### Gennemregnet eksempel

Løs $\mathbf{y}' = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}\mathbf{y}$ med $\mathbf{y}(0) = \begin{bmatrix} 1 \\ 4 \end{bmatrix}$.

**Trin 1:** Egenværdier: $\lambda_1 = 3$, $\lambda_2 = 2$ (fra Uge 11-kompendiet).

Egenvektorer: $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$, $\mathbf{v}_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}$.

**Trin 2:** Fuldstændig løsning:

$$\mathbf{y}(t) = c_1 e^{3t}\begin{bmatrix} 1 \\ 0 \end{bmatrix} + c_2 e^{2t}\begin{bmatrix} -1 \\ 1 \end{bmatrix}$$

**Trin 3:** Begyndelsesbetingelse $\mathbf{y}(0) = \begin{bmatrix} 1 \\ 4 \end{bmatrix}$:

$$c_1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + c_2\begin{bmatrix} -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 4 \end{bmatrix}$$

Fra 2. komponent: $c_2 = 4$. Fra 1. komponent: $c_1 - 4 = 1$, så $c_1 = 5$.

**Løsning:**

$$\mathbf{y}(t) = 5e^{3t}\begin{bmatrix} 1 \\ 0 \end{bmatrix} + 4e^{2t}\begin{bmatrix} -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 5e^{3t} - 4e^{2t} \\ 4e^{2t} \end{bmatrix}$$

---

## Komplekse egenværdier i ODE-systemer

Når $\mathbf{A}$ er reel og har komplekse egenværdier $\lambda = \alpha \pm i\beta$:

### Opskrift

1. Find den komplekse egenvektor $\mathbf{v}$ til $\lambda = \alpha + i\beta$
2. Beregn den komplekse løsning: $e^{(\alpha + i\beta)t}\mathbf{v}$
3. Brug Eulers formel: $e^{i\beta t} = \cos(\beta t) + i\sin(\beta t)$
4. De to reelle løsninger er **realdelen** og **imaginærdelen** af den komplekse løsning

### Gennemregnet eksempel

$\mathbf{y}' = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\mathbf{y}$

Egenværdier: $\lambda = \pm i$. Egenvektor til $\lambda = i$: $\mathbf{v} = \begin{bmatrix} i \\ 1 \end{bmatrix}$

Kompleks løsning: $e^{it}\begin{bmatrix} i \\ 1 \end{bmatrix} = (\cos t + i\sin t)\begin{bmatrix} i \\ 1 \end{bmatrix} = \begin{bmatrix} i\cos t - \sin t \\ \cos t + i\sin t \end{bmatrix}$

**Realdel:** $\begin{bmatrix} -\sin t \\ \cos t \end{bmatrix}$, **Imaginærdel:** $\begin{bmatrix} \cos t \\ \sin t \end{bmatrix}$

**Fuldstændig reel løsning:**

$$\mathbf{y}(t) = c_1\begin{bmatrix} -\sin t \\ \cos t \end{bmatrix} + c_2\begin{bmatrix} \cos t \\ \sin t \end{bmatrix}$$

---

## Matrixeksponentialen (via diagonalisering)

Hvis $\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$:

$$e^{\mathbf{A}t} = \mathbf{P} \begin{bmatrix} e^{\lambda_1 t} & & 0 \\ & \ddots & \\ 0 & & e^{\lambda_n t} \end{bmatrix} \mathbf{P}^{-1}$$

Og løsningen til $\mathbf{y}' = \mathbf{A}\mathbf{y}$ med $\mathbf{y}(0) = \mathbf{y}_0$ er:

$$\mathbf{y}(t) = e^{\mathbf{A}t}\mathbf{y}_0$$

---

## Partikulær og fuldstændig løsning

For inhomogene systemer $\mathbf{y}' = \mathbf{A}\mathbf{y} + \mathbf{f}(t)$:

$$\text{Fuldstændig løsning} = \text{Partikulær løsning} + \text{Homogen fuldstændig løsning}$$

(Samme princip som ved lineære ligningssystemer i Uge 6.)

---

## Typiske fejl at undgå

1. **Glemmer $e^{\lambda t}$-faktoren:** Løsningen er $e^{\lambda t}\mathbf{v}$, ikke bare $\mathbf{v}$!
2. **Forkert håndtering af komplekse egenværdier:** Tag real- og imaginærdel for at få reelle løsninger
3. **Glemmer at bestemme konstanterne** fra begyndelsesbetingelsen
4. **Forveksler $\mathbf{y}'$ og $\mathbf{y}$** – vær omhyggelig med notationen
5. **Antager at systemet altid er diagonaliserbart** – tjek først!
