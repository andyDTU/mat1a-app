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

(section:uge8S)=

# Opgaver -- Store Dag

----

+++

## Opgave 1: Udspænding af vektorer i $\mathbb{R}^3$

Der undersøges udspændingen af følgende tre vektorer fra $\mathbb{R}^3$.

$${\mathbf w}_1=\left[\begin{array}{r}1\\-1\\2\end{array}\right],
{\mathbf w}_2=\left[\begin{array}{r}1\\3\\2\end{array}\right] \ \mathrm{og} \ 
{\mathbf w}_3=\left[\begin{array}{r}7\\9\\14\end{array}\right].
$$

+++

### Spørgsmål a 

Undersøg om $\mathrm{Span}({\mathbf w}_1,{\mathbf w}_2,{\mathbf w}_3)$ kan udspændes af færre end tre vektorer.
Hvis svaret er ja, ønskes en af vektorerne skrevet som en linearkombination af de øvrige to. 

```{hint}
:class: dropdown
I Eksempel 9.1.5 fra lærebogen gennemgås en lignende opgave.
```

```{admonition} Svar
:class: dropdown
Svaret er ja. De tre givne vektorer er nemlig lineært afhængige. Der gælder for eksempel ${\mathbf w}_3=3{\mathbf w}_1+4{\mathbf w}_2.$
Derfor gælder ifølge Sætning 9.1.1 at $\mathrm{Span}({\mathbf w}_1,{\mathbf w}_2)=\mathrm{Span}({\mathbf w}_1,{\mathbf w}_2,{\mathbf w}_3)$.
```

+++

### Spørgsmål b 

Tjek at vektorerne ${\mathbf w}_1$ og ${\mathbf w}_2$ er lineært uafhængige og konkluder at listen $({\mathbf w}_1,{\mathbf w}_2)$ er en ordnet basis for $\mathrm{Span}({\mathbf w}_1,{\mathbf w}_2,{\mathbf w}_3)$.

```{hint}
:class: dropdown
Vi har allerede set at $\mathrm{Span}({\mathbf w}_1,{\mathbf w}_2)=\mathrm{Span}({\mathbf w}_1,{\mathbf w}_2,{\mathbf w}_3)$. 
Ifølge Korollar 9.2.2 følger den sidste påstand derfor af den første.
```

+++

### Spørgsmål c 

Beregn dimensionen af $\mathrm{Span}({\mathbf w}_1,{\mathbf w}_2,{\mathbf w}_3)$.

```{hint}
:class: dropdown
I Definition 9.4.1 fra lærebogen kan du læse hvordan dimension af en udspænding af vektorer er defineret.
```

+++

----

+++


## Opgave 2: En anden udspænding af vektorer i $\mathbb{R}^3$

Givet følgende tre vektorer i $\mathbb{R}^3$:

$${\mathbf v}_1=\left[\begin{array}{r}1\\-1\\2\end{array}\right],
{\mathbf v}_2=\left[\begin{array}{r}1\\3\\2\end{array}\right] \ \mathrm{og} \ 
{\mathbf v}_3=\left[\begin{array}{r}1\\0\\0\end{array}\right].
$$

+++

### Spørgsmål a

Vis at de givne tre vektorer er lineært uafhængige. 

```{hint}
:class: dropdown
Der er flere muligheder. En mulighed er at bruge Sætning 7.1.3 fra lærebogen, en anden er at bruge Korollar 8.2.5.
```

+++

### Spørgsmål b

Bestem en ordnet basis for $\mathrm{Span}({\mathbf v}_1,{\mathbf v}_2,{\mathbf v}_3)$. Hvad er udspændingens dimension?

```{hint}
:class: dropdown
Kan Korollar 9.2.2 fra lærebogen bruges?
```

```{admonition} Svar
:class: dropdown
En ordnet basis er listen $({\mathbf v}_1,{\mathbf v}_2,{\mathbf v}_3)$. 
Dimensionen af $\mathrm{Span}({\mathbf v}_1,{\mathbf v}_2,{\mathbf v}_3)$ er derfor lig med $3$. 
```


+++

----

+++

## Opgave 3: Nulrum og søjlerum af en matrix

Givet matricen $\mathbf A$ som følger

$$
{\mathbf A}=
\left[
\begin{array}{rrrr}
1 & 1 & 1 & 1\\ 
0 & 2 & 4 & -1\\ 
2 & 0& -2 & 3\\
2 & 4 & 6 & 1\\
\end{array}
\right].
$$

+++

### Spørgsmål a

Bestem en orndet basis for matricens nulrum. Hvad er nulrummets dimension?

```{hint}
:class: dropdown
I Eksempel 9.3.1 forklares i et andet konkret tilfælde hvordan man besvarer sådanne spørgsmål.
```

```{admonition} Svar
:class: dropdown
Den reducerede trappeform af matricen $\mathbf A$ viser sig til at være

$$
\left[
\begin{array}{rrrr}
1 & 0& -1 & 3/2\\ 
0 & 1 & 2 & -1/2\\ 
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
\end{array}
\right].
$$

Ud fra den kan ses at en ordnet basis for $\mathbf A$s nulrum er

$$\left( \left[\begin{array}{r}1\\-2\\ 1 \\ 0\end{array}\right], \left[\begin{array}{r}-3/2\\1/2\\0 \\1\end{array}\right] \right).$$

Fordi den fundne ordnede basis er en liste bestående af to vektorerer, konkluderes at nulrummets dimension er to.
```

+++

### Spørgsmål b

Bestem en ordnet basis for matricens søjlerum og tjek at dimensionssætningen holder (Sætning 9.4.2 fra lærebogen).

```{hint}
:class: dropdown
I Eksempel 9.3.2 forklares i et andet konkret tilfælde hvordan man besvarer sådanne spørgsmål.
```

```{admonition} Svar
:class: dropdown
En ordnet basis for $\mathbf A$s søjlerum er

$$\left( \left[\begin{array}{r}1\\0 \\ 2 \\ 2\end{array}\right], \left[\begin{array}{r}1\\2 \\ 0 \\ 4\end{array}\right] \right).$$

Søjlerummets dimension er derfor to. Dimensionssætningen er opfuldt som den burde, fordi $2+2=4$.
```

+++

----

+++

%## Opgave 2: Udspænding af tre vektorer i Lineær afhængighed eller uafhængighed i $\mathbb{C}^2$
%
%Undersøg om følgende vektorer fra $\mathbb{C}^2$ er lineært afhængige eller lineært uafhængige i følgende tilfælde. 
%Ved lineær afhængighed ønskes en af vektorerne skrevet som en linearkombination af de øvrige. 
%
%1. Vektorerne 
%
%$$\left[\begin{array}{r}1\\1\end{array}\right] \ \mathrm{og} \ 
%\left[\begin{array}{r}1+i\\-1+i\end{array}\right] \quad \mathrm{fra $\mathbb{C}^2$}.
%$$
%
%
%```{hint}
%:class: dropdown
%Det skal undersøges om der findes en linearkombination af de givne vektorer som giver nul, selvom ikke alle koefficienter er nul.
%```
%
%```{admonition} Svar
%:class: dropdown
%De to vektorer er lineært afhængige. Man har for eksempel $(1+i,-1+i)=(1+i)\cdot(1,i).$
%```

## Opgave 4: Dimension af nulrum og søjlerum

Om en kompleks matrix $\mathbf A \in \mathbb{C}^{5 \times 10}$ er det givet at dens reducerede trappeform er givet ved

$$
\left[
\begin{array}{rrrrrrrrrr}
0 & 1&-1+i& 0 &\sqrt{2}-i&-\pi& 0 & 1 &\pi^2& e^3\\ 
0 & 0 & 0 & 1 & 8        &3/2 & 0 & 1 &100  & -1/2\\
0 & 0 & 0 & 0 & 0        & 0  & 1 & i & -2  & 4/5\\
0 & 0 & 0 & 0 & 0        & 0  & 0 & 0 & 0   & 0\\
0 & 0 & 0 & 0 & 0        & 0  & 0 & 0 & 0   & 0\\
\end{array}
\right].
$$

Bestem, uden at udføre nogle beregninger, dimension af matricens nulrum $\mathrm{null}(\mathbf A)$ og dimension af matricens søjlerum $\rho(\mathbf A)$.

```{admonition} Svar
:class: dropdown
$\mathrm{null}(\mathbf A)=7$ og $\rho(\mathbf A)=3$.
```

+++

----

+++


## Opgave 5: Udspændinger og homogene lineære ligningssystemer


Gør rede for at løsningsmængden for det homogene lineære ligningssystem over $\mathbb R$

$$
\left\{
\begin{array}{rcl}
x_2 +3x_3 - x_4+2x_5 & = & 0\\ 
2x_1+3x_2+x_3+3x_4 & = & 0\\ 
x_1 + x_2 -x_3 + 2x_4-x_5 & = & 0
\end{array}
\right.
$$

er udspændingen af visse vektorer i $\mathbb{R}^5$ og find en ordnet basis for løsningsmængden. 
Hvad er udspændingens dimension? 

```{hint}
:class: dropdown
Find først den fuldstændige løsning til systemet ligesom i Eksempel 6.4.3 fra lærebogen. 
Kan du se hvad en mulig ordnet basis af løsningsmængden er? 
Sammenlign eventuelt med Korollar 9.2.3.  
```

```{admonition} Svar
:class: dropdown 
Dimensionen er $3$. 
En ordnet basis skal indholde tre lineært uafhængige vektorer i løsningsmængden. 
Der er derfor mange muligheder for korrekt svar. 
Følger man proceduren som i Sætning 6.4.4 til at finde den fuldstændige løsning, så finder man følgende ordnede basis (se eventuelt også Korollar 9.2.3):

$$\left( 
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
\right).$$
```

+++

----

+++

## Opgave 6: Udspænding af vektorer

I $\mathbb{R}^6$ er der givet fire vektorer: 

$${\mathbf u}_1=\left[\begin{array}{c}1\\0\\1\\0\\1\\0\end{array}\right]\, , \quad 
{\mathbf u}_2=\left[\begin{array}{c}0\\1\\1\\1\\1\\-1\end{array}\right]
\,, \quad {\mathbf v}_1=\left[\begin{array}{c}4\\-5\\-1\\-5\\-1\\5\end{array}\right]\, , 
\quad {\mathbf v}_2=\left[\begin{array}{c}-3\\2\\-1\\2\\-1\\-2\end{array}\right]\,.$$

+++

### Spørgsmål a

Vis at ${\mathbf u}_1$ og ${\mathbf u}_2$ udspænder det samme som ${\mathbf v}_1$ og ${\mathbf v}_2$. 
Med andre ord: vis at $\mathrm{Span}({\mathbf u}_1,{\mathbf u}_2)=\mathrm{Span}({\mathbf v}_1,{\mathbf v}_2)$.

```{hint}
:class: dropdown
Vis først at $({\mathbf u}_1,{\mathbf u}_2)$ er en ordnet basis for $\mathrm{Span}({\mathbf u}_1,{\mathbf u}_2,{\mathbf v}_1,{\mathbf v}_2)$ ved at bruge Sætning 9.2.1.
Overvej bagefter hvorfor det medfører at $\mathrm{Span}({\mathbf u}_1,{\mathbf u}_2) = \mathrm{Span}({\mathbf u}_1,{\mathbf u}_2,{\mathbf v}_1,{\mathbf v}_2).$
```

```{hint}
:class: dropdown
For at vise at $\mathrm{Span}({\mathbf u}_1,{\mathbf u}_2) = \mathrm{Span}({\mathbf u}_1,{\mathbf u}_2,{\mathbf v}_1,{\mathbf v}_2)$, beregn den reducerede trappeform af den $6 \times 4$ matrix med søjler 
${\mathbf u}_1,{\mathbf u}_2,{\mathbf v}_1,{\mathbf v}_2$.
```

### Spørgsmål b

Angiv en vektor i $\mathbb{R}^6$ som ikke er indeholdt i $\mathrm{Span}({\mathbf u}_1,{\mathbf u}_2)$.

```{hint}
:class: dropdown
Hvis ${\mathbf u}_3$ er en vektor i $\mathbb{R}^6$ således at vektorerne ${\mathbf u}_1,{\mathbf u}_2$ og ${\mathbf u}_3$ er lineært uafhængige, kan ${\mathbf u}_3$ være i $\mathrm{Span}({\mathbf u}_1,{\mathbf u}_2)$?
```

+++

----

+++

## Opgave 7: Ordnede baser

Ligesom i Opgave 2 betragtes udspændingen af følgende tre vektorer fra $\mathbb{R}^3$:

$${\mathbf v}_1=\left[\begin{array}{r}1\\-1\\2\end{array}\right],
{\mathbf v}_2=\left[\begin{array}{r}1\\3\\2\end{array}\right] \ \mathrm{og} \ 
{\mathbf v}_3=\left[\begin{array}{r}1\\0\\0\end{array}\right].
$$

+++

### Spørgsmål a

Vi har set i Opgave 2 at $({\mathbf v}_1,{\mathbf v}_2,{\mathbf v}_3)$ er en ordnet basis for $\mathrm{Span}({\mathbf v}_1,{\mathbf v}_2,{\mathbf v}_3)$ og at udspændingen derfor har dimension $3$.
Vis at hver vektor ${\mathbf v}$ i $\mathbb{R}^3$ kan skrives som linearkombination af ${\mathbf v}_1,{\mathbf v}_2$ og ${\mathbf v}_3$ og konkluder at $\mathrm{Span}({\mathbf v}_1,{\mathbf v}_2,{\mathbf v}_3)=\mathbb{R}^3$. 

Bemærkning: Intentionen bag opgaven er at illustrere at hver tre-dimensionalt udspænding indeholdt i $\mathbb{R}^3$ er lig med $\mathbb{R}^3$.


```{hint}
:class: dropdown
Undersøg om der findes skalarer $c_1,c_2,c_3 \in \mathbb{R}$ således at $c_1{\mathbf v}_1+c_2{\mathbf v}_2+c_3{\mathbf v}_3={\mathbf v}$.
Med andre ord: undersøg om ligningen 

$${\mathbf A} \left[ \begin{array}{r}c_1\\c_2\\c_3\end{array} \right]={\mathbf v}$$

har en løsning, hvor ${\mathbf A}$ er $3 \times 3$ matricen med søjler ${\mathbf v}_1, {\mathbf v}_2$ og ${\mathbf v}_3$.
```

```{admonition} Svar
:class: dropdown
Det vides fra Opgave 2a at vektorerne ${\mathbf v}_1,{\mathbf v}_2$ og ${\mathbf v}_3$ er lineært uafhængige. 
Sætning 7.1.3 fra lærebogen medfører at matricen ${\mathbf A}$ har rang $3$. 
Derfor er ${\mathbf A}$ invertibel ifølge Ligning (7.10) fra lærebogen.
Dette viser at ligningen 

$${\mathbf A} \left[ \begin{array}{r}c_1\\c_2\\c_3\end{array} \right]={\mathbf v}$$

har en løsning, nemlig 

$$\left[ \begin{array}{r}c_1\\c_2\\c_3\end{array} \right]={\mathbf A}^{-1}{\mathbf v}.$$
```

+++

### Spørgsmål b

Vis at $({\mathbf e}_1,{\mathbf e}_2,{\mathbf e}_3)$ også er en ordnet basis for $\mathrm{Span}({\mathbf v}_1,{\mathbf v}_2,{\mathbf v}_3)$. 
Her

$${\mathbf e}_1=\left[ \begin{array}{r}1\\0\\0\end{array} \right], {\mathbf e}_2=\left[ \begin{array}{r}0\\1\\0\end{array} \right] \ \text{og} \ {\mathbf e}_3=\left[ \begin{array}{r}0\\0\\1\end{array} \right]\,.$$

Bemærkning: Spørgsmålet illustrerer at den ordnede basis som Sætning 9.2.1 beskriver, ikke altid er den pænest mulige ordnede basis.

```{admonition} Svar
:class: dropdown
Dette følger fra resultatet i Spørgsmål a og fordi $({\mathbf e}_1,{\mathbf e}_2,{\mathbf e}_3)$ er den ordnede standardbasis for $\mathbb{R}^3$. 
Se eventuelt Eksempel 9.2.1 fra lærebogen hvis du er i tvivl om hvad den ordnede standardbasis af $\mathbb{F}^m$ er. 
```

+++

----

+++

## Opgave 8: Dimension og udspænding

Ligesom i Opgave 1 betragtes udspændingen af følgende tre vektorer fra $\mathbb{R}^3$

$${\mathbf w}_1=\left[\begin{array}{r}1\\-1\\2\end{array}\right],
{\mathbf w}_2=\left[\begin{array}{r}1\\3\\2\end{array}\right] \ \mathrm{og} \ 
{\mathbf w}_3=\left[\begin{array}{r}7\\9\\14\end{array}\right].
$$ 

Kan $\mathrm{Span}({\mathbf w}_1,{\mathbf w}_2,{\mathbf w}_3)$ udspændes af kun én vektor? 

Bemærkning: vi har set i Opgave 1 at udspændingen har dimension $2$. Intuitivt forventes derfor at svaret er nej. 

```{hint}
:class: dropdown
Hvis $\mathrm{Span}({\mathbf w}_1,{\mathbf w}_2,{\mathbf w}_3)$ kan udspændes af kun én vektor, lad os sige ${\mathbf u}$, så er ${\mathbf w}_1,{\mathbf w}_2,{\mathbf w}_3$ alle i $\mathrm{Span({\mathbf u})}$. 
Kan det lade sig gøre?
```

```{hint}
:class: dropdown
Hvis både ${\mathbf w}_1$ og ${\mathbf w}_2$ er et skalærmultiplum af en hvis vektor ${\mathbf u}$, kan vektorerne ${\mathbf w}_1$ og ${\mathbf w}_2$ være lineært uafhængige?
```

```{admonition} Svar
:class: dropdown
$\mathrm{Span}({\mathbf w}_1,{\mathbf w}_2,{\mathbf w}_3)$ kan ikke udspændes af kun én vektor.
```

+++

----

+++

## Opgave 9: Tematisk Python opgave 

Opgaven frigives kl 15:30 på DTU Learn.

