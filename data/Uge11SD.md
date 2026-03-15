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


(section:uge11S)=

# Opgaver -- Store Dag

----

+++

## Opgave 1: Egenværdier og egenvektorer

Givet matricen 

$${\mathbf A}=\left[\begin{array}{cc} -5 & 10\\ 1 & 4\end{array}\right] \in \mathbb{R}^{2 \times 2}\,.$$

Afgør om følgende vektorer er egenvektorer for matricen $\mathbf A$. Hvis ja, bestem den tilhørende egenværdi.

1. $\left[\begin{array}{c} 1 \\ 2\end{array}\right]$

2. $\left[\begin{array}{c} 1 \\ 1\end{array}\right]$

```{hint}
:class: dropdown
Man kan finde definitionen af en egenvektor i Definition 12.1.1. 
```

```{hint}
:class: dropdown
Undersøg for de givne to vektorer $\mathbf v$ om ${\mathbf A}\cdot {\mathbf v}$ kan skrives som et skalarmultiplum af ${\mathbf v}$.
```

```{admonition} Svar
:class: dropdown
1. Vektoren $\left[\begin{array}{c} 1 \\ 2\end{array}\right]$ er ikke en egenvektor for ${\mathbf A}$.

2. Vektoren $\left[\begin{array}{c} 1 \\ 1\end{array}\right]$ er en egenvektor for ${\mathbf A}$. Den tilhørende egenværdi er $5$.
```


+++

----

+++

## Opgave 2: Reelle egenværdier og egenvektorer

Som i den forrige opgave betragtes matricen

$${\mathbf A}=\left[\begin{array}{cc} -5 & 10\\ 1 & 4\end{array}\right] \in \mathbb{R}^{2 \times 2}\,.$$


+++

### Spørgsmål a

Opstil det karakteriske polynomium for $\mathbf A\,$, og find ved hjælp af dette egenværdierne for $\mathbf A\,$. 
Bestem også deres algebraiske multipliciteter.

```{hint}
:class: dropdown
Det karakteriske polynomium af en $n \times n$ matrix er defineret som $\mathrm{det}({\mathbf A}-Z\cdot {\mathbf I}_n)$. 
Du kan også finde det i lærebogen straks efter Sætningen 12.1.1.
```

```{admonition} Svar
:class: dropdown
Det karakteristiske polynomium er $Z^2+Z-30$. 
Egenværdierne er rødderne i dette polynomium: $5\,$ og $-6$ og man har $Z^2+Z-30=(Z-5)\cdot(Z+6)$. 
Derfor har begge egenværdier algebraisk multiplicitet $1$.
```

+++

### Spørgsmål b

Find egenrummet $E_{-6}$ hørende til egenværdien $-6$. 
Hvad er den geometriske multiplicitet af egenværdien $-6$? 

```{hint}
:class: dropdown
Er $\lambda$ en egenværdi for an matrix $\mathbf A$, så er ifølge Lemma 12.2.3 fra lærebogen egenrummet $E_\lambda$ lig med $\mathrm{ker}({\mathbf A}-\lambda\cdot {\mathbf I}_n)$.
```

```{hint}
:class: dropdown
For at finde $E_{-6}$ kan man bruge en lignende fremgangsmåde som i Eksempel 12.2.1 fra lærebogen. 
Bemærk at den geometriske multiplicitet af en egenværdi er defineret i Definition 12.2.1.
```

```{admonition} Svar
:class: dropdown
Matricen 

$$\left[\begin{array}{cc} -5 & 10\\ 1 & 4\end{array}\right]-\left[\begin{array}{cc} -6 & 0\\ 0 & -6\end{array}\right]\,$$

har reduceret trappeform 

$$\left[\begin{array}{cc} 1 & 10\\ 0 & 0\end{array}\right]\,.$$

Derfor gælder 

$$E_{-6}=\left\{ t \cdot \left[\begin{array}{c} -10 \\ 1\end{array}\right] \, \mid \, t \in \mathbb{R} \right\}.$$ 

Dette viser at vektoren $\left[\begin{array}{c} -10 \\ 1\end{array}\right]$ danner en basis for $E_{-6}$. 
Især kan man konkludere at $\mathrm{dim}(E_{-6})=1$, som er det samme som at sige at egenværdien $-6$ har geometrisk multiplicitet $1$. 
```

+++

### Spørgsmål c

Egenrummet hørende til egenværdien $5$ angives med $E_{5}$. 
Brug svaret fra spørgsmål a og Sætning 12.2.4 til at bestemme $\mathrm{dim}(E_5)$. 
Brug nu resultaterne fra Opgave 1 til at angive en basis for $E_{5}$.

```{hint}
:class: dropdown
Fra spørgsmål a vides at $\mathrm{am}(5)=1$. 
Sætning 12.2.4 fra lærebogen medfører derfor at $\mathrm{gm}(5)=1$.
```

```{admonition} Svar
:class: dropdown
Ifølge Definition 12.2.1 gælder derfor at $\mathrm{dim}(E_5)=\mathrm{gm}(5)$.
Derfor har $E_5$ dimension $1$. 
En basis for $E_5$ indeholder derfor kun én vektor.
Det ses nu at egenvektoren $\left[\begin{array}{c} 1 \\ 1\end{array}\right] \in E_5$ fundet i Opgave 1, danner en basis for $E_{5}$.
```

+++

----

+++

## Opgave 3: Egenværdier og egenvektorer i et uendeligdimensionelt tilfælde

Lad $C_\infty(\mathbb{R})$ være det uendeligdimensionelle, reelle vektorrum nævnt i Eksempel 10.4.5 fra lærebogen. 
Den består af funktioner fra $\mathbb{R}$ til $\mathbb{R}$ som kan differentieres vilkårligt mange gange. 
Der gives følgende lineære afbildning $L: C_\infty(\mathbb{R}) \to C_\infty(\mathbb{R})$ defineret ved $L(f)=f''$. 
Med andre ord: $L$ afbilder en funktion $f \in C_\infty(\mathbb{R})$ til dens andenafledte funktion.

+++

### Spørgsmål a

Afgør om følgende funktioner er egenvektorer for $L$. Hvis ja, bestem den tilhørende egenværdi.

1. $f_1(t)=t^2$

2. $f_2(t)=\cos(t)$

3. $f_3(t)=\sin(t)$

4. $f_4(t)=e^{4 t}$

5. $f_5(t)=te^t$


```{hint}
:class: dropdown
Undersøg for de givne funktioner $f$ om $L(f)$ kan skrives som et skalarmultiplum af $f$. 
Det er nemlig det der skal til for at være en egenvektor, se eventuelt Definition 12.1.1.
```

```{admonition} Svar
:class: dropdown
1. Funktionen $f_1(t)=t^2$ er ikke en egenvektor for $L$. 

2. Bemærk at $\cos(t)''=(-\sin(t))'=-\cos(t)$. 
Funktionen $f_2(t)=\cos(t)$ er derfor en egenvektor for $L$. 
Den tilhørende egenværdi er $-1$.

3. Funktionen $f_3(t)=\sin(t)$ er en egenvektor for $L$. Den tilhørende egenværdi er $-1$.

4. Funktionen $f_4(t)=e^{4t}$ er en egenvektor for $L$. Den tilhørende egenværdi er $16$.

5. Bemærk at $(te^t)''=(e^t+te^t)'=2e^t+te^t$. Funktionen $f_5(t)=te^t$ er derfor ikke en egenvektor for $L$. 


```

+++

----

+++

## Opgave 4: Komplekse egenværdier og egenvektorer

Givet matricen

$${\mathbf A}=\left[\begin{array}{cc} 2 & 2\\ -1 & 4\end{array}\right] \in \mathbb{C}^{2 \times 2}\,.$$

+++

### Spørgsmål a

Opstil det karakteriske polynomium for $\mathbf A\,$, og find ved hjælp af dette egenværdierne for $\mathbf A\,$.

```{hint}
:class: dropdown
Det karakteriske polynomium af en $n \times n$ matrix er defineret som $\mathrm{det}({\mathbf A}-Z\cdot {\mathbf I}_n)$. 
Du kan også finde det i lærebogen lige efter Sætning 12.1.1.
```

```{admonition} Svar
:class: dropdown
Det karakteristiske polynomium er $Z^2-6Z+10$. Egenværdierne er $\,3+i\,$ og $\,3-i\,.$
```

+++

### Spørgsmål b

Find egenrummet $E_{3+i}$ hørende til egenværdien $3+i$. 

```{hint}
:class: dropdown
Beregen først den reducerede trappematrix af matricen

$${\mathbf A}-(3+i){\mathbf I}_2=\left[\begin{array}{cc} 2 & 2\\ -1 & 4\end{array}\right]-(3+i)\left[\begin{array}{cc} 1 & 0\\ 0 & 1\end{array}\right]=\left[\begin{array}{cc} -1-i & 2\\ -1 & 1-i\end{array}\right] \,.$$

```

```{admonition} Svar
:class: dropdown
$E_{3+i}=\mathrm{span}\left( \left[\begin{array}{cc} 1-i\\ 1\end{array}\right]\right)\,.$ 
``` 

+++

### Spørgsmål c

Angiv uden videre beregninger det egenrum der hører til den anden egenværdi. 

```{admonition} Svar
:class: dropdown
Fordi matricen har reelle koefficienter, fås den ene egenvektor/egenrum fra den anden ved at tage den kompleks konjugerede. 
Man har derfor $E_{3-i}=\mathrm{span}\left( \left[\begin{array}{cc} 1+i\\ 1\end{array}\right]\right)\,.$ 
``` 
%
%+++
%
%### Spørgsmål d
%
%Tjek svaret med SymPy-kommandoen `eigenvects()` .
%
%```{hint}
%:class: dropdown
%Hvis `A` er den givne $2 \times 2$ matrix, så giver kommandoen `A.eigenvects()` en liste af to sæt som output. Hver sæt indholder følgende data: først en egenværdi, så dens algebraiske multiplicitet og til sidst en ordnet basis for egenrummet.
%```

+++

----

+++

## Opgave 5: Et pænt basisskift

Der betragtes den samme matrix 

$${\mathbf A}=\left[\begin{array}{cc} 2 & 2\\ -1 & 4\end{array}\right] \in \mathbb{C}^{2 \times 2}\,$$

som i Opgave 4. Lad $\epsilon$ være den ordnede standardbasis for $\mathbb{C}^2$. 
Der defineres en anden ordnet basis for $\mathbb{C}^2$ som følger:

$$\beta = \left( \left[\begin{array}{cc} 1-i\\ 1\end{array}\right], \left[\begin{array}{cc} 1+i\\ 1\end{array}\right] \right).$$

+++

### Spørgsmål a

Beregn basisskiftsmatricen ${}_\epsilon[\mathrm{id}_{\mathbb{C}^2}]_\beta$. 
Beregn bagefter basisskiftsmatricen ${}_\beta[\mathrm{id}_{\mathbb{C}^2}]_\epsilon$.

```{hint}
:class: dropdown
Til den anden del af spørgsmålet kan den tredje del af Lemma 11.3.6 fra lærebogen være nyttigt.
%Følgende ligning kan være nyttigt: ${}_\beta [\mathrm{id}_{\mathbb{C}^2}]_\epsilon = ({}_\epsilon[\mathrm{id}_{\mathbb{C}^2}]_\beta)^{-1}.$
```

+++

### Spørgsmål b

Beregn matricen ${}_\beta [\mathrm{id}_{\mathbb{C}^2}]_\epsilon \cdot {\mathbf A} \cdot {}_\epsilon [\mathrm{id}_{\mathbb{C}^2}]_\beta$. 
Resultatet skulle være en diagonalmatrix. 
Hvordan kunne man have vist det uden beregninger ved at bruge svarene til Opgave 4?

```{hint}
:class: dropdown
Læg mærke til at vektorerne i den ordnede basis $\beta$ er egenvektorerne for matricen $\mathbf A$. Se eventuelt svarene i Opgave 4. 
```

```{hint}
:class: dropdown
Den første søjle i matricen ${}_\beta [\mathrm{id}_{\mathbb{C}^2}]_\epsilon \cdot {\mathbf A} \cdot {}_\epsilon [\mathrm{id}_{\mathbb{C}^2}]_\beta$ er lig med 
${}_\beta [\mathrm{id}_{\mathbb{C}^2}]_\epsilon \cdot {\mathbf A} \cdot {}_\epsilon [\mathrm{id}_{\mathbb{C}^2}]_\beta \cdot \left[\begin{array}{cc} 1\\ 0\end{array}\right]$.
Bemærk nu at søjlevektoren ${}_\epsilon [\mathrm{id}_{\mathbb{C}^2}]_\beta \cdot \left[\begin{array}{cc} 1\\ 0\end{array}\right]=\left[\begin{array}{cc} 1-i\\ 1\end{array}\right]$ er en egenvektorer for matricen $\mathbf A$ med egenværdi $3+i$.
Kan det bruges til at bestemme ${}_\beta [\mathrm{id}_{\mathbb{C}^2}]_\epsilon \cdot {\mathbf A} \cdot {}_\epsilon [\mathrm{id}_{\mathbb{C}^2}]_\beta \cdot \left[\begin{array}{cc} 1\\ 0\end{array}\right]$ uden beregninger?
```

+++

----

+++

## Opgave 6: Egenværdier og egenvektorer for en reel $3 \times 3$ matrix. 

En lineær afbildning $f: \mathbb{R}^3 \to \mathbb{R}^3\,$ mellem reelle vektorrum har med hensyn til den ordnede standardbasis for $\mathbb{R}^3\,$ følgende afbildningsmatrix:

$$
{\mathbf A}=\left[\begin{array}{rrr} 1 & -1 & 1 \\  2 & 4 & -1 \\  0 & 0 & 3 \end{array}\right]\,.
$$

+++

### Spørgsmål a

Bestem det karakteristiske polynomium og find egenværdierne for $f\,$. Angiv egenværdiernes algebraiske multiplicitet. 

```{hint}
:class: dropdown
Det karakteriske polynomium af en lineær afbildning kan beregnes ved at bruge Definition 12.1.3 fra lærebogen. 
Det kan hjælpe at vælge en bekvemt række til udvikling af determinanten nævnt i denne definition og ikke at gange alt helt ud. 
```

```{admonition} Svar
:class: dropdown
Udvikles $\mathrm{det}({\mathbf A}-Z {\mathbf I}_3)$ efter den tredje række, fås det ønskede karakteristiske polynomium på formen:

$$\mathrm{det}({\mathbf A}-Z {\mathbf I}_3)=\mathrm{det}\left( \left[\begin{array}{rrr} 1-Z & -1 & 1 \\  2 & 4-Z & -1 \\  0 & 0 & 3-Z \end{array}\right] \right)=(3-Z) \cdot \left( Z^2-5Z+6 \right).$$

Egenværdierne er $2$, med $ \mathrm{am}(2) = 1$ og $3$, med $ \mathrm{am}(3) = 2$.
```

+++

### Spørgsmål b

Bestem egenrummene som hører til hver af $f$'s egenværdier og angiv egenværdiernes geometriske multiplicitet. 
Er egenværdiernes algebraiske og geometriske multipliciteter det samme?


```{hint}
:class: dropdown
Den geometriske multiplicitet er dimensionen af det egenrum hørende til $\lambda$ (dvs. underrummet, der udspændes af $f$'s egenvektorer med egenværdi $\,\lambda$).
```

```{hint}
:class: dropdown
For at beregne de geometriske multipliciteter skal egenrummene bestemmes. 
Lemma 12.2.3 beskriver hvordan egenrummene for en matrix ser ud.
%Prøv at følge den samme fremgangsmåde som i Eksempel 12.2.1 fra lærebogen. 
```

```{admonition} Svar
:class: dropdown
En mulig ordnet basis for egenrummet $E_2=\mathrm{ker}({\mathbf A}-2{\mathbf I}_3)\,$ er 

$$\left(\, \left[ \begin{array}{r} -1 \\ 1\\ 0 \end{array}\right]\,\right)\,.$$ 

Derfor gælder $\mathrm{gm}(2) = 1$ som er det samme som egenværdiens algebraiske multiplicitet.

En mulig ordnet basis for egenrummet $E_3=\mathrm{ker}({\mathbf A}-3{\mathbf I}_3)\,$ er 

$$\left(  \left[ \begin{array}{r} 1/2 \\ 0\\ 1 \end{array}\right], \left[ \begin{array}{r} -1/2 \\ 1\\ 0 \end{array}\right] \,\right)\,.$$ 

Derfor gælder $\mathrm{gm}(3) = 2$ som igen er det samme som egenværdiens algebraiske multiplicitet.
```

+++

----

+++

## Opgave 7: Egenværdier og deres multipliciteter for en anden reel $3 \times 3$ matrix.

Vi betragter nu matricen

$$
{\mathbf B}=\left[\begin{array}{rrr} 1 & 1 & 0 \\  2 & -1 & -1\\  0 & 2 & 1 \end{array}\right]\,.
$$

Det oplyses at det karakteristiske polynomium for matricen ${\mathbf B}$ er $(1-Z)\cdot (Z+1) \cdot (Z-1)$.

+++

### Spørgsmål a

Find egenværdierne for $\mathbf B$ og angiv deres algebraiske multipliciteter. 

```{admonition} Svar
:class: dropdown
Egenværdierne er $1$, med $\mathrm{am}(1)=2$ og $-1$, med $\mathrm{am}(-1) = 1$.
```

+++

### Spørgsmål b 

Angiv egenværdiernes geometriske multipliciteter. 
Er egenværdiernes algebraiske og geometriske multipliciteter det samme?

```{hint}
:class: dropdown
Overvej først hvorfor Sætning 12.2.4 medfører følgende: hvis en egenværdi har algebraisk multiplicitet $1$, så er dens geometriske multiplicitet også $1$.
```

```{admonition} Svar
:class: dropdown

Som forklaret i hinten, medfører $\mathrm{am}(\lambda)=1$ at $\mathrm{gm}(\lambda)=1$. 
Derfor fås uden yderligere beregninger at $\mathrm{gm}(-1) = \mathrm{am}(-1) = 1$. 
%En mulig ordnet basis for $E_{-1}\,$ er 
%$$ \left[ \begin{array}{r} 1/2 \\ -1\\ 1 \end{array}\right]\,.$$ 

Det samme trick kan ikke bruges for egenværdien $1$, fordi $\mathrm{am}(1)=2$.
Beregnes egenrummet $E_{1}\,$ så fås at den er udspændt af vektoren

$$\left[ \begin{array}{r} 1/2 \\ 0\\ 1 \end{array}\right]\, .$$

Derfor gælder $\mathrm{gm}(1) = 1$, som er strengt mindre end egenværdiens algebraiske multiplicitet (som var $2$).
```

+++

----

+++


## Opgave 8: Det karakteristiske polynomium for en $2 \times 2$ matrix

Lad $\mathbb{F}$ være et legeme og $a,b,c,d$ elementer i $\mathbb{F}$. Der betragtes matricen 

$${\mathbf A}=\left[ \begin{array}{r} a & b\\ c & d\end{array}\right].$$

+++

### Spørgsmål a

Vis at matricen $\mathbf A$ har karakteristisk polynomium $Z^2-(a+d)Z+\mathrm{det}({\mathbf A})$. Bemærkning: udtrykket $a+d$ kalder man for matricens spor (på engelsk "trace") og betegnes ved $\mathrm{tr}({\mathbf A})$.

+++

### Spørgsmål b

Antag at matricen ${\mathbf A}$ har egenværdier $\lambda_1$ og $\lambda_2$. Brug det forrige spørgsmål til at indse at $\lambda_1+\lambda_2=\mathrm{tr}({\mathbf A})$ og $\lambda_1 \cdot \lambda_2=\mathrm{det}({\mathbf A})$.

```{hint}
:class: dropdown
Hvis en $2 \times 2$ matrix ${\mathbf A}$ har egenværdier $\lambda_1$ og $\lambda_2$, så gælder at matricens karakteristiske polynomium er $(Z-\lambda_1)\cdot (Z-\lambda_2).$
```

```{admonition} Svar
:class: dropdown
På den ene side er $p_{\mathbf A}(Z)=Z^2-\mathrm{tr}({\mathbf A})Z+\mathrm{det}({\mathbf A})$, på den anden side gælder $p_{\mathbf A}(Z)=(Z-\lambda_1)\cdot (Z-\lambda_2)=Z^2-(\lambda_1+\lambda_2)Z+\lambda_1\cdot \lambda_2$. Sammenlignes koefficienterne, så fås det ønskede.
```

+++

----

+++


## Opgave 9: Lineær uafhængighed af to egenvektorer

Der gives en matrix ${\mathbf A} \in \mathbb{C}^{2 \times 2}$ og to af dens egenvektorer ${\mathbf v}_1,{\mathbf v}_2 \in \mathbb{C}^2$. Antag at de tilhørende egenværdier $\lambda_1,\lambda_2$ er forskellige. Vis at ${\mathbf v}_1$ og ${\mathbf v}_2$ er lineært uafhængige.

```{hint}
:class: dropdown
Hvis ${\mathbf v}_1$ og ${\mathbf v}_2$ er lineært afhængige, så findes to komplekse tal $c_1$ og $c_2$, ikke begge to lige med nul, således at 

$$c_1\cdot {\mathbf v}_1+c_2\cdot {\mathbf v}_2=\left[ \begin{array}{r} 0 \\ 0\end{array}\right].$$
```

```{hint}
:class: dropdown
Fra forrige hint følger at hvis to vektorer er lineært afhængige, så er en af dem et skalarmultiplum af den anden. Kan det lade sig gøre hvis de to vektorer er egenvektorer for den samme matrix ${\mathbf A}$ men med forskellige egenværdier? 
```

## Bemærkning

Der åbnes en Möbius test om forrige ugens Pythonopgave kl. 15:30