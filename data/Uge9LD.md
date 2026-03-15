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

# Opgaver -- Lille Dag

----

+++

## Opgave 1: Eksempel på en basisskiftematrix

I denne opgave betegnes med $V$ det reelle vektorrum $\mathbb{R}^2$. 
Ydermere gives følgende to ordnede baser $\beta$ og $\gamma$ for $\mathbb{R}^2$:

$$\beta=\left( \left[\begin{array}{c}
4\\
1
\end{array}\right],
\left[\begin{array}{c}
7\\
2
\end{array}\right]\right)$$

og 

$$\gamma=\left( \left[\begin{array}{c}
1\\
2
\end{array}\right],
\left[\begin{array}{c}
2\\
3
\end{array}\right]\right).$$


+++

### Spørgsmål a

Beregn $\left[\begin{array}{c}
4\\
1
\end{array}\right]_\gamma$ og $\left[\begin{array}{c}
7\\
2
\end{array}\right]_\gamma$.

```{hint}
:class: dropdown
Ifølge Definition 10.2.5 gælder $\left[\begin{array}{c}
4\\
1
\end{array}\right]_\gamma=\left[\begin{array}{c}
c_1\\
c_2
\end{array}\right],$ hvor $\left[\begin{array}{c}
4\\
1
\end{array}\right]=c_1\left[\begin{array}{c}
1\\
2
\end{array}\right]+c_2\left[\begin{array}{c}
2\\
3
\end{array}\right].$ 
Bestem nu $c_1,c_2$ ved at løse det tilhørende lineære ligningssystem.
```

```{admonition} Svar
:class: dropdown
$\left[\begin{array}{c}
4\\
1
\end{array}\right]_\gamma=\left[\begin{array}{c}
-10\\
7
\end{array}\right]$ og $\left[\begin{array}{c}
7\\
2
\end{array}\right]_\gamma=\left[\begin{array}{c}
-17\\
12
\end{array}\right]$.
```

+++

### Spørgsmål b

Brug svarene fra spørgsmål a til at bestemme basisskiftematricen ${ }_{\gamma}M_{\beta}$. 

```{hint}
:class: dropdown
I formuleringen af Sætning 10.2.5 står hvordan matricen ${ }_{\gamma}M_{\beta}$ er defineret.
```

```{admonition} Svar
:class: dropdown

$${ }_{\gamma}M_{\beta}=\left[\begin{array}{cc}
-10 & -17\\
7 & 12
\end{array}\right].$$

```

+++

----

+++


## Opgave 2: Mere om basisskiftematricer

Ligesom i Opgave 1, betegnes $V$ det reelle vektorrum $\mathbb{R}^2$. 
Rummets ordnede standardbasis betegnes med $\varepsilon$, mens $\beta$ og $\gamma$ er de ordnede baser givet i Opgave 1. 
Målet med opgaven er at beregne basisskiftematricen ${ }_{\gamma}M_{\beta}$ fra Opgave 1 på en anden måde, som nogle gange kan være lettere.

+++

### Spørgsmål a

Beregn basisskiftematricerne ${ }_{\varepsilon}M_{\beta}$ og ${ }_{\varepsilon}M_{\gamma}.$

```{admonition} Svar
:class: dropdown

$${ }_{\varepsilon}M_{\beta}=
\left[\begin{array}{rr}
4 & 7\\
1 & 2
\end{array}\right]$$

og

$${ }_{\varepsilon}M_{\gamma}=
\left[\begin{array}{rr}
1 & 2\\
2 & 3
\end{array}\right]\, .$$

Bemærkning: generelt er det nemt at bestemme en basisskiftematrix på formen ${ }_{\varepsilon}M_{\beta}$, når $\varepsilon$ er den ordnede standardbasis for $\mathbb{F}^n$.
```

+++

### Spørgsmål b

Brug del (iii) af Lemma 10.3.2 fra lærebogen, samt svarene fra spørgsmål a, til at bestemme basisskiftematricen 
${ }_{\gamma}M_{\varepsilon}$.

```{admonition} Svar
:class: dropdown
%$${ }_{\beta}M_{\varepsilon}=
%\left[\begin{array}{rr}
%4 & 7\\
%1 & 2
%\end{array}\right]^{-1}=\left[\begin{array}{rr}
%2 & -7\\
%-1 & 4
%\end{array}\right]\,
%$$
%
%og

$${ }_{\gamma}M_{\varepsilon}=
\left[\begin{array}{rr}
1 & 2\\
2 & 3
\end{array}\right]^{-1}=\left[\begin{array}{rr}
-3 & 2\\
2 & -1
\end{array}\right]\, .
$$

```

+++

### Spørgsmål c

Brug del (i) af Lemma 10.3.2 fra lærebogen, samt svarene fra spørgsmål a og b, til at bestemme basisskiftematricen ${ }_{\gamma}M_{\beta}$.

```{admonition} Svar
:class: dropdown

$$
{ }_{\gamma}M_{\beta}={ }_{\gamma}M_{\varepsilon} \, { }_{\varepsilon}M_{\beta}=\left[\begin{array}{rr}
-3 & 2\\
2 & -1
\end{array}\right]\left[\begin{array}{rr}
4 & 7\\
1 & 2
\end{array}\right]=\left[\begin{array}{rr}
-10 & -17\\
7 & 12
\end{array}\right].
$$

```
+++

----

+++

## Opgave 3: Koordinatvektoren af en vektor med hensyn til to ordnede baser

Notation i denne opgave er den samme som i Opgave 2 fra Uge 9, Store Dag. 
Især er $W= \{a+bZ+cZ^2 \, \mid \, a,b,c\in \mathbb{C}\} \subset \mathbb{C}[Z]$ det komplekse vektorrum bestående af alle polynomier af grad højst to.
Der betragtes to ordnede baser for $W$, nemlig $\beta=(1,Z,Z^2)$ og $\gamma=(1,1+Z,1+Z+Z^2)$. 
+++

### Spørgsmål a

Bestem basisskiftematricen ${ }_{\beta}M_\gamma$.

+++

### Spørgsmål b

Det oplyses at $\left[2+5Z+Z^2\right]_\gamma=
\left[\begin{array}{c}
-3\\
4\\
1\\
\end{array}\right]$. Brug Sætning 10.3.1 fra lærebogen til at bestemme $\left[2+5Z+Z^2\right]_\beta$.

```{admonition} Svar
:class: dropdown

$$
\left[2+5Z+Z^2\right]_\beta=
\left[\begin{array}{c}
2\\
5\\
1\\
\end{array}\right].$$

```

+++

### Spørgsmål c

Bestem basisskiftematricen ${ }_{\gamma}M_\beta$ ved hjælp af del (iii) af Lemma 10.3.2.

```{admonition} Svar
:class: dropdown

$${ }_{\gamma}M_\beta=\left[\begin{array}{ccc}
1 & -1 & 0\\
0 & 1 & -1\\
0 & 0 & 1\\
\end{array}\right].$$

```

+++

### Spørgsmål d

Det oplyses at $\left[5Z+10Z^2\right]_\beta=
\left[\begin{array}{c}
0\\
5\\
10\\
\end{array}\right]$. Brug Sætning 10.3.1 fra lærebogen til at bestemme $\left[5Z+10Z^2\right]_\gamma$.

```{admonition} Svar
:class: dropdown

$$
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

## Opgave 4: Udspænding af vektorer

Det gives følgende fire polynomier i $\mathbb{R}[Z]$: $p_1(Z)=1+3Z^2$, $p_2(Z)=-2+Z^2$, $p_3=5+6Z^2$ og $p_4(Z)=1+Z^2+Z^5$. 
Der defineres $W=\mathrm{Span}(p_1(Z),p_2(Z),p_3(Z),p_4(Z)).$ 

+++

### Spørgsmål a

Bestem den ordnede basis $\beta$ for $W$ som Sætning 10.4.4 fra lærebogen giver anledning til. 

```{admonition} Svar
:class: dropdown
$\beta=(p_1(Z),p_2(Z),p_(4))$.
```

+++

### Spørgsmål b 

Vis at polynomiet $p(Z)=Z^5$ er i $W$ og bestem $[p(Z)]_\beta$, hvor $\beta$ er den ordnede basis fundet i spørgsmål a. 

+++

### Spørgsmål c

Nogen påstår at listen $\gamma=(1,Z^2,Z^5)$ også er en ordnet basis for $W$. Er påstanden sand? 

```{admonition} Svar
:class: dropdown
Ja.
```

+++

### Spørgsmål d

Bestem koordinatskiftematricer ${ }_\beta M_\gamma$ og ${ }_\gamma M_\beta$. 
Inden du går i gang, overvej først hvilke af disse to er nemmest at bestemme.

```{admonition} Svar
:class: dropdown

$${ }_{\gamma}M_\beta=\left[\begin{array}{ccc}
1 & -2 & 1\\
3 & 1 & 1\\
0 & 0 & 1\\
\end{array}\right]$$

og

$${ }_{\beta}M_\gamma=\frac{1}{7}\left[\begin{array}{ccc}
1 & 2 & -3\\
-3 & 1 & 2\\
0 & 0 & 7\\
\end{array}\right].$$


```

+++

----

+++


## Opgave 5: Lineært uafhængighed

Lad $V$ være et endeligt dimensionelt vektorrum og $\beta$ en ordnet basis for $V$. 
Det oplyses at for givne vektorer $\mathbf{v}_1,\mathbf{v}_2, \cdots, \mathbf{v}_n$ sættet $([\mathbf{v}_1]_\beta, [\mathbf{v}_2]_\beta, \dots, [\mathbf{v}_n]_\beta)$ er lineært uafhængigt. 
Vis at for enhver anden ordnet basis $\gamma$ for $V$ sættet $([\mathbf{v}_1]_\gamma, [\mathbf{v}_2]_\gamma, \dots, [\mathbf{v}_n]_\gamma)$ også er lineært uafhængigt.

