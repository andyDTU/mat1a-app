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

(section:uge2L)=

# Opgaver -- Lille Dag

%## Opgave 1: Python opgave
%
%Den opgave omhandler formlen fra Opgave 2c fra denne uges store dag.
%
%Du kan bruge command console Python på din computer til at køre følgende program. Brug endelig Copy-Paste for at få Pythonkoden over i command consolen.
%
%
%### Spørgsmål a
%
%+++
%
%En mængde på formen $\{1,2,3\}$ kan indføres i Python ved at skrive følgende i command consolen `{1,2,3}`. Som forklaret i starten af Afsnit 2.1 fra lærebogen, er rækkefølgen at elementerne ikke vigtig i en mængde. Hvordan kan man checke i Python at for eksempel $\{1,2,3\}=\{1,3,2\}$? Gentagelse af elementer i en mængde ændrer ikke på mængden. Man har for eksempel $\{1,1,2\}=\{1,2\}$. Prøv at checke denne identitet i Python.
%
%```{hint}
%:class: dropdown
%To mængder $A$ og $B$ er lige med hinanden præcist hvis ligningen $A=B$ er sand. I sidste uger (Lille Dag, Opgave 2a og 2c) har vi dog allerede set hvordan man checker om to ting er lige med hinanden i Python.
%```
%
%```{hint}
%:class: dropdown
%Hvad sker der hvis man skrive `{1,2,3} == {1,3,2}` i Python?
%```
%
%
%### Spørgsmål b
%
%+++
%
%Kør følgende Python kode:
%
%`A={9, 12, 15, 21, 24, 27, 30, 33, 36, 42, 48, 51, 54, 57, 60, 63, 66, 69, 72, 78, 81, 84, 87, 90, 93, 96}`
%
%`B={12, 16, 24, 28, 32, 36, 48, 52, 56, 60, 64, 68, 72, 80, 84, 88, 92, 96}`
%
%`len(A)`
%
%`len(B)`
%
%Hvad er betydning af kommandoet `len`?
%
%```{admonition} Svar
%:class: dropdown
%`len(A)` giver antallet af elementer i mængden $A$. I Opgave 2c fra denne uges store dag blev dette antal betegnet med $|A|$.
%```
%
%
%### Spørgsmål c
%
%Foreningsmængde og fællesmængde af to mængder $A$ og $B$ kan beregnes i Python som `A.union(B)` og `A.intersection(B)`
%
%Afprøv kommandoerne på de to mængder $A$ og $B$ fra spørgsmål a.
%
%### Spørgsmål d
%
%Tjek nu ved hjælp af Python at formlen $|A \cup B|=|A|+|B|-|A \cap B|$ holder for de to mængder fra spørgsmål a.
%
%```{admonition} Svar
%:class: dropdown
%Man kan køre kommandoen `len(A.union(B))==len(A)+len(B)-len(A.intersection(B))`. Udkomsten er `True`, så formlen passer! 
%```
%
%
%### Spørgsmål e
%
%+++
%
%Vi introducerer nu en ny mængde C
%
%`C={6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96}`
%
%Prøv at formulere en identitet om $|A \cup B \cup C|$, nu altså med tre mængder $A$, $B$ og $C$ frem for to som før. Man kan afprøve med Python om man har fundet en formel der passer.
%
%----
%
%## Opgave 2: Sammensatte funktioner
%
%Givet er mængden $A=\{0,1,2\}$, samt to funktioner $f: A \to A$ og $g: A \to \mathbb{R}$. Funktionen $f$ har forskrift $f(x)=2-x$, mens funktionen $g$ har forskrift $g(x)=2x+e^x$.
%
%### Spørgsmål a
%
%+++
%
%Er den sammensatte funktion $f \circ g$ defineret? Hvad med $g \circ f$?
%
%```{hint}
%:class: dropdown
%I lærebogen, straks efter Example 2.2.2, kan du læse om hvad der skal til for at kunne sammensætte to funktioner.
%```
%
%```{admonition} Svar
%:class: dropdown
%$f \circ g$ er ikke defineret, fordi $g$'s dispositionsmængde er $\mathbb{R}$, som ikke er $f$'s definitionsmængde (den er nemlig $A$).
%
%$g \circ f$ er defineret, fordi $f$'s dispositionsmængde er det samme som $g$'s definitionsmængde (nemlig $A$).
%
%Bemærk at man ikke behøver at kende forskrifterne for to funktioner for at kunne afgøre om deres sammensætning er defineret. Kun at vide deres definitions- og dispositionsmængderne er tiltrækkeligt til afgørelsen.
%```
%### Spørgsmål b
%
%+++
%
%Beregn $(g\circ f)(a)$ for alle $a \in A$.
%
%```{admonition} Svar
%:class: dropdown
%$(g \circ f)(0)=4+e^2$, $(g \circ f)(1)=2+e$ og $(g \circ f)(2)=1$. 
%
%Mellemregning til det sidste svar: 
%
%$$(g \circ f)(2)=g(f(2))=g(2-2)=g(0)=2\cdot 0 +e^0=0+1=1.$$
%```
%
%### Spørgsmål c
%
%+++
%Bestem forskrift, definitionsmængde, dispositionsmængde og værdimængde af funktionen $g \circ f$.
%
%```{hint}
%:class: dropdown
%Værdimængden kan bestemmes ud fra svar til spørgsmål b. Definitionsmængde og dispositionsmængde kan bestemmes ud fra definitionen af en sammensat funktion.
%```
%
%```{admonition} Svar
%:class: dropdown
%Forskrift: $(g \circ f)(x)=2(2-x)+e^{2-x}$ (eller helst lidt pænere $(g \circ f)(x)=4-2x+e^{2-x}$).
%
%Værdimængde: $\{4+e^2,2+e,1\}$ (det er også fint at ordne tallene efter størrelse og give som svar $\{1,2+e,4+e^2\}$).
%
%Definitionsmængde: $A$, dvs. $\{0,1,2\}$.
%
%Dispositionsmængde: $\mathbb R$.
%```
%
%### Spørgsmål d
%
%+++
%
%Er funktionen $g \circ f$ injektiv? Hvad med surjektiv?
%
%```{admonition} Svar
%:class: dropdown
%Injektiv: ja. Surjektiv: nej.
%```
%----

## Opgave 1: Omvendte funktioner: eksponentialfunktionen og den naturlige logaritme

Givet en bijektive funktion $f: A \to B$, så betegnes den inverse funktion, også kaldt omvendt funktion, som $f^{-1}: B \to A$ (se Definition 2.2.1 fra lærebogen). 
Den naturlige logaritme $\mathrm{ln}$ indføres i Eksempel 2.3.2 som den omvendte funktion til eksponentialfunktionen $\mathrm{exp}: \mathbb{R} \to \mathbb{R}_{>0}$ givet ved forskriften $x\mapsto e^x.$

### Spørgsmål a

+++

Angiv definitionsmængde, dispositionsmængde og værdimængde af $\mathrm{ln}$.

```{admonition} Svar
:class: dropdown
Definitionsmængde: $\mathbb{R}_{>0}$.

Dispositionsmængde: $\mathbb{R}$.

Værdimængde: $\mathbb{R}$.
```

### Spørgsmål b

+++

Angiv forskrift, definitionsmængde, dispositionsmængde og værdimængde af de sammensatte funktioner $\mathrm{ln} \circ \mathrm{exp}$ og $\mathrm{exp} \circ \mathrm{ln}$.

```{hint}
:class: dropdown
Hvis du er i tvivl hvad notationen $g \circ f$ præcist betyder, se forklaring i lærebogen straks efter Eksempel 2.2.2. 
Hvis du vil læse om definitionen af en omvendt funktion, se Definition 2.2.1.
```

```{admonition} Svar
:class: dropdown
Fra Definition 2.2.1, fås at $\mathrm{ln} \circ \mathrm{exp}=\mathrm{id}_{\mathbb R}$ og $\mathrm{exp} \circ \mathrm{ln}=\mathrm{id}_{\mathbb{R}_{>0}}$. 
Derfor gælder følgende:

$\mathrm{ln} \circ \mathrm{exp}$ har forskrift $x \mapsto x$ (dvs. $\mathrm{ln}(e^x)=x$), definitionsmængde $\mathbb R$, dispositionsmængde $\mathbb R$ og værdimængde $\mathbb R$.

$\mathrm{exp} \circ \mathrm{ln}$ har forskrift $x \mapsto x$ (dvs. $e^{\mathrm{ln}(x)}=x$), definitionsmængde $\mathbb R_{>0}$, dispositionsmængde $\mathbb R_{>0}$ og værdimængde $\mathbb R_{>0}$.
```

### Spørgsmål c

+++

Bevis regnereglen

$$\ln(a\cdot b)=\ln(a)+\ln(b)$$

hvor $a$ og $b$ er positive reelle tal (dvs. $a,b \in \mathbb{R}_{>0}$). Du må bruge at $e^x \cdot e^y=e^{x+y}$ for alle reelle tal $x$ og $y$.

```{hint}
:class: dropdown
Som skrevet må du bruge at $e^x \cdot e^y=e^{x+y}$ for alle reelle tal $x$ og $y$. 
Hvad sker der hvis man vælger $x=\ln(a)$ og $y=\ln(b)$?
```

```{hint}
:class: dropdown
Fra det forrige hint fås $a \cdot b = e^{\ln(a)+\ln(b)}$. Brug nu at logaritmefunktionen $\ln$ er den inverse funktion til eksponentialfunktionen.
```
----

## Opgave 2: Rekursivt definerede funktioner

### Spørgsmål a

+++

En funktion $f: \mathbb{N} \to \mathbb{R}$ bliver defineret rekursivt som følger: $f(1)=0$ og $f(n)=2\cdot f(n-1)+1$ hvis $n \ge 2$.
Beregn $f(5)$.

```{hint}
:class: dropdown
Beregn først $f(2)$. Kan du bruge værdien $f(2)$ til at bestemme endnu en værdi af funktionen $f$?
```

```{admonition} Svar
:class: dropdown
$f(5)=15$ (undervejs i beregningen vil man også have fået at $f(2)=1$, $f(3)=3$ og $f(4)=7$). 
```

### Spørgsmål b

+++

En funktion $g: \mathbb{N} \to \mathbb{R}$ bliver defineret rekursivt som følger: $g(1)=3$, $g(2)=1$ og $g(n)=n\cdot g(n-1)+g(n-2)$ hvis $n \ge 3$.
Beregn $g(6)$.

```{hint}
:class: dropdown
For at bestemme $g(n)$ vha rekursionen bruges ikke kun $g(n-1)$, men også $g(n-2)$. 
Læs eventuelt først den rekursive definition af Fibonacci-tallene i Eksempel 3.1.2 i lærebogen hvis du vil se et andet eksempel hvor det sker.
```

```{hint}
:class: dropdown
Værdierne $g(1)$ og $g(2)$ er kendte direkte fra den rekursive definition. 
Prøv derfor Derfor kan man beregne $g(3)$ ud fra den rekursive definition. 
Den giver nemlig formlen $g(3)=3g(2)+g(1)$ for $n=3$. Bagefter kan $g(4)$ beregnes, så $g(5)$ osv.
```

```{admonition} Svar
:class: dropdown
$g(6)=811$ (undervejs i beregningen vil man også have fået at $g(3)=6$, $g(4)=25$ og $g(5)=131$). 
```

### Spørgsmål c

+++

En funktion $h: \mathbb{N} \to \mathbb{R}$ forsøges at blive defineret rekursivt som følger: $h(1)=11$ og $h(n)=h(n^2-5n+7)$ hvis $n \ge 2$.
Beregn $h(4)$. Kan $h(5)$ også beregnes?

```{hint}
:class: dropdown
Angående værdien af $h(4)$: den rekursive definition giver $h(4)=h(3)$. Prøv derfor at bestemme værdien af $h(3)$.
```

```{admonition} Svar
:class: dropdown
$h(4)=11$.

Hvis man prøver at beregne $h(5)$, fås

$$h(5)=h(7)=h(21)=h(343)=\cdots .$$

Man ser derfor at i hvert iteration, rekursionen kalder sig selv for en større inputværdi end før. 
Derfor afslutter rekursionen aldrig og kan $h(5)$ ikke beregnes.
```

----

## Opgave 3: Priknotationen og sumtegnet

Givet et naturligt tal $n$ og reelle tal $a_1,\dots,a_n$, så betegnes summen af disse reellee tal med $a_1+\cdots+a_n$ eller nogle gange også med $a_1+a_2+\cdots+a_n$. I denne opgave undersøges nogle eksempler.

+++

### Spørgsmål a

Der defineres $a_k=2k$ for $k=1,2,3,4$. Hvad er $a_1+\cdots+a_n$ hvis $n=4$? Og hvad hvis $n=3$?

```{admonition} Svar
:class: dropdown
$n=4$: $a_1+a_2+a_3+a_4=2+4+6+8=20$.

$n=3$: $a_1+a_2+a_3=2+4+6=12$.
```

+++

### Spørgsmål b

Det samme spørgsmål, men nu for $n=2$ og for $n=1$.

```{admonition} Svar
:class: dropdown
$n=2$: $a_1+a_2=2+4=6$. Det vil sige at "prikkerne" egentlig bare skal ignoreres i notation $a_1+\cdots+a_n$ hvis $n=2$.

$n=1$: Nu er svaret blot $a_1=2$. Det vil sige at notation $a_1+\cdots+a_n$ for $n=1$ kan være lidt misvisende, fordi man egentlig ikke har en sum med flere led, men blot leddet $a_1$. Dette er en af grundene at nogle foretrække at bruge sumtegn-notationen ($\sum$-notationen).
```

+++

### Spørgsmål c

Dette delspørgsmål handler om sumtegnet (notation: $\sum$). Beregn $\sum_{k=1}^4 k^2$. Hvad er $\sum_{k=1}^1 k^2$?

```{hint}
:class: dropdown
Sumtegnet blev defineret rekursivt i Ligning (3.5) i lærebogen. 
```

```{admonition} Svar
:class: dropdown
$\sum_{k=1}^4 k^2=1^2+2^2+3^2+4^2=30.$

$\sum_{k=1}^1 k^2=1^2=1.$
```

----

## Opgave 4: Graf af en invertibel funktion


### Spørgsmål a

+++

Skitser grafer til eksponential og logaritme funktionen fra Eksempel 2.3.2 i den samme figur. 
Er der en symmetri mellem disse to grafer? 

Hvad skyldes symmetrien?


```{admonition} Svar
:class: dropdown
Symmetrien er spejling i linjen $y=x$. Grunden af symmetrien er at $e^x=y$ hvis og kun hvis $x=\ln(y).$ 

Helt generelt, hvis $f: A \to B$ er en invertibel funktion og $x \in A$, $y \in B$, så gælder at $f(x)=y$ hvis og kun hvis $x=f^{-1}(y)$. 
Symmetrien giver derfor mening: hvis man spejler punktet $(x,f(x))$ på $f$'s graf, fås punktet $(f(x),x)$. 
Hvis vi nu betegner $f(x)$ med $y$ (dvs. $y=f(x)$), så fås $(f(x),x)=(y,f^{-1}(y)),$ som netop er et punkt på $f^{-1}$'s graf. 
Omvendt kan ses at hvis vi spejler et punkt på $f^{-1}$'s graf, så fås et punkt på $f$'s graf.
```

----

## Opgave 5: Logaritmer

Lad $a$ være et positivt reelt tal forskelligt fra $1$: Funktionen $f: \mathbb R \to \mathbb R_{>0}$ er givet ved forskriften $x \mapsto a^x$.

### Spørgsmål a

+++

Lav en skitse af funktionens graf hvis $a \in ]0,1[$. Er $f$ monoton? Mere præcist, er $f$ strengt voksende eller strengt aftagende? 

```{hint}
:class: dropdown
Hvis du er i tvivl om hvad ordene "monoton", "strengt voksende (på engelsk: strictly increasing)" og "strengt aftagende (på engelsk: strictly decreasing)" betyder, så kan du finde en forklaring i teksten straks efter Lemma 2.3.1 i lærebogen.
```

```{admonition} Svar
:class: dropdown
Funktionen $f$ er monoton. Mere præcist, den er strengt aftagende.
```

### Spørgsmål b

+++

Lav igen en skitse af funktionens graf, men nu under antagelse at $a \in \mathbb{R}_{>1}$. 
Er $f$ strengt voksende eller strengt aftagende? 

```{admonition} Svar
:class: dropdown
Funktionen $f$ er strengt voksende. 
```

### Spørgsmål c

+++

Man kan vise at funktionen $f$ er bijektiv, som betyder at $f$ har en inverse funktion. 
Giv en forskrift af den inverse funktion til $f$.

```{hint}
:class: dropdown
Prøve at løse for $x$ i ligningen $y=a^x$. 
Formlen $a=e^{\ln(a)}$ kan være behjælpsom, samt regnereglen at $(u^v)^w=u^{vw}$ for alle $u \in \mathbb R_{>0}$ og alle $v,w \in \mathbb R$.
```

```{admonition} Svar
:class: dropdown
$f^{-1}(x)=\ln(x)/\ln(a).$ 
Bemærkning: man skriver som regel $\log_a$ til at angive denne inverse funktion og kalder den logaritmen med base $a$. 
Hyppigt brugte logaritme-funktioner (udover $\ln$) er $\log_2$ og $\log_{10}$.  
```

%----
%
%## Opgave 6: Hældning og inverser
%
%I denne opgave må man bruge at hvis man spejler en linje i planen med hældningskoefficient $r \in \mathbb{R}\setminus \{0\}$ i linjen $y=x$, så fås en linje med hældningskoefficient $1/r$. Vi betragter en invertibel funktion $f: \mathbb R \to \mathbb R$.
%
%### Spørgsmål a
%
%+++
%
%Brug resultatet beskrivet i svaret til Opgave 5 til af indse grafisk at hvis grafen til $f$ har en tangentlinje gennem $(x,f(x))$ med hældningskoefficient $r \in \mathbb{R}\setminus \{0\}$, så har grafen til $f^{-1}$ en tangentlinje gennem $(f(x),x)$ med hældningskoefficient $1/r$.
%
%### Spørgsmål b
%
%+++
%
%Konkluder at hvis $f$ har en afledte $f'(x)$ i $x$, så gælder at den afledte af $f^{-1}$ i $f(x)$ er lige med $1/f'(x)$. Med andre ord: 
%
%$$(f^{-1})'(f(x))=1/f'(x).$$
%
%### Spørgsmål c
%
%+++
%
%Ved at skifte variablen $x$ ud med $f^{-1}(x)$, omskriv formlen fra spørgsmål b til $(f^{-1})'(x)=1/f'(f^{-1}(x)).$
%
%### Spørgsmål d
%
%+++
%
%Brug nu formlen fra spørgsmål c, til at indse at $\mathrm{arctan}'(x)=1/\tan'(\mathrm{arctan}(x))$. 
%
%### Spørgsmål e
%
%+++
%
%Brug formlen $\tan'(x)=\tan^2(x)+1$ til at nå frem til formlen 
%
%$$\mathrm{arctan}'(x)=1/(x^2+1).$$
%
%Bemærkning: en lignende fremgangsmåde giver anledning til formlerne:
%
%$$\mathrm{arccos}'(x)=-1/\sqrt{1-x^2}$$
%
%og
%
%$$\mathrm{arcsin}'(x)=1/\sqrt{1-x^2}.$$
%