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

(section:uge10S)=

# Opgaver -- Store Dag

----

+++

## Opgave 1: Linearitet

To afbildninger $f: \mathbb{R}^2 \to \mathbb{R}^2$ og $g: \mathbb{R}^2 \to \mathbb{R}^2$, er givet ved forskrifterne:

$$f\left(\left[\begin{array}{r}
x_1\\
x_2
\end{array}\right]\right)=\left[\begin{array}{r} x_1-x_2\\-x_1+x_2\end{array}\right] \quad \text{og} \quad g\left(\left[\begin{array}{r}x_1\\x_2\end{array}\right]\right)=\left[\begin{array}{r}-x_2\\x_1^{2}\end{array}\right].
$$

+++

### Spørgsmål a

Vis at netop én af de to afbildninger er en lineær afbildning mellem de reelle vektorrum $\mathbb{R}^2$ og $\mathbb{R}^2$. 
Find hvilken ved at undersøge om de opfylder de to linearitetskrav nævnt i Definition 11.0.1 fra lærebogen.

```{admonition} Svar
:class: dropdown
Det er afbildningen $f$ som er lineær. At $g$ ikke er lineær, vises nemmest ved et modeksempel. 
For eksempel gælder at $g\left(\left[\begin{array}{r}1\\1\end{array}\right]\right)+g\left(\left[\begin{array}{r}1\\1\end{array}\right]\right)$ ikke er det samme som $g\left(\left[\begin{array}{r}1\\1\end{array}\right]+\left[\begin{array}{r}1\\1\end{array}\right]\right)$.
```

+++

### Spørgsmål b

Angiv en ordnet basis og en basis for $f$'s kerne samt kernens dimension.

```{hint}
:class: dropdown
Definition 11.1.2 forklarer hvad kernen af en lineær afbildning er.
```

```{admonition} Svar
:class: dropdown
Man har 

$$\mathrm{ker}(f)=\left\{t\cdot \left[\begin{array}{r} 1\\1\end{array}\right] \, \mid \, t \in \mathbb{R} \right\}.$$

En ordnet basis for kernen er givet ved listen $\left(\left[\begin{array}{r} 1\\1\end{array}\right]\right)$ og en basis ved mængden $\left\{\left[\begin{array}{r} 1\\1\end{array}\right]\right\}.$ 
Fordi basen kun indeholder en vektor, gælder at $\dim(\mathrm{ker}(f))=1.$
```

+++

### Spørgsmål c

Angiv billedrummet for den fundne lineære afbildning. Angiv også en ordnet basis og en basis for billedrummet. 
Hvad er billedrummets dimension?

```{hint}
:class: dropdown
Billedrummet er afbildningens værdimængden. 
Man skal derfor finde ud af hvilke vektorer $\left[\begin{array}{r} b_1\\b_2\end{array}\right] \in \mathbb{R}^2\,$ 
kan optræde som højreside i ligningen $\left[\begin{array}{r} x_1-x_2\\-x_1+x_2\end{array}\right]=\left[\begin{array}{r} b_1\\b_2\end{array}\right].$

Med andre ord: det skal afgøres for hvilke højresider ligningen $\left[\begin{array}{r} x_1-x_2\\-x_1+x_2\end{array}\right]=\left[\begin{array}{r} b_1\\b_2\end{array}\right]$
har en løsning.
```

```{admonition} Svar
:class: dropdown

$$\mathrm{image}(f)=\left\{t\cdot\left[\begin{array}{r}-1\\1\end{array}\right] \, \mid \, t\in \mathbb{R}\right\}.$$ 

En ordnet basis for billedrummet er givet ved $\left(\left[\begin{array}{r} -1\\1\end{array}\right]\right)$ og en basis ved $\left\{\left[\begin{array}{r} -1\\1\end{array}\right]\right\}.$ 
Billedrummet har derfor dimension $1$ i dette tilfælde.
```

%+++
%
%### Spørgsmål d
%
%Check at dimensionssætningen for lineære afbildninger er opfyldt for den lineære afbildning $f$.
%
%```{hint}
%:class: dropdown
%Dimensionssætningen for lineære afbildninger gives i Korollar 11.4.3 i lærebogen. 
%Passer den når tallene beregnet i de forrige spørgsmål indsættes? 
%```
%
%```{admonition} Svar
%:class: dropdown
%Dimensionssætningen er opfyldt, fordi $\dim(\mathbb{R}^2)=2$ og $\dim(\mathrm{ker}(f))=\dim(\mathrm{image}(f))=1$.
%```

+++

----

+++

## Opgave 2: Lineære afbildninger defineret ved diagonalmatricer

Lad $\lambda_1,\lambda_2 \in \mathbb{R}$ og definer 

$${\mathbf A}=\left[\begin{array}{rr} \lambda_1 & 0\\ 0 & \lambda_2\end{array}\right].$$

I denne opgave undersøges den lineære afbildning $L_{\mathbf A}: \mathbb{R}^2 \to \mathbb{R}^2$ defineret ved $L_{\mathbf A}\left({\mathbf v}\right)={\mathbf A}\cdot {\mathbf v}.$

+++

### Spørgsmål a

Indtegn mængden $\mathcal{K}=\{(v_1,v_2) \, \mid \, 0 \le v_1 \le 1, \, 0 \le v_2 \le 1\}$ ind i $\mathbb{R}^2$. 

```{admonition} Svar
:class: dropdown
Mængden $\mathcal{K}$ er et kvadrat i $\mathbb{R}^2$ med hjørnepunkter $(0,0)$, $(0,1)$, $(1,0)$ og $(1,1)$. 
```

+++

### Spørgsmål b

Indtegn mængden $L_{\mathbf A}(\mathcal{K})$, dvs. mængden $\{L_{\mathbf A}({\mathbf v}) \, \mid \, {\mathbf v} \in \mathcal{K} \}$ i følgende tilfælde:

1. $\lambda_1=1$ og $\lambda_2=1$

2. $\lambda_1=2$ og $\lambda_2=3$

3. $\lambda_1=-1$ og $\lambda_2=2$

4. $\lambda_1=-4$ og $\lambda_2=-3$

```{hint}
:class: dropdown
Hvert ${\mathbf v}=(v_1,v_2) \in \mathcal{K}$ opfylder at

$$ 
\left[\begin{array}{r}v_1\\v_2\end{array}\right]
=
v_1\cdot \left[\begin{array}{r}1\\0\end{array}\right]+v_2\cdot \left[\begin{array}{r}0\\1\end{array}\right]\, , \quad  0 \le v_1 \le 1 \ \text{og} \ 0 \le v_2 \le 1.
$$

Brug nu at $L_{\mathbf A}$ er en lineær afbildning.
```

```{admonition} Svar
:class: dropdown
Det gælder at 

$$ 
L_{\mathbf A}\left(\left[\begin{array}{r}v_1\\v_2\end{array}\right]\right)
=
v_1\cdot \left[\begin{array}{r}\lambda_1\\0\end{array}\right]+v_2\cdot \left[\begin{array}{r}0\\\lambda_2\end{array}\right]\, , \quad  0 \le v_1 \le 1 \ \text{og} \ 0 \le v_2 \le 1.
$$

I samtlige tilfælde er $L_{\mathbf A}(\mathcal{K})$ derfor en rektangel med hjørnepunkter $(0,0),(\lambda_1,0),(0,\lambda_2),(\lambda_1,\lambda_2)$.
```

+++

### Spørgsmål c

Med $\mathcal{K}$ og ${\mathbf A} \in \mathbb{R}^{2 \times 2}$ som før, tjek at arealet af $L_{\mathbf A}(\mathcal{K})$ er lig med $|\det({\mathbf A})|.$ 

+++

### Spørgsmål d

Lad nu 

$${\mathbf A}=\left[\begin{array}{rr} 1 & \lambda\\ 0 & 1\end{array}\right] \quad \lambda \in \mathbb{R}.$$

Tjek at $L_{\mathbf A}(\mathcal{K})$ har areal $1$ og at $\det({\mathbf A})=1$. 
Bemærkning: det viser sig at det for en vilkårlig matrix ${\mathbf A} \in \mathbb{R}^{2 \times 2}$ holder at arealet af $L_{\mathbf A}(\mathcal{K})$ er lig med $|\det({\mathbf A})|.$ 


+++

----

+++

## Opgave 3: Lineære afbildninger og differentiation

Ligesom i Eksempel 10.4.5 fra lærebogen angives med $C_\infty (\mathbb{R})$ det reelle vektorrum bestående af alle funktioner fra $\mathbb{R}$ til $\mathbb{R}$ som kan differentieres vilkårligt mange gange. 
I denne opgave betragtes underrummet $V_1$ af $C_\infty(\mathbb{R})$ som er udspændt af funktionerne $e^t, e^{-t}, \cos(t)$ og $\sin(t)$. 
Det må bruges at disse fire funktioner er lineært uafhængige over $\mathbb{R}$ og derfor danner en ordnet basis for $V_1$.

Der defineres nu følgende funktion $L: V_1 \to V_1$ ved forskriften $L(f)=f'+f$, hvor $f \in V_1$ og hvor $f'$ angiver den afledte af funktionen $f$.

+++

### Spørgsmål a

Tjek at funktionen $L$ er en lineær afbildning mellem reelle vektorrum.

+++

### Spørgsmål b

Beregn afbildningsmatricen ${}_\beta [L] _\beta$, når $\beta=(e^t,e^{-t},\cos(t),\sin(t)).$

```{hint}
:class: dropdown
Formlen for en afbildningsmatrix står i Lemma 11.3.3 fra lærebogen. 
```

```{hint}
:class: dropdown
I Lemma 11.3.3 er det tale om to vektorrum $V_1$ og $V_2$ og to ordnede baser: én til hvert vektorrum. 
Læg mærke til at her $V_1=V_2$ og at den samme ordnede basis $\beta$ bruges for både $V_1$ og $V_2$.
```

```{admonition} Svar
:class: dropdown
$${}_\beta [L] _\beta= \left[\begin{array}{rrrr}
2 & 0 & 0 &  0\\
0 & 0 & 0 & 0\\
0 & 0 & 1 & 1\\
0 & 0 & -1 & 1
\end{array}\right].$$
```

+++

### Spørgsmål c

Der vælges nu en anden ordnet basis for $V_1$: $\gamma=(\mathrm{sinh(t)},\mathrm{cosh(t)},\sin(t),\cos(t))$. 
Funktionerne $\mathrm{sinh(t)}$ og $\mathrm{cosh(t)}$ blev defineret i Opgave 10 fra Uge 2, Store Dag.
Beregn afbildningsmatricen ${}_\gamma [L] _\gamma$ direkte fra formlen i Lemma 11.3.3 i lærebogen. 

```{admonition} Svar
:class: dropdown
$${}_\gamma [L] _\gamma= 
\left[\begin{array}{rrrr}
1 & 1  & 0 &  0\\
1 & 1  & 0 &  0\\
0 & 0  & 1 & -1\\
0 & 0  & 1 & 1
\end{array}\right].
$$
```

+++

### Spørgsmål d


Beregn basisskiftematricen ${}_\gamma [\mathrm{id}_{V_1}] _\beta$.
% og ${}_\beta [\mathrm{id}_{V_1}] _\gamma$.

```{admonition} Svar
:class: dropdown
$${}_\gamma [\mathrm{id}_{V_1}] _\beta= \left[\begin{array}{rrrr}
1 & -1 & 0 & 0\\
1 &  1 & 0 & 0\\
0 & 0  & 0 & 1\\
0 & 0  & 1 & 0
\end{array}\right].$$

%Den anden basisskiftematrix kan beregnes på flere måder. 
%For eksempel kan forlmlen ${}_\beta [\mathrm{id}_{V_1}] _\gamma=({}_\gamma [\mathrm{id}_{V_1}] _\beta)^{-1}$ fra Lemma 11.3.6 bruges.
```

+++

### Spørgsmål e

Brug anden del af Sætning 11.3.4 fra lærebogen til at indse at 
${}_\gamma [\mathrm{id}_{V_1}] _\beta \cdot {}_\beta [L] _\beta = {}_\gamma [L] _\gamma \cdot {}_\gamma [\mathrm{id}_{V_1}] _\beta.$ 
Regn efter at ligningen holder vha. resultaterne fra de forrige spørgsmål.

```{admonition} Svar
:class: dropdown
Ligningen holder, fordi ifølge Sætning 11.3.4 det gælder at ${}_\gamma [\mathrm{id}_{V_1}] _\beta \cdot {}_\beta [L] _\beta = {}_\gamma [\mathrm{id}_{V_1} \circ L] _\beta = {}_\gamma [L] _\beta$ og ${}_\gamma [L] _\gamma \cdot {}_\gamma [\mathrm{id}_{V_1}] _\beta={}_\gamma [L \circ \mathrm{id}_{V_1}] _\beta={}_\gamma [L] _\beta$. 
Her blev det brugt at $\mathrm{id}_{V_1} \circ L=L$ og $L \circ \mathrm{id}_{V_1}=L$, som gælder fordi $\mathrm{id}_{V_1}$ er identitetsfunktionen.   
```

+++

----

+++


## Opgave 4: Basisskifte og afbildningsmatricer


Givet vektorerne 

$$\mathbf v_1 = \left[\begin{array}{r} 1\\ 2\end{array}\right] \text{ og } \mathbf v_2=\left[\begin{array}{r} 3\\ 7\end{array}\right] \text{ fra $\mathbb{R}^2$},$$

samt

$$\mathbf w_1 = \left[\begin{array}{r} 1\\ 2\\ 2\end{array}\right], \mathbf w_2 = \left[\begin{array}{r} 2\\ 3\\1\end{array}\right] \text{ og } \mathbf w_3 = \left[\begin{array}{r} 1\\ 2\\1\end{array}\right] \text{ fra $\mathbb{R}^3$}.$$

Der defineres de ordnede baser 

$$\beta=\left(\mathbf v_1,\mathbf v_2\right) \quad \text{og} \quad \epsilon=\left( \left[\begin{array}{r} 1\\ 0\end{array}\right],\left[\begin{array}{r} 0\\ 1\end{array}\right]\right) \text{ for $\mathbb{R}^2$}$$

og

$$\gamma=\left(\mathbf w_1,\mathbf w_2,\mathbf w_3\right) \quad \text{og} \quad \eta=\left( \left[\begin{array}{r} 1\\ 0\\ 0\end{array}\right],\left[\begin{array}{r} 0\\ 1\\0\end{array}\right],\left[\begin{array}{r} 0\\ 0\\1\end{array}\right]\right) \text{ for $\mathbb{R}^3$}.$$

En lineær afbildning $L:\mathbb{R}^2\to \mathbb{R}^3\,$ opfylder at

$$L(\mathbf{v}_1)=\mathbf{w}_1+\mathbf{w}_2-3\mathbf{w}_3 \quad \mathrm{og} \quad L(\mathbf{v}_2)=\mathbf{w}_1-\mathbf{w}_2-2\mathbf{w}_3\,.$$

Målet med opgaven er at finde afbildningsmatricen ${}_\eta[L]_\epsilon$, 
som er afbildningsmatricen for $L$ mht. de ordnede standardbaser.

%I denne opgave må man gerne udføre matrixprodukter og beregning af inverse matricer med SymPy.

+++

### Spørgsmål a 

%Vis, at $\mathbf{v}_1\,$ og $\mathbf{v}_2\,$ udgør en basis for $\mathbb{R}^2\,$ og at $\mathbf{w}_1\,$, $\mathbf{w}_2\,$ og $\mathbf{w}_3\,$ udgør en basis for $\mathbb{R}^3\,.$
%
%```{hint}
%:class: dropdown
%Vis først at vektorerne $\mathbf{v}_1\,$ og $\mathbf{v}_2\,$ er linært uafhængige og at vektorerne $\mathbf{w}_1\,$, $\mathbf{w}_2\,$ og $\mathbf{w}_3\,$ er lineært uafhængige. Dette kan gøres på forskellige måder, som du kan læse mere om i Kap 7 og Kap 8. En måde er at følge den samme strategi som i Example 7.1.4 fra lærebogen. Alternativt kan man bruge Korollar 8.3.5. 
%```
%
%```{hint}
%:class: dropdown
%Hvis $n$ vektorer i $\mathbb{F}^n$ er lineært uafhængige, danner de så en basis for $\mathbb{F}^n$? Svaret kan udledes fra Sætning 9.2.7 i lærebogen.
%```
%
%+++
%
%### Spørgsmål b

Angiv afbildningsmatricen ${}_\gamma[L]_\beta$ for $L$.
% med hensyn til de ordnede baser $\delta=(\mathbf{v}_1,\mathbf{v}_2)\,$ i $\mathbb{R}^2\,$ og $\epsilon=(\mathbf{w}_1,\mathbf{w}_2,\mathbf{w}_3)$ i $\mathbb{R}^3$.

```{hint}
:class: dropdown
Formlen i Lemma 11.3.3 kan bruges her. 
Husk også at bruge de givne oplysninger om $L$, så der behøves ikke at udføres nogle beregninger! 
```

```{admonition} Svar
:class: dropdown
$${}_\gamma[L]_\beta =\left[\begin{array}{rr} 1 & 1 \\  1 & -1 \\  -3 & -2 \end{array}\right].$$
```

+++

### Spørgsmål b 

Angiv afbildningsmatricen ${}_\eta[L]_\beta$ for $L$, hvor $\beta$ er som før og $\eta$ er den ordnede standardbasis for $\mathbb{R}^3\,.$

```{hint}
:class: dropdown
I stedet for at starte fra definitionen af en afbildningsmatrix, kan man også bruge anden del af Sætning 11.3.4 fra lærebogen for at indse at 
${}_\eta[\mathrm{id}_{\mathbb{R}^3}]_\gamma \cdot {}_\gamma [L] _\beta = {}_\eta [L] _\beta.$ 
```

```{hint}
:class: dropdown
Beregningen af basisskifetmatricen ${}_\eta[\mathrm{id}_{\mathbb{R}^3}]_\gamma$ er ikke kompliceret, fordi $\eta$ er den ordnede standardbasis for $\mathbb{R}^3$.
```

```{admonition} Svar
:class: dropdown
$${}_\eta[L]_\beta =\left[\begin{array}{rr} 0 & -3 \\  -1 & -5 \\  0 & -1 \end{array}\right].$$
```

+++

### Spørgsmål c 
%
%Angiv afbildningsmatricen ${}_\gamma[L]_\epsilon$ for $L$, hvor $\gamma$ er som før og $\epsilon$ er den standard ordnede basis for $\mathbb{R}^2\,.$
%
%```{hint}
%:class: dropdown
%Man kan bruge anden del af Sætning 10.3.4 fra lærebogen til at indse at ${}_\epsilon [L] _\delta \cdot {}_\delta[\mathrm{id}_{\mathbb{R}^2}]_\beta  = {}_\epsilon [L] _\beta.$ Beregn derfor først basisskiftematricen ${}_\delta[\mathrm{id}_{\mathbb{R}^2}]_\beta.$
%```
%
%```{hint}
%:class: dropdown
%Matricen ${}_\delta[\mathrm{id}_{\mathbb{R}^2}]_\beta$ kan være lidt besværligt at beregne, men $({}_\delta[\mathrm{id}_{\mathbb{R}^2}]_\beta)^{-1}={}_\beta[\mathrm{id}_{\mathbb{R}^2}]_\delta$ ifølge Lemma 10.3.5 fra lærebogen. Matricen ${}_\beta[\mathrm{id}_{\mathbb{R}^2}]_\delta$ kan umiddelbart opskrives.
%```
%
%```{admonition} Svar
%:class: dropdown
%$${}_\epsilon[L]_\beta =\left[\begin{array}{rr} 5 & -2 \\  9 & -4 \\  -17 & 7 \end{array}\right].$$
%```
%
%### Spørgsmål e

Angiv nu afbildningsmatricen ${}_\eta[L]_\epsilon$ for $L$, hvor $\eta$ og $\epsilon$ er de ordnede standardbaser for $\mathbb{R}^2$ og $\mathbb{R}^3$.

```{hint}
:class: dropdown
En konsekvens af anden del af Sætning 11.3.4 er at ${}_\eta[L]_\epsilon={}_\eta[L]_\beta \cdot {}_\beta[\mathrm{id}_{\mathbb{R}^2}]_\epsilon$. 
Basisskiftematricen ${}_\beta[\mathrm{id}_{\mathbb{R}^2}]_\epsilon$ kan beregnes ved at bruge Lemma 11.3.6 fra lærebogen.
Den medfører nemlig at ${}_\beta[\mathrm{id}_{\mathbb{R}^2}]_\epsilon=({}_\epsilon[\mathrm{id}_{\mathbb{R}^2}]_\beta)^{-1}$. 
Matricen ${}_\epsilon[\mathrm{id}_{\mathbb{R}^2}]_\beta$ kan umiddelbart opskrives.
```

```{admonition} Svar
:class: dropdown
$${}_\eta[L]_\epsilon =\left[\begin{array}{rr} 6 & -3 \\  3 & -2 \\  2 & -1 \end{array}\right].$$
```

+++

----

+++

## Opgave 5: Kerne af en lineær afbildning

Lad $V_1$ og $V_2$ være to vektorrum over et legeme $\mathbb{F}$. 
Vis at kernen af en linær afbildning $L: V_1 \to V_2$ er et underrum af $V_1.$

```{hint}
:class: dropdown
Kernen af en lineær afbildning er defineret i Definition 11.2.1 i lærebogen. 
Lemma 10.4.2 i lærebogen kan med fordel bruges til at afgøre om den er et underrum af $V_1$.
```

+++

----

+++

## Opgave 6: Lineær afbildning fra et polynomiumsrum

Lad $V_1=\{a+bZ+cZ^2 \, \mid \, a,b,c \in \mathbb{R}\}$ være underrummet af det reelle vektorrum $\mathbb{R}[Z]$ bestående af alle polynomier af grad højst to. Der defineres en funktion $L: V_1 \to \mathbb{R}$ ved forskriften $p(Z) \mapsto p'(1)$. 
Udtrykket $p'(1)$ er tallet man får når man indsætter $1$ i $p'(Z)$, mens $p'(Z)$ betegner den afledte af $p(Z)$.

+++

### Spørgsmål a

Beregn $L(Z^2+Z)$ og $L(5Z^2-10Z+4)$.

```{admonition} Svar
:class: dropdown
Fordi $(Z^2+Z)'=2Z+1$, gælder at $L(Z^2+Z)=2\cdot 1 +1=3$. 
På lignende måde gælder at $(5Z^2-10Z+4)'=10Z-10$ og derfor at $L(5Z^2-10Z+4)=10\cdot 1-10=0.$
```

+++

### Spørgsmål b

Vis at $L$ er en lineær afbildning mellem reelle vektorrum.

```{hint}
:class: dropdown
Betingelserne for at være en lineær afbildning kan man læse i Definition 11.0.1 fra lærebogen.
```

+++

### Spørgsmål c

Bestem en basis for $\mathrm{ker}(L)$.

```{hint}
:class: dropdown
Hvis $L(a+bZ+cZ^2)=0$, hvilken betingelse skal koefficienterne $a,b$ og $c$ opfylde?
```

```{admonition} Svar
:class: dropdown
En mulig basis er $\{1,Z^2-2Z\}$
```

+++

### Spørgsmål d

Vis at $\mathrm{image}(L)=\mathbb{R}$. Konkluder at afbildningen $L$ er surjektiv.
%Brug dimensionssætningen (Corollary 10.4.3 fra lærebogen) til at konkludere at den givne lineære afbildning $L$ er surjektiv.

```{hint}
:class: dropdown
Prøv først at finde et polynomium $p(Z)$ i $V_1$ således at $L(p(Z))=1$. 
Reflekter bagefter hvad $L(ap(Z))$ så er, hvor $a \in \mathbb{R}$ kan vælges frit.
```

```{hint}
:class: dropdown
At sige at en lineær afbildning $M:V_1 \to V_2$ er surjektiv er præcist det samme som at sige at afbildningens billedrum er lig med hele $V_2$. 
Se eventuelt teksten lige før Eksempel 2.2.4 fra lærebogen hvor det blev forklaret hvad det betyder for en funktion at være surjektiv.  
Har man derfor vist at $\mathrm{image}(L)=\mathbb{R}$, så følger direkte at $L$ er surjektiv.
```

```{admonition} Svar
:class: dropdown
$L(aZ)=a$ for et vilkærligt $a \in \mathbb{R}$. Derfor gælder at $\mathrm{image}(L)=\mathbb{R}$. 
Med andre ord: $L$'s værdimængde lig med dens dispositionsmængde.
Dette betyder at $L$ er surjektiv.
%Dimensionssætningen (Corollary 10.4.3 fra lærebogen) medfører at $\dim(\mathrm{image}(L))=\dim V_1 -\dim(\mathrm{ker}(L))=3-2=1$. Siden $\dim \mathbb{R}=1$, kan vi konkludere at $\mathrm{image}(L)=\mathbb{R}$ og derfor at $L$ er surjektiv.
```

+++

----

+++


## Opgave 7: Injektive lineære afbildninger

En funktion $f: A \to B$ kaldes injektiv hvis og kun hvis for alle $a_1,a_2 \in A$ det gælder at $f(a_1)=f(a_2)$ medfører $a_1=a_2$. 
Se eventuelt teksten lig før Eksempel 2.2.4 i lærebogen. 
I denne opgave undersøges hvad det betyder at være injektiv for en lineær afbildning $L: V_1 \to V_2$ mellem to vektorrum $V_1$ og $V_2$ over $\mathbb{F}$.

+++

### Spørgsmål a

Antag at en lineær afbildning $L: V_1 \to V_2$ er injektiv. Vis at i så fald $\mathrm{ker}(L)=\{{\mathbf 0}\}.$

```{hint}
:class: dropdown
Bruges kontraposition, så ses at det ønskede udsagn er logisk ækvivalent med udsagnet: hvis $\mathrm{ker}(L) \neq \{{\mathbf 0}\}$, så er $L$ ikke injektiv. 
```

```{hint}
:class: dropdown
Det vides at $L({\mathbf 0})={\mathbf 0}$ for alle lineære afbildninger $L$ (se for eksempel Ligning (11.1) fra lærebogen). 
Hvis $\mathrm{ker}(L) \neq \{{\mathbf 0}\}$, så findes ${\mathbf v} \in V_1$ forskellig fra $\mathbf 0$ således at $L({\mathbf v})={\mathbf 0}$.
```

```{admonition} Skitse af svar
:class: dropdown
Hvis $\mathrm{ker}(L) \neq \{{\mathbf 0}\}$, så findes ${\mathbf v} \in V_1$ forskellig fra $\mathbf 0$ således at $L({\mathbf v})={\mathbf 0}$. 
Derfor afbilder $L$ både ${\mathbf v}$ og ${\mathbf 0}$ på nulvektoren i $V_2$. 
Dette betyder at $L$ ikke er injektiv.   
```

+++

### Spørgsmål b

Antag at en lineær afbildning $L: V_1 \to V_2$ er givet og at $\mathrm{ker}(L)=\{{\mathbf 0}\}.$ 
Vis at $L$ i så fald $L$ er injektiv.

```{hint}
:class: dropdown
Det ønskede udsagn er logisk ækvivalent med udsagnet: hvis $L$ ikke er injektiv, så gælder $\mathrm{ker}(L) \neq \{{\mathbf 0}\}$. 
```

```{hint}
:class: dropdown
Antag at der findes to forskellig vektorer ${\mathbf v}_1,{\mathbf v}_2 \in V_1$ således at $L({\mathbf v}_1)=L({\mathbf v}_2)$. 
Brug lineariteten af $L$ til at indse at i så fald $L({\mathbf v}_2-{\mathbf v}_1)={\mathbf 0}$.
```

```{admonition} Svar
:class: dropdown
Hvis $L$ ikke er injektiv, så findes to forskellig vektorer ${\mathbf v}_1,{\mathbf v}_2 \in V_1$ således at $L({\mathbf v}_1)=L({\mathbf v}_2)$. 
Dette medfører at $L({\mathbf v}_2-{\mathbf v}_1)={\mathbf 0}$ og derfor at ${\mathbf v}_2-{\mathbf v}_1 \in \ker(L)$. 
Derfor indeholder kernen en vektor forskellig fra nulvektoren, som medfører at $\mathrm{ker}(L) \neq \{{\mathbf 0}\}.$
```

+++

### Spørgsmål c

Konkluder fra de forrige to spørgsmål at en lineær afbildning $L: V_1 \to V_2$ er injektiv hvis og kun hvis $\mathrm{ker}(L) = \{{\mathbf 0}\}.$

```{hint}
:class: dropdown
Brug de forrige spørgsmål, samt Ligning (1.22) fra Kapitel 1.
```

+++

----

+++

## Opgave 8: Undersøgelse af en lineær afbildning fra $\mathbb{R}^4$ til $\mathbb{R}^3$

Lad $L:\mathbb{R}^4 \to \mathbb{R}^3$ være givet ved forskriften

$$
L\left(\left[\begin{array}{r}
v_1\\
v_2\\
v_3\\
v_4
\end{array}\right]
\right)=
\left[\begin{array}{r}
v_1+v_2+3v_3+v_4\\
3v_1-v_2+2v_3+4v_4\\
2v_1+2v_2+6v_3+2v_4
\end{array}\right].
$$

+++

### Spørgsmål a

Find en matrix ${\mathbf A} \in \mathbb{R}^{3 \times 4}$ hvorom det gælder at 

$$
L\left(\left[\begin{array}{r}
v_1\\
v_2\\
v_3\\
v_4
\end{array}\right]
\right)={\mathbf A}\cdot \left[\begin{array}{r}
v_1\\
v_2\\
v_3\\
v_4
\end{array}\right].
$$

Brug Lemma 11.1.1 fra lærebogen til at konkludere at $L$ er en lineær afbildning. 

```{admonition} Svar
:class: dropdown
$$
{\mathbf A}=
\left[\begin{array}{rrrr}
1 & 1 & 3 & 1\\
3 & -1 & 2 & 4\\
2 & 2 & 6 & 2
\end{array}\right].
$$

Fordi $L=L_{\mathbf A}$ hvor $\mathbf A$ er ovenstående matrix, medfører Lemma 11.1.1 fra lærebogen at $L$ er en lineær afbildning.
```

+++

### Spørgsmål b

Lad $\beta$ være den ordnede standardbasis for $\mathbb{R}^4$ og $\gamma$ den for $\mathbb{R}^3$. 
Tjek at ${\mathbf A} = {}_\gamma[L]_\beta$. 

```{hint}
:class: dropdown
Lemma 11.3.3 beskrives hvordan afbildningsmatricen ${}_\gamma[L]_\beta$ ser ud.
```

```{hint}
:class: dropdown
Det er også nyttigt at huske at $[\mathbf w]_\gamma=\mathbf w$ for alle $\mathbf w \in \mathbb{R}^3$, fordi i opgaven $\gamma$ er den ordnede standardbasis for $\mathbb{R}^3$. 
```

+++

### Spørgsmål c

Angiv en ordnet basis for $L$'s kerne. Hvad er kernens dimension?

```{hint}
:class: dropdown
Fordi $L=L_{\mathbf A}$, gælder det, at $L$'s kerne er det samme som $\mathbf A$'s kerne (også kendt som $\mathbf A$'s nulrum). 
En ordnet basis for $\mathbf A$'s kerne kan fås ved at følge den samme procedure som i Eksempel 11.1.4 fra lærebogen. 
```

```{hint}
:class: dropdown
Tjek først at matricen 

$${\mathbf A}=\left[\begin{array}{rrrr}
1 & 1 & 3 & 1\\
3 & -1 & 2 & 4\\
2 & 2 & 6 & 2
\end{array}\right]$$

har reduceret trappeform

$${\mathbf A}=\left[\begin{array}{rrrr}
1 & 0 & 5/4 &  5/4\\
0 & 1 & 7/4 & -1/4\\
0 & 0 & 0   &    0
\end{array}\right].$$
```

```{admonition} Svar
:class: dropdown
Vektorerne 

$$\left[\begin{array}{r}
-5/4 \\
-7/4\\
1\\
0
\end{array}\right],\left[\begin{array}{r}
-5/4\\
1/4\\
0\\
1
\end{array}\right]$$

danner en ordnet basis for $\mathrm{ker} A$ og derfor også til $\mathrm{ker} L$. 
Antallet af elementer i den funde ordnede basis er $2$ og derfor gælder $\dim(\mathrm{ker}(L))=2.$ 
```

+++

### Spørgsmål d

Angiv en ordnet basis for $L$'s billedrum samt billedrummets dimension. 
%Check at dimensionssætningen for lineære afbildninger er opfyldt for den givne lineære afbildning $L$.


```{hint}
:class: dropdown
Brug at $L=L_{\mathbf A}$ og Lemma 11.1.2, for at indse at $L$'s billedrum er det samme som $\mathbf A$'s søjlerum. 
Spørgsmålet kan derfor besvares ved at beregne en ordnet basis for $\mathbf A$'s søjlerum.
```

```{admonition} Svar
:class: dropdown
Da kun de første to søjler af ${\mathbf A}$'s reducerede trappeform indeholder pivot-elementer, 
medfører Sætning 9.2.1 fra lærebogen at en mulig ordnet basis for ${\mathbf A}$'s søjlerum er 

$$\left( \left[\begin{array}{r}
1 \\
3\\
2
\end{array}\right], \left[\begin{array}{r}
1 \\
-1\\
2
\end{array}\right]\right).
$$

Fordi $L=L_{\mathbf A}$ er ${\mathbf A}$'s søjlerum er det samme som $L$'s billedrum, så den ønskede ordnede basis er fundet.
Antallet af elementer i den funde ordnede basis er $2$ og derfor gælder $\dim(\mathrm{image}(L))=2.$ 
%Dimensionssætningen er opfyldt, fordi $\dim(\mathbb{R}^4)=4$ og $\dim(\mathrm{ker}(L))=\dim(\mathrm{image}(L))=2$.
```

+++

----

+++

%## Opgave 8: Koefficientmatricer og sammensætte afbildninger
%
%Lad $V$ være et vektorrum over $\mathbb{F}$ af dimension $n$. Der opgives to ordnede baser $\beta=(%{\mathbf v}_1,\dots,{\mathbf v}_n)$ og $\gamma=({\mathbf v}_1,\dots,{\mathbf v}_n)$ i $V$, samt to %linære afbildninger $L: V \to V$ og $M: V \to V$. 
%
%+++
%
%Definer ${\mathbf A}_1={}_\beta[L]_\beta$ og ${\mathbf A}_2={}_\gamma[L]_\gamma$. Ydermere defineres $%{\mathbf Q}={}_\gamma[\mathrm{id}_V]_\gamma$. Vis at ${\mathbf A}_2={\mathbf Q}^{-1}\cdot {\mathbf A}_1 %\cdot {\mathbf Q}.$
%
%```{hint}
%:class: dropdown
%Matricen ${\mathbf Q}^{-1}$ kan opfattes som en basisskiftematrix ved at bruge tredje del af Lemma 10.%37. Brug nu Sætning 10.33.
%```
%
%+++
%
%### Spørgsmål b
%
%Definer nu også ${\mathbf B}_1={}_\beta[M]_\beta$ og ${\mathbf B}_2={}_\gamma[M]_\gamma$. Vis at 
%${\mathbf A}_2 \cdot {\mathbf B}_2={\mathbf Q}^{-1}\cdot {\mathbf A}_1 \cdot {\mathbf B}_1 \cdot 
%{\mathbf %Q}.$
%
%+++
%
%----
%
%+++

## Opgave 9: Potenser af matricer

Lad ${\mathbf A} \in \mathbb{F}^{n \times n}$ være en matrix og ${\mathbf Q} \in \mathbb{F}^{n \times n}$ en invertibel matrix. Lad $k$ være et naturlig tal. Den $k$te potens af ${\mathbf A}$, notation ${\mathbf A}^k$, er defineret som matricen man får ved at gange ${\mathbf A}$ $k$ gange med sig selv. Mere formelt defineres ${\mathbf A}^k$ rekursivt som følger:

$${\mathbf A}^k = \left\{ \begin{array}{rl} {\mathbf A} & \text{hvis $k=1$}\\ {\mathbf A}^{k-1}\cdot {\mathbf A} & \text{hvis $k \ge 2$.}\end{array} \right.$$

+++

### Spørgsmål a

Antag at ${\mathbf D}$ er en diagonalmatrix. Vis ved hjælp af induktion efter $k$, at matricen ${\mathbf D}^k$ også er en diagonalmatrix for alle naturlige tal $k$.

+++

### Spørgsmål b

Vis ved hjælp af induktion efter $k$, at $({\mathbf Q}^{-1} \cdot {\mathbf A} \cdot {\mathbf Q})^k={\mathbf Q}^{-1} \cdot {\mathbf A}^k \cdot {\mathbf Q}.$

+++

### Spørgsmål c

Lad 

$$
{\mathbf A}=\left[\begin{array}{rr} 0 & 1\\ -6 & 5\end{array}\right] \quad \text{og} \quad {\mathbf Q}=\left[\begin{array}{rr} 1 & 1\\ 2 & 3\end{array}\right].
$$

Tjek at ${\mathbf Q}^{-1} \cdot {\mathbf A} \cdot {\mathbf Q}$ er en diagonalmatrix og brug dette til at finde et lukket udtryk for ${\mathbf A}^k$. 

```{admonition} Svar
:class: dropdown
$${\mathbf A}^k=\left[\begin{array}{rr}3\cdot 2^k-2 \cdot 3^k & -2^k+3^k\\3 \cdot 2^{k+1}-2 \cdot 3^{k+1} & -2^{k+1}+3^{k+1}\end{array}\right].$$
```

## Opgave 10: Tematisk Python Opgave

+++

Opgaven frigives kl 15:30 på DTU Learn.
