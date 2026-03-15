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

(section:uge6S)=

# Opgaver -- Store Dag

----

+++

## Opgave 1: Egenskaber af lineære ligningssystemer

Givet er følgende lineære ligningssystem over $\mathbb R$ i de tre ubekendte $x$, $y$ og $z$.

$$
\left\{
  \begin{array}{rrrrr} 
3x  & - 7y & + z & = & 1\\ 
11x & -y & +4z & = & 4
\end{array}
\right.
$$

+++

### Spørgsmål a 

Er systemet homogent eller inhomogent?

```{hint}
:class: dropdown
Hvis du er i tvivl om hvad ordene "homogen" og "inhomogen" betyder, så kan du finde en forklaring i lærebogen lige inden Sætning 6.1.1.
```

```{admonition} Svar
:class: dropdown
Det givne lineære ligningssystem er inhomogent, fordi ikke alle konstanterne på højresiden af ligningerne er lig med nul. 
```

+++

### Spørgsmål b 

Er tuplen $(-1,-1,-3) \in \mathbb{R}^3$ en løsning til systemet? Hvad med tuplen $(0,0,1)$?

```{admonition} Svar
:class: dropdown
Tuplen $(-1,-1,-3)$ er ikke en løsning til systemet (den første ligning er opfyldt, men den anden ligning er ikke).

Tuplen $(0,0,1)$ er en løsning til systemet. 
```

+++

### Spørgsmål c

Vi betragter fortsat det lineære ligningssystem givet i starten af opgaven. Hvad er det tilsvarende homogene lineære ligningssystem?

```{hint}
:class: dropdown
I Sætning 6.1.2 fra lærebogen beskrives det tilsvarende homogene system (på engelsk: ``corresponding homogeneous system'').
```

```{admonition} Svar
:class: dropdown

$$
\left\{
  \begin{array}{rrrrr} 
3x  & - 7y & + z & = & 0\\ 
11x & -y & +4z & = & 0
\end{array}
\right.
$$
```

+++

### Spørgsmål d

Det opgives at tuplen $(27,1,-74)$ er en løsning til det homogene system fra spørgsmål c. 
Brug nu resultatet fra spørgsmål b, til at finde en anden løsning til det givne inhomogene lineære ligningssystem.

```{hint}
:class: dropdown
Læs eventuelt først Sætning 6.1.2 fra lærebogen.
```

```{admonition} Svar
:class: dropdown
Tuplen $(27,1,-73)$ er en løsning til det inhomogene lineære ligningssystem.
```

+++

----

+++

## Opgave 2: Totalmatrix og rækkeoperationer

Der defineres følgende matrix

$$
{\mathbf A}=\left[
\begin{array}{ccc} 
1 & 3 & 4\\
0 & 4 & -4\\
-2 & 0 & -9\\
\end{array}
\right]
$$

og følgende vektor

$$
{\mathbf b}=
\left[
\begin{array}{cccc} 
1\\
0\\
-1\\
\end{array}
\right].
$$

+++

### Spørgsmål a

Opskriv det lineære ligninssystem over $\mathbb R$ i de ubekendte $x_1$, $x_2$ og $x_3$ som har totalmatricen $[{\mathbf A}|{\mathbf b}]$.

```{admonition} Svar
:class: dropdown
$$
\left\{
  \begin{array}{rrrrr} 
x_1  & +3x_2 & + 4x_3 & = & 1\\ 
 & 4x_2 & -4x_3 & = & 0\\
-2x_1  &  & - 9x_3 & = & -1 
\end{array}
\right.
$$
```

+++

### Spørgsmål b

Beregn matricen som man får når man udfører rækkeoperationen $R_3 \leftarrow R_3+2R_1$ på matricen $[\mathbf{A}|\mathbf{b}]$.

```{hint}
:class: dropdown
Hvis du er i tvivl om hvad rækkeoperationen $R_3 \leftarrow R_3+2R_1$ præcist betyder, så kan du finde en beskrivelse lige inden Eksempel 6.2.4 fra lærebogen. 
I Eksempel 6.2.4 udføres en lignende rækkeoperation i et konkret tilfælde.
```

```{admonition} Svar
:class: dropdown
$$
\left[
\begin{array}{cccc} 
1 & 3 & 4 & 1\\
0 & 4 & -4 & 0\\
-2 & 0 & -9 & -1\\
\end{array}
\right]
\begin{array}{c}
\longrightarrow \\
R_3 \leftarrow R_3+2R_1 \\
\end{array}
\left[
\begin{array}{cccc} 
1 & 3 & 4 & 1\\
0 & 4 & -4 & 0\\
0 & 6 & -1 & 1\\
\end{array}
\right]
$$
```

+++

### Spørgsmål c

Tag nu matricen man fandt i sidste spørgsmål og udfør rækkeoperationen $R_2 \leftarrow (1/4)\cdot R_2$ efterfulgt af rækkeroperationerne $R_1 \leftarrow R_1-3R_2$ og $R_3 \leftarrow R_3-6R_2$. 
Hvad er svaret?

```{admonition} Svar
:class: dropdown
$$
\left[
\begin{array}{cccc} 
1 & 3 & 4 & 1\\
0 & 4 & -4 & 0\\
0 & 6 & -1 & 1\\
\end{array}
\right]
\begin{array}{c}
\longrightarrow \\
R_2 \leftarrow (1/4)\cdot R_2\\
\end{array}
\left[
\begin{array}{cccc} 
1 & 3 & 4 & 1\\
0 & 1 & -1 & 0\\
0 & 6 & -1 & 1\\
\end{array}
\right]
$$

$$
\left[
\begin{array}{cccc} 
1 & 3 & 4 & 1\\
0 & 1 & -1 & 0\\
0 & 6 & -1 & 1\\
\end{array}
\right]
\begin{array}{c}
\longrightarrow \\
R_1 \leftarrow R_1-3\cdot R_2\\
\end{array}
\left[
\begin{array}{cccc} 
1 & 0 & 7  & 1\\
0 & 1 & -1 & 0\\
0 & 6 & -1 & 1\\
\end{array}
\right]
$$

$$
\left[
\begin{array}{cccc} 
1 & 0 & 7  & 1\\
0 & 1 & -1 & 0\\
0 & 6 & -1 & 1\\
\end{array}
\right]
\begin{array}{c}
\longrightarrow \\
R_3 \leftarrow R_3-6\cdot R_2\\
\end{array}
\left[
\begin{array}{cccc} 
1 & 0 & 7  & 1\\
0 & 1 & -1 & 0\\
0 & 0 & 5  & 1\\
\end{array}
\right]
$$
```

+++

### Spørgsmål d

Beregn den reducerede trappeform (på engelsk: "reduced row echelon form") af matricen $[\mathbf{A}|\mathbf{b}]$.

```{hint}
:class: dropdown
Man behøver ikke at starte helt forfra, men kan fortsætte med matricen som var svaret til spørgsmål c.
```

```{admonition} Svar
:class: dropdown
Efter rækkeoperationerne: $R_3 \leftarrow (1/5)\cdot R_3$, efterfulgt af $R_2 \leftarrow R_2+R_3$ og $R_1 \leftarrow R_1-7R_3$ fås matricen

$$
\left[
\begin{array}{cccc} 
1 & 0 & 0  & -2/5\\
0 & 1 & 0  & 1/5\\
0 & 0 & 1  & 1/5\\
\end{array}
\right]
$$

Denne matrix er den ønskede reducerede trappematrix.
```

+++

### Spørgsmål e

Beskriv og løs det lineære ligningssystem over $\mathbb R$ som har den fundne reducerede trappematrix fra spørgsmål d som totalmatrix. 
Tjek at den fundne løsning er løsning til det oprindelige lineære ligningssystem som havde totalmatricen $[{\mathbf A}|{\mathbf b}].$

```{admonition} Svar
:class: dropdown
Ligningssystemet hørende til den fundne reducerede trappematrix er

$$
\left\{
  \begin{array}{rrrrr} 
x_1  &   &   & = & -2/5\\ 
 &  x_2 &  & = & 1/5\\
  &  &  x_3 & = & 1/5 
\end{array}
\right.
$$

Løsningen er tuplen $(-2/5,1/5,1/5).$ 
Ved indsættelse ses at denne tupel er løsning til det oprindelige system. 
Dette er som det burde være, fordi Sætning 6.2.1 fra lærebogen forudsiger at løsningsmængden til et lineært ligningssystem ikke ændrer sig når man udfører elementære rækkeoperationer.
```

+++

----

+++

## Opgave 3: Trappematricer.

Der defineres følgende matricer

$$
{\mathbf A}=\left[
\begin{array}{ccc} 
1 & 3 & 4\\
0 & 1 & 5\\
0 & 0 & 1\\
\end{array}
\right], \quad
{\mathbf B}=\left[
\begin{array}{ccc} 
2 & 0 & 4\\
0 & 4 & 0\\
\end{array}
\right], \quad
{\mathbf C}=\left[
\begin{array}{ccc} 
1 & 0 & 0\\
0 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1\\
\end{array}
\right], \quad
{\mathbf D}=\left[
\begin{array}{ccc} 
1 & 4 & 0 & 9\\
0 & 0 & 1 & 2\\
\end{array}
\right].
$$

+++

### Spørgsmål a

Hvilke af disse matricer er på trappeform? Hvilke er på reduceret trappeform?

```{hint}
:class: dropdown
Definitionen af en matrix på reduceret trappeform er givet i Definition 6.3.2 fra lærebogen. 
Straks efter denne definition står der, hvad en matrix på trappeform opfylder.
```

```{admonition} Svar
:class: dropdown
Matricerne ${\mathbf A}$, ${\mathbf B}$ og ${\mathbf D}$ er på trappeform, de øvrige ikke. Kun matrix ${\mathbf D}$ er på reduceret trappeform.
```

+++

### Spørgsmål b

Beregn den reducerede trappeform til hver af de givne matricer ${\mathbf A}$, ${\mathbf B}$, ${\mathbf C}$ og ${\mathbf D}$.

```{admonition} Svar
:class: dropdown
Følgende følge af rækkeoperationer fører til matricernes reducerede trappeformer:

$$
{\mathbf A}=\left[
\begin{array}{ccc} 
1 & 3 & 4\\
0 & 1 & 5\\
0 & 0 & 1\\
\end{array}
\right]
\begin{array}{c}
\longrightarrow \\
R_1 \leftarrow R_1-3\cdot R_2\\
\end{array}
\left[
\begin{array}{ccc} 
1 & 0 & -11\\
0 & 1 & 5\\
0 & 0 & 1\\
\end{array}
\right]
\begin{array}{c}
\longrightarrow \\
R_1 \leftarrow R_1+11\cdot R_3\\
\end{array}
\left[
\begin{array}{ccc} 
1 & 0 & 0\\
0 & 1 & 5\\
0 & 0 & 1\\
\end{array}
\right]
$$

$$
\begin{array}{c}
\longrightarrow \\
R_2 \leftarrow R_2-5\cdot R_3\\
\end{array}
\left[
\begin{array}{ccc} 
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1\\
\end{array}
\right].
$$

$$
{\mathbf B}=\left[
\begin{array}{ccc} 
2 & 0 & 4\\
0 & 4 & 0\\
\end{array}
\right]
\begin{array}{c}
\longrightarrow \\
R_1 \leftarrow (1/2)\cdot R_1\\
\end{array}
\left[
\begin{array}{ccc} 
1 & 0 & 2\\
0 & 4 & 0\\
\end{array}
\right]
\begin{array}{c}
\longrightarrow \\
R_2 \leftarrow (1/4)\cdot R_2\\
\end{array}
\left[
\begin{array}{ccc} 
1 & 0 & 2\\
0 & 1 & 0\\
\end{array}
\right].
$$

$$
{\mathbf C}=\left[
\begin{array}{ccc} 
1 & 0 & 0\\
0 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1\\
\end{array}
\right]
\begin{array}{c}
\longrightarrow \\
R_2 \leftrightarrow R_3\\
\end{array}
\left[
\begin{array}{ccc} 
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 0\\
0 & 0 & 1\\
\end{array}
\right]
\begin{array}{c}
\longrightarrow \\
R_3 \leftrightarrow R_4\\
\end{array}
\left[
\begin{array}{ccc} 
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1\\
0 & 0 & 0\\
\end{array}
\right].
$$

Matricen $\mathbf D$ er allerede på reduceret trappeform.
```

+++

----

+++


## Opgave 4: Reduceret trappeform af en $4 \times 5$ matrix.

Der defineres en matrix 

$${\mathbf A}=
\left[
\begin{array}{ccc} 
1  & 0 & 0 & 1 & 0\\
-2 & 1 & 0 & 3 & 1\\
5  & 0 & 1 & -4 & 1\\
4  & 1 & 1 & 0 & 2\\
\end{array}
\right].
$$

Hvor mange rækker, der ikke er nulrækker, har $\mathbf A$'s reducerede trappeform? 
%Beregen matricens rang. Med andre ord, beregn $\rho({\mathbf A})$. 

```{admonition} Svar
:class: dropdown
Den reducerede trappeform af den givne matrix $\mathbf A$ er

$$
\left[
\begin{array}{ccc} 
1  & 0 & 0 & 1 & 0\\
0  & 1 & 0 & 5 & 1\\
0  & 0 & 1 & -9 & 1\\
0  & 0 & 0 & 0 & 0\\
\end{array}
\right].
$$

Den har tre rækker, der ikke er nulrækker. 
Dette antal kaldes i øvrigt rangen af matricen $\mathbf A$ (se Definition 6.3.3).
```

+++

----

+++


## Opgave 5: Relation mellem trappematrix og reduceret trappematrix

Der defineres følgende trappematrix 

$${\mathbf B}=
\left[
\begin{array}{ccc} 
1  & 6 & 10 & 1 & 0\\
0  & 0 & 1 & 3 & 1\\
0  & 0 & 0 & 0 & 1\\
0  & 0 & 0 & 0 & 0\\
\end{array}
\right].
$$

+++

### Spørgsmål a

Gør rede for uden at udføre nogle beregninger at $\mathbf B$ vil have en reduceret trappematrix på formen

$$
\left[
\begin{array}{ccc} 
1  & a & 0 & b & 0\\
0  & 0 & 1 & c & 0\\
0  & 0 & 0 & 0 & 1\\
0  & 0 & 0 & 0 & 0\\
\end{array}
\right]
$$

for visse tal $a,b,c \in \mathbb{R}$.


+++

### Spørgsmål b

%Konkluder at $\rho(B)=3$. 
Overvej hvorfor det mere generelt gælder, at antallet af rækker, der ikke er nulrækker, i en trappematrix er det samme som antallet i dens reducerede trappematrix 
%Overvej hvorfor mere generelt det gælder at rangen af en trappematrix er lig med dens antal af ikke-nul rækker. 

+++

----

+++

## Opgave 6: Eksempler på lineære ligningssystemer

### Spørgsmål a

Giv et eksempel på et inhomogent lineært ligningssystem over $\mathbb R$ i tre ubekendte $x_1$, $x_2$ og $x_3$ uden løsninger.

```{hint}
:class: dropdown
Korollar 6.4.3 beskriver hvornår et inhomogent lineært ligningssystem ingen løsninger har.
```

### Spørgsmål b

Kan et homogent lineart ligningssystem ingen løsninger have?

### Spørgsmål c

Giv et et eksempel på et homogent lineart ligningssystem over $\mathbb R$ med mindst to ligninger og mindst to løsninger.

+++

----

+++

## Opgave 7: Et system med fire ligninger og fire ubekendte

Vi betragter igen matricen 

$$
\left[
\begin{array}{ccc} 
1  & 0 & 0 & 1 & 0\\
-2 & 1 & 0 & 3 & 1\\
5  & 0 & 1 & -4 & 1\\
4  & 1 & 1 & 0 & 2\\
\end{array}
\right]
$$

fra Opgave 4. 
Det oplyses at matricen er totalmatricen til et lineært ligningssystem over $\mathbb R$ i de ubekendte $x_1,x_2,x_3$ og $x_4$. 

+++

### Spørgsmål a 

Find en løsning til systemet som opfylder $x_4=0$. Find også en løsning til systemet som opfylder $x_4=1$.  

+++

### Spørgsmål b 

Givet er et reelt tal $t$. Find en løsning til systemet som opfylder $x_4=t$.
%
%+++
%
%----
%
%+++
%
%## Opgave 8: Reduceret trappeform
%
%For en given $m \times (n+1)$ matrix ${\mathbf B}$, betegner vi i denne opgave med ${\mathbf B}^{(1)}$ (hhv. ${\mathbf B}^{(n+1)}$) den $m \times n$ matrix man får ved at slette den første (hhv. sidste) søjle i $\mathbf B$.
%
%+++
%
%### Spørgsmål a 
%
%Find et eksempel på en $2 \times 3$ matrix $\mathbf B$ med koefficienter i $\mathbb C$, således at $\mathbf B$ er på reduceret trappeform, men ikke den $2 \times 2$ matrix ${\mathbf B}^{(1)}$. Er matricen ${\mathbf B}^{(3)}$ på reduceret trappeform?
%
%+++
%
%### Spørgsmål b
%
%For en given matrix $m \times (n+1)$ matrix ${\mathbf B}$, oplyses at $\mathbf B$ er på reduceret trappeform. Gør rede for at den $m \times n$ matrix ${\mathbf B}^{(n+1)}$ er også på reduceret trappeform.
%
%```{hint}
%:class: dropdown
%En matrix på reduceret trappeform opfylder de fire krav givet i Definition 6.3.1 fra lærebogen. Prøv at indse at hvis ${\mathbf B}$ opfylder disse krav, så opfylder ${\mathbf B}^{(n+1)}$ (hvor kun den sidste søjle af ${\mathbf B}$ er blevet fjernet) dem også.
%```

+++

----

+++


## Opgave 8: Kvadratiske matricer og tilhørende lineære ligningssystemer

En matrix $\mathbf A$ kaldes for en kvadratisk matrix, hvis den indeholder lige mange rækker og søjler. 
Med andre ord, matricen $\mathbf A$ er kvadratisk præcist hvis ${\mathbf A} \in \mathbb{F}^{n \times n}$ for et naturligt tal $n$. 

+++

### Spørgsmål a
%
%Givet en kvadratisk matrix ${\mathbf A} \in \mathbb{R}^{4 \times 4}$, vis at $\rho({\mathbf A})%=4$ hvis og kun hvis den reducerede trappeform af $\mathbf A$ er følgende $4 \times 4$ matrix:
%
%$$
%\left[
%\begin{array}{ccc} 
%1 & 0 & 0 & 0\\
%0 & 1 & 0 & 0\\
%0 & 0 & 1 & 0\\
%0 & 0 & 0 & 1\\
%\end{array}
%\right].
%$$
%
%+++
%
%### Spørgsmål b

Givet er en matrix ${\mathbf A} \in \mathbb{R}^{4 \times 4}$ og en vektor ${\mathbf b} \in \mathbb{R}^{4}$. 
Det oplyses at ${\mathbf A}$'s reducerede trappeform er som følger:

$$
\left[
\begin{array}{ccc} 
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{array}
\right].
$$

Vis at det lineære ligningssystem over $\mathbb R$ med totalmatricen ${[{\mathbf A}|{\mathbf b}]} \in \mathbb{R}^{4 \times 5}$ har netop én løsning.
%$\rho({\mathbf A})=4$. Vis at det lineare ligningssystem over $\mathbb R$ med totalmatricen ${[{\mathbf A}|{\mathbf b}]} \in \mathbb{R}^{4 \times 5}$ har netop en løsning.

```{hint}
:class: dropdown
Det er givet at ${\mathbf A}$'s reducerede trappeform er 

$$
\left[
\begin{array}{ccc} 
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{array}
\right].
$$

Prøv nu at bruge det til  at indse at den reducerede trappeform til totalmatricen ${[{\mathbf A}|{\mathbf b}]}$ har udseende

$$
\left[
\begin{array}{ccc} 
1 & 0 & 0 & 0 & c_1\\
0 & 1 & 0 & 0 & c_2\\
0 & 0 & 1 & 0 & c_3\\
0 & 0 & 0 & 1 & c_4\\
\end{array}
\right]
$$

for visse $c_1,c_2,c_3,c_4 \in \mathbb{R}.$
```

+++

----

+++

## Opgave 9: Tematisk Python opgave. 

Opgaven frigives kl 15:30 på DTU Learn.
