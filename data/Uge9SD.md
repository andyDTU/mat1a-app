---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.4.1+dev
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(section:uge9S)=

# Opgaver -- Store Dag

----

+++

## Opgave 1: Første eksempler på vektorrum

I denne opgave betragtes følgende eksempler på vektorrum.

1. Det reelle vektorrum $V_1=\mathbb{R}^{4}$.
  
2. Det komplekse vektorrum $V_2=\mathbb{C}^{3}$.

+++

### Spørgsmål a

Ifølge Definition 10.1.1 fra lærebogen, har hvert vektorrum en nulvektor ${\mathbf 0}$. 
Angiv nulvektoren i hvert af de ovenstående vektorrum.

```{admonition} Svar
:class: dropdown
1. 

$${\mathbf 0}=
\left[\begin{array}{c}
0\\
0\\
0\\
0
\end{array}\right].$$

2. 

$${\mathbf 0}=
\left[\begin{array}{c}
0\\
0\\
0
\end{array}\right].$$

```

+++

### Spørgsmål b

Angiv en ordnet basis og en basis for de givne vektorrum. 
Hvad er rummenes dimensioner?

```{hint}
:class: dropdown
For det reelle vektorrum $\mathbb{R}^{4}$ kan du finde en mulig ordnet basis i Eksempel 9.2.1.
```

```{admonition} Svar
:class: dropdown
Der gives svar for det reelle vektorrum $\mathbb{R}^{4}$. En mulig ordnet basis er den ordnede standardbasis fra Eksempel 9.2.1, som er

$$\left(
\left[\begin{array}{c}
1\\
0\\
0\\
0
\end{array}\right],
\left[\begin{array}{c}
0\\
1\\
0\\
0
\end{array}\right],
\left[\begin{array}{c}
0\\
0\\
1\\
0
\end{array}\right],
\left[\begin{array}{c}
0\\
0\\
0\\
1
\end{array}\right]       
\right).$$

Dimensionen af rummet er derfor $4$.

En basis for $\mathbb{R}^{4}$ fås ved at tage mængden af vektorerne som indgår i dens ordnede standardbasis. 
En mulig basis er derfor:

$$\left\{
\left[\begin{array}{c}
1\\
0\\
0\\
0
\end{array}\right],
\left[\begin{array}{c}
0\\
1\\
0\\
0
\end{array}\right],
\left[\begin{array}{c}
0\\
0\\
1\\
0
\end{array}\right],
\left[\begin{array}{c}
0\\
0\\
0\\
1
\end{array}\right]       
\right\}.$$
```

+++

----

+++

## Opgave 2: Koordinatvektoren af en vektor med hensyn til en ordnet basis

Lad $W= \{a+bZ+cZ^2 \, \mid \, a,b,c\in \mathbb{C}\} \subset \mathbb{C}[Z]$ være mængden bestående af alle polynomier af grad højst to.

+++

### Spørgsmål a

Tjek at $W$ er et underrum af det komplekse vektorrum $\mathbb{C}[Z]$. 
+++

```{hint}
:class: dropdown
Lemma 10.4.2 fra lærebogen kan være nyttigt her.
```

+++

### Spørgsmål b

Tjek at listen $(1,Z,Z^2)$ er en ordnet basis for $W$. Tjek at listen $(1,1+Z,1+Z+Z^2)$ også er en ordnet basis for $W$.

```{hint}
:class: dropdown
Ifølge Definition 10.2.4 skal man tjekke to ting til hver givet følge: 1. at de tre givne polynomier i følgen er lineært uafhængige og 2. at hvert polynomium fra $W$ kan skrives som en linearkombination af de tre polynomier i listen.
```

+++

### Spørgsmål c

Der betragtes de to ordnede baser for $W$ fra spørgsmål b, nemlig $\beta=(1,Z,Z^2)$ og $\gamma=(1,1+Z,1+Z+Z^2)$. 
Bestem følgende koordinatvektorer:

$$\left[2+5Z+Z^2\right]_\beta \, , \quad \left[5Z+10Z^2\right]_\beta$$

og

$$\left[2+5Z+Z^2\right]_\gamma \, , \quad \left[5Z+10Z^2\right]_\gamma \, .$$

```{hint}
:class: dropdown
Hvis du er i tvivl om hvad en koordinatvektor for en vektor med hensyn til en ordnet basis er, se Definition 10.2.5 fra lærebogen.
```

```{admonition} Svar
:class: dropdown
$$
\left[2+5Z+Z^2\right]_\beta=
\left[\begin{array}{c}
2\\
5\\
1\\
\end{array}\right], 
\quad 
\left[5Z+10Z^2\right]_\beta=
\left[\begin{array}{c}
0\\
5\\
10\\
\end{array}\right], 
\quad 
\left[2+5Z+Z^2\right]_\gamma=
\left[\begin{array}{c}
-3\\
4\\
1\\
\end{array}\right], 
\quad 
\left[5Z+10Z^2\right]_\gamma=
\left[\begin{array}{c}
-5\\
-5\\
10\\
\end{array}\right].$$
```

+++

----

+++

## Opgave 3: Flere eksempler på vektorrum

I denne opgave stilles de samme spørgsmål som i opgave 1, men nu for nogle andre vektorrum:

1. Det reelle vektorrum $V_3=\mathbb{R}^{4 \times 2}$.

2. Det komplekse vektorrum $V_4=\mathbb{C}[Z]$.

3. Det reelle vektorrum $V_5=\mathbb{C}$.

### Spørgsmål a

Angiv nulvektoren i hvert af de ovenstående vektorrum.

```{admonition} Svar
:class: dropdown
1. 

$${\mathbf 0}=
\left[\begin{array}{cc}
0 & 0\\
0 & 0\\
0 & 0\\
0 & 0\\
\end{array}\right].$$

2.

Nulvektoreren er nulpolynomiet $0$, dvs. polynomiet hvorom det gælder at alle dets koefficienter er nul.

3.

Nulvektoreren er det komplekse tal $0$.
```

+++

### Spørgsmål b

Angiv en basis af de givne vektorrum og bestem rummenes dimensioner.


```{hint}
:class: dropdown
I hvert tilfælde kan du finde en mulig basis i lærebogen. Se Eksempler 10.2.5, 10.2.6 og 10.2.7.
```

```{admonition} Svar
:class: dropdown
Mulige baser for vektorrummene er hhv. 

$$\left\{
\left[\begin{array}{cc}
1 & 0\\
0 & 0\\
0 & 0\\
0 & 0\\
\end{array}\right],
\left[\begin{array}{cc}
0 & 0\\
1 & 0\\
0 & 0\\
0 & 0\\
\end{array}\right],
\left[\begin{array}{cc}
0 & 0\\
0 & 0\\
1 & 0\\
0 & 0\\
\end{array}\right],
\left[\begin{array}{cc}
0 & 0\\
0 & 0\\
0 & 0\\
1 & 0\\
\end{array}\right],
\left[\begin{array}{cc}
0 & 1\\
0 & 0\\
0 & 0\\
0 & 0\\
\end{array}\right],
\left[\begin{array}{cc}
0 & 0\\
0 & 1\\
0 & 0\\
0 & 0\\
\end{array}\right],
\left[\begin{array}{cc}
0 & 0\\
0 & 0\\
0 & 1\\
0 & 0\\
\end{array}\right],
\left[\begin{array}{cc}
0 & 0\\
0 & 0\\
0 & 0\\
0 & 1\\
\end{array}\right]
\right\},$$

$\{1,Z,Z^2,Z^3,\dots\}$ og $\{1,i\}$. Dimensionerne er givet ved hhv. $8, \infty, 2$.
```

+++

----

+++


## Opgave 4: Lineær afhængighed eller uafhængighed


Undersøg om vektorerne er lineært afhængige eller lineært uafhængige i følgende tilfælde. 
Ved lineær afhængighed ønskes én af vektorerne skrevet som en linearkombination af de øvrige. 

1. Vektorerne $\left[
    \begin{array}{r}
1 \newline  i
    \end{array}\right],
    \left[
    \begin{array}{r}
1+i \newline  -1+i
    \end{array}\right]$ 
i det komplekse vektorrum $\mathbb{C}^{2}$.

2. Matricerne 
$\left[
    \begin{array}{rrr}
1 & 2 & 0 \newline  1 & 1 & 1
    \end{array}\right], \left[
    \begin{array}{rrr}
1 & 1 & 2 \newline  0 & 0 & 1
    \end{array}\right], \left[
    \begin{array}{rrr}
2 & 5 & -2 \newline  3 & 3 & 2
    \end{array}\right]$ i det reelle vektorrum $\mathbb{R}^{2\times 3}$.

3. Vektorerne $\left[
    \begin{array}{r}
1 \newline  i
    \end{array}\right],
    \left[
    \begin{array}{r}
1+i \newline  -1+i
    \end{array}\right]$ i det reelle vektorrum $\mathbb{C}^{2}$.

4. Polynomierne $1 + 2Z + Z^{2}, \, 2 + 7Z +3Z^{2} + Z^{3}, \, 3 + 12Z + 5Z^{2} +2Z^{3}$  i  det reelle vektorrum $\mathbb{R}[Z]$.


```{hint}
:class: dropdown
Ifølge Definition 10.2.1 fra lærebogen skal det undersøges om der findes en linearkombination af de givne vektorer som giver nul, selvom ikke alle skalarer i linearkombinationen er nul.

Tilfælde 1. kan derfor direkte løses vha. teorien om systemer af lineære ligninger. 

Tilfælde 2. kan løses direkte ved at undersøge om en linearkombination kan give nulvektoren. 
Alternativt, kan man også løse opgaven vha. Sætning 10.2.4 fra lærebogen efter man vælger en ordnet basis for $\mathbb{R}^{2\times 3}$.

Tilfælde 3. kan løses på lignende måde som Tilfælde 2. Bemærk dog at $\mathbb{C}^{2}$ betragtes som et reelt vektorrum i opgaven. 
Derfor skal skalarerne i en linearkombination være reelle tal.

Tilfælde 4. foregår i princippet i det reelle, uendelig-dimensionelle vektorrum $\mathbb{R}[Z]$. Bemærk dog at ligningen 

$$c_1\cdot(1 + 2Z + Z^{2})+c_2\cdot(2 + 7Z +3Z^{2} + Z^{3})+c_3\cdot(3 + 12Z + 5Z^{2} +2Z^{3})=0$$ 

straks giver anledning til et system af lineære ligninger i de ubekendte $c_1,c_2$ og $c_3$. Hvilket?
%hvis og kun hvis 
%
%$$c_1\cdot\left[\begin{array}{c}1\\2\\1\\0\end{array}\right]+c_2\cdot\left[\begin{array}{c}2\\7\\3\\1\end{array}\right]+c_3\cdot\left[\begin{array}{c}3\\12\\5\\2\end{array}\right]=\left[\begin{array}{c}0\\0\\0\\0\end{array}\right].$$
```

```{admonition} Svar
:class: dropdown
1. De to vektorer er lineært afhængige. Man har for eksempel 
$\left[
    \begin{array}{r}
1+i \newline  -1+i
    \end{array}\right]
=
(1+i)\left[
    \begin{array}{r}
1 \newline  i
    \end{array}\right]\, .
$

2. De tre matricer er lineært afhængige. Det gælder for eksempel at 

$$
\left[
\begin{array}{rrr}
2 & 5 & -2 \\ 
3 & 3 & 2
\end{array}\right]
=
3\left[
\begin{array}{rrr}
1 & 2 & 0 \\  
1 & 1 & 1
\end{array}\right]
-
\left[
\begin{array}{rrr}
1 & 1 & 2 \\  
0 & 0 & 1
\end{array}\right]\,. 
$$ 

3. Vektorerne $\left[
    \begin{array}{r}
1 \newline  i
    \end{array}\right]$ og 
$\left[
    \begin{array}{r}
1+i \newline  -1+i
    \end{array}\right]$
er lineært uafhængige hvis $\mathbb{C}^2$ betragtes som reel vektorrum.


4. De tre polynomier er lineært afhængige. Der gælder for eksempel

$$
3 + 12Z + 5Z^{2} +2Z^{3}=-(1 + 2Z + Z^{2})+2\cdot(2 + 7Z +3Z^{2} + Z^{3}).
$$  
```

+++

----

+++


## Opgave 5: Underrum af $\mathbb{R}^{3 \times 3}$

Lad $V=\mathbb{R}^{3 \times 3}$ være det reelle vektorrum bestående af alle $3 \times 3$ matricer med reelle koefficienter. 
Der gives følgende tre delmængder af $V$.

1. $W_1$ er mængden af alle øvre trekantsmatricer i $V$.

2. $W_2$ er mængden af alle diagonalmatricer i $V$

3. $W_3=\left\{ {\mathbf A} \in \mathbb{R}^{3 \times 3} \, \mid \, {\mathbf A} = -{\mathbf A}^T\right\}.$

+++

### Spørgsmål a

Tjek at $W_1$, $W_2$ og $W_3$ alle er underrum af $V$.

```{hint}
:class: dropdown
Lemma 10.4.2 fra lærebogen kan med fordel bruges til at vise at en delmængde af et vektorrum er et underrum.
```

+++

### Spørgsmål b

Find en basis for de tre underrum $W_1$, $W_2$ og $W_3$. Hvad er underrummenes dimensioner?

```{admonition} Svar
:class: dropdown 
1. En mulig basis til $W_1$ er 

$$\left\{ 
\left[
\begin{array}{rrr}
1 & 0 & 0 \\  
0 & 0 & 0 \\
0 & 0 & 0\\
\end{array}\right],
\left[
\begin{array}{rrr}
0 & 1 & 0 \\  
0 & 0 & 0 \\
0 & 0 & 0\\
\end{array}\right],
\left[
\begin{array}{rrr}
0 & 0 & 1 \\  
0 & 0 & 0 \\
0 & 0 & 0\\
\end{array}\right],
\left[
\begin{array}{rrr}
0 & 0 & 0 \\  
0 & 1 & 0 \\
0 & 0 & 0\\
\end{array}\right],
\left[
\begin{array}{rrr}
0 & 0 & 0 \\  
0 & 0 & 1 \\
0 & 0 & 0\\
\end{array}\right],
\left[
\begin{array}{rrr}
0 & 0 & 0 \\  
0 & 0 & 0 \\
0 & 0 & 1\\
\end{array}\right]
\right\}.$$ 

Derfor gælder $\dim_{\mathbb R}(W_1)=6.$

2. En mulig basis til $W_2$ er 

$$\left\{ 
\left[
\begin{array}{rrr}
1 & 0 & 0 \\  
0 & 0 & 0 \\
0 & 0 & 0\\
\end{array}\right],
\left[
\begin{array}{rrr}
0 & 0 & 0 \\  
0 & 1 & 0 \\
0 & 0 & 0\\
\end{array}\right],
\left[
\begin{array}{rrr}
0 & 0 & 0 \\  
0 & 0 & 0 \\
0 & 0 & 1\\
\end{array}\right]
\right\}.$$ 

Derfor gælder $\dim_{\mathbb R}(W_2)=3.$

3. En mulig basis til $W_3$ er 

$$\left\{ 
\left[
\begin{array}{rrr}
0 & 1 & 0 \\  
-1 & 0 & 0 \\
0 & 0 & 0\\
\end{array}\right],
\left[
\begin{array}{rrr}
0 & 0 & 1 \\  
0 & 0 & 0 \\
-1 & 0 & 0\\
\end{array}\right],
\left[
\begin{array}{rrr}
0 & 0 & 0 \\  
0 & 0 & 1 \\
0 & -1 & 0\\
\end{array}\right]
\right\}.$$ 

Derfor gælder $\dim_{\mathbb R}(W_3)=3.$
```

+++

----

+++


## Opgave 6: Underrum af $\mathbb{C}[Z]$.

Hvilke af følgende tre mængder er underrum af det komplekse vektorrum $\mathbb{C}[Z]$?

1. $W_1=\{p(Z) \in \mathbb{C}[Z] \, \mid \, p(0)=0\}.$

2. $W_2=\{p(Z) \in \mathbb{C}[Z] \, \mid \, 0 \text{ er rod i } p(Z) \text{ med multiplicitet } 1\}.$

3. $W_3=\{p(Z) \in \mathbb{C}[Z] \, \mid \, Z\cdot p'(Z)=p(Z)\},$ hvor $p'(Z)$ betegner den afledte til $p(Z)$. 
Dvs, hvis $p(Z)=a_0+a_1Z+a_2Z^2+\cdots+a_nZ^n$, så er $p'(Z)=a_1+2a_2Z+\cdots+na_nZ^{n-1}$. 

```{admonition} Svar
:class: dropdown 
1. Lemma 10.4.2 fra lærebogen kan bruges til at vise at $W_1$ er et underrum af $\mathbb{C}[Z]$.

2. $W_2$ er ikke et underrum af $\mathbb{C}[Z]$. 
Problemet er at en linearkombination af polynomier som hvert har $0$ som rod med multiplicitet $1$, kan have $0$ som rod med multiplicitet strengt større end $1$. 
For eksempel: $Z\cdot(Z-1)=Z^2-Z$ og $Z$ er i $W_2$, men $Z\cdot(Z-1)+Z=Z^2$ er ikke i $W_2$, fordi $Z^2$ har $0$ som rod med multiplicitet $2$.

3. $p(Z)=p'(Z)$ præcist hvis $p(Z)=a_1Z$ med $a\1 \in \mathbb{C}$. 
Derfor gælder $W_3=\{a_1Z \, \mid \, a_1 \in \mathbb{C}\}.$ 
Men i så fald gælder at $W_3=\mathrm{Span}(Z)$ og medfører Proposition 10.4.3 fra lærebogen at $W_3$ er et underrum af $\mathbb{C}[Z]$.
```

+++

----

+++

## Opgave 7: Underrum og lineære ligningssystemer

Der betragtes følgende lineære ligningssystem over $\mathbb R$

$$
\left\{
\begin{array}{rcl}
x_2 +3x_3 - x_4+2x_5 & = & 0\\ 
2x_1+3x_2+x_3+3x_4 & = & 0\\ 
x_1 + x_2 -x_3 + 2x_4-x_5 & = & 0
\end{array}
\right.
$$

Bemærk at dette system også blev undersøgt i Opgave 5 i opgaveprogrammet fra Uge 8, Store Dag. Systemets løsningsmængde betegnes med $W$.


+++

### Spørgsmål a

Gør rede for at $W$ er et underrum i $\mathbb{R}^5\,$, bestem $\dim(W)$ dimension og bestem en basis for $W$.

```{hint}
:class: dropdown
I Opgave 5 i opgaveprogrammet fra Uge 8, Store Dag, blev det allerede vist at løsningsmængden er en udspænding at visse vektorer. 
Hvorfor medfører dette at løsningsmængden er et underrum i $\mathbb{R}^5\,$?
```

```{admonition} Svar
:class: dropdown 
Proposition 10.4.3 og observationen fra vinket medfører at $W$ er et underrum $\mathbb{R}^5\,$.
I Opgave 5 i opgaveprogrammet fra Uge 8, Store Dag blev der allerede fundet en ordnet basis for $W$, samt at dens dimension er $3$.
Bruges den ordnede basis angivet i svaret fra Opgave 5, Uge 8, Store Dag, så få at følgende er en mulig basis for $W$:

$$\left\{ 
\left[\begin{array}{c}
4\\
-3\\
1\\
0\\
0\\
\end{array}\right], \, 
\left[\begin{array}{c}
-3\\
1\\
0\\
1\\
0\\
\end{array}\right], \, 
\left[\begin{array}{c}
3\\
-2\\
0\\
0\\
1\\
\end{array}\right]
\right\}.$$
```

+++

### Spørgsmål b

Lad $\beta$ være en ordnet basis for $W$. 
Der gives tre vektorer $\mathbf{v}_1,\mathbf{v}_2$ og $\mathbf{v}_3$ i $W$ som opfylder at

$$[\mathbf{v}_1]_\beta=\left[\begin{array}{c} 1\\ 0 \\ -2\end{array}\right]\, , \quad [\mathbf{v}_2]_\beta=\left[\begin{array}{c} 1 \\ 1 \\ 1\end{array}\right] \quad \text{og} \quad [\mathbf{v}_3]_\beta=\left[\begin{array}{c} 2 \\ 0 \\ 1 \end{array}\right].$$

Er $\{\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3\}$ en basis for $W$?

```{hint}
:class: dropdown
Prøv først at vise at sættet $(\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3)$ er lineært uafhængigt. 
Læs eventuelt først Sætning 10.2.4 fra lærebogen.
```

```{hint}
:class: dropdown
Kan Sætning 10.2.7 fra lærebogen bruges?
```

```{admonition} Svar
:class: dropdown 
Ja, $\{\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3\}$ er en basis for $W$.
```

+++

----

+++


## Opgave 8: Underrum

Lad $V$ være et vektorrum over et legeme $\mathbb F$. 

+++

### Spørgsmål a

Givet to underrum $W_1$, $W_2$ i $V$, vis at $W_1 \cap W_2$ også er et underrum i $V$.


+++

### Spørgsmål b

Find et eksempel på et reelt vektorrum $V$ og to underrum $W_1$, $W_2$ i $V$, således at $W_1 \cup W_2$ ikke er et underrum i $V$.

## Bemærkning

Der åbnes en Möbius test om forrige ugens Pythonopgave kl. 15:30