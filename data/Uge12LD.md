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


(section:uge12L)=

# Opgaver -- Lille Dag

+++

----

## Opgave 1: Et homogent, komplekst system af lineære differentialligninger

Givet følgende komplekse system af differentialligninger:

$$
\left\{
\begin{array}{rcl} 
f_1'(t) & = & 2f_1(t)-5f_2(t)\\ 
f_2'(t) & = & f_1(t)-2f_2(t)
\end{array}.
\right.
$$

+++

### Spørgsmål a

Systemet kan skrives på formen 

$$
\left[\begin{array}{c} f_1'(t)\\ f_2'(t)\end{array}\right] = {\mathbf A} \cdot \left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right].
$$

Hvad er matricen $\mathbf A$? Bestem også matricens karakteristiske polynomium.

```{admonition} Svar
:class: dropdown
Matricen ${\mathbf A}$ er systemets koefficientmatrix. Det vil sige at:

$$ 
{\mathbf A}=\left[\begin{array}{rr} 2 & -5\\ 1 & -2\end{array}\right].
$$

Vi har 

$$
p_{\mathbf A}(Z)=\mathrm{det}\left(\left[\begin{array}{cc} 2-Z & -5\\ 1 & -2-Z\end{array}\right]\right)=Z^2+1.
$$
```

+++

### Spørgsmål b

Det oplyses at over de komplekse tal er egenrummet $E_i$ for matricen $\mathbf A$ fra spørgsmål a givet ved 

$$
E_i=\mathrm{span}_{\mathbb C}\left( \left[\begin{array}{c} 2+i\\ 1\end{array}\right] \right).$$

Beskriv uden yderligere beregninger egenrummet $E_{-i}$.

```{hint}
:class: dropdown
Kan man bruge kompleks konjugation til noget her?
```

```{admonition} Svar
:class: dropdown
Fordi matricen $\mathbf A$ har reelle koefficienter, fås at ${\mathbf v} \in E_i$ hvis og kun hvis $\overline{\mathbf v} \in E_{-i}$. Med $\overline{\mathbf v}$ menes vektoren man får ved at tage den komplekse konjugerede af samtlige elementer i $\mathbf v$. Derfor fås:

$$
E_{-i}=\mathrm{span}_{\mathbb C}\left( \left[\begin{array}{c} 2-i\\ 1\end{array}\right] \right).
$$
``` 

+++

### Spørgsmål c

Giv den fuldstændige, komplekse løsning til det givne system af differentialligninger.

```{admonition} Svar
:class: dropdown

$$
\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] =c_1 \cdot \left[\begin{array}{c} 2+i\\ 1\end{array}\right]\cdot e^{it}+c_2 \cdot \left[\begin{array}{c} 2-i\\ 1\end{array}\right] \cdot e^{-it}=\left[\begin{array}{c} c_1\cdot (2+i)\cdot e^{it}+c_2\cdot (2-i)\cdot e^{-it}\\ c_1\cdot e^{it}+c_2\cdot e^{-it}\end{array}\right]\, , \quad \text{ hvor } c_1,c_2 \in \mathbb{C}.
$$
``` 

+++

----

+++


## Opgave 2: Fra komplekse til reelle løsninger

I denne opgave betragtes det samme system af differentialligninger som i Opgave 1:

$$
\left\{
\begin{array}{rcl} 
f_1'(t) & = & 2f_1(t)-5f_2(t)\\ 
f_2'(t) & = & f_1(t)-2f_2(t)
\end{array}.
\right.
$$

Den fuldstændige, komplekse løsning til dette system er:

$$
\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] =c_1 \cdot \left[\begin{array}{c} 2+i\\ 1\end{array}\right]\cdot e^{it}+c_2 \cdot \left[\begin{array}{c} 2-i\\ 1\end{array}\right] \cdot e^{-it}=\left[\begin{array}{c} c_1\cdot (2+i)\cdot e^{it}+c_2\cdot (2-i)\cdot e^{-it}\\ c_1\cdot e^{it}+c_2\cdot e^{-it}\end{array}\right]\, , \quad \text{ hvor } c_1,c_2 \in \mathbb{C}.
$$

Målet med opgaven er at eksemplificere hvordan man udfra komplekse løsninger kan finde reelle løsninger. 
Den generelle fremgangsmåde beskrives i Korrolar 13.2.6 fra lærebogen.

+++

### Spørgsmål a 

I den givne fuldstændige løsning vælges konstanterne $c_1$ og $c_2$ således at $c_1=c_2=a$, hvor $a$ er et reelt tal. 
Vis at løsningen i dette tilfælde kan omskrives til følgende:

$$
\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] =a \cdot \left[\begin{array}{c} 2(e^{it}+e^{-it})\\ e^{it}+e^{-it}\end{array}\right] +a \cdot \left[\begin{array}{c} i(e^{it}-e^{-it})\\ 0\end{array}\right].
$$

Brug nu Eulers formler (Ligning (4.7) og (4.8) fra lærebogen) til at omskrive $e^{it}$ og $e^{-it}$ til udtryk i $\cos(t)$ og $\sin(t)$. 
Hvad er resultatet?

```{admonition} Svar
:class: dropdown

$$
\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] =a \cdot \left[\begin{array}{c} 4\cos(t)\\ 2\cos(t)\end{array}\right] +a \cdot \left[\begin{array}{c} -2\sin(t)\\ 0\end{array}\right]=a \cdot \left[\begin{array}{c} 4\cos(t)-2 \sin(t)\\ 2\cos(t)\end{array}\right].
$$
```

### Spørgsmål b 

I den givne fuldstændige løsning vælges nu konstanterne $c_1$ og $c_2$ således at $c_1=b\cdot i$ og $c_2=-b \cdot i$, hvor $b$ er et reelt tal. 
Omskriv i dette tilfælde løsningen til et udtryk i $\cos(t)$ og $\sin(t)$.

```{hint}
:class: dropdown
Man kunne starte med at tjekke at

$$
\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] =b \cdot \left[\begin{array}{c} -(e^{it}+e^{-it})\\ 0\end{array}\right]+b \cdot \left[\begin{array}{c} 2i(e^{it}-e^{-it})\\ i(e^{it}-e^{-it})\end{array}\right].
$$
```

```{admonition} Svar
:class: dropdown

$$
\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] = b \cdot \left[\begin{array}{c} -2\cos(t)\\ 0\end{array}\right]+b \cdot \left[\begin{array}{c} -4\sin(t)\\ -2\sin(t)\end{array}\right] =b \cdot \left[\begin{array}{c} -2\cos(t)-4 \sin(t)\\ -2\sin(t)\end{array}\right].
$$
```

+++

----

+++

## Opgave 3: Begyndelsesbetingelser i et reelt system af lineære differentialligninger

Systemet fra Opgave 1 betragtes igen, men nu som et reelt system af differentialligninger. 
Fra Opgave 2 (og Korrolar 13.2.6) konkluderes at systemets fuldstændige, reelle løsning er:

$$
\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] = a \cdot \left[\begin{array}{c} 4\cos(t)-2 \sin(t)\\ 2\cos(t)\end{array}\right]+b\cdot \left[\begin{array}{c} -2\cos(t)-4 \sin(t)\\ -2\sin(t)\end{array}\right]\, , \quad \text{ hvor } a,b \in \mathbb{R}.
$$

Bestem den løsning til systemet som opfylder begyndelsesbetingelserne $f_1(\pi)=1$ og $f_2(\pi)=3$.

```{hint}
:class: dropdown
Indsættes $t=\pi$ i den fuldstændige løsning og bruges begyndelsesbetingelserne, så fås to lineære ligninger som konstanterne $a$ og $b$ skal opfylde. Hvilke to?
```

```{hint}
:class: dropdown
De to ligninger som $a$ og $b$ skal opfylde er $-4a+2b=1$ og $-2a=3$. 
```

```{admonition} Svar
:class: dropdown
$$
\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] = (-3/2) \cdot \left[\begin{array}{c} 4\cos(t)-2 \sin(t)\\ 2\cos(t)\end{array}\right]+(-5/2)\cdot \left[\begin{array}{c} -2\cos(t)-4 \sin(t)\\ -2\sin(t)\end{array}\right]=\left[\begin{array}{c} -\cos(t)+13 \sin(t)\\ -3\cos(t)+5 \sin(t)\end{array}\right].
$$
```

+++

----

+++

## Opgave 4: Et inhomogent, reelt system af lineære differentialligninger

Givet følgende reelle system af differentialligninger:

$$
\left\{
\begin{array}{rcl} 
f_1'(t) & = & 2f_1(t)-5f_2(t)+e^{2t}\\ 
f_2'(t) & = & f_1(t)-2f_2(t)-e^{2t}
\end{array}.
\right.
$$

Læg mærke til at det tilhørende homogene system af differentialligninger er systemet betragtet i Opgave 3.

+++

### Spørgsmål a

Det oplyses at der findes en partikulær løsning til det givne system på formen:

$$
\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] = \left[\begin{array}{c} d_1\cdot e^{2t}\\ d_2\cdot e^{2t}\end{array}\right]\, ,
$$

hvor $d_1$ og $d_2$ er visse uopgivne reelle tal. Bestem $d_1$ og $d_2$.

```{hint}
:class: dropdown
Indsætter man $f_1(t)=d_1 \cdot e^{2t}$ og $f_1(t)=d_2 \cdot e^{2t}$ i systemet, så får man at $2d_1 e^{2t}= (2d_1-5d_2+1)e^{2t}$ og $2d_2 e^{2t}= (d_1-2d_2-1)e^{2t}$. Hvilke ligninger skal $d_1$ og $d_2$ derfor opfylde?
```

```{admonition} Svar
:class: dropdown
Konstanterne $d_1$ og $d_2$ skal opfylde ligningerne $2d_1=2d_1-5d_2+1$ og $2d_2=d_1-2d_2-1.$ Løses disse to ligninger, så fås at $d_1=9/5 \, $ og $d_2=1/5$.
```

+++

### Spørgsmål b

Giv den fuldstændige, reelle løsning til det givne inhomogene system af differentialligninger.

```{admonition} Svar
:class: dropdown
Lægges den fundne partikulære løsning fra spørgmål a sammen med den fundne fuldstændige, reelle løsning som beskrevet i Opgave 3, så fås det ønskede:

$$
\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] = \left[\begin{array}{c} 9e^{2t}/5\\ e^{2t}/5\end{array}\right]+a \cdot \left[\begin{array}{c} 4\cos(t)-2 \sin(t)\\ 2\cos(t)\end{array}\right]+b\cdot \left[\begin{array}{c} -2\cos(t)-4 \sin(t)\\ -2\sin(t)\end{array}\right]\, , \quad \text{ hvor } a,b \in \mathbb{R}.
$$
```

+++

----

+++


## Opgave 5: En koefficientmatrix som ikke kan diagonaliseres

Der betragtes følgende homogene, reelle system af differentialligninger:

$$
\left\{
\begin{array}{rcl} 
f_1'(t) & = & 2f_1(t)+f_2(t)\\ 
f_2'(t) & = & -4f_1(t)-2f_2(t)
\end{array}
\right.
$$

+++

### Spørgsmål a

Bestem systemets koefficientmatrix $\mathbf A$ og undersøg dens egenværdier samt egenvektorer. 
Kan koefficientmatricen diagonaliseres?

```{admonition} Svar
:class: dropdown
Det gælder at:

$${\mathbf A}= \left[\begin{array}{cc} 2 & 1\\ -4 & -2\end{array}\right].$$

Matricen har kun $0$ som egenværdi og gælder at $\mathrm{am}(0)=2$ samt $\mathrm{gm}(0)=1$. 
Derfor kan $\mathbf A$ ikke diagonaliseres. En mulig basis for egenrummet $E_0$ er:

$$\left\{ \left[\begin{array}{c} -1/2\\1\end{array}\right] \right\}.$$

En anden mulig basis for $E_0$ er

$$\left\{ \left[\begin{array}{c} 1\\-2\end{array}\right] \right\}.$$
```

+++

### Spørgsmål b

Find nu først den fuldstændige løsning til følgende homogene system af differentialligninger:

$$
\left[\begin{array}{c} g'_1(t)\\ g'_2(t)\end{array}\right] = {\mathbf J} \cdot \left[\begin{array}{c} g_1(t)\\ g_2(t)\end{array}\right],$$

hvor

$$
{\mathbf J}= \left[\begin{array}{cc} 0 & 1\\0 & 0\end{array}\right].
$$

```{hint}
:class: dropdown
Hvis man skriver ned hvilke ligninger $g_1(t)$ og $g_2(t)$ skal opfylde, fås $g_1'(t)=g_2(t)$ og $g_2'(t)=0$. Hvilke muligheder er der for $g_2(t)$?
```

```{hint}
:class: dropdown
Man får at $g_2(t)$ skal være en konstant funktion, så man kan skrive $g_2(t)=c_1$. Find nu alle muligheder for $g_1(t)$.
```

```{admonition} Svar
:class: dropdown
Den fuldstændige løsning er  

$$\left[\begin{array}{c} g_1(t)\\ g_2(t)\end{array}\right] = c_1 \cdot \left[\begin{array}{c} t\\ 1\end{array}\right]+c_2 \cdot \left[\begin{array}{c} 1\\ 0\end{array}\right]=\left[\begin{array}{c} c_1\cdot t+c_2\\ c_1\end{array}\right]\, , \quad \text{ hvor } c_1,c_2 \in \mathbb{R}.$$
```

+++

### Spørgsmål c

Det oplyses at ${\mathbf A}={\mathbf Q} \cdot {\mathbf J} \cdot {\mathbf Q}^{-1}$, hvor $\mathbf J$ er som før og hvor

$$
{\mathbf Q}= \left[\begin{array}{cc} 1 & 0\\-2 & 1\end{array}\right].
$$

Det kan vises at dette medfører at

$$\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] \quad \text{ er løsning til systemet } \quad \left[\begin{array}{c} f'_1(t)\\ f'_2(t)\end{array}\right] = {\mathbf A} \cdot \left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right]$$ 

hvis og kun hvis 

$$\left[\begin{array}{c} g_1(t)\\ g_2(t)\end{array}\right] = {\mathbf Q}^{-1} \cdot \left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] \quad \text{ er løsning til systemet } \quad \left[\begin{array}{c} g'_1(t)\\ g'_2(t)\end{array}\right] = {\mathbf J} \cdot \left[\begin{array}{c} g_1(t)\\ g_2(t)\end{array}\right].$$ 

Find nu den fuldstændige løsning til det oprindelige homogene system af differentialligninger som havde koefficientmatricen $\mathbf A$.

```{hint}
:class: dropdown
Brug den fuldstændige løsning fra det forrige spørgsmål og den givne sammenhæng mellem løsninger til de to nævnte systemer af differentialligninger.
```

```{admonition} Svar
:class: dropdown
Den fuldstændige løsning er

$$\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] = \left[\begin{array}{cc} 1 & 0\\-2 & 1\end{array}\right] \cdot \left[\begin{array}{c} c_1\cdot t+c_2\\ c_1\end{array}\right] = \left[\begin{array}{c} c_1\cdot t+c_2\\ -2\cdot c_1 \cdot t-2\cdot c_2 +c_1\end{array}\right]
\, , \quad \text{ hvor } c_1,c_2 \in \mathbb{R}.$$
```


