# Uge 4: Kompleks eksponentialfunktion og polynomier

## Eulers formel og den komplekse eksponentialfunktion

### Eulers formel

$$e^{i\theta} = \cos\theta + i\sin\theta$$

Dette er en af de vigtigste formler i kurset!

### Polær form med eksponentialfunktionen

Ethvert komplekst tal $z \neq 0$ kan nu skrives:

$$z = r \cdot e^{i\theta}$$

hvor $r = |z|$ og $\theta = \text{arg}(z)$.

### Gennemregnet eksempel

Skriv $z = -1 + i\sqrt{3}$ på polær form:
- $r = |z| = \sqrt{1 + 3} = 2$
- $\theta = \text{arg}(z) = \frac{2\pi}{3}$ (2. kvadrant)
- $z = 2e^{i \cdot 2\pi/3}$

---

## Regneregler for polær form

### Multiplikation

$$z_1 \cdot z_2 = r_1 e^{i\theta_1} \cdot r_2 e^{i\theta_2} = r_1 r_2 \cdot e^{i(\theta_1 + \theta_2)}$$

**Moduli ganges, argumenter lægges sammen!**

### Division

$$\frac{z_1}{z_2} = \frac{r_1}{r_2} \cdot e^{i(\theta_1 - \theta_2)}$$

### Potensopløftning (de Moivres formel)

$$z^n = r^n \cdot e^{in\theta} = r^n(\cos(n\theta) + i\sin(n\theta))$$

### Konjugering i polær form

$$\overline{re^{i\theta}} = re^{-i\theta}$$

---

## Polynomier

Et **polynomium** af grad $n$ er:

$$p(z) = a_n z^n + a_{n-1}z^{n-1} + \cdots + a_1 z + a_0$$

hvor $a_n \neq 0$ (den **ledende koefficient**).

### Rødder

En **rod** i $p(z)$ er en værdi $z_0$ hvor $p(z_0) = 0$.

**Algebraens fundamentalsætning:** Ethvert polynomium af grad $n \geq 1$ med komplekse koefficienter har **præcis $n$ rødder** i $\mathbb{C}$ (talt med multiplicitet).

### Rod ↔ faktor

$z_0$ er en rod i $p(z)$ $\iff$ $(z - z_0)$ er en faktor i $p(z)$.

Dvs. $p(z) = (z - z_0) \cdot q(z)$ for et polynomium $q$ af grad $n-1$.

---

## Andengradspolynomier

For $p(z) = az^2 + bz + c$ finder vi rødderne med **diskriminanten**:

$$D = b^2 - 4ac$$

$$z = \frac{-b \pm \sqrt{D}}{2a}$$

### Tre tilfælde (for reelle koefficienter):

| $D > 0$ | $D = 0$ | $D < 0$ |
|:---|:---|:---|
| To forskellige reelle rødder | Én dobbeltrod (reel) | To komplekst konjugerede rødder |
| $z = \frac{-b \pm \sqrt{D}}{2a}$ | $z = \frac{-b}{2a}$ | $z = \frac{-b \pm i\sqrt{|D|}}{2a}$ |

### Gennemregnet eksempel

Løs $z^2 + 2z + 5 = 0$:

$D = 4 - 20 = -16$

$z = \frac{-2 \pm \sqrt{-16}}{2} = \frac{-2 \pm 4i}{2} = -1 \pm 2i$

**Rødderne er $z_1 = -1 + 2i$ og $z_2 = -1 - 2i$** (konjugerede!).

---

## Polynomier med reelle koefficienter

### Vigtig egenskab

Hvis $p(z)$ har **reelle koefficienter** og $z_0$ er en rod, så er $\bar{z_0}$ **også en rod**.

**Konsekvens:** Komplekse rødder optræder altid **parvis** som konjugerede par.

### Faktorisering

Hvert polynomium med reelle koefficienter kan skrives som et produkt af:
- **Førstegrads faktorer:** $(z - r)$ for reelle rødder $r$
- **Andengrads faktorer:** $(z^2 + bz + c)$ med $D < 0$ for komplekse rodpar

---

## Den binome ligning

### Problemet

Løs $z^n = w$ for et givet $w \in \mathbb{C}$.

### Opskrift:

1. Skriv $w$ på polær form: $w = Re^{i\phi}$
2. De $n$ løsninger er:

$$z_k = \sqrt[n]{R} \cdot e^{i(\phi + 2\pi k)/n}, \quad k = 0, 1, 2, \ldots, n-1$$

### Gennemregnet eksempel

Løs $z^3 = 8$:

1. $w = 8 = 8e^{i \cdot 0}$, så $R = 8$, $\phi = 0$
2. $\sqrt[3]{8} = 2$
3. De tre løsninger:
   - $z_0 = 2 \cdot e^{i \cdot 0/3} = 2$
   - $z_1 = 2 \cdot e^{i \cdot 2\pi/3} = 2\left(-\frac{1}{2} + i\frac{\sqrt{3}}{2}\right) = -1 + i\sqrt{3}$
   - $z_2 = 2 \cdot e^{i \cdot 4\pi/3} = -1 - i\sqrt{3}$

### Gennemregnet eksempel 2

Løs $z^4 = -16$:

1. $w = -16 = 16 \cdot e^{i\pi}$, så $R = 16$, $\phi = \pi$
2. $\sqrt[4]{16} = 2$
3. De fire løsninger ($k = 0, 1, 2, 3$):
   - $z_k = 2 \cdot e^{i(\pi + 2\pi k)/4}$
   - $z_0 = 2e^{i\pi/4} = \sqrt{2} + i\sqrt{2}$
   - $z_1 = 2e^{i \cdot 3\pi/4} = -\sqrt{2} + i\sqrt{2}$
   - $z_2 = 2e^{i \cdot 5\pi/4} = -\sqrt{2} - i\sqrt{2}$
   - $z_3 = 2e^{i \cdot 7\pi/4} = \sqrt{2} - i\sqrt{2}$

**Geometrisk:** Rødderne ligger jævnt fordelt på en cirkel med radius $\sqrt[n]{R}$.

---

## Typiske fejl at undgå

1. **Glemmer alle $n$ rødder** i den binome ligning – der er altid præcis $n$
2. **Forkert argument** ved omregning til polær form
3. **Glemmer at komplekse rødder kommer i par** (ved reelle koefficienter)
4. **Blander $e^{i\theta}$ sammen med $e^{\theta}$** – den første er kompleks, den anden reel
5. **Forkert fortegn i diskriminanten:** Hvis $D < 0$, skriv $\sqrt{D} = i\sqrt{|D|}$
