# Uge 13: Andenordens differentialligninger

## Andenordens lineær ODE med konstante koefficienter

### Standardformen

$$y'' + by' + cy = f(t)$$

**Homogen:** $y'' + by' + cy = 0$ (når $f(t) = 0$)

**Inhomogen:** $y'' + by' + cy = f(t)$ (når $f(t) \neq 0$)

---

## Den homogene ligning: $y'' + by' + cy = 0$

### Det karakteristiske polynomium

Vi gætter på løsningen $y = e^{rt}$ og indsætter:

$$r^2 e^{rt} + bre^{rt} + ce^{rt} = 0 \implies r^2 + br + c = 0$$

Polynomiet $r^2 + br + c$ er det **karakteristiske polynomium**.

### Tre tilfælde

**Diskriminant:** $D = b^2 - 4c$

### Tilfælde 1: $D > 0$ – to forskellige reelle rødder

Rødder: $r_1 \neq r_2$ (begge reelle).

**Fuldstændig løsning:**

$$y(t) = c_1 e^{r_1 t} + c_2 e^{r_2 t}$$

**Gennemregnet eksempel:** $y'' - 5y' + 6y = 0$

Karakteristisk polynomium: $r^2 - 5r + 6 = (r-2)(r-3) = 0$

$r_1 = 2$, $r_2 = 3$

$$y(t) = c_1 e^{2t} + c_2 e^{3t}$$

### Tilfælde 2: $D = 0$ – dobbeltrod

Rod: $r_1 = r_2 = r = -\frac{b}{2}$

**Fuldstændig løsning:**

$$y(t) = c_1 e^{rt} + c_2 \cdot t \cdot e^{rt} = (c_1 + c_2 t)e^{rt}$$

⚠️ Bemærk den ekstra faktor $t$ i det andet led!

**Gennemregnet eksempel:** $y'' + 4y' + 4y = 0$

$r^2 + 4r + 4 = (r+2)^2 = 0 \implies r = -2$ (dobbeltrod)

$$y(t) = (c_1 + c_2 t)e^{-2t}$$

### Tilfælde 3: $D < 0$ – komplekse rødder

Rødder: $r = \alpha \pm i\beta$ hvor $\alpha = -\frac{b}{2}$ og $\beta = \frac{\sqrt{|D|}}{2}$

**Fuldstændig løsning (reel form):**

$$y(t) = e^{\alpha t}(c_1 \cos(\beta t) + c_2 \sin(\beta t))$$

**Gennemregnet eksempel:** $y'' + 2y' + 5y = 0$

$r^2 + 2r + 5 = 0$, $D = 4 - 20 = -16$

$r = \frac{-2 \pm 4i}{2} = -1 \pm 2i$, så $\alpha = -1$, $\beta = 2$

$$y(t) = e^{-t}(c_1 \cos(2t) + c_2 \sin(2t))$$

---

## Begyndelsesbetingelser

For en andenordens ODE har vi to betingelser: $y(t_0) = y_0$ og $y'(t_0) = y_0'$.

### Opskrift:

1. Find den fuldstændige løsning (med $c_1$ og $c_2$)
2. Indsæt $y(t_0) = y_0$ → én ligning med $c_1$ og $c_2$
3. Beregn $y'(t)$ og indsæt $y'(t_0) = y_0'$ → anden ligning
4. Løs de to ligninger for $c_1$ og $c_2$

### Gennemregnet eksempel

$y'' - 5y' + 6y = 0$, $y(0) = 1$, $y'(0) = 0$.

Fuldstændig: $y = c_1 e^{2t} + c_2 e^{3t}$

$y(0) = c_1 + c_2 = 1$

$y'(t) = 2c_1 e^{2t} + 3c_2 e^{3t}$, så $y'(0) = 2c_1 + 3c_2 = 0$

Fra ligning 1: $c_1 = 1 - c_2$. Indsæt: $2(1-c_2) + 3c_2 = 0 \implies 2 + c_2 = 0 \implies c_2 = -2$.

$c_1 = 3$, $c_2 = -2$.

$$y(t) = 3e^{2t} - 2e^{3t}$$

---

## Sammenhæng med systemer (Uge 12)

En andenordens ODE $y'' + by' + cy = 0$ kan omskrives til et system:

Sæt $y_1 = y$ og $y_2 = y'$:

$$\begin{bmatrix} y_1' \\ y_2' \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -c & -b \end{bmatrix} \begin{bmatrix} y_1 \\ y_2 \end{bmatrix}$$

Egenværdierne for denne matrix er netop rødderne $r_1, r_2$ af det karakteristiske polynomium!

---

## Opsummering: Hurtigoversigt

| Diskriminant | Rødder | Fuldstændig løsning |
|:---:|:---|:---|
| $D > 0$ | $r_1 \neq r_2$ reelle | $c_1 e^{r_1 t} + c_2 e^{r_2 t}$ |
| $D = 0$ | $r$ dobbeltrod | $(c_1 + c_2 t)e^{rt}$ |
| $D < 0$ | $\alpha \pm i\beta$ | $e^{\alpha t}(c_1\cos\beta t + c_2\sin\beta t)$ |

---

## Typiske fejl at undgå

1. **Glemmer $t$-faktoren** ved dobbeltrod – løsningen er $(c_1 + c_2 t)e^{rt}$, ikke $(c_1 + c_2)e^{rt}$
2. **Forkert fortegn i det karakteristiske polynomium** – vær omhyggelig med at overføre koefficienter
3. **Glemmer at differentiere korrekt** ved begyndelsesbetingelser – brug produktreglen for $te^{rt}$!
4. **Forveksler $\alpha$ og $\beta$:** $\alpha$ er realdelen (dæmpning), $\beta$ er imaginærdelen (frekvens)
5. **Glemmer at der er to begyndelsesbetingelser** for en andenordens ODE
