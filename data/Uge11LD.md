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

(section:uge11L)=

# Opgaver -- Lille Dag

----

+++

## Opgave 1: Diagonalisering af en $2 \times 2$ matrix.

Givet matricen:

$${\mathbf A}=\left[\begin{array}{cc} 9 & -6\\ 8 & -7 \end{array}\right] \in \mathbb{R}^{2 \times 2}.$$

Undersøg om $\,\mathbf A\,$ kan diagonaliseres og angiv i givet fald en invertibel matrix $\,\mathbf Q\,$ og en diagonalmatrix $\,\mathbf{D}\,$, således at 

$$\,\mathbf{D}={\mathbf Q}^{-1}\cdot{\mathbf A}\cdot{\mathbf Q}.$$


```{admonition} Svar
:class: dropdown
Matricen ${\mathbf A}$ har to egenværdier $-3$ og $5$ som begge har algebraisk og geometrisk multiplicitet lig med $1$. 
Derfor findes der to lineært uafhængige egenvektorer for $\,\mathbf A\,$ og er diagonalisering mulig.
Flere rigtige svar for $\mathbf D$ og $\mathbf Q$ er mulige.
Her er et af dem: 

$$\,{\mathbf Q} =\left[\begin{array}{cc} 1 & 3\\ 2 & 2 \end{array}\right] \,\,\,\,\text{og}\,\,\,\, \mathbf{D}=\left[\begin{array}{cc} -3 & 0\\ 0 & 5 \end{array}\right].$$
```

+++

----

+++

## Opgave 2: Diagonalisering af en lineær afbildning.

En lineær afbildning $\,f: \mathbb{R}^3\rightarrow\ \mathbb{R}^3\,$ har med hensyn til den ordnede standardbasis $\epsilon$ i $\, \mathbb{R}^3 \,$ afbildningsmatricen:

$${{}_\epsilon [f]_\epsilon}=\left[\begin{array}{cc} 1 & 0 & 0\\ 1 & 1 & 1\\ 1 & 0 & 2 \end{array}\right] \in \mathbb{R}^{3 \times 3}\, .$$

+++

### Spørgsmål a

Kan afbildningen $f$ diagonaliseres? 

```{hint}
:class: dropdown
Afbildningen $f$ kan diagonaliseres hvis og kun hvis afbildningsmatricen ${}_\epsilon [f]_\epsilon$ kan diagonaliseres.
Bestem derfor først egenværdierne og egenrummene for afbildningsmatricen ${}_\epsilon [f]_\epsilon$.
```

```{hint}
:class: dropdown
Det viser sig at ${\mathbf {}_\epsilon [f]_\epsilon}$ har to egenværdier: én med geometrisk multiplicitet $1$ og én med geometrisk multiplicitet $2$.
Hvordan kan man udfra det konkludere at der er tre lineært uafhængige egenvektorer af ${\mathbf {}_\epsilon [f]_\epsilon}$ som udspænder $\mathbb{R}^3$? 
```

```{admonition} Svar
:class: dropdown
$\,{{}_\epsilon [f]_\epsilon}\,$ har egenværdierne $1$ og $2$, hvor $\mathrm{am}(1)=\mathrm{gm}(1)=2$ og $\mathrm{am}(2)=\mathrm{gm}(2)=1$. 
Afbildningsmatricen $\,{{}_\epsilon [f]_\epsilon}\,$ kan derfor diagonaliseres. Men så kan afbildningen $f$ også diagonaliseres.

For at bestemme de nævnte geometriske multipliciteter beregnes egenrummene. 
De fås til at være:

$$\,E_1=\mathrm{span}_\mathbb{R}\left(\left[\begin{array}{cc} 0 \\ 1 \\ 0 \end{array}\right], \left[\begin{array}{cc} -1 \\ 0 \\ 1 \end{array}\right]\right)\,\,\,\,\text{og}\,\,\,\,\, E_2=\mathrm{span}_\mathbb{R}\left(\left[\begin{array}{cc} 0 \\ 1 \\ 1 \end{array}\right]\right).$$

```


+++

### Spørgsmål b

Angiv en ordnet basis $\,\beta\,$ for $\,\mathbb{R}^3\,$ med hensyn til hvilken afbildningsmatricen for $\,f\,$ bliver en diagonalmatrix.
Angiv også den tilsvarende basisskiftematrix $\, \mathbf {}_\epsilon [\mathrm{id}_{\mathbb{R}^3}]_\beta \,$ som skifter fra $\beta$-koordinater til $\epsilon$-koordinater.


```{hint}
:class: dropdown
Egenvektorerne fundet i Spørgsmål a kan bruges.
```

```{admonition} Svar
:class: dropdown
Den ønskede ordnede basis $\beta$ skal bestå af lineært uafhængige egenvektorer for $f$. 
Et muligt svar er derfor:

$$\beta = \left( \left[\begin{array}{cc} 0 \\ 1 \\ 1 \end{array}\right],\left[\begin{array}{cc} 0 \\ 1 \\ 0 \end{array}\right], \left[\begin{array}{cc} -1 \\ 0 \\ 1 \end{array}\right]\right)$$

og

$$\mathbf {}_\epsilon [\mathrm{id}_{\mathbb{R}^3}]_\beta=\left[\begin{array}{cc} 0 & 0 & -1\\ 1 & 1 & 0\\ 1 & 0 & 1 \end{array}\right].$$

```



+++

### Spørgsmål c
Angiv en invertibel matrix $\, \mathbf Q\,$ og en diagonalmatrix $\, \mathbf{D}\, $, så 

$$\mathbf{D} = {\mathbf Q}^{-1} \cdot {\mathbf {}_\epsilon [f]_\epsilon} \cdot {\mathbf Q}.$$

```{hint}
:class: dropdown
En matrix $\, \mathbf Q\,$ bestående af lineært uafhængige egenvektorer har de ønskede egenskaber.
Kan basisskiftematricen fra Spørgsmål b bruges her?
```

```{hint}
:class: dropdown
Det gælder at 

$${}_\beta [f]_\beta=\mathbf {}_\beta [\mathrm{id}_{\mathbb{R}^3}]_\epsilon \cdot {}_\epsilon [f]_\epsilon \cdot {}_\epsilon [\mathrm{id}_{\mathbb{R}^3}]_\beta=\left({}_\epsilon [\mathrm{id}_{\mathbb{R}^3}]_\beta\right)^{-1} \cdot {}_\epsilon [f]_\epsilon \cdot {}_\epsilon [\mathrm{id}_{\mathbb{R}^3}]_\beta$$

Derfor har basisskiftematricen $\,\mathbf {}_\epsilon [\mathrm{id}_{\mathbb{R}^3}]_\beta\,$ de ønskede egenskaber og kan man vælge $\, \mathbf Q=\mathbf {}_\epsilon [\mathrm{id}_{\mathbb{R}^3}]_\beta\,$.
Bemærk at $\mathbf Q$'s søjler er lineært uafhængige egenvektorer.
```

```{admonition} Svar
:class: dropdown
Ved at vælge $\,\mathbf Q=\mathbf {}_\epsilon [\mathrm{id}_{\mathbb{R}^3}]_\beta=\left[\begin{array}{cc} 0 & 0 & -1\\ 1 & 1 & 0\\ 1 & 0 & 1 \end{array}\right]$ opnås, 
at $\mathbf{D} = {\mathbf Q}^{-1} \cdot {\mathbf{}_\epsilon [f]_\epsilon} \cdot {\mathbf Q}$, 
hvor $\,\mathbf{D}=\left[\begin{array}{cc} 2 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1 \end{array}\right]\,.$
```

+++

----

+++

## Opgave 3: Diagonalisering

### Spørgsmål a

Der er givet matricen 

$${\mathbf B}=\left[\begin{array}{cc} 3 & 1 & -2 \\ 1 & 3 & 1 \\0 & 0 & 2 \end{array}\right] \in \mathbb{R}^{3 \times 3}.$$

Undersøg om $\,\mathbf B \,$ kan diagonaliseres og angiv i givet fald en invertibel matrix $\,\mathbf Q \,$ og en diagonalmatrix $\,\mathbf{D}\,,$ 
således at 

$$\mathbf{D}={\mathbf Q}^{-1}\cdot\mathbf B\cdot\mathbf Q.$$

```{hint}
:class: dropdown
Find alle egenværdier for $\,\mathbf B\,$ og bestem deres algebraiske og geometriske multipliciter.
```

```{admonition} Svar
:class: dropdown
En af $\,\mathbf B\,$'s egenværdier har algebraisk multiplicitet $2$ og geometrisk multiplicitet $1$. 
Matricen $\,\mathbf B\,$ kan derfor ikke diagonaliseres.
```

+++

### Spørgsmål b

Der er givet matricen 

$${\mathbf C}=\left[\begin{array}{cc} 2 & 0 & 0 \\ 1 & 1 & 1 \\-1 & 1 & 1 \end{array}\right] \in \mathbb{R}^{3 \times 3}.$$

Undersøg om $\,\mathbf C\,$ kan diagonaliseres og angiv i givet fald en invertibel matrix $\,\mathbf Q\,$ og en diagonalmatrix $\,\mathbf{D}\,,$ således at 

$$\mathbf{D}={\mathbf Q}^{-1}\cdot{\mathbf C}\cdot{\mathbf Q}.$$


```{admonition} Svar
:class: dropdown

Bemærk at $0$ er en af egenværdierne. 
Diagonalisering er mulig, da der findes tre lineært uafhængige egenvektorer for $\mathbf C\,.$
Flere rigtige svar er mulige, her er et af dem:

$${\mathbf Q}=\left[\begin{array}{cc} 1 & 0 & 1 \\  1 & -1 & 0 \\  0 & 1 & -1 \end{array}\right] \,\,\,\,\text{og}\,\,\,\,{\mathbf D}=\left[\begin{array}{cc}  2 & 0 & 0 \\  0 & 0 & 0 \\  0 & 0 & 2 \end{array}\right].$$

```

+++

----

+++

## Opgave 4: Diagonalisering over de komplekse tal

Givet matricen

$${\mathbf M}=\left[\begin{array}{cc} 3 & 0 & 0 \\ 0 & 1 & -1 \\  5 & 1 & 1 \end{array}\right] \in \mathbb{C}^{3 \times 3}.$$

### Spørgsmål a

Find egenværdier og de tilhørende komplekse egenrum for $\,\mathbf M\,.$

```{admonition} Svar
:class: dropdown

Egenværdierne er $1+i$, $1-i$ og $3$. Alle med algebraisk multiplicitet $1$.
De til $\lambda=1+i$ hørende egenvektorer er $\mathbf v=t_1\cdot \left[\begin{array}{cc} 0 \\  i \\  1 \end{array}\right]$, hvor $t_1\in\mathbb{C}$,

de til $\lambda=1-i$ hørende egenvektorer er $\mathbf v=t_2\cdot \left[\begin{array}{cc} 0 \\ -i \\  1 \end{array}\right]$, hvor $t_2\in\mathbb{C}$ og

de til $\lambda=3$ hørende egenvektorer er $\mathbf v=t_3\cdot\ \left[\begin{array}{cc} 1 \\  -1 \\  2 \end{array}\right]$, hvor $t_3\in\mathbb{C}$.
```

### Spørgsmål b
Diagonalisér $\,\mathbf M \,$, det vil sige bestem matricer $\mathbf Q$ og $\mathbf{D}$ så:

$${\mathbf D}={\mathbf Q}^{-1}\,{\mathbf M}\,{\mathbf Q}.$$  

```{admonition} Svar
:class: dropdown
Hvis vi sætter $\,{\mathbf Q}=\left[\begin{array}{cc} 0&0&1\\ i&-i&-1\\ 1&1&2 \end{array}\right] \,$ og $\,{\mathbf D}=\left[\begin{array}{cc} 1+i&0&0\\ 0&1-i&0\\ 0&0&3 \end{array}\right]\,$ 
så gælder der som ønsket: 

$${\mathbf D}={\mathbf Q}^{-1}\,{\mathbf M}\,{\mathbf Q}.$$

```

+++

----

+++

%## Opgave 4: Diagonalisering af matrix med SymPy.
%
%### Spørgsmål a
%
%Find ved hjælp af SymPy's `eigenvects()` samtlige egenværdier og de tilhørende reelle egenrum for matricen
%
%$${\mathbf A}=\left[\begin{array}{cc} -1 & -1 & -6 & 3\\ 1 & -2 & -3 & 0\\ -1 & 1 & 0 & 1 \\ -1 & -1 & -5 & 3 \end{array}\right] \in \mathbb{R}^{4 \times 4}.$$
%
%```{admonition} Svar
%:class: dropdown
%Egenværdierne er $1$, med $\mathrm{gm}(1) = \mathrm{am}(1) = 1$, $0$ med $\mathrm{gm}(0) =1 < 2 = \mathrm{am}(0)$ og $-1$ med $\mathrm{gm}(-1) = \mathrm{am}(-1) = 1$.
%De tilhørende egenvektorrum er:
%
%$$E_1=\mathrm{span}_\mathbb{R}\left(\left[\begin{array}{cc} 3 \\ 0 \\ 1 \\ 4 \end{array}\right]\right)\,,\,\, E_0 = \mathrm{span}_\mathbb{R}\left(\left[\begin{array}{cc} 2 \\ 1 \\ 0 \\ 1\end{array}\right]\right) \,\,\,\,\text{og}\,\,\,\,E_{-1}= \mathrm{span}_\mathbb{R}\left(\left[\begin{array}{cc} 3 \\ 0 \\ 1 \\ 2 \end{array}\right]\right).$$
%
%```
%
%+++
%
%### Spørgsmål b
%Undersøg om der findes en invertibel matrix $\, \mathbf V\,$ og en diagonalmatrix $\,\mathbf{\Lambda}\,$, så:
%
%$${\mathbf \Lambda}={\mathbf V}^{-1}\cdot {\mathbf A}\cdot{\mathbf V}.$$

## Opgave 5: Diagonaliserbar eller ej?

### Spørgsmål a

Om en reel matrix $\mathbf A \in \mathbb{R}^{2 \times 2}$ er givet at den har to forskellige reelle egenværdier. 
Kan matricen diagonaliseres?
Med andre ord: findes $\mathbf Q \in \mathbb{R}^{2 \times 2}$ således at ${\mathbf Q}^{-1}\cdot {\mathbf A}\cdot{\mathbf Q}$ 
er en diagonalmatrix?

```{admonition} Svar
:class: dropdown
Ja.
```

+++

### Spørgsmål b

Om en reel matrix $\mathbf B \in \mathbb{R}^{2 \times 2}$ er givet at den ingen reelle egenværdier har. 
Kan matricen diagonaliseres? 

```{admonition} Svar
:class: dropdown
Nej. Hvis der ikke er (reelle) egenværdier, er der heller ikke egenvektorer i $\mathbb{R}^2$. 
Derfor kan der heller ikke være en ordnet basis for $\mathbb{R}^2$ bestående af egenvektorer.
```

+++

### Spørgsmål c

Om en reel matrix $\mathbf B \in \mathbb{R}^{2 \times 2}$ er givet at den ingen reelle egenværdier har. 
Kan matricen diagonaliseres over de komplekse tal? 
Med andre ord: findes $\mathbf Q \in \mathbb{C}^{2 \times 2}$ således at ${\mathbf Q}^{-1}\cdot {\mathbf B}\cdot{\mathbf Q}$ 
er en diagonalmatrix?

```{hint}
:class: dropdown
Fordi $\mathbf B \in \mathbb{R}^{2 \times 2}$, har matricens karakteristiske polynomium reelle koefficienter.
Hvad kan siges om de komplekse rødder i matricens karakteristiske polynomium? 
Se eventuelt Lemma 5.3.3 fra lærebogen.
```

```{admonition} Svar
:class: dropdown
Ja. 
Matricens karakteristiske polynomium har to forskellige komplekse rødder som er hinandens kompleks konjugerede.
Derfor ses på lignende måde som i Spørgsmål a at matricen kan diagonaliseres over de komplekse tal.
```

+++

### Spørgsmål d

Giv et eksempel på en matrix $\mathbf C \in \mathbb{R}^{2 \times 2}$ 
som ikke kan diagonaliseres over de reelle tal og heller ikke over de komplekse tal.

```{admonition} Svar
:class: dropdown
Man skal finde en matrix der kun har én reel egenværdi $\lambda$ som oven i købet har geometrisk multiplicitet $1$.
Et muligt svar er ${\mathbf C}=\left[\begin{array}{cc} 0&1\\ 0&0 \end{array}\right]$. 
Denne matrix har kun $0$ som egenværdi og det gælder at $\mathrm{am}(0)=2$ og $\mathrm{gm}(0)=1$.
```

+++

----

+++

## Opgave 6: Lineær afbildning mellem polynomiumsrum

Lad $\mathbb{C}[Z]$ være det komplekse vektorrum bestående af polynomier med komplekse koefficienter. 
Givet $n \in \mathbb{N}$ et naturligt tal, defineres $V=\mathrm{span}_{\mathbb{C}}(1,Z,\dots,Z^{n})$ 
som underrummet af $\mathbb{C}[Z]$ bestående af polynomier af grad op til $n$.
Der defineres en lineær afbildning $L: V \to V$ ved forskriften $L(p(Z))=p'(Z)$, hvor $p'(Z)$ betegner den afledte af $p(Z)$. 

+++

### Spørgsmål a

Bestem afbildningsmatricen ${}_m[L]_m$, hvor $m$ er den ordnede basis for $V$ givet ved $m=(1,Z,\dots,,Z^n)$.

```{admonition} Svar
:class: dropdown
$${}_m[L]_m=
\left[\begin{array}{ccccc} 
0&1&0&\cdots&0\\ 
0&0&2&\ddots&\vdots\\ 
\vdots& & \ddots & \ddots & 0\\ 
\vdots & & & \ddots & n\\
0 & & \cdots & & 0
\end{array}\right].$$
```

+++

### Spørgsmål b

Kan $L$ diagonaliseres?

```{admonition} Svar
:class: dropdown
Nej.
```
%+++
%
%### Spørgsmål c
%
%For $a \in \mathbb{C}$ defineres nu den lineære afbildning $M_a : V \to V$ 
%ved forskriften $M(p(Z))=p(Z)+a \cdot p'(Z)$. 
%Vis at $M_a$ kan diagonaliseres hvis og kun hvis $a=0$.
%
%## Opgave 6: Similære matricer
%
%Givet matricerne
%
%$${\mathbf A}=\left[\begin{array}{cc} 0&1\\ -1&0 \end{array}\right]  \,\,\, , \,\,\, {\mathbf B}=\left[\begin{array}{cc} 0&-1\\ 1&0 \end{array}\right] \in \mathbb{C}^{2 \times 2}.$$
%
%### Spørgsmål a
%Gør rede for at $\mathbf A$ og $\mathbf B$ er similære.
%
%```{hint}
%:class: dropdown
%Vis at $\mathbf A$ og $\mathbf B$ er similære med den samme diagonalmatrix.
%```
%
%```{hint}
%:class: dropdown
%Hvis vi sætter $\,{\mathbf Q}=\left[\begin{array}{cc} -i&i\\ 1&1 \end{array}\right] \,,$ $\,{\mathbf P}=\left[\begin{array}{cc} i&-i\\ 1&1 \end{array}\right] \,$ og $\,{\mathbf D}=\left[\begin{array}{cc} i&0\\ 0&-i \end{array}\right] \,$ så gælder: 
%
%$${\mathbf D}={\mathbf Q}^{-1}\cdot{\mathbf A}\cdot{\mathbf Q}={\mathbf P}^{-1}\cdot{\mathbf B}\cdot{\mathbf P} \,.$$
%
%```
%
%```{hint}
%:class: dropdown
%Bestem nu en invertibel matrix $\, \mathbf M \,$ der opfylder
%
%$${\mathbf B}={\mathbf M}^{-1}\,{\mathbf A}\,{\mathbf M}\,.$$
%
%```
%
%```{admonition} Svar
%:class: dropdown
%
%$${\mathbf M} ={\mathbf Q} \cdot {\mathbf P}^{-1} = \left[\begin{array}{cc} -1&0\\ 0&1 \end{array}\right].$$ 
%
%```
