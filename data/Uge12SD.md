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


(section:uge12S)=

# Opgaver -- Store Dag

----

+++

## Opgave 1: En reel, ikke lineær differentialligning

Givet den reelle differentialligning $f'(t)^2-4e^{2t} \cdot f(t)=0$.

+++

### Spørgsmål a

Er funktionen $f(t)=t$ løsning til differentialligningen?

```{hint}
:class: dropdown
Er ligningen $f'(t)^2-4e^{2t} \cdot f(t)= 0$ opfyldt hvis du indsætter funktionen $f(t)=t$? 
```

```{admonition} Svar
:class: dropdown
Nej.
```

+++

### Spørgsmål b

Er funktionen $f(t)=e^{2t}$ løsning til differentialligningen?

```{hint}
:class: dropdown
Den afledte til $f(t)=e^{2t}$ er $f'(t)=2e^{2t}$. Er ligningen $f'(t)^2-4e^{2t} \cdot f(t)= 0$ opfyldt hvis du indsætter funktionen $f(t)=e^{2t}$? 
```

```{admonition} Svar
:class: dropdown
Ja.
```

+++

----

+++

## Opgave 2: En reel, lineær differentialligning

I denne opgave undersøges den reelle differentialligning

$$f'(t)-3f(t)=t.$$ 

+++

### Spørgsmål a

Det opgives at der findes reelle tal $a$ og $b$ sådan, at funktionen $at+b$ er en løsning til
differentialligningen. Find $a$ og $b$.

```{hint}
:class: dropdown
Indsæt funktionen $f(t)=at+b$ i differentialligningen og undersøg hvad $a$ og $b$ skal opfylde for at funktionen er en løsning.
```

```{admonition} Svar
:class: dropdown
$a=-1/3$ og $b=-1/9$.
```

### Spørgsmål b

Find den fuldstændige løsning til den reelle differentialligning $f'(t)-3f(t)=0$.

```{admonition} Svar
:class: dropdown
$f(t)=c \cdot e^{3t}$, hvor $c \in \mathbb{R}.$
```

### Spørgsmål c

Brug svarene fra de forrige spørgsmål til at finde den fuldstændige løsning for den reelle differentialligning $f'(t)-3f(t)=t$.

```{admonition} Svar
:class: dropdown
Den ønskede fuldstændige løsning er $f(t)=c \cdot e^{3t}+(-1/3)t+(-1/9)$, hvor $c \in \mathbb{R}.$ Det er lidt enklere at skrive $f(t)=c \cdot e^{3t}-t/3-1/9$, hvor $c \in \mathbb{R}.$
```

+++

----

+++


## Opgave 3: Begyndelsesbetingelser

Den fuldstændige løsning til den reelle differentialligning $f'(t)=e^t \cdot f(t)$ er givet ved $f(t)=c\cdot e^{(e^t)},$ hvor $c \in \mathbb{R}.$

+++

### Spørgsmål a

Tjek ved indsættelse i den givne differentialligning at $f(t)=3\cdot e^{(e^t)}$ er en løsning.

+++

### Spørgsmål b

Find løsningen til den givne differentialligning som opfylder begyndelsesbetingelsen $f(0)=1$. 

```{hint}
:class: dropdown
Fordi den fuldstændige løsning er givet ved $f(t)=c\cdot e^{(e^t)},$ skal man prøve at bestemme en værdi for $c$ således at begyndelsesbetingelsen er opfyldt.
```

```{admonition} Svar
:class: dropdown
Den ønskede løsning er funktionen $f(t)=(1/e)\cdot e^{(e^t)}$, 
som også kan skrives som $f(t)=e^{(-1+e^t)}$. 
```

+++

----

+++

## Opgave 4: Et homogent, reelt system af lineære differentialligninger

Et lineært, reelt differentialligningssystem med konstante koefficienter er givet således:

$$
\left[\begin{array}{c} f_1'(t)\\ f_2'(t)\end{array}\right] = \left[\begin{array}{rr} 1 & 8\\ 1 &-1\end{array}\right] \cdot \left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right].
$$

+++

### Spørgsmål a

Find koefficientmatricens egenværdier og tilhørende egenrum, og opstil ved hjælp heraf den fuldstændige løsning til det givne differentialligningssystem.

```{hint}
:class: dropdown
```

```{admonition} Svar
:class: dropdown
Egenværdierne er $3$ og $-3$. De tilhørende egenrum er 

$$E_3=\mathrm{span}\left(\left[\begin{array}{c} 4\\ 1\end{array}\right]\right) \quad \text{ og } \quad E_{-3}=\mathrm{span}\left(\left[\begin{array}{c} -2\\ 1\end{array}\right]\right).$$

Ifølge Korollar 13.2.4 fra lærebogen er den fuldstændige løsning derfor 

$$\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right]=c_1 \cdot \left[\begin{array}{c} 4\\ 1\end{array}\right]e^{3t}+c_2 \cdot \left[\begin{array}{c} -2\\ 1\end{array}\right]e^{-3t}, \quad \text{ hvor } c_1,c_2 \in \mathbb{R}.$$
```

+++

### Spørgsmål b

Find løsningen til det givne differentialligningssystem som opfylder $f_1(0)=0$ og $f_2(0)=3$.


```{hint}
:class: dropdown
Fra spørgsmål a vides hvordan den fuldstændige løsning ser ud. 
Indsættes $t=0$ i denne fuldstændige løsning, så fås en betingelse som konstanterne $c_1$ og $c_2$ skal opfylde. 
Prøv nu at løse for $c_1$ og $c_2$. 
```

```{admonition} Svar
:class: dropdown
$$\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right]=1 \cdot \left[\begin{array}{c} 4\\ 1\end{array}\right]e^{3t}+2 \cdot \left[\begin{array}{c} -2\\ 1\end{array}\right]e^{-3t}=\left[\begin{array}{c} 4e^{3t}-4e^{-3t}\\ e^{3t}+2e^{-3t}\end{array}\right].$$
```

+++

----

+++


## Opgave 5: Et andet homogent, reelt system af lineære differentialligninger

Givet følgende reelle system af differentialligninger:

$$
\left\{
\begin{array}{rcl} 
f_1'(t) & = & 8f_1(t)+5f_2(t)\\ 
f_2'(t) & = & -10f_1(t)-7f_2(t)
\end{array}
\right.
$$

+++

### Spørgsmål a

Find en matrix $\mathbf A$ og funktioner $q_1(t)$ og $q_2(t)$ således at 

$$
\left[\begin{array}{c} f_1'(t)\\ f_2'(t)\end{array}\right] = {\mathbf A} \cdot \left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right]+\left[\begin{array}{c} q_1(t)\\ q_2(t)\end{array}\right]
$$

Er systemet homogent eller inhomogent?

```{admonition} Svar
:class: dropdown
Det gælder at

$$
\left[\begin{array}{c} f_1'(t)\\ f_2'(t)\end{array}\right] = \left[ \begin{array}{cc} 8 & 5\\ -10 & -7\end{array} \right]\cdot \left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right]
$$

Derfor fås $q_1(t)=0$, $q_2(t)=0$ og

$${\mathbf A}=\left[ \begin{array}{cc} 8 & 5\\ -10 & -7\end{array} \right].$$

Systemet er homogent, fordi både $q_1(t)$ og $q_2(t)$ er nul.
```

+++

### Spørgsmål b

Det oplyses at matricen 

$${\mathbf A}=\left[ \begin{array}{cc} 8 & 5\\ -10 & -7\end{array} \right]$$

har egenværdier $-2$ og $3$ og egenrum

$$E_{-2}=\mathrm{span}\left(\left[\begin{array}{c} -1/2\\ 1\end{array}\right]\right) \quad \text{og} \quad E_{3}=\mathrm{span}\left(\left[\begin{array}{c} -1\\ 1\end{array}\right]\right).$$

Nogen påstår at den fuldstændige løsning til det givne reelle system af differentialligninger er

$$
\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] = c_1\cdot \left[ \begin{array}{c} 1 \\ -2\end{array} \right]\cdot e^{-2t}+c_2\cdot \left[ \begin{array}{c} 1 \\ -1\end{array} \right]\cdot e^{3t}, \quad \text{ hvor } c_1,c_2 \in \mathbb{R}.
$$

Er den påståede fuldstændige løsning korrekt?

%```{hint}
%:class: dropdown
%Indføres matricen som `A` og bruges kommandoen `A.eigenvects()`, så fås det ønskede output. Corollary 12.2.4 kan nu bruges til at finde den ønskede fuldstændige løsning.
%```

```{hint}
:class: dropdown
Bruges Korollar 13.2.4 og de givne oplysninger, så fås at den fuldstændige løsning er 

$$
\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] = c_1\cdot \left[ \begin{array}{c} -1/2 \\ 1\end{array} \right]\cdot e^{-2t}+c_2\cdot \left[ \begin{array}{c} -1 \\ 1\end{array} \right]\cdot e^{3t}, \quad \text{ hvor } c_1,c_2 \in \mathbb{R}.
$$

Udtrykker denne fuldstændige løsning andre løsninger end den påståede fuldstændige løsning når $c_1$ og $c_2$ vælges frit fra $\mathbb{R}$?
```

```{admonition} Svar
:class: dropdown
Ja, den er korrekt (og den givne fuldstændige løsning i vinket er også korrekt). 
En måde at se det på er følgende. 

Fordi $\left[ \begin{array}{c} 1 \\ -2\end{array} \right]=-2\cdot \left[\begin{array}{c} -1/2\\ 1\end{array}\right]$ og 
$\left[ \begin{array}{c} 1 \\ -1\end{array} \right]=-1\cdot\left[ \begin{array}{c} -1 \\ 1\end{array} \right]$, 
medfører de givne oplysninger at $\left[ \begin{array}{c} 1 \\ -2\end{array} \right]$ og $\left[ \begin{array}{c} 1 \\ -1\end{array} \right]$ er 
egenvektorer for $\mathbf A$ med egenværdi $-2$, hhv. $3$.
Derfor er

$$\left( \left[ \begin{array}{c} 1 \\ -2\end{array} \right],\left[ \begin{array}{c} 1 \\ -1\end{array} \right]\right)$$

en ordnet basis for $\mathbb{R}^2$ bestående af egenvektorer for matricen $\mathbf A$. 
Men i så fald giver Korollar 13.2.4 at den påståede fuldstændige løsning er korrekt.
```

+++

----

+++

## Opgave 6: Et inhomogent, reelt system af lineære differentialligninger

Givet følgende reelle system af differentialligninger:

$$
\left\{
\begin{array}{rcl} 
f_1'(t) & = & 8f_1(t)+5f_2(t)+3\\ 
f_2'(t) & = & -10f_1(t)-7f_2(t)+1
\end{array}
\right.
$$

+++

### Spørgsmål a 

Tjek at det tilhørende homogene system af differentialligninger er systemet givet i Opgave 5.

+++

### Spørgsmål b 

Det oplyses at der findes reelle tal $a$ og $b$ således at de konstante funktioner $f_1(t)=a$ og $f_2(t)=b$ danner en partikulær løsning til det givne inhomogene system. 
Beregn nu $a$ og $b$. 

```{hint}
:class: dropdown
Indsæt funktionerne $f_1(t)=a$ og $f_2(t)=b$ i systemet. Hvad skal $a$ og $b$ opfylde?
```

```{hint}
:class: dropdown
Betegnes med ${\mathbf A}$ matricen fra Opgave 5, så fås at $a$ og $b$ skal opfylde 

$$\left[\begin{array}{c} 0\\ 0\end{array}\right]={\mathbf A} \cdot \left[\begin{array}{c} a\\ b\end{array}\right]+\left[\begin{array}{c} 3\\ 1\end{array}\right].$$

${\mathbf A}^{-1}$ beregnes nemmest ved at bruge formlen fra Eksempel 8.1.3 i lærebogen.
```

```{admonition} Svar
:class: dropdown
$a=-13/3$ og $b=19/3$. Ud fra hintet fås for eksempel

$$\left[\begin{array}{c} a\\ b\end{array}\right]={\mathbf A}^{-1}\left[\begin{array}{c} -3\\ -1\end{array}\right]=\frac{1}{-6}\left[ \begin{array}{cc} -7 & -5\\ 10 & 8\end{array} \right]\left[\begin{array}{c} -3\\ -1\end{array}\right]=\frac{1}{6}\left[ \begin{array}{cc} -7 & -5\\ 10 & 8\end{array} \right]\left[\begin{array}{c} 3\\ 1\end{array}\right]=\frac{1}{6}\left[\begin{array}{c} -26\\ 38\end{array}\right]=\left[\begin{array}{c} -13/3\\ 19/3\end{array}\right].$$
```

+++

### Spørgsmål c 

Find den fuldstændige løsning til det givne inhomogene, reelle system af differentialligninger.

```{hint}
:class: dropdown
Definition 13.2.2 og resultaterne fra de forrige spørgsmål kan bruges her.
```

```{admonition} Svar
:class: dropdown
$$
\left[\begin{array}{c} f_1(t)\\ f_2(t)\end{array}\right] = \left[ \begin{array}{c} -13/3 \\ 19/3\end{array} \right]+c_1\cdot \left[ \begin{array}{c} 1 \\ -2\end{array} \right]\cdot e^{-2t}+c_2\cdot \left[ \begin{array}{c} 1 \\ -1\end{array} \right]\cdot e^{3t}, \quad \text{ hvor } c_1,c_2 \in \mathbb{R}.
$$
```

+++

----

+++

## Opgave 7: Begyndelsesbetingelser i et system af lineære differentialligninger

Der betragtes det samme inhomogene, reelle system af differentialligninger som i Opgave 6. 
Beregn løsningen til systemet som opfylder begyndelsesbetingelserne

$$\left[ \begin{array}{c} f_1(0) \\ f_2(0) \end{array} \right]=\left[ \begin{array}{c} 2/3 \\ 1/3\end{array} \right].$$

```{admonition} Svar
:class: dropdown

$$\left[ \begin{array}{c} f_1(t) \\ f_2(t) \end{array} \right]=\left[ \begin{array}{c} -13/3 \\ 19/3\end{array} \right]+1\cdot \left[ \begin{array}{c} 1 \\ -2\end{array} \right]\cdot e^{-2t}+4\cdot \left[ \begin{array}{c} 1 \\ -1\end{array} \right]\cdot e^{3t}=\left[ \begin{array}{c} -13/3+e^{-2t}+4e^{3t} \\ 19/3-2 e^{-2t}-4e^{3t}\end{array} \right].$$
```

+++

----

+++

## Opgave 8: Panserformlen

Givet den reelle differentialligning $f'(t)+f(t)/t=3t.$ Det antages $t>0$. 

+++

### Spørgsmål a

Find differentialligningens fuldstændige løsning.

```{hint}
:class: dropdown
Differentialligningen kan omskrives til $f'(t)=\frac{-1}{t} \cdot f(t)+3t$. 
Derfor kan Sætning 13.1.1 fra lærebogen bruges.
```

```{hint}
:class: dropdown
Det forrige hint medfører at man kan bruge Sætning 13.1.1 med $a(t)=-1/t$ og $q(t)=3t$. 
I Eksempel 13.1.2 fra lærebogen gennemgås et eksempel hvor $a(t)=-1/t$ ligesom her.
```

```{admonition} Svar
:class: dropdown
$f(t)=t^2+c/t$, hvor $c \in \mathbb{R}$.
```

+++

### Spørgsmål b

Find den løsning til differentialligningen som opfylder begyndelsesbetingelsen $f(1)=5$. 

```{admonition} Svar
:class: dropdown
$f(t)=t^2+4/t$.
```

+++

----

+++


## Opgave 9: En drilsk koefficientmatrix

Lad $\lambda$ være et reelt tal og betragt følgende reelle differentialligningssystem: 

$$
\left[\begin{array}{c} f_1'(t)\\ f_2'(t)\\ f_3'(t)\end{array}\right] = \left[\begin{array}{rrr} \lambda & 1 & 0\\ 0 & \lambda &1\\ 0 & 0 & \lambda\end{array}\right] \cdot \left[\begin{array}{c} f_1(t)\\ f_2(t)\\ f_3(t)\end{array}\right].
$$

Hvad er systemets fuldstændige løsning?

```{hint}
:class: dropdown
De sædvanlige metoder virker ikke, fordi koefficientmatricen har én egenværdi $\lambda$, som har algebraisk multiplicitet $3$ og geometrisk multiplicitet $1$. 
Prøv i stedet for at hente inspiration fra Eksempel 13.2.7 i lærebogen.
```

```{hint}
:class: dropdown
At følgende to vektorer er løsninger kan vises på lignende måde some i Eksempel 13.2.7:

$$\left[ \begin{array}{c} f_1(t) \\ f_2(t) \\ f_3(t) \end{array} \right]=\left[ \begin{array}{c} e^{\lambda t}\\ 0 \\ 0\end{array} \right] \quad \text{ og} \left[ \begin{array}{c} f_1(t) \\ f_2(t) \\ f_3(t) \end{array} \right] = \left[ \begin{array}{c} te^{\lambda t} \\ e^{\lambda t} \\ 0\end{array} \right].$$

Der mangler nu én løsning, lineært uafhængigt af de forrige to, til at finde den fuldstændige løsning.
```

```{hint}
:class: dropdown
Prøv at finde en løsning på formen

$$\left[ \begin{array}{c} f_1(t) \\ f_2(t) \\ f_3(t) \end{array} \right]= \left[ \begin{array}{c} at^2e^{\lambda t} \\ te^{\lambda t} \\ e^{\lambda t}\end{array} \right],$$

hvor $a \in \mathbb{R}.$
```

```{admonition} Svar
:class: dropdown

$$\left[ \begin{array}{c} f_1(t) \\ f_2(t) \\ f_3(t) \end{array} \right]=c_1\cdot \left[ \begin{array}{c} e^{\lambda t}\\ 0 \\ 0\end{array} \right]+c_2 \cdot \left[ \begin{array}{c} te^{\lambda t} \\ e^{\lambda t} \\ 0\end{array} \right]+c_3 \cdot \left[ \begin{array}{c} (1/2)t^2 e^{\lambda t} \\ te^{\lambda t}\\ e^{\lambda t}\end{array} \right], \quad \text{ hvor } c_1,c_2,c_3 \in \mathbb{R}.$$
```

+++

----

+++

## Opgave 10: Tematisk Python Opgave

+++

Opgaven frigives kl 15:30 på DTU Learn.
