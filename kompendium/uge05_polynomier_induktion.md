# Uge 5: Polynomiers division og induktion

## Divisionsalgoritmen for polynomier

### Sætningen

For polynomier $p(z)$ (grad $n$) og $d(z)$ (grad $m \leq n$) findes unikke polynomier $q(z)$ (kvotient) og $r(z)$ (rest) så:

$$p(z) = d(z) \cdot q(z) + r(z)$$

hvor $\text{grad}(r) < \text{grad}(d)$ (eller $r = 0$).

### Opskrift: Polynomiel lang division

**Eksempel:** Del $p(z) = 2z^3 + 3z^2 - 5z + 1$ med $d(z) = z - 2$.

1. $2z^3 \div z = 2z^2$. Gang: $2z^2(z-2) = 2z^3 - 4z^2$. Træk fra: $(2z^3 + 3z^2) - (2z^3 - 4z^2) = 7z^2$.
2. $7z^2 \div z = 7z$. Gang: $7z(z-2) = 7z^2 - 14z$. Træk fra: $(7z^2 - 5z) - (7z^2 - 14z) = 9z$.
3. $9z \div z = 9$. Gang: $9(z-2) = 9z - 18$. Træk fra: $(9z + 1) - (9z - 18) = 19$.

**Resultat:** $2z^3 + 3z^2 - 5z + 1 = (z-2)(2z^2 + 7z + 9) + 19$

---

## Rod og faktor

### Rests sætningen

Når $p(z)$ divideres med $(z - z_0)$, er resten lig $p(z_0)$.

### Faktorsætningen

$z_0$ er rod i $p(z)$ $\iff$ $(z - z_0)$ er en faktor i $p(z)$ $\iff$ resten er 0.

### Multiplicitet

En rod $z_0$ har **multiplicitet** $m$ hvis:

$$p(z) = (z - z_0)^m \cdot q(z) \quad \text{hvor } q(z_0) \neq 0$$

**Eksempel:** $p(z) = (z-1)^3(z+2)$ har rod $z=1$ med multiplicitet 3 og rod $z=-2$ med multiplicitet 1.

**Summen af multipliciteterne = graden af polynomiet.**

### Opskrift: Find multiplicitet af en rod

1. Dividér $p(z)$ med $(z - z_0)$ og få $q(z)$
2. Tjek om $z_0$ stadig er rod i $q(z)$
3. Hvis ja, dividér igen. Gentag indtil $z_0$ ikke længere er rod
4. Antallet af gange du dividerede = multipliciteten

---

## Induktion

### Hvornår bruges induktion?

Når du vil bevise at et udsagn $P(n)$ gælder for **alle** naturlige tal $n \geq n_0$.

### Opskrift (induktionsbeviset):

**Trin 1 – Basisskridt:** Vis at $P(n_0)$ er sandt.

**Trin 2 – Induktionsskridt:** Antag at $P(k)$ er sandt (for et vilkårligt $k \geq n_0$). Denne antagelse kaldes **induktionshypotesen**. Vis derefter at $P(k+1)$ også er sandt.

**Konklusion:** Så gælder $P(n)$ for alle $n \geq n_0$.

### Gennemregnet eksempel

**Vis at** $\sum_{j=1}^{n} j = \frac{n(n+1)}{2}$ for alle $n \geq 1$.

**Basisskridt** ($n = 1$):
- Venstreside: $\sum_{j=1}^{1} j = 1$
- Højreside: $\frac{1 \cdot 2}{2} = 1$ ✓

**Induktionsskridt:** Antag at $\sum_{j=1}^{k} j = \frac{k(k+1)}{2}$ (induktionshypotesen).

Vis at $\sum_{j=1}^{k+1} j = \frac{(k+1)(k+2)}{2}$:

$$\sum_{j=1}^{k+1} j = \underbrace{\sum_{j=1}^{k} j}_{\text{induktionshypotese}} + (k+1) = \frac{k(k+1)}{2} + (k+1)$$

$$= (k+1)\left(\frac{k}{2} + 1\right) = (k+1) \cdot \frac{k+2}{2} = \frac{(k+1)(k+2)}{2} \checkmark$$

### Gennemregnet eksempel 2

**Vis at** $n! > 2^n$ for alle $n \geq 4$.

**Basisskridt** ($n = 4$): $4! = 24 > 16 = 2^4$ ✓

**Induktionsskridt:** Antag $k! > 2^k$ for $k \geq 4$.

$$(k+1)! = (k+1) \cdot k! > (k+1) \cdot 2^k \geq 5 \cdot 2^k > 2 \cdot 2^k = 2^{k+1} \checkmark$$

(Vi brugte at $k+1 \geq 5 > 2$ for $k \geq 4$.)

---

## Rekursivt definerede følger

### Opskrift: Find en lukket formel via induktion

1. Beregn de første led: $a_0, a_1, a_2, a_3, \ldots$
2. Gæt en lukket formel
3. Bevis formlen med induktion

### Eksempel

Givet: $a_0 = 1$, $a_{n+1} = 2a_n$ for $n \geq 0$.

Beregn: $a_0 = 1, a_1 = 2, a_2 = 4, a_3 = 8, \ldots$

**Gæt:** $a_n = 2^n$.

**Bevis med induktion:**
- Basis: $a_0 = 1 = 2^0$ ✓
- Skridt: Antag $a_k = 2^k$. Så $a_{k+1} = 2a_k = 2 \cdot 2^k = 2^{k+1}$ ✓

---

## Typiske fejl at undgå

1. **Glemmer basisskridtet** – uden det er beviset ugyldigt!
2. **Bruger ikke induktionshypotesen** i induktionsskridtet – den SKAL bruges, ellers er det ikke induktion
3. **Forveksler $P(k)$ med $P(k+1)$** – vær præcis med hvad du antager og hvad du viser
4. **Glemmer at summen af multipliciteterne = graden** af polynomiet
5. **Forkert rest** ved polynomiel division – tjek altid ved at gange kvotienten med divisoren og lægge resten til
