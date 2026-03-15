# Uge 3: Komplekse tal

## Den imaginære enhed

Vi definerer tallet $i$ ved:

$$i^2 = -1$$

Altså er $i = \sqrt{-1}$ (den "imaginære enhed").

### Potenser af $i$ (cyklisk mønster!)

| $i^1$ | $i^2$ | $i^3$ | $i^4$ | $i^5$ | $i^6$ | ... |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $i$ | $-1$ | $-i$ | $1$ | $i$ | $-1$ | ... |

**Huskemåde:** Potenserne gentager sig med periode 4: $i, -1, -i, 1, i, -1, -i, 1, \ldots$

For at beregne $i^n$: Find $n \mod 4$ (resten ved division med 4):
- Rest 0: $i^n = 1$
- Rest 1: $i^n = i$
- Rest 2: $i^n = -1$
- Rest 3: $i^n = -i$

---

## Rektangulær form

Ethvert komplekst tal kan skrives som:

$$z = a + ib$$

hvor $a, b \in \mathbb{R}$.

- $a = \text{Re}(z)$ er **realdelen**
- $b = \text{Im}(z)$ er **imaginærdelen**

⚠️ **Vigtigt:** Imaginærdelen er et **reelt** tal! For $z = 3 - 5i$ er $\text{Im}(z) = -5$ (ikke $-5i$).

---

## Regning med komplekse tal

### Addition/subtraktion

Regn komponentvist:

$$(a + ib) + (c + id) = (a+c) + i(b+d)$$

### Multiplikation

Gang ud som med parenteser og brug $i^2 = -1$:

$$(a + ib)(c + id) = ac + iad + ibc + i^2bd = (ac - bd) + i(ad + bc)$$

### Gennemregnet eksempel

$(3 + 2i)(1 - 4i) = 3 \cdot 1 + 3 \cdot (-4i) + 2i \cdot 1 + 2i \cdot (-4i)$
$= 3 - 12i + 2i - 8i^2 = 3 - 10i - 8(-1) = 3 - 10i + 8 = 11 - 10i$

---

## Kompleks konjugering

Den **konjugerede** af $z = a + ib$ er:

$$\bar{z} = a - ib$$

### Vigtige egenskaber

- $z \cdot \bar{z} = a^2 + b^2$ (altid et reelt, ikke-negativt tal!)
- $\overline{z_1 + z_2} = \bar{z_1} + \bar{z_2}$
- $\overline{z_1 \cdot z_2} = \bar{z_1} \cdot \bar{z_2}$
- $\overline{\bar{z}} = z$
- $\text{Re}(z) = \frac{z + \bar{z}}{2}$ og $\text{Im}(z) = \frac{z - \bar{z}}{2i}$
- $z$ er reelt $\iff$ $z = \bar{z}$

---

## Division (brøker med komplekse tal)

### Opskrift:

For at beregne $\frac{z_1}{z_2}$: **gang tæller og nævner med den konjugerede af nævneren**.

$$\frac{z_1}{z_2} = \frac{z_1 \cdot \bar{z_2}}{z_2 \cdot \bar{z_2}} = \frac{z_1 \cdot \bar{z_2}}{|z_2|^2}$$

### Gennemregnet eksempel

$$\frac{3 + 2i}{1 - 4i} = \frac{(3+2i)(1+4i)}{(1-4i)(1+4i)} = \frac{3 + 12i + 2i + 8i^2}{1 + 16} = \frac{3 + 14i - 8}{17} = \frac{-5 + 14i}{17} = -\frac{5}{17} + \frac{14}{17}i$$

---

## Absolutværdi (modulus)

Absolutværdien (eller modulus) af $z = a + ib$ er:

$$|z| = \sqrt{a^2 + b^2}$$

Geometrisk: afstanden fra $z$ til origo i den komplekse talplan.

### Vigtige egenskaber

- $|z| \geq 0$ og $|z| = 0 \iff z = 0$
- $|z|^2 = z \cdot \bar{z}$
- $|z_1 \cdot z_2| = |z_1| \cdot |z_2|$
- $\left|\frac{z_1}{z_2}\right| = \frac{|z_1|}{|z_2|}$
- **Trekantsuligheden:** $|z_1 + z_2| \leq |z_1| + |z_2|$

---

## Argument

**Argumentet** af $z \neq 0$ er vinklen $\theta$ som $z$ danner med den positive reelle akse:

$$\text{arg}(z) = \theta \quad \text{hvor } z = |z|(\cos\theta + i\sin\theta)$$

### Opskrift til at finde argumentet:

1. Tegn $z = a + ib$ i den komplekse talplan
2. Find $|z| = \sqrt{a^2 + b^2}$
3. Brug $\cos\theta = \frac{a}{|z|}$ og $\sin\theta = \frac{b}{|z|}$
4. Bestem $\theta$ ud fra hvilken kvadrant $z$ ligger i

⚠️ **Pas på kvadranten!** $\arctan\left(\frac{b}{a}\right)$ giver ikke altid den rigtige vinkel – du skal justere afhængigt af fortegnene af $a$ og $b$.

| Kvadrant | $a$ | $b$ | $\theta$ |
|:---:|:---:|:---:|:---|
| I | $+$ | $+$ | $\theta = \arctan(b/a)$ |
| II | $-$ | $+$ | $\theta = \pi + \arctan(b/a)$ |
| III | $-$ | $-$ | $\theta = -\pi + \arctan(b/a)$ |
| IV | $+$ | $-$ | $\theta = \arctan(b/a)$ |

### Gennemregnet eksempel

Find argumentet for $z = -1 + i\sqrt{3}$:

- $|z| = \sqrt{1 + 3} = 2$
- $\cos\theta = \frac{-1}{2}$, $\sin\theta = \frac{\sqrt{3}}{2}$
- Vi er i 2. kvadrant ($a < 0$, $b > 0$)
- $\theta = \frac{2\pi}{3}$

---

## Polære koordinater

Ethvert komplekst tal $z \neq 0$ kan skrives:

$$z = |z|(\cos\theta + i\sin\theta)$$

hvor $\theta = \text{arg}(z)$.

### Omregning mellem former:

**Rektangulær → polær:** Find $|z|$ og $\theta$ som ovenfor.

**Polær → rektangulær:** $a = |z|\cos\theta$, $b = |z|\sin\theta$.

---

## Mængder i den komplekse talplan

Mange opgaver beder dig beskrive mængder geometrisk:

| Mængde | Geometrisk betydning |
|:---|:---|
| $|z - z_0| = r$ | Cirkel med centrum $z_0$ og radius $r$ |
| $|z - z_0| < r$ | Åben cirkelskive (indre) |
| $|z - z_0| \leq r$ | Lukket cirkelskive |
| $\text{Re}(z) = c$ | Lodret linje |
| $\text{Im}(z) = c$ | Vandret linje |
| $|z - z_1| = |z - z_2|$ | Midtnormal mellem $z_1$ og $z_2$ |

---

## De inverse trigonometriske funktioner

**$\arccos$:** $\arccos: [-1, 1] \to [0, \pi]$ – giver den vinkel i $[0, \pi]$ hvis cosinus er $x$.

**$\arcsin$:** $\arcsin: [-1, 1] \to [-\frac{\pi}{2}, \frac{\pi}{2}]$ – giver den vinkel i $[-\frac{\pi}{2}, \frac{\pi}{2}]$ hvis sinus er $x$.

⚠️ **Vigtigt:** $\cos(\arccos(x)) = x$ for alle $x \in [-1,1]$, men $\arccos(\cos(\theta)) = \theta$ kun for $\theta \in [0, \pi]$!

---

## Typiske fejl at undgå

1. **$\text{Im}(3-5i) = -5$, ikke $-5i$!** Imaginærdelen er et reelt tal.
2. **Glemmer $i^2 = -1$** ved multiplikation
3. **Division:** Ganger ikke med den konjugerede af nævneren
4. **Argument i forkert kvadrant:** Tegn altid tallet i talplanen!
5. **$|z|^2 \neq z^2$** – det er $|z|^2 = z \cdot \bar{z}$
