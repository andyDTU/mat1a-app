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

(section:uge6L)=

# Opgaver -- Lille Dag

+++

## Opgave 1: Pivot-elementer i en reduceret trappematrix

Givet er følgende matrix:

$${\mathbf B}=
\left[
\begin{array}{cccccccc} 
0   & 1 & \sqrt{2} & 0 & 5 & 0 & 0 & 9   \\
0   & 0 & 0        & 1 & e & 0 & 0 & \pi \\
0   & 0 & 0        & 0 & 0 & 0 & 1 & 42  \\
0   & 0 & 0        & 0 & 0 & 0 & 0 & 0   \\
\end{array}
\right].
$$

+++

### Spørgsmål a

Er matricen $\mathbf B$ på reduceret trappeform?

```{admonition} Svar
:class: dropdown
Ja: alle fire krav fra Definition 6.3.2 er opfyldte.
```

+++

### Spørgsmål b

Angiv pivot-elementerne i den givne matrix ${\mathbf B}$. 
Hvor mange pivot-elementer har matricen ${\mathbf B}$ og i hvilke søjler befinder de sig?

```{admonition} Svar
:class: dropdown
Der er tre pivot-elementer, som befinder sig hhv. i $\mathbf B$'s anden, fjerde og syvende søjle. 
De tre pivot-elementer er angivet med fedt skrift i følgende:

$${\mathbf B}=
\left[
\begin{array}{cccccccc} 
0   & {\mathbf 1} & \sqrt{2} & 0 & 5 & 0 & 0 & 9   \\
0   & 0 & 0        & {\mathbf 1} & e & 0 & 0 & \pi \\
0   & 0 & 0        & 0 & 0 & 0 & {\mathbf 1} & 42  \\
0   & 0 & 0        & 0 & 0 & 0 & 0 & 0   \\
\end{array}
\right].
$$
```

+++

----

+++


## Opgave 2: Rang af en matrix

Følgende $4 \times 4$ matrix med komplekse elementer er givet:

$${\mathbf C}=
\left[
\begin{array}{ccc} 
1   & i & 1   & 0\\
3   & 3i & 0   & 0\\
1+2i & -2+i & -1-i   & 0\\
i   & -1 & -1 & 0\\
\end{array}
\right].
$$

Hvad er matricens rang? 

```{hint}
:class: dropdown
Definition 6.3.3 forklarer hvordan rang af en matrix er defineret og hvordan man kan beregne rangen ud fra matricens reducerede trappeform. 
Beregn derfor først matricens reducerede trappeform.
```

```{hint}
:class: dropdown
Matricens reducerede trappeform er 

$$
\left[
\begin{array}{ccc} 
1   & i & 0  & 0\\
0   & 0 & 1  & 0\\
0   & 0 & 0  & 0\\
0   & 0 & 0  & 0\\
\end{array}
\right].
$$

Afgør nu hvor mange pivot-elementer $\mathbf C$'s reducerede trappeform har og brug Definition 6.3.3.
```

```{admonition} Svar
:class: dropdown
$\rho({\mathbf C})=2$
```

+++

----

+++

## Opgave 3: Parameterfremstilling med en fri parameter

Et lineær ligningssystem over $\mathbb R$ i de ubekendte $x_1,x_2,x_3$ og $x_4$ har følgende totalmatrix:

$$[{\mathbf A} |{\mathbf b}]=
\left[
\begin{array}{ccccc} 
1  & 0 & 0 & 1 & 0\\
-2 & 1 & 0 & 3 & 1\\
5  & 0 & 1 & -4 & 1\\
4  & 1 & 1 & 0 & 2\\
\end{array}
\right].
$$

Denne matrix og det tilsvarende lineære ligningssystem optrådte også i Opgaver 4 og 7 på Store Dag.

+++

### Spørgsmål a 

Hvad er det lineære ligningssystem svarende til den givne totalmatrix?

```{admonition} Svar
:class: dropdown
$$
\left\{
\begin{array}{ccccc} 
x_1   &     &     & +x_4   & =0\\
-2x_1 & +x_2 &     & +3x_4  & =1\\
5x_1  &     & +x_3 & -4x_4 & =1\\
4x_1  & +x_2 & +x_3 &       & =2\\
\end{array}
\right. 
$$

eller skrevet mere kompakt

$$
\left\{
\begin{array}{ccc} 
x_1 + x_4  & = & 0\\
-2x_1+x_2 +3x_4 & = & 1\\
5x_1 +x_3 -4x_4 & = & 1\\
4x_1 +x_2 +x_3 & = & 2\\
\end{array}
\right.
$$
```

+++

### Spørgsmål b

Tjek at vektoren 


$$
\left[
\begin{array}{c} 
0\\
1\\
1\\
0\\
\end{array}
\right]
$$

er en partikulær løsning til det lineære ligningssystem med totalmatrix $[{\mathbf A} |{\mathbf b}]$.

+++

### Spørgsmål c

I Opgave 4 fra Store Dag var facit at matricen $[{\mathbf A} |{\mathbf b}]$ har rang $3$ og at dens reducerede trappeform er

$$
\left[
\begin{array}{ccccc} 
1  & 0 & 0 & 1 & 0\\
0  & 1 & 0 & 5 & 1\\
0  & 0 & 1 & -9 & 1\\
0  & 0 & 0 & 0 & 0\\
\end{array}
\right].
$$

Brug den reducerede trappeform til at beskrive den fuldstændige løsning til det homogene lineære ligningssystem med koefficientmatrix $\mathbf A$.

```{hint}
:class: dropdown
Overvej hvorfor den reducerede trappeform af koefficientmatricen $\mathbf A$ kan fås ved at slette den sidste søjle i den reducerede trappeform af matricen $[{\mathbf A}|{\mathbf b}]$. 
Den er derfor

$$
\left[
\begin{array}{cccc} 
1  & 0 & 0 & 1 \\
0  & 1 & 0 & 5 \\
0  & 0 & 1 & -9\\
0  & 0 & 0 & 0 \\
\end{array}
\right].
$$

Hvad er det tilhørende homogene lineære ligningssystem? 
Hvilke søjler indeholder et pivot-element? Fortsæt nu på lignende måde som i Eksempel 6.4.3 fra lærebogen.
```

```{admonition} Svar
:class: dropdown
$$
\left[
\begin{array}{c} 
x_1\\
x_2\\
x_3\\
x_4\\
\end{array}
\right]
=
t\cdot
\left[
\begin{array}{c} 
-1\\
-5\\
9\\
1\\
\end{array}
\right] \quad (t \in \mathbb R).
$$

Det er også helt fint at bruge et andet symbol for den frie parameter $t$, for eksempel $t_1$ eller $s$.
```

+++

### Spørgsmål d

Hvad er den fuldstændige løsning til det lineære ligningssystem over $\mathbb R$ svarende til den givne totalmatrix $[{\mathbf A}|{\mathbf b}]?$ 
Sammenlign eventuelt til kontrol dit svar med svaret til Opgave 7b fra Store Dag.

```{hint}
:class: dropdown
Sætning 6.1.2 fra lærebogen medfører at du kan finde svaret ved at kombinere spørgsmål b og svaret til spørgsmål c. 
Læs eventuelt Eksempel 6.4.4 hvis du vil se et eksempel.
```


```{admonition} Svar
:class: dropdown
$$
\left[
\begin{array}{c} 
x_1\\
x_2\\
x_3\\
x_4\\
\end{array}
\right]
=
\left[
\begin{array}{c} 
0\\
1\\
1\\
0\\
\end{array}
\right]
+
t\cdot
\left[
\begin{array}{c} 
-1\\
-5\\
9\\
1\\
\end{array}
\right]  \quad (t \in \mathbb R).
$$

Svaret skulle være identisk med den til Opgave 7b fra Store Dag udover at man måske havde skrevet det på formen $(-t,1-5t,1+9t,t)$ eller lignende.
```

+++

----

+++

## Opgave 4: Parameterfremstilling med flere frie parametre

Vi betragter igen matricen ${\mathbf B}$ fra Opgave 1:

$${\mathbf B}=
\left[
\begin{array}{cccccccc} 
0   & 1 & \sqrt{2} & 0 & 5 & 0 & 0 & 9   \\
0   & 0 & 0        & 1 & e & 0 & 0 & \pi \\
0   & 0 & 0        & 0 & 0 & 0 & 1 & 42  \\
0   & 0 & 0        & 0 & 0 & 0 & 0 & 0   \\
\end{array}
\right].
$$

+++

### Spørgsmål a

Matricen ${\mathbf B}$ kan opfattes som en totalmatricen af et lineært ligningssystem over $\mathbb C$. 
Er systemet homogent eller inhomogent? Hvor mange ubekendte/variable indgår i systemet? 

```{admonition} Svar
:class: dropdown
Systemet er inhomogent. Det indgår syv ubekendte. 
```

+++

### Spørgsmål b

Hvad er det lineære ligningssystem svarende til den givne totalmatrix $\mathbf B$? 

```{admonition} Svar
:class: dropdown
Hvis de syv ubekendte navngives som man plejer at gøre med $x_1,x_2,x_3,x_4,x_5,x_6$ og $x_7$, så fås:

$$
\left\{
\begin{array}{cccccccc} 
   & x_2 & +\sqrt{2}\cdot x_3 &     & +5\cdot x_5 &  &     & = 9   \\
   &     &              & x_4 & +e\cdot x_5 &  &     & = \pi \\
   &     &              &     &       &  & x_7 & = 42  \\
   &     &              &     &       &  &  0  & = 0   \\
\end{array}
\right.
$$
```

+++

### Spørgsmål c

Find en partikulær løsning til systemet fra spørgsmål b.


```{hint}
:class: dropdown
Det vides fra Opgave 1 at matricen $\mathbf B$ har tre pivot-elementer, som befinder sig hhv. i $\mathbf B$'s anden, fjerde og syvende søjle. Man kan derfor finde en partikulær løsning ved at følge den samme strategi som i Theorem 6.4.2. Mere præcist: hvis man sætter $x_1,x_3,x_5$ og $x_6$ alle lig med nul, så kan man bagefter beregne værdierne af $x_2,x_4$ og $x_7$ fra ligningssystemet. 
```

```{admonition} Svar
:class: dropdown
Hvis man følger ovenstående vink, så finder man følgende partikulære løsning:

$$
\left[
\begin{array}{c} 
x_1\\
x_2\\
x_3\\
x_4\\
x_5\\
x_6\\
x_7\\
\end{array}
\right]
=
\left[
\begin{array}{c} 
0\\
9\\
0\\
\pi\\
0\\
0\\
42\\
\end{array}
\right]
$$
```

+++

### Spørgsmål d

Find den fuldstændige løsning til systemet fra spørgsmål b.

```{admonition} Svar
:class: dropdown
$$
\left[
\begin{array}{c} 
x_1\\
x_2\\
x_3\\
x_4\\
x_5\\
x_6\\
x_7\\
\end{array}
\right]
=
\left[
\begin{array}{c} 
0\\
9\\
0\\
\pi\\
0\\
0\\
42\\
\end{array}
\right]
+
t_1 \cdot 
\left[
\begin{array}{c} 
1\\
0\\
0\\
0\\
0\\
0\\
0\\
\end{array}
\right]
+
t_2 \cdot 
\left[
\begin{array}{c} 
0\\
-\sqrt{2}\\
1\\
0\\
0\\
0\\
0\\
\end{array}
\right]
+
t_3 \cdot 
\left[
\begin{array}{c} 
0\\
-5\\
0\\
-e\\
1\\
0\\
0\\
\end{array}
\right]
+
t_4 \cdot 
\left[
\begin{array}{c} 
0\\
0\\
0\\
0\\
0\\
1\\
0\\
\end{array}
\right] \quad (t_1,t_2,t_3,t_4 \in \mathbb C).
$$
```

+++

----

+++

## Opgave 5: Et inhomogent system

Afgør om følgende lineære ligningssystem over $\mathbb R$ i de ubekendte $x_1,x_2$ og $x_3$ har en løsning:

$$
\left\{
\begin{array}{ccc} 
x_1 + x_3  & = & 0\\
x_1+x_2 +3x_3 & = & 0\\
10x_1 +3x_2+16x_3 & = & 1\\
\end{array}
\right.
$$

```{hint}
:class: dropdown
Korollar 6.4.3 fra lærebogen kan bruges til at afgøre om systemet har en løsning eller ej. 
Det er derfor en god ide at beregne den reducerede trappeform af systemets totalmatrix først.
```

```{admonition} Svar
:class: dropdown
Systemet har ingen løsninger.
```

+++

----

+++


## Opgave 6: Tre eksempler på lineære ligningssystemer

Bestem den fuldstændige løsning til følgende tre lineære ligningssystemer over $\mathbb R$:

1. 

$$
\left\{
\begin{array}{ccc} 
x_1 + x_2+ x_3  & = & 1\\
x_1+ 2x_2 +4x_3 & = & 1\\
x_1 +3x_2+9x_3 & = & 1\\
\end{array}
\right.
$$

2. 

$$
\left\{
\begin{array}{ccc} 
x_1 + x_2+ x_3  & = & 1\\
x_1+ 2x_2 +4x_3 & = & 1\\
x_1 +3x_2+7x_3 & = & 1\\
\end{array}
\right.
$$

3. 

$$
\left\{
\begin{array}{ccc} 
x_1 + x_2+ x_3  & = & 1\\
x_1+ 2x_2 +4x_3 & = & 1\\
x_1 +3x_2+7x_3  & = & 0\\
\end{array}
\right.
$$

```{admonition} Svar
:class: dropdown
1. Den fuldstændige løsning er

$$
\left[
\begin{array}{c} 
x_1\\
x_2\\
x_3\\
\end{array}
\right]
=
\left[
\begin{array}{c} 
1\\
0\\
0\\
\end{array}
\right]
$$

2. Den fuldstændige løsning er

$$
\left[
\begin{array}{c} 
x_1\\
x_2\\
x_3\\
\end{array}
\right]
=
\left[
\begin{array}{c} 
1\\
0\\
0\\
\end{array}
\right]
+
t \cdot 
\left[
\begin{array}{c} 
2\\
-3\\
1\\
\end{array}
\right] \quad (t \in \mathbb R).
$$

3. Systemet har ingen løsninger.
```