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

(section:uge7L)=

# Opgaver -- Lille Dag

----

+++

## Opgave 1: Transponerede matricer

Beregn 

$$\left[
\begin{array}{cc}
1 & 2\\
3 & 4\\
5 & 6\\
\end{array}
\right]^T.$$


```{admonition} Svar
:class: dropdown
Den transponerede matrix er

$$\left[
\begin{array}{ccc}
1 & 3 & 5\\
2 & 4 & 6\\
\end{array}
\right].$$
%I SymPy kan den transponerede af en matrix `A` beregnes med kommandoen `A.transpose()`.
```

+++

----

+++

## Opgave 2: Determinanter

Givet er følgende matrix:

$$
{\mathbf A}=\left[
\begin{array}{ccc}
1 & 3 & 5\\
2 & 4 & 6\\
3 & 0 & 0\\
\end{array}
\right].
$$

Formålet med opgaven er at beregne matricens determinant, ved at udvikle determinanten efter en række eller søjle.

+++

### Spørgsmål a

Beregn matricerne ${\mathbf A}(1;1)$, ${\mathbf A}(2;1)$ og ${\mathbf A}(3;1)$ og deres determinanter.

```{hint}
:class: dropdown
I Definition 8.1.1 fra lærebogen bliver notationen ${\mathbf A}(i;j)$ forklaret.
```

```{admonition} Svar
:class: dropdown
$$
{\mathbf A}(1;1)=\left[
\begin{array}{ccc}
4 & 6\\
0 & 0\\
\end{array}
\right] \quad {\mathbf A}(2;1)=\left[
\begin{array}{ccc}
3 & 5\\
0 & 0\\
\end{array}
\right] \quad {\mathbf A}(3;1)=\left[
\begin{array}{ccc}
3 & 5\\
4 & 6\\
\end{array}
\right].
$$

Determinanterne fås direkte ved at bruge Eksempel 8.1.1 fra lærebogen: 

$$\mathrm{det}({\mathbf A(1;1)})=0 \quad \mathrm{det}({\mathbf A(2;1)})=0 \quad \mathrm{det}({\mathbf A(3;1)})=-2.$$
```

+++

### Spørgsmål b

Beregn $\mathrm{det}({\mathbf A})$ ved at bruge Definition 8.1.2 fra lærebogen. 
Med andre ord: beregn $\mathrm{det}({\mathbf A})$ ved at udvikle determinanten efter den 1. søjle.

```{admonition} Svar
:class: dropdown
Ved at udvikle efter den 1. søjle, fås fra Definition 8.1.2 at

$$\mathrm{det}({\mathbf A})=1\cdot \mathrm{det}({\mathbf A}(1;1))-2\cdot \mathrm{det}({\mathbf A}(2;1))+3\cdot \mathrm{det}({\mathbf A}(3;1))=-6.$$
```

+++

### Spørgsmål c

For den givne matrix ${\mathbf A}$ er det mere bekvemt at udvikle determinanten efter matricens tredje række. Hvorfor?
 
```{hint}
:class: dropdown
I starten af Afsnit 8.2 forklares hvad det betyder at udvikle en determinant efter en række eller en søjle. 
```

```{admonition} Svar
:class: dropdown
På grund af de mange nuller i matricens tredje række gælder:

$$
\mathrm{det}({\mathbf A})=3\cdot \mathrm{det}({\mathbf A}(3;1))=3 \cdot (3 \cdot 6-4 \cdot 5)=-6.
$$
```

+++

### Spørgsmål d

For at øve sig i udvikling af en determinant efter en række, bestemmes $\mathrm{det}({\mathbf A})$ en sidste gang.
Beregn matricerne ${\mathbf A}(2;1)$, ${\mathbf A}(2;2)$ og ${\mathbf A}(2;3)$ og deres determinanter. 
Beregn nu $\mathrm{det}({\mathbf A})$ ved at udvikle determinanten efter den 2. række.

```{admonition} Svar
:class: dropdown
$$
{\mathbf A}(2;1)=\left[
\begin{array}{ccc}
3 & 5\\
0 & 0\\
\end{array}
\right] \quad {\mathbf A}(2;2)=\left[
\begin{array}{ccc}
1 & 5\\
3 & 0\\
\end{array}
\right] \quad {\mathbf A}(2;3)=\left[
\begin{array}{ccc}
1 & 3\\
3 & 0\\
\end{array}
\right].
$$

og

$$\mathrm{det}({\mathbf A(2;1)})=0 \quad \mathrm{det}({\mathbf A(2;2)})=-15 \quad \mathrm{det}({\mathbf A(2;3)})=-9.$$

Nu fås ved at udvikle efter den 2. række, at

$$\mathrm{det}({\mathbf A})=-2\cdot \mathrm{det}({\mathbf A}(2;1))+4\cdot \mathrm{det}({\mathbf A}(2;2))-6\cdot \mathrm{det}({\mathbf A}(2;3))=-6.$$
```
%
%+++
%
%### Spørgsmål e
%
%Til sidst, beregn $\mathrm{det}({\mathbf A})$ i SymPy.
%
%```{hint}
%:class: dropdown
%Determinanten af en kvadratisk matrix `A` kan beregnes med kommandoen `A.det()`.
%```

+++

----

+++

## Opgave 3: Determinanter og lineært uafhængighed

Givet er følgende tre vektorer i $\mathbb{R}^3$: 

$$
{\mathbf v_1}=\left[
\begin{array}{c} 
1\\
0\\
4\\
\end{array}
\right], \quad 
{\mathbf v_2}=\left[
\begin{array}{c} 
1\\
1\\
7\\
\end{array}
\right], \quad 
{\mathbf v_3}=\left[
\begin{array}{c} 
1\\
-1\\
1\\
\end{array}
\right].
$$

+++

Brug Korollar 8.2.5 fra lærebogen til at afgøre om vektorerne ${\mathbf v}_1, {\mathbf v}_2$ og ${\mathbf v}_3$ er lineært uafhængige eller ej. 
%SymPy kan bruges til at beregne determinanter.

```{hint}
:class: dropdown
Beregn først determinanten af matricen som har søjler ${\mathbf v}_1, {\mathbf v}_2$ og ${\mathbf v}_3$. 
Udvikl determinanten efter en søjle eller række mest flest nultaller for at bespare lidt arbejde.
```

```{hint}
:class: dropdown
I Korollar 8.2.5 er det afgørende punkt om determinanten af matricen nævnt i det forrige vink er nul er ej.
```

```{admonition} Svar
:class: dropdown
De givne tre vektorer er lineært afhængige. 
```

+++

----

+++

## Opgave 4: Lineært afhængighed

Givet er vektorerne 

$$
{\mathbf u}_1=\left[
\begin{array}{c}
1\\
1\\
-6\\
\end{array}
\right] \quad
{\mathbf u}_2=\left[
\begin{array}{c}
1\\
1\\
a\\
\end{array}
\right] \quad
{\mathbf u}_3=\left[
\begin{array}{c}
a\\
-2\\
0\\
\end{array}
\right],
$$

hvor $a \in \mathbb{R}$ er en konstant. 
Bestem alle værdier af konstanten $a$ således at vektorerne ${\mathbf u}_1$, ${\mathbf u}_2$ og ${\mathbf u}_3$ er lineært afhængige. 

```{hint}
:class: dropdown
Korollar 8.2.5 fra lærebogen kan igen bruges. 
```

```{hint}
:class: dropdown
Determinanten til matricen 

$$
{\mathbf A}=\left[
\begin{array}{ccc}
1 & 1 & a\\
1 & 1 & -2\\
-6 & a & 0\\
\end{array}
\right]
$$

viser sig efter nogle mellemregninger til at være lig med $a^2+8a+12$. 
For hvilke værdier af $a$ er determinanten lig med nul? 
```

```{admonition} Svar
:class: dropdown
Fordi $a^2+8a+12=0$ hvis og kun hvis $a=-2 \, \vee a=-6$, fås vha. Korollar 8.2.5 at de tre givne vektorer er lineært afhængige hvis og kun hvis $a \in \{-2,-6\}.$
```

+++

----

+++

## Opgave 5: Kvadratiske transponerede matricer

Det vides fra Sætning 7.2.2 i lærebogen at $({\mathbf A} \cdot {\mathbf B})^T={\mathbf B}^T \cdot {\mathbf A}^T$ for alle ${\mathbf A} \in \mathbb{F}^{m \times n}$ og ${\mathbf B} \in \mathbb{F}^{n \times \ell}$. 
Betegnelsen $\mathbb{F}$ står for $\mathbb{R}$ eller $\mathbb{C}.$

+++

### Spørgsmål a

Konkluder at $({\mathbf A} \cdot {\mathbf B})^T={\mathbf B}^T \cdot {\mathbf A}^T$ for alle ${\mathbf A},{\mathbf B} \in \mathbb{F}^{n \times n}$. 

```{hint}
:class: dropdown
Man kan sætte $m$ og $\ell$ lig med $n$. 
```

+++

### Spørgsmål b

Antag at matricen $\mathbf A \in \mathbb{F}^{n \times n}$ og at $\rho({\mathbf A})=n$. Brug resultatet fra spørgsmål a til at indse at $({\mathbf A}^{T})^{-1}=({\mathbf A}^{-1})^T.$ 

```{hint}
:class: dropdown
Start med at finde ude af hvilke egenskaber den inverse matrix til ${\mathbf A}^{T}$ skulle have ifølge Definition 7.3.1.
```

```{hint}
:class: dropdown
${\mathbf A}^{-1}$ findes, fordi $\rho({\mathbf A})=n$. Derfor kan vi definere matricen $\mathbf B=({\mathbf A}^{-1})^T$. 
Brug nu resultatet fra spørgsmål a for at indse at matricen $\mathbf B$ har præcist de ønskede egenskaber som den inverse til ${\mathbf A}^T$ skal have ifølge Definition 7.3.1. Hvis egenskaberne er opnået, så kan man konkludere at ${\mathbf B}=({\mathbf A}^T)^{-1}$.
```

