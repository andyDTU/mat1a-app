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

(section:uge2S)=

# Opgaver -- Store Dag

## Opgave 1: Mængder på listeform
Lad $A$ og $B$ være endelige mængder, givet på listeformerne: 

$$A = \{n \in \Bbb{N}\, | \, n=m^2 \,\,\,\mathrm{hvor} \,\,\, m \in \{1,2,3,4,5\}\},$$

$$B = \{n \in \Bbb{N} \, |\, n=2m-1 \,\,\,\mathrm{hvor} \,\,\,   m \in \{1,2,3,4,5\}\}.$$

### Spørgsmål a

+++

Hvilke elementer indgår i mængderne $A$ og $B$?

```{hint}
:class: dropdown
Elementerne i mængden $A$ er tallene $m^2$ man får når $m$ gennemløber alle tal i $\{1,2,3,4,5\}$.
```

```{admonition} Svar
:class: dropdown
$A=\{1,4,9,16,25\}$ og $B=\{1,3,5,7,9\}$.
```

### Spørgsmål b

+++

Hvilke elementer indgår i mængderne $A \cap B$ og  $A \cup B\,$?

```{hint}
:class: dropdown
Hvis du vil se hvordan $\cap$ (fællesmængdesymbol) og $\cup$ (foreningsmængdesymbol) blev defineret, se Ligning (2.1) og (2.2) fra lærebogen.
```

### Spørgsmål c

+++

Hvilke elementer indgår i mængderne $A \setminus B$ og  $B \setminus A\,$?

```{admonition} Svar
:class: dropdown
$A\setminus B=\{4,16,25\}$ og $B\setminus A=\{3,5,7\}$.
```

----


## Opgave 2: Mængder på listeform

Lad $C$ og $D$ være mængder, givet på listeformerne: 

$$C = \{n \in \Bbb{N}\, | \, n=2m \,\,\,\mathrm{hvor} \,\,\,   m \in \Bbb{N}\},$$

$$D = \{n \in \Bbb{N}\,  |\,  n=3m \,\,\,\mathrm{hvor} \,\,\,  m \in  \Bbb{N}\}.$$


Hvilke elementer indgår i mængderne $C \cap D$ og  $C \cup D\,$?


```{admonition} Svar
:class: dropdown
$C \cap D$ indeholder alle naturlige tal som er både et multiplum af $2$ og af $3$. 
Derfor består $C \cap D$ af alle naturlige tal som er et multiplum af $6$.
Det vil sige: $C \cap D= \{n \in \Bbb{N} \, | \, n=6m \,\,\,\mathrm{hvor} \,\,\,   m \in \Bbb{N}\}$. 

$C \cup D$ indeholder alle naturlige tal som er et multiplum af $2$ eller et multiplum af $3$. Derfor $C \cup D = \{2,3,4,6,8,9,10,12,\dots\}.$
```

----

## Opgave 3: Talmængder

Beskriv med dine egne ord mængderne $\Bbb{R} \setminus \Bbb{Q}$ og $\Bbb{Z} \setminus \Bbb{N}\,.$

----

## Opgave 4: Regneregler for mængdeoperationer

### Spørgsmål a

+++

Nogle identiteter i mængdeteori kan illustreres ved at lave en cirkeldiagram (også kendt som Venn-diagram). I lærebogen blev for eksempel fællesmængden, foreningsmængden og differensmængden illustreres på denne måde i Afsnit 2.1. Også mængdeidentiteter som dem i lærebogens Sætning 2.1.2 kan visualiseres vha. sådanne diagrammer. 

Lav cirkeldiagrammer der visualiserer identiteterne (2.8)-(2.11) i lærebogens Sætning 2.1.2.


### Spørgsmål b

+++

Brug udsagnslogik til at bevise identiteterne (2.4) og (2.10) i lærebogens Sætning 2.1.2.


```{hint}
:class: dropdown
Især for at bevise identitet (2.10), kan du lade dig inspirere af beviset for identitet (2.11) i Sætning 2.1.2 fra lærebogen.
```

### Spørgsmål c

+++

Lad $A$ og $B$ være mænger med et endeligt antal elementer. Lad $|A|$ betegne antal elementer i en mængde $A$.
Giv en forklaring på følgende identitet.

$|A \cup B| = |A| + |B| - |A \cap B|$. 

```{hint}
:class: dropdown
For at få intuitionen på plads, check først at identiteten holder for mængderne $A$ og $B$ fra Opgave 1.
```

----
## Opgave 5: Surjektiv, injektiv og bijektiv

Fire mængder er givet ved:

$$A=\{ x \in \Bbb N \, | \, 1 \leq x \leq 7 \},$$

$$B=\{ x^2 \, | \, x \in A\},$$

$$C=\{ x \in \Bbb N \, | \, 1 \leq x \leq 6 \},$$

$$D=\{x \in \Bbb Z \, |  \, -7 \leq x \leq 7 \wedge x \neq 0\}.$$

Nedenfor er givet fire funktioner. Afgør hvilke der er surjektive, injektive eller bijektive.

### Spørgsmål a

+++

$f_1 :A\rightarrow B$

$\ \ x \mapsto x^2$

```{hint}
:class: dropdown
Hvis du er i tvivl om hvad begreberne "injektiv", "surjektiv" og "bijektiv" går ud på, så kan du genopfriske din hukommelse ved at læse Afsnit 2.2 fra lærebogen igen (mere præcist teksten efter Lemma 2.2.1 op til Definition 2.2.1).
```

```{hint}
:class: dropdown
Det kan hjælpe først at skrive mængderne $A$ og $B$ ned mere eksplicit. Prøv for eksempel at indse at $A=\{1,2,3,4,5,6,7\}.$
```

```{admonition} Svar
:class: dropdown
$f_1$ er både injektiv og surjektiv. Derfor er den også bijektiv.
```

### Spørgsmål b

+++

$f_2 :D\rightarrow B$

$\ \ x \mapsto x^2$

```{hint}
:class: dropdown
For at vise at en funktion ikke er injektiv, er det tilstrækkeligt at finde to forskellige elementer fra funktions definitionsmængde som bliver afbildt på det samme element fra dispositionsmængden.
```


```{admonition} Svar
:class: dropdown
$f_2$ er surjektiv, men ikke injektiv og derfor heller ikke bijektiv.
```


### Spørgsmål c

+++

$f_3 :C\rightarrow B$

$\ \ x \mapsto x^2$

```{hint}
:class: dropdown
For at vise at en funktion ikke er surjektiv, er det tilstrækkeligt at vise at funktionens billedmængde ikke er hele dispositionsmængden.
```

```{admonition} Svar
:class: dropdown
$f_3$ er injektiv, men ikke surjektiv og derfor heller ikke bijektiv.
```

### Spørgsmål d

+++

$f_4 :\Bbb Z\rightarrow \Bbb Z$

$\ \ x \mapsto |x|$

```{admonition} Svar
:class: dropdown
$f_4$ er ikke injektiv, ikke surjektiv og heller ikke bijektiv.
```

## Opgave 6: Sammensatte funktioner

Givet er mængden $A=\{0,1,2\}$, samt to funktioner $f: A \to A$ og $g: A \to \mathbb{R}$. Funktionen $f$ har forskrift $f(x)=2-x$, mens funktionen $g$ har forskrift $g(x)=2x+e^x$.


### Spørgsmål a

+++

Er den sammensatte funktion $f \circ g$ defineret? Hvad med $g \circ f$?

```{hint}
:class: dropdown
I lærebogen, straks efter Eksempel 2.2.2, kan du læse om hvad der skal til for at kunne sammensætte to funktioner.
```

```{admonition} Svar
:class: dropdown
$f \circ g$ er ikke defineret, fordi $g$'s dispositionsmængde er $\mathbb{R}$, som ikke er $f$'s definitionsmængde (den er nemlig $A$).

$g \circ f$ er defineret, fordi $f$'s dispositionsmængde er det samme som $g$'s definitionsmængde (nemlig $A$).

Bemærk at man ikke behøver at kende forskrifterne for to funktioner for at kunne afgøre om deres sammensætning er defineret. Kun at vide deres definitions- og dispositionsmængderne er tiltrækkeligt til afgørelsen.
```
### Spørgsmål b

+++

Beregn $(g\circ f)(a)$ for alle $a \in A$.

```{admonition} Svar
:class: dropdown
$(g \circ f)(0)=4+e^2$, $(g \circ f)(1)=2+e$ og $(g \circ f)(2)=1$. 

Mellemregning til det sidste svar: 

$$(g \circ f)(2)=g(f(2))=g(2-2)=g(0)=2\cdot 0 +e^0=0+1=1.$$
```

### Spørgsmål c

+++
Bestem forskrift, definitionsmængde, dispositionsmængde og værdimængde af funktionen $g \circ f$.

```{hint}
:class: dropdown
Værdimængden kan bestemmes ud fra svar til spørgsmål b. Definitionsmængde og dispositionsmængde kan bestemmes ud fra definitionen af en sammensat funktion.
```

```{admonition} Svar
:class: dropdown
Forskrift: $(g \circ f)(x)=2(2-x)+e^{2-x}$ (eller helst lidt pænere $(g \circ f)(x)=4-2x+e^{2-x}$).

Værdimængde: $\{4+e^2,2+e,1\}$ (det er også fint at ordne tallene efter størrelse og give som svar $\{1,2+e,4+e^2\}$).

Definitionsmængde: $A$, dvs. $\{0,1,2\}$.

Dispositionsmængde: $\mathbb R$.
```

### Spørgsmål d

+++

Er funktionen $g \circ f$ injektiv? Hvad med surjektiv?

```{admonition} Svar
:class: dropdown
Injektiv: ja. Surjektiv: nej.
```
----

----
## Opgave 7: En inverse funktion

Givet er en funktion $f: \mathbb{R} \rightarrow \mathbb{R}$ som har funktionsforskriften

$$f(x)=3x-7.$$

### Spørgsmål a

+++

Lad $g: \mathbb{R} \rightarrow \mathbb{R}$ være funktionen med funktionsforskriften

$$g(x)=(x+7)/3.$$

Vis ved at bruge Definition 2.2.1 fra lærebogen at $g$ er den inverse funktion til $f$. 
%Bemærkning: hvis du tegner graferne til $f$ og $g$ vil du kunne se en symmetrisk sammenhæng mellem dem. Hvilken symmetri er det? Se eventuelt sidste del af Eksempel 2.3.1 hvor en lignende symmetri optræder.

### Spørgsmål b

+++

Redegør for at $f$ er bijektiv.

```{hint}
:class: dropdown
Frem for at starte med at vise at $f$ er injektiv og surjektiv, prøv at benytte Lemma 2.2.2.
```

%----
%## Opgave 5: Fra vinkelmål til radiantal og omvendt
%
%Bijektioner optræder når man konverterer fra en bestemt enhed til en anden. I denne opgave genopfriskes konverting fra vinkelmål til radiantal og omvendt.
%
%### Spørgsmål a
%
%+++
%
%Angiv de radiantal der svarer til vinkelmålene $30, 60, 120, 135$ og $300$ grader.
%
%```{admonition} Svar
%:class: dropdown
%$\frac{\pi}{6}$, $\frac{\pi}{3}$, $\frac{2\pi}{3}$, $\frac{3\pi}{4}$, $\frac{5\pi}{3}$. Generelt: $x$ grader svarer til radiantal $x \pi / 180.$
%```
%
%### Spørgsmål b
%
%+++
%
%Tegn enhedscirklen i et $(x,y)$-koordinatsystem med centrum i Origo. Afsæt punkter på enhedscirklen svarende til buelængderne 
%
%$$\pi\,,\, \frac{\pi}{3}\,, \,\frac{-\pi}{6}\,, \,-\frac{\pi}{6}\,, \,\frac{7\pi}{12}\,,\,-\frac{3\pi}{2}\,,\,\frac{7\pi}{4}\,.$$
%
%Hvilke vinkelmål i grader svarer de til?
%
%```{admonition} Svar
%:class: dropdown
%$180$, $60$, $330$, $330$, $105$, $90$, $315$. Generelt: buelængden $x$ svarer til $180x/\pi$ grader hvis $x \in [0,2\pi[$. Hvis $x \not\in [0,2\pi[$, lægges først et multiplum af $2\pi$ til således at udkomsten ligger i intervallet $[0,2\pi[$. 
%```
%
%----
%## Opgave 6: Cosinus og sinus repetition
%
%![](../media/enhedscirkelU2SD.png)
%
%### Spørgsmål a
%
%+++
%
%Benyt figuren (den blå trekant) til geometrisk bestemmelse af de eksakte værdier for 
%$\,\displaystyle{\cos\left(\frac{\pi}{4}\right)}\,$ og $\,\displaystyle{\sin\left(\frac{\pi}{4}\right)}\,.$
%
%```{hint}
%:class: dropdown
%Husk at Pythagoras' sætning medfører at $\cos^2(x)+\sin^2(x)=1$ for all reelle tal $x$.
%```
%
%```{admonition} Svar
%:class: dropdown
%De giver begge $\frac{\sqrt{2}}{2}\,. $
%```
%
%### Spørgsmål b
%
%+++
%
%Bestem ved hjælp af symmetribetragtninger tallene
%
%$$
%\cos\left(p\,\frac{\pi}{4}\right)\,\,\,\mathrm{og}\,\,\,\sin\left(p\,\frac{\pi}{4}\right)
%\,\,\,\mathrm{for}\,\,\,p \in \{3, 5, 7, -1, -3, -5, -7\}\,.
%$$
%
%```{admonition} Svar
%:class: dropdown
%$(-\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2}),(-\frac{\sqrt{2}}{2},-\frac{\sqrt{2}}{2}),(\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}),(\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}),(-\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}), 
%(-\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}),(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}).$
%```
%
%### Spørgsmål c
%
%+++
%
%Det oplyses at 
%$\,\displaystyle{\cos\left(\frac{\pi}{6}\right)}=\frac{\sqrt 3}{2}\,$ og $\,\displaystyle{\sin\left(\frac{\pi}{6}\right)}=\frac{1}{2}\,.$ Indtegn punktet 
%
%$$\,
%\displaystyle{\left(\cos\left(\frac{\pi}{6}\right)\,,\,\sin\left(\frac{\pi}{6}\right)\right)}
%\,$$ 
%
%på en enhedscirkel og find ved hjælp af symmetribetragtninger tallene 
%
%$$
%\cos\left(p\,\frac{\pi}{6}\right)\,\,\,\mathrm{og}\,\,\,\sin\left(p\,\frac{\pi}{6}\right)
%\,\,\,\mathrm{for}\,\,\,p \in \{2, 4, 5, 7, 8, 10, 11\}\,.
%$$
%
%```{hint}
%:class: dropdown
%Bemærkning: i Appendiks 1 fra lærebogen, som står straks efter det sidste kapitel, kan du finde en enhedscirkel, samt værdien af cosinus og sinus i visse "pæne" vinkler.
%```
%
%## Opgave 7: $\mathrm{arccos}$, $\mathrm{arcsin}$ og trigonometriske ligninger
%
%I denne opgave betragtes de inverse trigonometriske funktioner $\mathrm{arccos}$ og $\mathrm{arcsin}$, samt nogle trigonometriske ligninger. Hvis du har behov for at genopfriske eller se graferne til disse funktioner, så kan du kigge på Afsnit 2.3 fra lærebogen (især underafsnittet "De inverse trigonometriske funktioner").
%
%### Spørgsmål a
%
%+++
%
%Angiv tallene $\,\displaystyle{\mathrm{arccos}\left(\frac{1}{2}\right),\,\mathrm{arcsin}\left(-\frac{\sqrt 3}{2}\right)}$ og $\displaystyle{\mathrm{arcsin}(1)}\,.$
%
%
%```{admonition} Svar
%:class: dropdown
%$\frac{1}{3} \, \pi$, $-\frac{1}{3} \, \pi$, $\frac{1}{2} \, \pi$.
%```
%
%### Spørgsmål b
%
%+++
%
%Lad $x \in \mathbb{R}$ og $y \in [-1,1]$ være reelle tal. Lad $P$ være det logiske udsagn $\mathrm{arccos(y)}=x$ og $Q$ det logiske udsagn $y=\cos(x)$. Vis at $P \Rightarrow Q$ er sandt, men at $Q \Rightarrow P$ ikke behøves at være sandt.
%
%```{hint}
%:class: dropdown
%Til $P \Rightarrow Q$: hvad sker der hvis man anvender $\cos$-funktionen på begge sider af lighedstegnet i $P$?
%
%Til $Q \Rightarrow P$: kan du finde $x \in \mathbb{R}$ og $y \in [-1,1]$ således at $Q$ er sandt, men $P$ ikke?
%```
%
%### Spørgsmål c
%
%+++
%
%Der er givet mængderne $\,A=\left[\,0\,,\,2\pi\,\right]\,$ og $\,B=\left[\,-\pi\,,\,\pi\,\right]\,.$
%
%Løs ligningen $\,\displaystyle{\cos(x)=\frac{1}{2}}\,$ inden for hver af mængderne $\,A,\,B\,$ og $\,\Bbb R\,.$
% 
%```{hint}
%:class: dropdown
%En løsning til ligningen fås direkte fra spørgsmål a, fordi ifølge spørgsmål b $\mathrm{arccos}(y)=x$ medfører at $y=\cos(x).$ Find nu samtlige løsninger i $\mathbb{R}$ ved at lave en skitse af grafen til $\cos$-funktionen.
%```
%
%```{admonition} Svar
%:class: dropdown
%Indenfor $A$ er løsningerne: $\,\frac{\pi}{3}\,$ og $\,\frac{5\pi}{3}\,.$
%
%Indenfor $B$ er løsningerne $\,\frac{-\pi}{3}\,$ og $\,\frac{\pi}{3}\,.$
%
%Indenfor $\mathbb{R}$ er løsningerne $\,\frac{-\pi}{3}+p\cdot 2\pi\,$ og $\,\frac{\pi}{3}+p\cdot 2\pi\,$ hvor $\,p \in \Bbb Z\,.$
%```
%
%### Spørgsmål d
%
%+++
%
%Løs ligningen $\,\displaystyle{\sin(x)=-\frac{\sqrt 3}{2}}\,$ inden for hver af mængderne $\,A,\,B\,$ og $\,\Bbb R\,.$
% 
%
%```{admonition} Svar
%:class: dropdown
%Indenfor $A$ er løsningerne: $\,\frac{4\pi}{3}\,$ og $\,\frac{5\pi}{3}\,.$
%
%Indenfor $B$ er løsningerne: $\,\frac{-2\pi}{3}\,$ og $\,-\frac{\pi}{3}\,.$
%
%Indenfor $\mathbb R$ er løsningerne: $\,\frac{4\pi}{3}+p\cdot 2\pi\,$ og $\,\frac{5\pi}{3}+p\cdot 2\pi\,$ hvor $\,p \in \Bbb Z\,.$
%```
%
----

## Opgave 8: Andengradspolynomiumsfunktioner

Der betragtes en funktion $h: \mathbb{R} \rightarrow \mathbb{R}$ som har funktionsforskriften

$$h(x)=2x^2 -20x +57.$$ 


### Spørgsmål a

+++

Bring funktionen $h$ på formen $h(x)=2(x-k_1)^2+k_2$ og angiv konstanterne $k_1$ og $k_2$. Brug denne form til at bestemme værdimængden til $h$.

```{hint}
:class: dropdown
En mulig metoden som man kan bruge her, er kendt som "kvadratkomplettering".
```

```{admonition} Svar
:class: dropdown
$h$ har værdimængden $\{ x \in \mathbb{R} \, | \, x \ge 7\}.$ Man kan også beskrive denne mængde som $\mathbb{R}_{\ge 7}$.
```

### Spørgsmål b

+++

For en delmængde $J \subseteq {\Bbb R}_{\geq 0}$ kaldes $h$'s restriktion til $J$ funktionen som har samme 
funktionensforskrift og dispositionsmængde som $h$, men hvor funktionens definitionsmængde indskrænkes til $J$.
Angiv det størst mulige interval $J \subseteq {\Bbb R}_{\geq 0}$ hvorpå restriktionen af $h$ til $J$ bliver injektiv.

```{hint}
:class: dropdown
Brug spørgsmål a til at lave en skitse af grafen til $h$.
```

```{admonition} Svar
:class: dropdown
$J=\{ x \in \mathbb{R} \, | \, x \ge 5\}.$ Man kan også beskrive denne mængde som $\mathbb{R}_{\ge 5}$.
```

### Spørgsmål c

+++

Vi betrager nu $h$'s restriktion til intervallet $J$ fra spørgsmål b og indskrænker dispositionsmængden til mængden $\mathbb{R}_{\ge 7}$ fra spørgsmål a. 
Den resulterende funktion er bijektiv og betegnes med $h_1$. 
Mere konkret, $h_1$ er funktionen $h_1: J \rightarrow \mathbb{R}_{\ge 7}$ givet ved $h_1(x)=2x^2 -20x +57.$

Angiv en forskrift for den inverse funktion ${h_1}^{-1}$

```{hint}
:class: dropdown
En god start er at løse for $x$ i ligningen $2x^2 -20x +57=y$.
```

### Spørgsmål d

+++

Angiv definitions- og værdimængden for ${h_1}^{-1}$

```{admonition} Svar
:class: dropdown
Funktionen $h_1^{-1}$ har definitionsmængde $\mathbb{R}_{\ge 7}$ og dispositionsmængde $\mathbb{R}_{\ge 5}$. Fordi $h_1^{-1}$ er surjektiv (faktisk bijektiv), er $h_1^{-1}$'s værdimængde det samme som dens dispositionsmængde, dvs. $\mathbb{R}_{\ge 5}$.
```


----

## Opgave 9: Bijektion


Givet er funktionen $f :\Bbb N\rightarrow \Bbb Z$ defineret ved

$ x \mapsto    \left\{
\begin{array}{ll}
      \frac{x}{2} & x\ \mathrm{lige,} \\
      -\frac{x-1}{2} & x\ \mathrm{ulige.} \\
\end{array} 
\right.  
$

### Spørgsmål a

+++

Er $f$ en bijektion?

```{hint}
:class: dropdown
For at få en ide om funktionens opførsel, beregn først $f(1)$, $f(2)$, $f(3)$, $f(4)$ og $f(5)$.
```

```{admonition} Svar
:class: dropdown
Ja.
```

## Opgave 10: Hyperbolske funktioner

I denne opgave indføres to nye funktioner, men som er dannet af allerede kendte funktioner.
De to funktioner kaldes sinus og cosinus hyperbolsk, og er defineret ved:

$\mathrm{sinh}(x)=\frac{e^x-e^{-x}}{2}$ og $\mathrm{cosh}(x)=\frac{e^x+e^{-x}}{2}.$

Det antages for begge funktioner at både deres definitionsmængder og dispositionsmængder er lige med $\mathbb R$. 

### Spørgsmål a

+++

Redegør for at $\mathrm{sinh}(x)$ er injektiv og at $\mathrm{cosh}(x)$ ikke er injektiv.


```{hint}
:class: dropdown
Er funktionerne monotone?
```

### Spørgsmål b

+++

Find en forskrift for $\mathrm{sinh}^{-1}$ ved at isolere $x$ i ligningen $y=\mathrm{sinh}(x)$. 

```{hint}
:class: dropdown
Gang din ligning igennem med $e^x$ og løs den fremkommende andengradsligning.
```

```{hint}
:class: dropdown
Hvorfor kan vi smide den ene løsning væk?
```

