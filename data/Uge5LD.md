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

(section:uge5L)=

# Opgaver -- Lille Dag


%## Opgave 1: Python opgave
%
%Rekursive definitioner kan i den grad bruges til at lave computerberegninger. I denne opgave gives nogle eksempler på det.
%
%+++
%
%### Spørgsmål a
%
%+++
%
%Fakultetsfunktionen blev defineret i Example 5.1.1 fra lærebogen. Især blev der givet en rekursiv definition i Ligning (5.1) og en pseudokode beskrivelse i starten af eksempet (Algorithm 8). Om nødvendigt, genopfrisk din hukommelse, især hvad angår pseudokoden. Følgende Pythonkoden er en direkte "oversættelse" til Python af pseudokoden fra Algorithm 8 i lærebogen.
%
%```{code-cell} ipython3
%def fac(n):
%    if n == 1: # This is the base case
%        return 1
%    else: # This is the recursive case
%        return(fac(n-1)*n)
%
%  
%```
%
%Kopier Pythonkoden ved at klikke i det grå tekstfelt øverst til høje. Indsæt bagefter teksten i command console Python. Afprøv nu kommandoen `fac(5)`. Giver det resultatet du forventer? Hvad med `fac(500)` og `fac(1000)`?
%
%```{admonition} Trouble shooting
%:class: dropdown
%Hvis af en eller anden grund prompten i command consolen ser ud som `...` efter man har indført Pythonkoden, tryk på Enter-knappen indtil prompten skifter udseende til `>>>`. Nu burde man kunne indtaste kommandoen `fac(5)`.
%```
%
%```{admonition} Svar
%:class: dropdown
%`fac(5)` og `fac(500)` giver de rigtige svar.
%
%`fac(1000)` giver dog som regel en fejlmelding, fordi funktionen kalder sig selv for mange gange. Matematisk set er der ikke noget galt, men alle computersystemer har deres grænser. Her opdager man at der er en grænse for hvor mange gange en funktion må kalde sig selv rekursivt i Python. Standard Python har en såkaldt rekursionsdybde på 1000.
%```
%
%### Spørgsmål b
%
%For at afprøve rekursive definitioner yderligere, skriver nogen følgende Python kode for at definere en funktion $h: \mathbb{N} \to \mathbb{R}$ rekursivt:
%
%```{code-cell} ipython3
%def h(n):
%    if n == 1: # This is the base case
%        return 11
%    else: # This is the recursive case
%        return(h(n**2-5*n+7))
%
%```
%
%Kopier koden ind i command console Python og kør kommandoerne `h(1)`, `h(2)`, `h(3)` og `h(4)`. Check i hånden at outputtet er hvad det skulle være.
%
%+++
%
%### Spørgsmål c
%
%+++
%
%Prøv nu at beregne $h(5)$ i hånden. Hvad er problemet? Afprøv alligevel kommandoen `h(5)` i Python, men husk at man kan afbryde Pythonprogrammet med Ctrl-c (dvs. tryk på Ctrl knappen, hold den indtrykket, mens man trykker på c knappen). 
%
%
%```{hint}
%:class: dropdown
%Der et lignende problem med den rekursive definition af funktionen $g$ lige inden Example 5.1.2 i lærebogen. 
%```
%
%```{admonition} Svar
%:class: dropdown
%Hvis man prøver at beregne $h(5)$ i hånden, fås
%
%$$h(5)=h(7)=h(21)=h(343)=\cdots .$$
%
%Man ser derfor at i hvert iteration, $h$ kalder sig selv for en større inputværdi end før. Derfor afslutter rekursionen aldrig.
%```
%
%----
%
%+++
%
%## Opgave 2: Rekursioner af dybde to.
%
%+++
%
%### Spørgsmål a
%
%+++
%
%En følge af tal $c_1,c_2,c_3,\dots$ er defineret som følger:
%
%$c_1=3$, $c_2=1$ og $c_{n}=n\cdot c_{n-1}+c_{n-2}$ hvis $n \ge 3$.
%
%Beregn i hånden $c_6$.
%
%```{hint}
%:class: dropdown
%Læs eventuelt først den rekursive definition af Fibonacci-tallene i Example 5.1.2 i lærebogen.
%```
%
%```{hint}
%:class: dropdown
%Tallene $c_1$ og $c_2$ er kendte. Derfor kan man beregne $c_3$ ud fra den rekursive definition. Den giver nemlig formlen $c_3=3c_2+c_1$ for $n=3$. Bagefter kan $c_4$ beregnes, så $c_5$ osv.
%```
%
%```{admonition} Svar
%:class: dropdown
%$c_6=811$ (undervejs i beregningen vil man også have fået at $c_3=6$, $c_4=25$ og $c_5=131$). 
%```
%
%+++
%
%### Spørgsmål b
%
%+++
%
%En anden følge af tal $d_1,d_2,d_3,\dots$ er defineret som følger:
%
%$d_1=1$, $d_2=2$ og $d_{n}=d_{n-1}d_{n-2}-n+1$ hvis $n \ge 3$.
%
%Tjek at $d_6=7$.
%
%```{hint}
%:class: dropdown
%Ligesom i spørgsmål a er det en god strategi at beregne $d_3$ først, så $d_4$, osv. 
%```
%
%```{hint}
%:class: dropdown
%Rekursionen giver at $d_3=d_2d_1-3+1$, $d_4=d_3d_2-4+1$, osv. 
%```
%
%```{admonition} Svar
%:class: dropdown
%Mens man regner, vil man få at $d_3=0$, $d_4=-3$, $d_5=-4$ og til sidst $d_6=7$. 
%```
%
%----
%
%+++
%
%## Opgave 3: Priknotation
%
%Givet et naturligt tal $n$ og komplekse tal $a_1,\dots,a_n$, så betegnes summen af disse komplekse tal med $a_1+\cdots+a_n$ eller nogle gange også med $a_1+a_2+\cdots+a_n$. I denne opgave undersøges nogle eksempler.
%
%+++
%
%### Spørgsmål a
%
%Der defineres $a_k=2k$ for $k=1,2,3,4$. Hvad er $a_1+\cdots+a_n$ hvis $n=4$? Og hvad hvis $n=3$?
%
%```{admonition} Svar
%:class: dropdown
%$n=4$: $a_1+a_2+a_3+a_4=2+4+6+8=20$.
%
%$n=3$: $a_1+a_2+a_3=2+4+6=12$.
%```
%
%+++
%
%### Spørgsmål b
%
%Det samme spørgsmål, men nu for $n=2$ og for $n=1$.
%
%```{admonition} Svar
%:class: dropdown
%$n=2$: $a_1+a_2=2+4=6$. Det vil sige at "prikkerne" egentlig bare skal ignoreres i notation $a_1+\cdots+a_n$ hvis $n=2$.
%
%$n=1$: Nu er svaret blot $a_1=2$. Det vil sige at notation $a_1+\cdots+a_n$ for $n=1$ kan være lidt misvisende, fordi man egentlig ikke har en sum med flere led, men blot leddet $a_1$. Dette er en af grundene at nogle foretrække at bruge sumtegn-notationen ($\sum$-notationen).
%```
%
%+++
%
%### Spørgsmål c
%
%Betragt funktionen $f: \mathbb{N} \to \mathbb{C}$ med forskrift $f(k)=k^2-k$. Beregn $f(1)+\cdots + f(n)$ for $n=1,2,3$ og $4$.
%
%```{admonition} Svar
%:class: dropdown
%$n=1$: $f(1)=0$.
%
%$n=2$: $f(1)+f(2)=0+2=2$.
%
%$n=3$: $f(1)+f(2)+f(3)=2+f(3)=2+6=8$.
%
%$n=4$: $f(1)+f(2)+f(3)+f(4)=8+f(4)=8+12=20$.
%```
%
%----
%
%+++
%
%## Opgave 4: Sumtegnet
%
%Sumtegnet blev defineret rekursivt i Ligning (5.5) i lærebogen. Dette spørgsmål handler om sumtegnet.
%
%+++
%
%### Spørgsmål a
%
%+++
%
%Beregn $\sum_{k=1}^4 k^2$. Hvad er $\sum_{k=1}^1 k^2$?
%
%```{admonition} Svar
%:class: dropdown
%$\sum_{k=1}^4 k^2=1^2+2^2+3^2+4^2=30.$
%
%$\sum_{k=1}^1 k^2=1^2=1.$
%```
%+++
%
%### Spørgsmål b
%
%+++
%
%Vi skriver $k!$ for $k$ facultet i denne opgave og benytter også den sædvanlige definition $0!=1$.
%
%Beregn $\sum_{k=0}^4 1/k!$.
%
%```{admonition} Svar
%:class: dropdown
%$\sum_{k=0}^4 k^2=\frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\frac{1}{3!}+\frac{1}{4!}=\frac{1}{1}+\frac{1}{1}+\frac{1}{2}+\frac{1}{6}+\frac{1}{24}=\frac{65}{24}.$
%
%Bemærkning: det kan vises at summen $\sum_{k=0}^n 1/k!$ går mod tallet $e$, hvis $n$ går mod uendelig. 
%```
%
%----
%
%+++
%
%## Opgave 5: Hermite polynomier.
%
%I denne opgave vil vi definere en følge af polynomier $\mathrm{He}_0(Z), \mathrm{He}_1(Z), \dots $ med heltalskoefficienter som kaldes Hermitepolynomierne. Disse polynomier optræder i mange sammenhænge, blandt andet i signalbehandling, sandsynlighedsregning og kvantemekanik. Hermitepolynomierne kan defineres rekursivt som følger:
%
%$\mathrm{He}_0(Z)=1$, $\mathrm{He}_1(Z)=Z$ og $\mathrm{He}_n(Z)=Z\mathrm{He}_{n-1}(Z)-(n-1)\mathrm{He}_{n-2}(Z)$ hvis $n \ge 2$.
%
%Hvad er $\mathrm{He}_n(Z)$ for $n=0,1,\dots,4$? 
%
%```{admonition} Svar
%:class: dropdown
%$\mathrm{He}_0(Z)=1$, $\mathrm{He}_1(Z)=Z$, $\mathrm{He}_2(Z)=Z^2-1$, $\mathrm{He}_3(Z)=Z^3-3Z$ og $\mathrm{He}_4(Z)=Z^4-6Z^2+3$.  
%```
%
%----
%
%+++
%
%## Opgave 6: En rekursiv defineret stamfunktion
%
%I Opgave 6 fra Uge 2 Lille Dag blev formlen $\mathrm{arctan}'(x)=1/(1+x^2)$ nævnt. Det betyder at 
%
%$$\int \frac{1}{1+x^2} dx = \mathrm{arctan}(x)+C.$$
%
%Hvis $n$ er et naturligt tal, kan man ligeledes spørge om der findes en lignende formel til den ubestemte integral 
%
%$$\int \frac{1}{(1+x^2)^n} dx.$$
%
%Det viser sig at der er en rekursiv løsning til dette spørgsmål.
%
%+++
%
%### Spørgsmål a
%
%Produktreglen siger at $(f(x)\cdot g(x))'=f(x)' \cdot g(x)+f(x) \cdot g(x)'$ (se eventuelt Appendix A.2 fra lærebogen for denne og andre regler angående differentiation). Gør rede for at 
%
%$$\int f(x)' \cdot g(x) dx = f(x)\cdot g(x) - \int f(x)\cdot g(x)' dx.$$
%
%Denne formel kaldes for partiel integration.
%
%```{hint}
%:class: dropdown
%Funktionen $(f(x)\cdot g(x))'$ har stamfunktion $f(x) \cdot g(x)$. På den anden side kan man omskrive $(f(x)\cdot g(x))'$ ved hjælp af produktreglen.
%```
%
%+++
%
%### Spørgsmål b 
%
%Anvend partiel integration på $f(x)=x$ og $g(x)=1/(1+x^2)^n$ for at indse at
%
%$$\int \frac{1}{(1+x^2)^n}dx = \frac{x}{(1+x^2)^n}+2n\int \frac{x^2}{(1+x^2)^{n+1}}dx.$$
%
%+++
%
%### Spørgsmål c 
%
%Brug nu formlen 
%
%$$
%\frac{x^2}{(1+x^2)^{n+1}}=\frac{1+x^2-1}{(1+x^2)^{n+1}}=\frac{1}{(1+x^2)^{n}}-\frac{1}{(1+x^2)^{n+1}}
%$$
%
%for at konkludere at 
%
%$$\int \frac{1}{(1+x^2)^n}dx = \frac{x}{(1+x^2)^n}+2n\int \frac{1}{(1+x^2)^{n}}dx-2n\int \frac{1}{(1+x^2)^{n+1}}dx.$$
%
%Løs nu for $\int \frac{1}{(1+x^2)^{n+1}}dx$ i den sidste formel og konkluder at hvis $n \ge 1$, så gælder
%
%$$\int \frac{1}{(1+x^2)^{n+1}}dx = \frac{x}{2n(1+x^2)^n}+\frac{2n-1}{2n} \int \frac{1}{(1+x^2)^{n}}dx.$$
%
%Dette formel er præcist hvad vi skulle bruge! Formlen udtrykker stamfunktionen til $1/(1+x^2)^{n+1}$ som en sum af funktionen $\frac{x}{2n(1+x^2)^n}$ og stamfunktionen af $1/(1+x^2)^{n}$. Derfor kan formlen bruges til at finde stamfunktionen til $1/(1+x^2)^{n+1}$ på en rekursiv måde.
%
%+++
%
%### Spørgsmål d 
%
%Brug den fundne rekursion til at bestemme stamfunktionen til $1/(1+x^2)^2$.
%
%```{admonition} Svar
%:class: dropdown
%$$\int \frac{1}{(1+x^2)^2}dx=\frac{x}{2(1+x^2)}+\frac12 \mathrm{arctan}(x)+C.$$
%```

----

+++

## Opgave 1: Repetitionsopgave om rekursion og sumtegnet

Der defineres rekursivt en følge af tal $c_0,c_1,c_2,\dots$ på følgende måde:

$c_0=0$, $c_1=1$, $c_2=2$ og for $n \ge 3$ gælder $c_n=c_{n-1}c_{n-2}+c_{n-3}.$

+++

### Spørgsmål a 

Hvilken værdier har $c_3,c_4$ og $c_5$?

```{admonition} Svar
:class: dropdown
$c_3=c_2c_1+c_0=2\cdot 1+0=2$

$c_4=c_3c_2+c_1=2\cdot 2+1=5$

og

$c_5=c_4c_3+c_2=5\cdot 2+2=12.$
```

+++

### Spørgsmål b 

Hvilken værdier har $\sum_{k=0}^n c_k$ for $n=0,1,2,3,4$ og $5$?

```{hint}
:class: dropdown
I stedet for sumtegnet, kan man også bruge priknotationen: $\sum_{k=0}^n c_k=c_0+\cdots + c_n$.
```

```{admonition} Svar
:class: dropdown
$\sum_{k=0}^0c_k=c_0=0$, 

$\sum_{k=0}^1c_k=c_0+c_1=1$, 

$\sum_{k=0}^2c_k=c_0+c_1+c_2=1+2=3$, 

$\sum_{k=0}^3c_k=c_0+c_1+c_2+c_3=3+c_3=5$   

$\sum_{k=0}^4c_k=c_0+c_1+c_2+c_3+c_4=5+c_4=10$   

$\sum_{k=0}^5c_k=c_0+c_1+c_2+c_3+c_4+c_5=10+c_5=22.$   
```

----

%+++
%
%## Opgave 2: Afledte funktioner og induktion
%
%Som kendt fra gymnasiet, gælder for alle $n \in \mathbb{Z}_{\ge 1}$ at den afledte af $x^n$ er lig med $nx^{n-1}$, dvs. $(x^n)'=nx^{n-1}$.  I denne opgave vises det ved hjælp af induktion. I må i denne opgave bruge at den afledte af $x$ er $1$, samt produktreglen $(f(x)\cdot g(x))'=f(x)'\cdot g(x)+f(x) \cdot g(x)'.$  
%
%+++
%
%### Spørgsmål a
%
%Formuler induktionsstarten (på engelsk: "base case of the induction"). Tjek bagefter at induktionsstarten holder.
%
%```{hint}
%:class: dropdown
%Fordi der skal vises at $(x^n)'=nx^{n-1}$ for alle $n \in \mathbb{Z}_{\ge 1}$, er induktionsstarten tilfældet hvor $n=1$. Sæt derfor nu $n=1$ ind i ligningen $(x^n)'=nx^{n-1}$ for at se helt præcist hvad man skal tjekke i induktionsstarten.  
%```
%
%```{admonition} Svar
%:class: dropdown
%Induktionsstarten er udsagnet at formlen $(x^n)'=nx^{n-1}$ holder for $n=1$. Med andre ord: induktionsstarten er udsagnet $(x^1)'=1$. Hvis man nu bruger at $x^1=x$, $x'=1$ og $x^0=1$, følger resultatet efter nogle få mellemregninger. 
%```
%
%
%### Spørgsmål b
%
%Formuler nu induktionsskridtet. Hvad er induktionshypotesen i dette tilfælde?
%
%```{admonition} Svar
%:class: dropdown
%Induktionshypotesen er at ligningen $(x^{n-1})'=(n-1)x^{n-2}$ holder for et vist $n \ge 2$. 
%```
%
%+++
%
%### Spørgsmål c
%
%Vis at induktionsskridtet holder. Induktionsprincippet medfører nu at formlen $(x^n)'=nx^{n-1}$ holder for alle $n \in \mathbb{Z}_{n \ge 1}.$
%
%```{hint}
%:class: dropdown
%Bemærk at $x^n=x^{n-1} \cdot x$. Udforsk først hvad produktreglen siger hvis der vælges $f(x)=x^{n-1}$ og $g(x)=x$. Brug induktionshypotesen bagefter.
%```
%
%```{admonition} Svar
%:class: dropdown
%Produktreglen kombineret med induktionshypotesen giver at $(x^n)'=(n-1)x^{n-2} \cdot x+x^{n-1} \cdot 1=n x^{n-1}$.  
%
%Bemærk i øvrigt at formlen $(x^n)'=n x^{n-1}$ faktisk holder for alle reelle tal $n$ og ikke kun for naturlige tal $n$. At vise dette er dog ikke en del af opgaven. 
%```

## Opgave 2: Summen af ulige tal og induktion

+++


### Spørgsmål a

+++

Beregn for $n=1,2,3,4$ summen af de første $n$ ulige naturlige tal. 
Med andre ord: bestem værdien af $\sum_{k=1}^n (2k-1)$ for $n \in \{1,2,3,4\}.$ 
Er der et mønster i de fundne værdier? 
Find/gæt nu et kort udtryk for $\sum_{k=1}^n (2k-1)$ som giver det rigtige svar for $n \in \{1,2,3,4\}$ og check at dit gæt også giver den rigtige værdi for $\sum_{k=1}^n (2k-1)$ hvis $n=5.$ 

```{hint}
:class: dropdown
De fundne værdier er altid kvadrater.
```

```{admonition} Svar
:class: dropdown
$\sum_{k=1}^1 (2k-1) = 1$, $\sum_{k=1}^2 (2k-1) = 4$, $\sum_{k=1}^3 (2k-1) = 9$ og $\sum_{k=1}^4 (2k-1) = 16$. 

Baseret på ovenstående er det rimeligt at gætte at $\sum_{k=1}^n (2k-1)=n^2$ er sandt for alle naturlige tal $n$. 
For $n=5$ passer gættet også: $5^2=25$ og $1+3+5+7+9=25$.
```

+++

### Spørgsmål b

+++

Lad $P(n)$ være det logiske udsagn at $\sum_{k=1}^n (2k-1)$ er lig med det korte udtryk du fandt i spørgsmål a. 
Målet er nu at vise at $P(n)$ er sandt for alle naturlige tal $n$ (dvs. for alle $n \in \mathbb{N}=\mathbb{Z}_{\ge 1}$).


Vis at induktionsstarten holder. 

```{hint}
:class: dropdown
Induktionsstarten er udsagnet $P(1)$. Med andre ord, for at vise at induktionsstarten holder, skal man vise at $P(1)$ er sandt. 
```

```{admonition} Svar
:class: dropdown
$P(1)$ er udsagnet at $\sum_{k=1}^1 (2k-1) = 1^2$, men det holder pga. spørgsmål a. 
Faktisk ved man fra spørgsmål a at $P(n)$ holder for $n \in \{1,2,3,4,5\}$, men i induktionsstarten behøver man her kun at tjekke for $n=1$.
```

### Spørgsmål c

Gennemfør nu induktionsskridtet og brug bagefter induktionsprincippet til at konkludere at $P(n)$ er sandt for alle naturlige tal $n$.

```{hint}
:class: dropdown
I induktionsskridtet skal man vise for et vilkårligt heltal $n \ge 2$ at implikationen $P(n-1) \Rightarrow P(n)$ er sandt. 
Med andre ord: i induktionsskridtet man må antage at $P(n-1)$ er sandt og derudfra vise at $P(n)$ også er sandt.
```

```{hint}
:class: dropdown
I induktionsskridtet kan den rekursive definition af sum-tegnet som givet i Ligning (3.5) i lærebogen være nyttigt.
```

%----
%
%## Opgave 4: En identitet med logaritmer
%
%+++
%
%Denne opgave er en fortsættelse af Opgave 3c fra Uge 2, Lille Dag. Lad $c$ være et positivt reelt tal. Vis med induktion efter $n$ %følgende udsagn:
%
%$\ln(c^n)=n\cdot \ln(c)$ for alle $n \in \mathbb{Z}_{\ge 0}$.
%
%+++
%
%```{hint}
%:class: dropdown
%Induktionsstartet er påstanden at $\ln(c^0)=0\cdot \ln(c)$ er sandt. For at vise det, brug at $c^0=1$.
%```
%
%```{hint}
%:class: dropdown
%I induktionsskridtet kunne formlen fra Opgave 3c Uge 2 Lille Dag være behjælpsom samt observationen at $c^n=c\cdot c^{n-1}$.
%```
%
%----
%
%+++
%
%## Opgave 4: At gange ind i parenteser
%
%Lad $n \in \mathbb{Z}_{\ge 2}$ og $a,b_1,\dots,b_n$ være komplekse tal. Vis følgende ved hjælp af induktion efter $n$:
%
%$$a \cdot (b_1+\cdots+b_n)=a\cdot b_1+\cdots + a \cdot b_n.$$
%
%Man må bruge at ligningen holder for $n=2$, ved at henvise til Sætning 4.2.2, 3. del fra lærebogen.  
%
%```{hint}
%:class: dropdown
%Induktionsstartet følger fra Sætning 4.2.2 hvis man i denne sætning vælger $z_1=a$, $z_2=b_1$ og $z_3=b_2$. 
%```
%
%```{hint}
%:class: dropdown
%Til indukstionsskridet: $b_1+\cdots+b_n$ kan også skrives som $\sum_{k=1}^n b_k$. Kan Ligning (3.5) fra lærebogen bruges? 
%```
%
%```{hint}
%:class: dropdown
%Fra Ligning (3.5) i lærebogen ses $\sum_{k=1}^n b_k = \left( \sum_{k=1}^{n-1} b_k\right)+b_n$. Derfor gælder
%
%$$a \cdot \left(\sum_{k=1}^n b_k \right)= a\cdot \left( \left( \sum_{k=1}^{n-1} b_k\right)+b_n \right).$$
%
%Kan Sætning 4.2.2 (3. del) nu bruges til at komme videre?
%```
%
----

+++

----

+++

## Opgave 3: Den geometriske række

I en geometrisk talfølge er hvert tal lig det forrige tal ganget med en fastholdt faktor. 
En geometrisk række er en sum af en geometrisk talfølge.
Lad $r \in \mathbb{C} \setminus \{1\}$ være et komplekst tal og $n$ et naturligt tal. 
I denne opgave vises følgende identitet:

$$1+r+\cdots + r^n= \frac{r^{n+1}-1}{r-1}.$$

+++

### Spørgsmål a

Hvorfor må $r$ ikke være lig med $1$ i identiteten?

```{admonition} Svar
:class: dropdown
Hvis $r=1$, så er nævneren i brøken $\frac{r^{n+1}-1}{r-1}$ lig med nul. Derfor er brøken ikke defineret hvis $r=1$.
```

+++

### Spørgsmål b

Tjek at identiteten holder for $n=1$. 

```{hint}
:class: dropdown
Hvis man betragter udtrykket $r^2-1$ som et polynomium i variablen $r$, så har polynomiet rødder $1$ og $-1$. 
Brug nu Lemma 5.6.2 fra lærebogen til at skrive $r^2-1$ som produkt af to førstegradspolynomier. 
```

+++

### Spørgsmål c

Vis at identiteten $1+r+\cdots + r^n= \frac{r^{n+1}-1}{r-1}$ holder for alle naturlige tal $n$. 

```{hint}
:class: dropdown
Brug induktion efter $n$. Bemærk at induktionsstarten allerede blev klaret i spørgsmål b.
```

```{hint}
:class: dropdown
Til induktionstrinnet: induktionshypotesen er at $1+r+\cdots + r^{n-1}= \frac{r^{n}-1}{r-1}$. 
Brug nu at $1+r+\cdots + r^{n}=(1+r+\cdots + r^{n-1})+r^n$ og bagefter induktionshypotesen.
```

----

## Opgave 4: En hoppebold og den geometriske række

### Spørgsmål a 

En hoppebold slippes to meter over gulvet. 
Efter at have ramt gulvet hopper den én meter op igen, anden gang en halv meter, en kvart meter tredje gang, osv. 
Altså faldhøjden halveres, for hvert påbegyndt nyt fald. Lad nu $n$ være et naturligt tal. 
Find et udtryk som giver afstanden bolden har tilbagelagt, når den rammer gulvet for $n$’te gang.

```{hint}
:class: dropdown
Første gang bolden rammer gulvet har bolden tilbagelagt en afstand på to meter, fordi bolden holdes på to meters højde i starten: i alt altså $2$ meter. Anden gang hopper bolden først en meter op igen for så at falde en meters afstand til den rammer gulvet: i alt har bolden derfor på det tidspunkt tilbagelagt $2+2\cdot 1=4$ meter. Tredje gang hoppen den først en halv meter op og falder bagefter en halv meter ned: i alt fås nu $2+2\cdot (1+\frac12)$ meter. 
Fjerde gang fås i alt på ligende måde: $2+2\cdot (1+\frac12+\frac14)$. 
Kan du se et mønster og udtrykke det ved hjælp af sumtegnet?
```

```{admonition} Svar
:class: dropdown
Hvis $n=1$ er svaret $2$ meter, for $n \ge 2$ er svaret $2+2\cdot \sum_{j=0}^{n-2} \frac{1}{2^j}.$
```

+++

### Spørgsmål b

Hvor mange meter når hoppebolden at tilbagelægge inden den ligger stille på gulvet? 

```{hint}
:class: dropdown
Hvis du vælger $r$ og $n$ passende, så kan du simplificere udtrykket ved at bruge identiteten fra Opgave 3:

$$1+r+\cdots + r^n= \frac{r^{n+1}-1}{r-1}.$$ 

Hvad får man nu når $n$ går mod uendelig?
```

```{admonition} Svar
:class: dropdown
$6$ meter.
```

----

+++

## Opgave 5: En ulighed

En følge af reelle tal $a_1,a_2,\dots$ bliver defineret rekursivt som følger:

$a_1=0$ og $a_n=\sqrt{2+a_{n-1}}$ hvis $n \ge 2$. 

+++

### Spørgsmål a

Beregn $a_1,a_2,a_3$ og $a_4$.

```{admonition} Svar
:class: dropdown
$a_1=0$, $a_2=\sqrt{2}$, $a_3=\sqrt{2+\sqrt{2}}$ og $a_4=\sqrt{2+\sqrt{2+\sqrt{2}}}.$ 

Eventuelt numerisk: 

$a_1=0.00000000000000000000000000000$.

$a_2=1.41421356237309504880168872421$.

$a_3=1.84775906502257351225636637879$.

$a_4=1.96157056080646089825236447227$.
```

+++

### Spørgsmål b

Påstanden er nu at der for alle naturlige tal $n$ gælder, at $a_n<2$. Bevis det vha. induktion efter $n$.

```{hint}
:class: dropdown
I induktionsskridtet må man bruge at kvadratrodsfunktionen $f: \mathbb{R}_{\ge 0} \to \mathbb{R}$ givet ved $x\mapsto \sqrt{x}$, er strengt voksende. 
```

----

%
%+++
%
%## Opgave 8: En sum med brøker
%
%Vis at identiteten 
%
%$$\sum_{k=1}^n \frac{1}{k(k+1)}=1-\frac{1}{n+1}$$ 
%
%gælder for alle $n \in \mathbb{N}.$
%
%----
%
%+++
%

## Opgave 6: Areal under en parabel

Lad $N$ være et positivt reelt tal og $n$ et naturligt tal. Vi definerer $d=N/n$. Som kendt fra gymnasiet kan arealet mellem parablen og første aksen fra $x=0$ til $x=N$ beregnes som følger:

$$\int_0^N x^2 dx =\frac13 N^3-\frac13 0^3=\frac13 N^3.$$

I denne opgave undersøges i hvilken grad dette areal tilnærmes med den endelige sum $\sum_{k=1}^n d\cdot(kd)^2$. 
Situationen illustreres i følgende figur:

![](../media/uge6_6.png)

+++

### Spørgsmål a

Brug tegningen til at indse at 

$$\frac13 N^3 \le \sum_{k=1}^n d\cdot (kd)^2.$$

+++

### Spørgsmål b

Det kan vises at for alle naturlige tal $n$ og alle komplekse tal $a,b_1,\dots,b_n$ det gælder at 

$$a \cdot (b_1+\cdots+b_n)=a\cdot b_1+\cdots + a \cdot b_n.$$

Bruge dette til at indse at

$$d^3\sum_{k=1}^n k^2=\sum_{k=1}^n d^3\cdot k^2=\sum_{k=1}^n d\cdot (kd)^2.$$

+++

### Spørgsmål c

Brug induktion efter $n$ til at indse at $\sum_{k=1}^n k^2=\frac13 n(n+1/2)(n+1)$ for alle naturlige tal $n$.

```{hint}
:class: dropdown
I induktionsskridtet når man på et tidspunkt til formlen 

$$\frac13 (n-1)(n-1/2)n+n^2.$$

Man kan gange alt ud og se om det giver det rigtige, men det kan bespare en hel del arbejde først at tage $n$ udenfor parenteser:

$$\frac13 (n-1)(n-1/2)n+n^2=n\left( \frac13 (n-1)(n-1/2)+n\right).$$

Prøv nu først at indse at udtrykket indenfor parenteserne er lig med $\frac13 (n+1/2)(n+1).$
```

```{admonition} Svar
:class: dropdown
Induktionsstarten: Hvis $n=1$, så gælder formlen, fordi $\sum_{k=1}^1 k^2=1^2=1$ og $\frac13 1(1+1/2)(1+1)=\frac{3}{3}=1$.

Induktionsskridtet: Hvis $n \ge 2$ og der antages induktionshypotesen at $\sum_{k=1}^{n-1} k^2=\frac13 (n-1)(n-1/2)n$, så fås

$$\sum_{k=1}^{n} k^2 = \sum_{k=1}^{n-1} k^2 +n^2=\frac13 (n-1)(n-1/2)n+n^2.$$

For eksempel ved at følge ovenstående vink, så kan man indse at $\frac13 (n-1)(n-1/2)n+n^2=\frac13 n(n+1/2)(n+1)$, som betyder at induktionsskridtet holder. Induktionsprincippet medfører derfor at formlen $\sum_{k=1}^n k^2=\frac13 n(n+1/2)(n+1)$ holder for alle naturlige tal $n$.
```

+++

### Spørgsmål d

Vis nu at $\sum_{k=1}^n d\cdot (kd)^2=\frac{1}{3}N(N+d/2)(N+d)$. 

```{admonition} Svar
:class: dropdown
Fra de forrige spørgsmål fås

$$\sum_{k=1}^n d\cdot (kd)^2=d^3\sum_{k=1}^n k^2=d^3\left(\frac13 n(n+1/2)(n+1)\right)=\frac{1}{3}N(N+d/2)(N+d).$$

I den sidste lighed bruges at $N=dn$. 

Bemærkning: ligningen medfører at hvis $N$ holdes fast og $n$ går mod uendeligt, så går $d$ mod nul og summen går derfor mod $\frac13 N^3,$ som netop er arealet under parablen.
```

%----
%
%+++
%
%## Opgave 9: Rentesatsen
%
%Beløbet man kan låne hos en bank er afhængig af mang ting, blandt andet ens indkomst samt rentesatsen. I denne opgave undersøges og %opstilles en model.
%
%+++
%
%### Spørgsmål a
%
%
%----
