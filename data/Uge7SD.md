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

(section:uge7S)=

# Opgaver -- Store Dag

----

%+++
%
%## Opgave 1: Intro til lineære ligningssystemer med SymPy
%
%I Opgave 6 fra Uge 7, Lille Dag blev følgende tre lineære ligningssystemer over $\mathbb R$ undersøgt:
%
%1. 
%
%$$
%\left\{
%\begin{array}{ccc} 
%x_1 + x_2+ x_3  & = & 1\\
%x_1+ 2x_2 +4x_3 & = & 1\\
%x_1 +3x_2+9x_3 & = & 1\\
%\end{array}
%\right.
%$$
%
%2. 
%
%$$
%\left\{
%\begin{array}{ccc} 
%x_1 + x_2+ x_3  & = & 1\\
%x_1+ 2x_2 +4x_3 & = & 1\\
%x_1 +3x_2+7x_3 & = & 1\\
%\end{array}
%\right.
%$$
%
%3. 
%
%$$
%\left\{
%\begin{array}{ccc} 
%x_1 + x_2+ x_3  & = & 1\\
%x_1+ 2x_2 +4x_3 & = & 1\\
%x_1 +3x_2+7x_3  & = & 0\\
%\end{array}
%\right.
%$$
%
%Vi vil nu undersøge disse tre systemer igen, men nu ved hjælp af CAS-værktøjet *SymPy*. Åbn derfor et Jupyter notebook og start med at køre kommandoen `from sympy import *`. Kommandoen sørger for at man nu kan bruge Sympy-kommandoer. 
%
%+++
%
%### Spørgsmål a 
%
%Totalmatricen $T1$ til det første lineære ligningssystem kan defineres i Sympy på følgende måde: `T1=Matrix([[1,1,1,1],[1,2,4,1],[1,3,9,1]])`. Afprøv kommmandoen. For at se matricen $T1$ på dit skærm, behøver du blot at skrive `T1`. For at beregne $T1$'s reducerede trappeform kan man skrive `T1.rref()`. Bemærk at "rref" blot er en forkortelse af "*r*educed *r*ow *e*chelon *f*orm". Hvordan skal outputtet fortolkes?  
%
%```{admonition} Svar
%:class: dropdown
%Outputtet er `(Matrix([[1,0,0,1],[0,1,0,0],[0,0,1,0]]),(0,1,2))`. Den første del af outputtet,  `Matrix([[1,0,0,1],[0,1,0,0],[0,0,1,0]])`, er den reducerede trappeform af matricen $T1$. Den anden del, `(0,1,2)`, angiver søjlene af den reducerede trappeform som indeholder et pivot-element. Husk at Python bruger nul-indeksering, så det faktisk er den 1., 2. og 3. søjle af den reducerede trappeform som indeholder et pivot-element i dette tilfælde. 
%```
%
%Hvis man bruger kommandoen `T1.rref(pivots=False)`, så får man kun $T1$'s reducerede trappeform at se. Afprøv også denne kommando. 
%
%+++
%
%### Spørgsmål b
%
%Ud fra $T1$'s reducerede trappeform kan løsningen til lineær ligningssystem nr. 1., direkte aflæses. Man kan også løse systemet direkte i Sympy. Først skal man definere systemets koefficientmatrix `A=Matrix([[1,1,1],[1,2,4],[1,3,9]])` og systemets højreside `b=Matrix([[1],[1],[1]])`. Afprøv nu kommandoen `linsolve((A,b))` og fortolk outputtet.
%
%```{admonition} Svar
%:class: dropdown
%Outputtet er løsningsmængde til lineær ligningssystem nr. 1. 
%```
%
%+++
%
%### Spørgsmål c
%
%Prøv nu selv at gå igennem de samme trin som i spørgsmål a og b, men nu for ligningssystem nr 2. Hvilke søjler af totalmatricens reducerede trappeform indeholder et pivot-element? Hvad er systemets løsningsmængde?
%
%```{hint}
%:class: dropdown
%Kommandoen `T2=Matrix([[1,1,1,1],[1,2,4,1],[1,3,7,1]])` definerer totalmatricen af system nr. 2.
%```
%
%```{admonition} Svar
%:class: dropdown
%Den reducerede trappeform af $T2$ har kun to pivot-elementer, som befinder sig i dens 1. og 2. søjle. Sympy's bud på løsningsmængden er $\{(2\tau_0+1,-3\tau_0,\tau_0)\}$. Læg mærke til at Sympy bruger $\tau_0$ til at angive en fri parameter (og $\tau_0$, $\tau_1$, osv., hvis der er behov for flere frie parametre). Læg også mærke til at systemets løsningsmængde egentligt er $\{(2\tau_0+1,-3\tau_0,\tau_0) \, \mid \, \tau_0 \in \mathbb{R}\}.$
%```
%
%+++
%
%### Spørgsmål d 
%
%Gør nu det samme en gang til, men nu for ligningsssytem nr 3. Hvilke søjler af totalmatricens reducerede trappeform indeholder et pivot-element? Hvad er systemets løsningsmængde?
%
%```{admonition} Svar
%:class: dropdown
%Den reducerede trappeform af systemets totalmatrix har tre pivot-elementer, som befinder sig i dens 1., 2. og 4. søjle. Sympy angiver helt korrekt $\emptyset$, den tomme mængde, som løsningsmængde.
%```
%
%+++
%
%----

+++


## Opgave 1: Linearkombinationer

Givet er følgende vektorer i $\mathbb{R}^3$:

$$
{\mathbf u}=\left[
\begin{array}{c} 
4\\
-2\\
0\\
\end{array}
\right], \quad 
{\mathbf v}=\left[
\begin{array}{c} 
7\\
4\\
3\\
\end{array}
\right], \quad 
{\mathbf w}=\left[
\begin{array}{c} 
1\\
7\\
3\\
\end{array}
\right].
$$

+++

### Spørgsmål a 

Beregn følgende linearkombinationer af de tre vektorer ${\mathbf u}, {\mathbf v}$ og ${\mathbf w}.$

1. $4{\mathbf v}.$

2. $2{\mathbf u}-3{\mathbf w}$.

3. $3{\mathbf u}-2{\mathbf v}+2{\mathbf w}$.

```{admonition} Svar
:class: dropdown

1. $$4{\mathbf v}=\left[
\begin{array}{c} 
28\\
16\\
12\\
\end{array}
\right].
$$

2.

$$
2{\mathbf u}-3{\mathbf w}=\left[
\begin{array}{c} 
5\\
-25\\
-9\\
\end{array}
\right].
$$

3.

$$3{\mathbf u}-2{\mathbf v}+2{\mathbf w}=\left[
\begin{array}{c} 
0\\
0\\
0\\
\end{array}
\right].$$

```

+++

### Spørgsmål b 

Afgør om vektorerne ${\mathbf u}, {\mathbf v}$ og ${\mathbf w}$ er lineært uafhængige baseret på svarene fra spørgsmål a.

```{hint}
:class: dropdown
Du kan finde i Definition 7.1.1 hvad det betyder for vektorer at være lineært uafhængige/afhængige. 
Ligning (7-3) og (7-4) kan også være nyttige at se på. 
```

```{admonition} Svar
:class: dropdown
Vektorerne ${\mathbf u}$, ${\mathbf v}$ og ${\mathbf w}$ er ikke linært uafhængige, på grund af del 3. af spørgsmål a og Ligning (7-4) fra lærebogen.
``` 

+++

### Spørgsmål c 

Vis at vektorerne ${\mathbf u}$ og ${\mathbf v}$ er lineært uafhængige. 

```{hint}
:class: dropdown
Betragt først Ligning (7-3) fra lærebogen. 
Hvis $c_1,c_2 \in \mathbb{R}$ opfylder at 

$$c_1 \cdot {\mathbf u}+c_2 \cdot {\mathbf v}=\left[
\begin{array}{c} 
0\\
0\\
0\\
\end{array}
\right],$$ 

kan man da vise at $c_1=c_2=0$? 
```

```{admonition} Svar
:class: dropdown
Vektorerne ${\mathbf u}$ og ${\mathbf v}$ er lineært uafhængige.
``` 

+++

----

+++

## Opgave 2: Lineært uafhængige vektorer i $\mathbb{R}^4$

Der opgives følgende tre vektorer i $\mathbb{R}^4$:

$$
{\mathbf u}=\left[
\begin{array}{c} 
1\\
1\\
0\\
0\\
\end{array}
\right], \quad 
{\mathbf v}=\left[
\begin{array}{c} 
0\\
1\\
1\\
0\\
\end{array}
\right], \quad 
{\mathbf w}=\left[
\begin{array}{c} 
0\\
0\\
1\\
1\\
\end{array}
\right].
$$

+++

### Spørgsmål a 

Vis at vektorerne ${\mathbf u}, {\mathbf v}$ og ${\mathbf w}$ er lineært uafhængige.

```{hint}
:class: dropdown
Antag at

$$
c_1\cdot\left[
\begin{array}{c} 
1\\
1\\
0\\
0\\
\end{array}
\right]+c_2\cdot\left[
\begin{array}{c} 
0\\
1\\
1\\
0\\
\end{array}
\right]+c_3\cdot\left[
\begin{array}{c} 
0\\
0\\
1\\
1\\
\end{array}
\right]=\left[
\begin{array}{c} 
0\\
0\\
0\\
0\\
\end{array}
\right].
$$

Hvad kan der siges om $c_1, c_2$ og $c_3$?
```

+++

### Spørgsmål b

Antag at ${\mathbf c} \in \mathbb{R}^4$ opfylder at vektorerne ${\mathbf u}, {\mathbf v}, {\mathbf w}$ og ${\mathbf c}$ er lineært uafhængige. Vis, at i så fald kan vektor $\mathbf c$ ikke skrives som en linearkombination af ${\mathbf u}, {\mathbf v}$ og ${\mathbf w}$.

```{hint}
:class: dropdown
Bruges kontraposition (Ligning (1.21) fra lærebogen), så ses at det man skal vise er logisk ækvivalent med udsagnet: hvis ${\mathbf c}$ kan skrives som en linearkombination af ${\mathbf u}, {\mathbf v}$ og ${\mathbf w}$, så er vektorerne ${\mathbf u}, {\mathbf v}, {\mathbf w}$ og ${\mathbf c}$ lineært afhængige.
Prøv at visse dette udsagn.
```

```{hint}
:class: dropdown
Hvis ${\mathbf c}=c_1\cdot {\mathbf u}+c_2\cdot {\mathbf v}+c_3\cdot {\mathbf w}$ for visse $c_1,c_2,c_3 \in \mathbb{R}$, så gælder 

$${\mathbf c}-c_1\cdot {\mathbf u}-c_2\cdot {\mathbf v}-c_3\cdot {\mathbf w}=\left[
\begin{array}{c} 
0\\
0\\
0\\
0\\
\end{array}
\right].$$
``` 

+++

### Spørgsmål c 

Find en vektor ${\mathbf b} \in \mathbb{R}^4$ således at vektorerne ${\mathbf u}, {\mathbf v}, {\mathbf w}$ og ${\mathbf b}$ er lineært uafhængige.

```{hint}
:class: dropdown
Spørgsmål b kan bruges her. 
Prøv derfor at finde en vektor ${\mathbf b} \in \mathbb{R}^4$ som ikke kan skrives som en linearkombination af ${\mathbf u}, {\mathbf v}$ og ${\mathbf w}$.
```

```{hint}
:class: dropdown
Kan vektoren

$$\left[
\begin{array}{c} 
1\\
0\\
0\\
0\\
\end{array}
\right]$$

skrives som en linearkombination af ${\mathbf u}, {\mathbf v}$ og ${\mathbf w}$?
``` 

+++

----

+++

## Opgave 3: Lineært uafhængighed og reduceret trappeform.

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
2\\
3\\
\end{array}
\right].
$$

### Spørgsmål a

Lad $\mathbf A$ være den $3 \times 3$ matrix som har søjler ${\mathbf v}_1, {\mathbf v}_2$ og ${\mathbf v}_3$. 
Beregn matricens reducerede trappeform og brug trappeformen til at finde ${\mathbf A}$'s rang.

```{admonition} Svar
:class: dropdown
$\mathbf A$'s reducerede trappeform er 

$$
\left[
\begin{array}{ccc} 
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{array}
\right].
$$

Det vil sige at $\mathbf A$'s reducerede trappeform er ${\mathbf I}_3$, den $3 \times 3$ identitetsmatrix. 
Trappeformen har tre pivot-elementer, som betyder at $\rho(\mathbf A)=3.$
```

+++

### Spørgsmål b

Er de givne vektorer ${\mathbf v}_1, {\mathbf v}_2$ og ${\mathbf v}_3$ lineært uafhængige?

```{hint}
:class: dropdown
Sætning 7.1.3 fra lærebogen er nyttigt her.
```

```{admonition} Svar
:class: dropdown
Bruges Sætning 7.1.3, så kan man konkludere at de givne tre vektorer er lineært uafhængige.
```

+++

### Spørgsmål c

Kan fire vektorer ${\mathbf w}_1, {\mathbf w}_2, {\mathbf w}_3$ og ${\mathbf w}_4$ i $\mathbb{R}^3$ være lineært uafhængige?

```{hint}
:class: dropdown
Lad $\mathbf B$ være den $3 \times 4$ matrix som har søjler ${\mathbf w}_1, {\mathbf w}_2, {\mathbf w}_3$ og ${\mathbf w}_4$. 
Overvej hvorfor rangen af $\mathbf B$ højest kan være tre.
```

```{admonition} Svar
:class: dropdown
Fordi $\mathbf B$ har tre rækker, kan dens reducerede trappeform højest have tre pivotelementer. 
Derfor gælder at $\rho(\mathbf B) \le 3$.
Bruges Sætning 7.1.3, så kan man konkludere at fire vektorer ${\mathbf w}_1, {\mathbf w}_2, {\mathbf w}_3$ og ${\mathbf w}_4$ i $\mathbb{R}^3$ altid er lineært afhængige.
Svaret er derfor nej.
```

%+++
%
%## Opgave 4: Lineært uafhængighed og reduceret trappeform.
%
%Givet er følgende fire vektorer i $\mathbb{C}^4$: 
%
%$$
%{\mathbf v_1}=\left[
%\begin{array}{c} 
%1+i\\
%1\\
%0\\
%4\\
%\end{array}
%\right], \quad 
%{\mathbf v_2}=\left[
%\begin{array}{c} 
%0\\
%1\\
%0\\
%7\\
%\end{array}
%\right], \quad 
%{\mathbf v_3}=\left[
%\begin{array}{c} 
%2+2i\\
%0\\
%1\\
%1\\
%\end{array}
%\right], \quad
%{\mathbf v_4}=\left[
%\begin{array}{c} 
%2+2i\\
%5\\
%1+i\\
%1\\
%\end{array}
%\right].
%$$
%
%+++
%
%### Spørgsmål a
%
%Definer i SymPy den $4 \times 4$ matrix $\mathbf A$ som har søjler ${\mathbf v}_1, {\mathbf v}_2, {\mathbf v}_3$ og ${\mathbf v}_4$. 
%Brug SymPy til at beregne matricens reducerede trappeform. Brug trappeformen til at finde ${\mathbf A}$'s rang.
%
%```{admonition} Svar
%:class: dropdown
%$\mathbf A$'s reducerede trappeform er 
%
%$$
%\left[
%\begin{array}{cccc} 
%1 & 0 & 0 & 0\\
%0 & 1 & 0 & 0\\
%0 & 0 & 1 & 0\\
%0 & 0 & 0 & 1\\
%\end{array}
%\right].
%$$
%
%Det vil sige at $\mathbf A$'s reducerede trappeform er ${\mathbf I}_4$. Trappeformen har fire pivot-elementer, som betyder at $\rho(\mathbf A)=4.$
%```
%
%+++
%
%### Spørgsmål b
%
%Er de givne vektorer ${\mathbf v}_1, {\mathbf v}_2, {\mathbf v}_3$ og ${\mathbf v}_4$ lineært uafhængige?
%
%```{hint}
%:class: dropdown
%Theorem 7.1.3 fra lærebogen kan være nyttigt her.
%```
%
%```{admonition} Svar
%:class: dropdown
%Ja, de er lineært uafhængige.
%```
%
%+++

----

+++

## Opgave 4: Matrixprodukt

Givet er følgende tre matricer:

$$
{\mathbf A}=\left[
\begin{array}{ccc} 
1 & 0 & 0 \\
0 & 1 & 0 \\
\end{array}
\right] \quad
{\mathbf B}=\left[
\begin{array}{cc} 
1 & 4\\
2 & 1\\
3 & 0\\
\end{array}
\right] \quad
{\mathbf C}=\left[
\begin{array}{ccc} 
1 & 0 & 0 \\
0 & -1 & 0 \\
2 & 0 & 0 \\
\end{array}
\right].
$$

+++

### Spørgsmål a

Hvilke af de ni mulige matrixprodukter ${\mathbf A}\cdot{\mathbf A}$, $\, {\mathbf A}\cdot{\mathbf B}$, $\, {\mathbf A}\cdot{\mathbf C}$, $\, {\mathbf B}\cdot{\mathbf A}$, $\, {\mathbf B}\cdot{\mathbf B}$, $\, {\mathbf B}\cdot{\mathbf C}$, $\, {\mathbf C}\cdot{\mathbf A}$, $\, {\mathbf C}\cdot{\mathbf B}$, $\, {\mathbf C}\cdot{\mathbf C}$ er definerede? 

```{hint}
:class: dropdown
Ifølge Definition 7.2.2 fra lærebogen, kan man kun gange to matricer sammen hvis antallet af søjler i den første matrix er lig med antallet af rækker i den anden matrix.
```

```{admonition} Svar
:class: dropdown
Kun følgende matrixprodukter kan dannes: ${\mathbf A}\cdot{\mathbf B}, \, {\mathbf A}\cdot{\mathbf C}, \, {\mathbf B}\cdot{\mathbf A}, \, {\mathbf C}\cdot{\mathbf B}, \, {\mathbf C}\cdot{\mathbf C}$.
```

### Spørgsmål b

Beregn matrixprodukterne ${\mathbf A}\cdot{\mathbf B}$ og ${\mathbf B}\cdot{\mathbf A}$. 
Gælder det at ${\mathbf A}\cdot{\mathbf B}={\mathbf B}\cdot{\mathbf A}$?

```{admonition} Svar
:class: dropdown
$${\mathbf A}\cdot{\mathbf B}=\left[
\begin{array}{cc} 
1 & 4  \\
2 & 1  \\
\end{array}
\right]$$

$${\mathbf B}\cdot{\mathbf A}=\left[
\begin{array}{ccc} 
1 & 4 & 0 \\
2 & 1 & 0 \\
3 & 0 & 0 \\
\end{array}
\right].$$

Det er klart fra svaret at ${\mathbf A}\cdot{\mathbf B} \neq  {\mathbf B}\cdot{\mathbf A}$. 
Matricerne ${\mathbf A}\cdot{\mathbf B}$ og ${\mathbf B}\cdot{\mathbf A}$ har ikke engang den samme størrelse!
```

+++

### Spørgmål c

Beregn produktet af skalaren $-1/2$ og matricen $\mathbf C$. Med andre ord: beregn $(-1/2) \cdot {\mathbf C}$.

```{admonition} Svar
:class: dropdown
$$(-1/2) \cdot {\mathbf C}=\left[
\begin{array}{ccc} 
-1/2 & 0 & 0 \\
0 & 1/2 & 0 \\
-1 & 0 & 0 \\
\end{array}
\right]$$
```
+++

### Spørgmål d

Afgør om følgende summer af matricer er definerede og beregn dem der er: $(-1/2) \cdot {\mathbf C}+{\mathbf A} \cdot {\mathbf B}$ og $(-1/2) \cdot {\mathbf C}+{\mathbf B} \cdot {\mathbf A}.$


```{admonition} Svar
:class: dropdown
Summen $(-1/2) \cdot {\mathbf C}+{\mathbf A} \cdot {\mathbf B}$ er ikke defineret, fordi $(-1/2) \cdot {\mathbf C}$ er en $3 \times 3$ matrix og ${\mathbf A} \cdot {\mathbf B}$ en $2 \times 2$ matrix.

Summen $(-1/2) \cdot {\mathbf C}+{\mathbf B} \cdot {\mathbf A}$ er defineret, fordi matricerne $(-1/2) \cdot {\mathbf C}$ og ${\mathbf B} \cdot {\mathbf A}$ har den samme størrelse. 
Udkomsten er:

$$
(-1/2) \cdot {\mathbf C}+{\mathbf B} \cdot {\mathbf A}=\left[
\begin{array}{ccc} 
1/2 & 4 & 0 \\
2 & 3/2 & 0 \\
2 & 0 & 0 \\
\end{array}
\right].
$$
```
+++

----

+++

## Opgave 5: Matrix-vektorprodukt og lineære ligningssystemer 

Givet er det lineære ligningssystem 

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

+++

### Spørgsmål a

Skriv systemet på formen som i Ligning (7-5) fra lærebogen.

```{admonition} Svar
:class: dropdown
$$
\left[
\begin{array}{ccccc}
1  & 0  & 0 & 1  \\
-2 & 1  & 0 & 3  \\
5  & 0  & 1 & -4 \\
4  & 1  & 1 & 0  \\
\end{array}
\right] \cdot
\left[
\begin{array}{c}
x_1 \\
x_2 \\
x_3 \\
x_4 \\
\end{array}
\right]=
\left[
\begin{array}{c}
0 \\
1 \\
1 \\
2 \\
\end{array}
\right].
$$
```

+++

### Spørgsmål b

Der defineres 

$${\mathbf A}=\left[
\begin{array}{ccccc}
1  & 0  & 0 & 1  \\
-2 & 1  & 0 & 3  \\
5  & 0  & 1 & -4 \\
4  & 1  & 1 & 0  \\
\end{array}
\right], \quad {\mathbf b}=\left[
\begin{array}{c}
0 \\
1 \\
1 \\
2 \\
\end{array}
\right].$$

Tjek at det givne lineære ligningssystem har totalmatrix $[{\mathbf A}|{\mathbf b}]$. 
I Opgave 3b fra Uge 6 Lille Dag, blev det tjekket at det lineære ligninssystem med totalmatrix $[{\mathbf A}|{\mathbf b}]$ har følgende partikulære løsning:

$$
{\mathbf v}=\left[
\begin{array}{c}
0 \\
1 \\
1 \\
0 \\
\end{array}
\right].
$$

Tjek det igen, men denne gang ved at udregne produktet ${\mathbf A}\cdot{\mathbf v}$.

%```{hint}
%:class: dropdown
%Definer først matricen $\mathbf A \in \mathbb{R}^{4 \times 4}$ og vektoren $\mathbf v \in \mathbb{R}^4$ i SymPy. Et produkt af en matrix `A` og en vektor `v` beregnes i SymPy ved kommandoen `A*v`.
%```

%+++
%
%### Spørgsmål c
%
%Lad ${\mathbf A},{\mathbf v}$ være som før. Produktet ${\mathbf v}\cdot{\mathbf A}$ er ikke defineret. Hvad sker der når man prøver at beregne produktet i SymPy alligevel?
%
%```{admonition} Svar
%:class: dropdown
%Man burde få en fejlmeddelelse som slutter med `Matrix size mismatch: (4, 1) * (4, 4).`, som giver mening fordi en vector $\mathbf v \in \mathbb{R}^4$ kan opfattes som en $4 \times 1$ matrix og $\mathbf A$ er en $4 \times 4$ matrix.
%```

+++

----

+++

## Opgave 6: Beregning af inverse matricer

Givet er følgende kvadratiske matrix:

$${\mathbf A}=\left[
\begin{array}{ccc}
1  & 1  & 0   \\
-1 & 1  & 0   \\
5  & 0  & 1   \\
\end{array}
\right].$$

+++

### Spørgsmål a

Afgør om matricen ${\mathbf A}^{-1}$ findes og beregn den, hvis den gør.

```{hint}
:class: dropdown
Man kan følge proceduren som forklaret lige inden Eksempel 7.3.1 i lærebogen. 
Eksempel 7.3.1 og Eksempel 7.3.2 kan være nyttige også hvis man vil se nogle eksempler. 
```

```{admonition} Svar
:class: dropdown
Den reducerede trappeform af matricen $[{\mathbf A}|{\mathbf I}_3]$ er 

$$\left[
\begin{array}{cccccc}
1 & 0 & 0 & 1/2  & -1/2  & 0   \\
0 & 1 & 0 & 1/2 & 1/2  & 0   \\
0 & 0 & 1 & -5/2  & 5/2  & 1   \\
\end{array}
\right].
$$

Derfor findes ${\mathbf A}^{-1}$ og der gælder

$${\mathbf A}^{-1}=\left[
\begin{array}{ccc}
1/2  & -1/2  & 0   \\
1/2 & 1/2  & 0   \\
-5/2  & 5/2  & 1   \\
\end{array}
\right].$$
```

%+++
%
%### Spørgsmål b
%
%Tjek dine beregninger i SymPy.
%
%```{hint}
%:class: dropdown
%Hvis `A` er en matrix defineret i SymPy, så kan kommandoen `A**(-1)` bruges til at beregne den inverse matrix hvis den findes. Hvis den inverse matrix ikke findes, fås en fejlmeddelelse.
%```

+++

----

+++

## Opgave 7: Inverse matricer og lineære ligningssystemer

Lad ${\mathbf A} \in \mathbb{C}^{n \times n}$ være en kvadratisk matrix og antag at ${\mathbf A}$ er en invertibel matrix. 
Ydermere, lad ${\mathbf b} \in \mathbb{C}^n$ være en vektor.

+++

### Spørgsmål a

Vis at vektoren ${\mathbf A}^{-1}\cdot {\mathbf b} \in \mathbb{C}^n$ er løsning til det lineære ligningssystem med totalmatrix $[{\mathbf A}|{\mathbf b}].$

```{hint}
:class: dropdown
Skriv først ligningssystemet på matrixform ligesom i Ligning (7-5) i lærebogen.  
```

```{hint}
:class: dropdown
På matrixform ser systemet ud som følger:

$$ {\mathbf A} \cdot \left[
\begin{array}{c}
x_1 \\
x_2 \\
\vdots \\
x_n \\
\end{array}
\right]={\mathbf b}.$$

Er dette opfyldt hvis 

$$ \left[
\begin{array}{c}
x_1 \\
x_2 \\
\vdots \\
x_n \\
\end{array}
\right]={\mathbf A}^{-1} \cdot {\mathbf b}?$$
```

+++

### Spørgsmål b 

Vis at vektoren ${\mathbf A}^{-1} \cdot {\mathbf b}$ er den eneste løsning til det lineære ligningssystem med totalmatrix $[{\mathbf A}|{\mathbf b}].$

```{hint}
:class: dropdown
Gang ligningen 

$$ {\mathbf A} \cdot \left[
\begin{array}{c}
x_1 \\
x_2 \\
\vdots \\
x_n \\
\end{array}
\right]={\mathbf b}$$

med ${\mathbf A}^{-1}$ på begge sider af lighedstegnet fra venstre side.
```

+++

----

+++

## Opgave 8: Ligningssystemer med variabel koefficient

For enhver reel værdi af $a$ er givet det lineære ligningssystem:

\begin{align*}
ax_1 + x_2 + x_3 &= 1\\
x_1 + ax_2 + x_3 &= 1\\ 
x_1 + x_2 + ax_3 &= 1
\end{align*}

### Spørgsmål a
Angiv ligningssystemets totalmatrix.

### Spørgsmål b

Angiv løsningen i tilfældet når $a=-2$.

### Spørgsmål c
Bestem løsningen til det lineære ligningssystem.

```{hint}
:class: dropdown
Undervejs i dine beregninger risikerer du at dividere med nul, noter disse specialtilfælde ned og behandl dem separat.
```

```{admonition} Answer
:class: dropdown

For $a\in\mathbb R\setminus\{-2,1\}$ er løsningen $(x_1,x_2,x_3)=(\frac1{a+2},\frac1{a+2},\frac1{a+2})$, og for $a=1$ er løsningen $(x_1,x_2,x_3)=(1,0,0)+t_1(-1,1,0)+t_2(-1,0,1)\quad,t_1,t_2\in\mathbb R$. 
Der er ingen løsning for $a=-2$.
```

+++

----

+++

## Bemærkning 

Der åbnes en Möbius test om forrige ugens Pythonopgave kl. 15:30.

%+++
%
%### Spørgsmål d
%
%Kan SymPy løse opgaven?
%
+++

