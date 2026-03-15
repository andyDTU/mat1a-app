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

(section:uge10L)=

# Opgaver -- Lille Dag

----

+++

%## Opgave 1: SymPy opgaven
%
%I denne opgave bruges SymPy til at analysere en lineær afbildning. Der defineres de komplekse vektorrum $V_1 = \{ p(Z) \in \mathbb{C}[Z] \, \mid \, \deg p(Z) \le 6\}$ og $V_2=\mathbb{C}^5$. Ydermere defineres den lineære afbildning $L: V_1 \to V_2$ ved $p(Z) \mapsto (p(0),p(2i),p(1),p(-3),p(1+2i)).$ 
%
%+++
%
%### Spørgsmål a
%
%Der vælges den ordnede basis $\beta=(1,Z,Z^2,Z^3,Z^4,Z^5,Z^6)$ i $V_1$ og den standard ordnede basis $\gamma$ i $V_2$. Bestem afbildningsmatricen ${}_\gamma[L]_\beta$ og indfør matricen i SymPy. Alle beregninger med komplekse tal kan også udføres ved hjælp af SymPy.
%
%```{hint}
%:class: dropdown
%Et komplekst tal som $(1+2i)^6$ kan hurtigt beregnes i SymPy ved at indtaste `(1+2*I)**6`. Hvis potensen ønskes at beregnes eksplicit, indtast eventuelt `expand((1+2*I)**6)`.
%```
%
%```{admonition} Svar
%:class: dropdown
%$$
%{}_\gamma[L]_\beta=
%\left[
%\begin{array}{ccccccc}
%1 & 0    & 0     & 0      & 0      & 0      & 0   \\
%1 & 2i   & -4    & -8i    & 16     & 32i    & -64 \\
%1 & 1    & 1     & 1      & 1      & 1      & 1   \\
%1 & -3   & 9     & -27    & 81     & -243   & 729 \\
%1 & 1+2i & −3+4i & −11−2i & −7−24i & 41−38i & 117+44i  
%\end{array}
%\right].
%$$
%```
%
%+++
%
%### Spørgsmål b
%
%Find en basis af $\mathrm{ker}(L)$.
%
%```{hint}
%:class: dropdown
%Brug gerne SymPy til at finde kernen af matricen ${}_\gamma[L]_\beta$. Dette kan gøres ved at løse det lineære ligningssystem ${}_\gamma[L]_\beta \cdot {\mathbf x}={\mathbf 0}$. Alternativt giver kommandoen `A.nullspace()` en ordnet basis til kernen af en matrix `A`.
%```
%
%```{hint}
%:class: dropdown
%Ved hjælp af SymPy fås at de to vektorer 
%
%$${\mathbf v}_1=
%\left[
%\begin{array}{c}
%0\\
%12 - 6i\\
%-5 + 16i\\
%-9 - 6i\\
%1 - 4i\\
%1\\
%0
%\end{array}
%\right]
% \quad \text{og} \quad 
%{\mathbf v}_2=
%\left[
%\begin{array}{c}
%0\\
%12 + 54 i\\
%-47 - 42 i\\
%28 - 14 i\\
%6 + 2 i\\
%0\\
%1
%\end{array}
%\right]
%%
%danner en mulig basis til kernen af afbildningsmatricen ${}_\gamma[L]_\beta$. Brug nu Sætning 10.4.2 fra lærebogen til at finde en basis til $\mathrm{ker}(L).$
%
%```{admonition} Svar
%:class: dropdown
%En mulig basis til $\mathrm{ker}(L)$ er 
%
%$$\{
%(12 - 6i)Z+(-5 + 16i)Z^2+(-9 - 6i)Z^3+(1 - 4i)Z^4+Z^5,
%(12 + 54 i)Z+(-47 - 42 i)Z^2+(28 - 14 i)Z^3+(6 + 2 i)Z^4+Z^6
%\}.$$
%```
%
%+++
%
%### Spørgsmål c
%
%Find et polynomium $p(Z) \in V_1$ af lavest mulig grad således at $L(p(Z))=(1,3,1,3,1)$.
%
%```{hint}
%:class: dropdown
%Find først ved hjælp af SymPy den fuldstændige løsning på formen ${}_\gamma[L]_\beta \cdot {\mathbf x}={\mathbf b}$ for et passend valg af $\mathbf b$. Se eventuelt Sætning 10.4.2 for flere detaljer.  
%```
%
%```{hint}
%:class: dropdown
%Den fuldstændige løsning omtalt i det forrige hint er
%
%$$
%\left[
%\begin{array}{c}
%1\\
%5/6\\
%-7/10+7i/20\\
%-1/5-7i/30\\
%1/15-7i/60\\
%0\\
%0
%\end{array}
%\right]
%+
%\tau_0 \cdot 
%\left[
%\begin{array}{c}
%0\\
%12 - 6i\\
%-5 + 16i\\
%-9 - 6i\\
%1 - 4i\\
%1\\
%0
%\end{array}
%\right]
%+
%\tau_1\cdot 
%\left[
%\begin{array}{c}
%0\\
%12 + 54 i\\
%-47 - 42 i\\
%28 - 14 i\\
%6 + 2 i\\
%0\\
%1
%\end{array}
%\right]\, , \quad \tau_0,\tau_1 \in \mathbb{C}.
%$$
%```
%
%```{admonition} Svar
%:class: dropdown
%Det ønskede polynomium er 
%
%$$
%1+(5/6)Z+(-7/10+7i/20)Z^2+(-1/5-7i/30)Z^3+(1/15-7i/60)Z^4.
%$$
%```
%
%+++
%
%----
%
%+++

## Opgave 1: I billerrummet eller ej?

Om en linear afbildning $L:\mathbb{R}^4 \to \mathbb{R}^3$ vides at billedrummet $\mathrm{image}(L)$ har en ordnet basis $\beta$ givet ved

$$\beta=\left( \left[\begin{array}{r}
1 \\
3\\
2
\end{array}\right], \left[\begin{array}{r}
1 \\
-1\\
2
\end{array}\right]\right).
$$

+++

### Spørgsmål a

Tilhører vektorerne

$${\mathbf v}=\left[\begin{array}{r}
1 \\
2\\
3
\end{array}\right] \quad \text{og} \quad {\mathbf w}=\left[\begin{array}{r}
2 \\
2\\
4
\end{array}\right]$$

billedrummet $\mathrm{image}(L)$?

```{hint}
:class: dropdown
Kan ${\mathbf v}$ skrives som linearkombination af vektorerne som optræder i den givne ordnede basis? 
Hvad med ${\mathbf w}$?
```

```{hint}
:class: dropdown
Har ligningen 

$$c_1\left[\begin{array}{r}
1 \\
3\\
2
\end{array}\right]+c_2\left[\begin{array}{r}
1 \\
-1\\
2
\end{array}\right]={\mathbf v}$$

en løsning? Hvad med ligningen

$$c_1\left[\begin{array}{r}
1 \\
3\\
2
\end{array}\right]+c_2\left[\begin{array}{r}
1 \\
-1\\
2
\end{array}\right]={\mathbf w}?
$$

```

```{admonition} Svar
:class: dropdown
Vektoren $\mathbf v$ er ikke element i $\mathrm{image}(L)$.

Vektoren $\mathbf w$ er element i $\mathrm{image}(L)$. 
```


## Opgave 2: Dimensionssætningen i et eksempel

En lineær afbildning $L:\mathbb{R}^3\rightarrow \mathbb{R}^3$ har med hensyn til den ordnede standardbasis $\epsilon$ for $\mathbb R^3$ afbildningsmatricen

$${}_\epsilon[L]_\epsilon =\left[\begin{array}{rrr}1&2&1\\ 2&4&0\\ 3&6&0\end{array}\right]\,.$$

Det oplyses at $\dim (\mathrm{ker}(L))=1$, med andre ord: kernen for $L$ har dimensionen $1$. 
Find, alene ved hovedregning, en ordnet basis for $\mathrm{image}(L)\,.$ 


```{admonition} Svar
:class: dropdown
Fordi den anden søjle i afbildningsmatricen er to gange den første, udspænder de resterende to søjler matricens søjlerummet. 
Fordi det oplyses at $L$'s kerne har dimension $1$, medfører dimensionssætningen at $L$'s billedrum har dimension $2$. 
En mulig ordnet basis for billedrummet er derfor

$$\left(\left[\begin{array}{r}1\\2\\3\end{array}\right],\left[\begin{array}{r}1\\0\\0\end{array}\right]\right).$$

```

+++

----

+++

## Opgave 3: Vektorligninger og billedrum

Der defineres følgende funktion:

$$M: \mathbb{R}^{2 \times 3} \to \mathbb{R}^{2 \times 2}\, , \quad {\mathbf A} \mapsto {\mathbf A} \cdot \left[\begin{array}{rr}1 & 2\\ 0 & 0\\ 2 & 1\end{array}\right].$$

+++

### Spørgsmål a 

Vis at $M$ er en lineær afbildning mellem reelle vektorrum og angiv en ordnet basis for $\mathrm{ker}(M).$

```{hint}
:class: dropdown
Angående lineæritet: brug Definition 11.0.1 og læs eventuelt først Sætning 7.2.1, især del (v). 

Angående at angive en ordnet basis for $\mathrm{ker}(M)$: hvad skal en matrix ${\mathbf A} \in \mathbb{R}^{2 \times 3}$ opfylde for at være i $\mathrm{ker}(M)\,$?
```

```{hint}
:class: dropdown

$$\left[\begin{array}{rr}a & b & c\\ d & e & f\end{array}\right] \cdot \left[\begin{array}{rr}1 & 2\\ 0 & 0\\ 2 & 1\end{array}\right]=\left[\begin{array}{rr}a+2c & 2a+c\\ d+2f & 2d+f\end{array}\right].$$
```

```{admonition} Svar
:class: dropdown
En mulig ordnet basis for $\mathrm{ker}(M)$ er 

$$\left( \left[\begin{array}{rr}0 & 1 & 0\\ 0 & 0 & 0\end{array}\right]\, , \left[\begin{array}{rr}0 & 0 & 0\\ 0 & 1 & 0\end{array}\right] \right).$$
```
+++

### Spørgsmål b 

Brug dimensionssætningen for lineære afbildninger (Korollar 11.4.3 fra lærebogen) til at vise at $\dim(\mathrm{image}(M))=4$. 
Konkluder at $\mathrm{image}(M)=\mathbb{R}^{2 \times 2}$.

```{admonition} Svar
:class: dropdown
Hvis $V$ er et vektorrum med en endelig dimension $n$ og $W$ er et underrum af $V$ af samme dimension $n$, så gælder $W=V$. 
Derfor gælder $\mathrm{image}(M)=\mathbb{R}^{2 \times 2}$.
```

+++

### Spørgsmål c 

Gør rede for at ligningen $M({\mathbf A})=\left[\begin{array}{rr}3 & 3\\ 3 & 3\end{array}\right]$ har en løsning udfra resultatet fra spørgsmål b.

Find nu løsningsmængden.

```{hint}
:class: dropdown
Sætning 11.4.1 forklarer hvornår en ligning af den givne type har en løsning. 
Strukturen af løsningsmængden er også beskrevet i Sætning 11.4.1.
```

```{admonition} Svar
:class: dropdown
Løsningsmængden er

$$\left\{ \left[\begin{array}{rr}1 & 0 & 1\\ 1 & 0 & 1\end{array}\right]+t_1 \cdot \left[\begin{array}{rr}0 & 1 & 0\\ 0 & 0 & 0\end{array}\right]+t_2 \cdot \left[\begin{array}{rr}0 & 0 & 0\\ 0 & 1 & 0\end{array}\right] \, \mid \, t_1,t_2 \in \mathbb{R}\right\}.$$

Bemærkning: Udtrykket 

$$\left[\begin{array}{rr}1 & 0 & 1\\ 1 & 0 & 1\end{array}\right]+t_1 \cdot \left[\begin{array}{rr}0 & 1 & 0\\ 0 & 0 & 0\end{array}\right]+t_2 \cdot \left[\begin{array}{rr}0 & 0 & 0\\ 0 & 1 & 0\end{array}\right], \quad t_1,t_2 \in \mathbb{R}$$

kaldes for ligningens fuldstændige løsning.
```

+++

----

+++

## Opgave 4: Undersøgelse af en lineær afbildning

Definer $V_1$ (hhv. $V_2$) til at være mængden af polynomier i $\mathbb{R}[Z]$ af grad højst tre (hhv. to). 
Bemærk at både $V_1$ og $V_2$ er reelle vektorrum. 
Lad afbildningen $M:V_1 \to V_2$ være givet ved forskriften

$$
M(a+bZ+cZ^2+dZ^3)=(a+b+3c+d)+(3a-b+2c+4d)Z+(2a+2b+6c+2d)Z^2\, , \text{hvor $a,b,c,d \in \mathbb{R}$}.
$$

+++

### Spørgsmål a

Der vælges den ordnede basis $\beta=(1,Z,Z^2,Z^3)$ til $V_1$ og den ordnede basis $\gamma=(1,Z,Z^2)$ til $V_2$. 
Bestem afbildningsmatricen ${}_\gamma[M]_\beta$.

```{hint}
:class: dropdown
Lemma 11.3.3 forklarer hvordan man beregner afbildningsmatricen ${}_\gamma[M]_\beta$.
```

```{admonition} Svar
:class: dropdown
$$
{}_\gamma[M]_\beta
=
\left[\begin{array}{rrrr}
1 & 1 & 3 & 1\\
3 & -1 & 2 & 4\\
2 & 2 & 6 & 2
\end{array}\right].
$$
```
+++

### Spørgsmål b

%Bemærk at den fundne afbildningsmatrix er nøjagtigt den samme matrix som matricen $\mathbf A$ fundet i Opgave 2b. 
Bestem en ordnet basis for $M$'s kerne.

```{hint}
:class: dropdown
Bestem først en ordnet basis for kerne af afbildningsmatricen ${}_\gamma[M]_\beta$.
Bagefter kan den sidste del af Sætning 11.4.2 bruges.
```

```{admonition} Svar
:class: dropdown
Polynomierne $-5/4-(7/4)Z+Z^2$ og $-5/4+(1/4)Z+Z^3$ danner en ordnet basis for $\mathrm{ker}(M)$. 
```

+++

### Spørgsmål c

Bestem en ordnet basis for $M$'s billedrum.

```{hint}
:class: dropdown
Bestem først en ordnet basis for søjlerummet af afbildningsmatricen ${}_\gamma[M]_\beta$. 
Overvej hvordan denne ordnede basis kan bruges til at finde en ordnet basis for $\mathrm{image}(M).$
```

```{admonition} Svar
:class: dropdown
Listen $(1+3Z+2Z^2, 1-Z+2Z^2)$ er en ordnet basis for $\mathrm{image}(M).$
```

+++

### Spørgsmål d

Afgør om polynomierne

$$p_1(Z)=1+2Z+3Z^2 \quad \text{og} \quad p_2(Z)=2+2Z+4Z^2$$

tilhører billedrummet $\mathrm{image}(M)$.

```{hint}
:class: dropdown
Brug den ordnede basis for $M$'s billedrum fundet i spørgsmål c.
```

```{hint}
:class: dropdown
Har ligningen $c_1\cdot(1+3Z+2Z^2)+c_2\cdot(1-Z+2Z^2) =p_1(Z)$ en løsning $c_1,c_2 \in \mathbb{R}$? 
Hvad med ligningen $c_1\cdot(1+3Z+2Z^2)+c_2\cdot(1-Z+2Z^2) =p_1(Z)$?
```

```{admonition} Svar
:class: dropdown
Polynomiet $p_1(Z)$ er ikke element i $\mathrm{image}(M)$. 
Polynomiet $p_2(Z)$ er element i $\mathrm{image}(M)$. 
```

+++

----

+++


## Opgave 5: Lineære afbildninger og differentiation

Ligesom i Eksempel 10.4.5 fra lærebogen angives med $C_\infty (\mathbb{R})$ det reelle vektorrum bestående af alle funktioner fra $\mathbb{R}$ til $\mathbb{R}$ som kan differentieres vilkårligt mange gange. 
I denne opgave betragtes den lineære afbildning $M: C_\infty (\mathbb{R}) \to C_\infty (\mathbb{R})$ ved forskriften $M(f)=f'+f$, hvor $f \in C_\infty (\mathbb{R})$ og hvor $f'$ angiver den afledte til funktionen $f$. 

+++

### Spørgsmål a

Det oplyses at $\dim \mathrm{ker}(M)=1$. Find en basis for $\mathrm{ker}(M)$. 

```{hint}
:class: dropdown
Fordi det er givet at kernen til $M$ er et $1$-dimensionalt underrum af $C_\infty$, udspænder ethvert element i $\mathrm{ker}(M)$ forskelligt fra nul hele kernen.  
```

```{hint}
:class: dropdown
Prøv at finde et element $f(t)$ i $\mathrm{ker}(M)$ forskelligt fra nul på formen $f(t)=e^{at}$ for et vist $a \in \mathbb{R}$. 
```

```{admonition} Svar
:class: dropdown
Fordi $(e^{at})'=ae^{at}$, gælder at $M(e^{-t})=0$. Fra den første hint fås at $\{e^{-t}\}$ er en basis for $\mathrm{ker}(M)$.
```

+++

### Spørgsmål b

Find løsningsmængden til følgende ligninger

1. $M(f)=e^{t}$, 

2. $M(f)=t$,

3. $M(f)=e^{-t}$.

```{hint}
:class: dropdown
Sætning 11.4.1 forklarer løsningsmængdens struktur: hver løsning er på formen ${\mathbf v}_p+{\mathbf v}$, hvor ${\mathbf v}_p$ er en partikulær løsning og hvor ${\mathbf v} \in \mathrm{ker}(M)$.
```

```{hint}
:class: dropdown
For at finde en partikulær løsning til den første ligning, find $a \in \mathbb{R}$ således at $f(t)=ae^{t}$ opfylder ligningen. 

For at finde en partikulær løsning til den anden ligning, prøv en funktion på formen $f(t)=t+a$, hvor $a \in \mathbb{R}$. 

For at finde en partikulær løsning til den tredje ligning, prøv en funktion på formen $f(t)=ate^{-t}$, hvor $a \in \mathbb{R}$. 
```

```{admonition} Svar
:class: dropdown
1. Løsningsmængden er $\{(1/2)e^{t}+c_1\cdot e^{-t} \, \mid \, c_1 \in \mathbb{R}\}.$ Man siger også at $(1/2)e^{t}+c_1\cdot e^{-t}, \ c_1 \in \mathbb{R}$ er den fuldstændige løsning til ligningen $f'+f=e^t$.

2. Løsningsmængden er $\{t-1+c_1\cdot e^{-t} \, \mid \, c_1 \in \mathbb{R}\}.$ Man siger også at $t-1+c_1\cdot e^{-t}, \ c_1 \in \mathbb{R}$ er den fuldstændige løsning til ligningen $f'+f=t$.

3. Løsningsmængden er $\{te^{-t}+c_1\cdot e^{-t} \, \mid \, c_1 \in \mathbb{R}\}.$ Man siger også at $te^{-t}+c_1\cdot e^{-t}, \ c_1 \in \mathbb{R}$ er den fuldstændige løsning til ligningen $f'+f=e^{-t}$.
```

+++

----

+++


## Opgave 6: Eksempler på lineære afbildninger 

Lad $n$ være et naturligt tal og $d$ et helt tal som opfylder $0 \le d \le n$. 
Find et eksempel på en lineær afbildning $L: \mathbb{C}^n \to \mathbb{C}^n$ mellem komplekse vektorrum, 
således at $\dim(\mathrm{ker}(L))=d$ og $\dim(\mathrm{image}(L))=n-d$.  

