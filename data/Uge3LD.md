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

(section:uge3L)=

# Opgaver -- Lille Dag


%## Opgave 1: Python opgave
%
%+++
%
%Følgende spørgsmål handler om at illustrere visse dele af teorien om komplekse tal ved hjælp af Python. 
%
%### Spørgsmål a
%
%+++
%
%Givet et følgende Pythonkode. Prøv at køre det i command console Python. Tekst i koden efter et $\#$ tegn er kommentar og behøves ikke at blive kopieret/indtastes, men det skader heller ikke.
%
%`from math import sqrt # Denne regel sørger for at man kan bruge kvadratrod-funktionen sqrt senere`
%
%`Re=3`
%
%`Im=-2`
%
%`mod=sqrt(Re**2+Im**2)`
%
%`mod`
%
%Hvad er betydningen af `mod` i programmet?
%
%```{admonition} Svar
%:class: dropdown
%`mod` giver modulus af det komplekse tal som har realdel `Re` og imaginærdel `Im`.
%```
%
%### Spørgsmål b
%
%+++
%
%Givet er et andet stykke Pythonkode. Prøv at køre det i command console Python. 
%
%`from math import cos, sin, pi #Sørger for man kan bruge funktionerne cos og sin samt cirkelkonstanten pi`
%
%`mod=4 #mod=modulus`
%
%`Arg=pi/3 #Arg=argumentet`
%
%`Re=mod*cos(Arg)`
%
%`Im=mod*sin(Arg)`
%
%`Re`
%
%`Im`
%
%`print(f"Realdel er {Re} og Imaginærdel er {Im}")`
%
%`Re==2`
%
%Hvad skyldes det overraskende svar i sidste linje af programmet?
%
%```{hint}
%:class: dropdown
%Ved håndregning fås at $4\cos(\pi/3)=2$. Pythons svar er derfor lidt overraskende. Python regner dog ikke i hånden!
%```
%
%```{admonition} Svar
%:class: dropdown
%Python bruger numeriske algoritmer til af beregne $\cos(\pi/3)$. Dette betyder at resultatet af en beregning som `4*\cos(pi/3)` vil være en approximation og derfor vil være behæfted med en lille fejl. Fejlen er dog stort nok til at give svaret `False` til `Re==2` sidst i programmet, selvom vi fra håndregningen ved at svaret egentligt skulle have været `True`.  
%```
%
%----
%----
## Opgave 1: Fra grader til radiantal og omvendt

I denne opgave genopfriskes konverting fra grader til radiantal og omvendt.

### Spørgsmål a

+++

Angiv de radiantal der svarer til vinkelmål $30, 60, 120, 135$ og $300$ grader.

```{admonition} Svar
:class: dropdown
$\frac{\pi}{6}$, $\frac{\pi}{3}$, $\frac{2\pi}{3}$, $\frac{3\pi}{4}$, $\frac{5\pi}{3}$. Generelt: $x$ grader svarer til radiantal $x \pi / 180.$
```

### Spørgsmål b

+++

Tegn enhedscirklen i et $(x,y)$-koordinatsystem med centrum i Origo. 
Afsæt punkter på enhedscirklen svarende til buelængderne 

$$\pi\,,\, \frac{\pi}{3}\,, \,\frac{-\pi}{6}\,, \,-\frac{\pi}{6}\,, \,\frac{7\pi}{12}\,,\,-\frac{3\pi}{2}\,,\,\frac{7\pi}{4}\,.$$

Hvilke vinkelmål i grader svarer de til?

```{admonition} Svar
:class: dropdown
$180$, $60$, $330$, $330$, $105$, $90$, $315$. Generelt: buelængden $x$ svarer til $180x/\pi$ grader hvis $x \in [0,2\pi[$. Hvis $x \not\in [0,2\pi[$, lægges først et multiplum af $2\pi$ til således at udkomsten ligger i intervallet $[0,2\pi[$. 
```

----

## Opgave 2: Cosinus og sinus repetition

![](../media/enhedscirkelU2SD.png)

### Spørgsmål a

+++

Benyt figuren (den blå trekant) til geometrisk bestemmelse af de eksakte værdier for 
$\,\displaystyle{\cos\left(\frac{\pi}{4}\right)}\,$ og $\,\displaystyle{\sin\left(\frac{\pi}{4}\right)}\,.$

```{hint}
:class: dropdown
Husk at Pythagoras' sætning medfører at $\cos^2(x)+\sin^2(x)=1$ for all reelle tal $x$.
```

```{admonition} Svar
:class: dropdown
De giver begge $\frac{\sqrt{2}}{2}\,. $
```

### Spørgsmål b

+++

Bestem ved hjælp af symmetribetragtninger tallene

$$
\cos\left(p\,\frac{\pi}{4}\right)\,\,\,\mathrm{og}\,\,\,\sin\left(p\,\frac{\pi}{4}\right)
\,\,\,\mathrm{for}\,\,\,p \in \{3, 5, 7, -1, -3, -5, -7\}\,.
$$

```{admonition} Svar
:class: dropdown
$(-\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2}),(-\frac{\sqrt{2}}{2},-\frac{\sqrt{2}}{2}),(\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}),(\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}),(-\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}), 
(-\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}),(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}).$
```

### Spørgsmål c

+++

Det oplyses at 
$\,\displaystyle{\cos\left(\frac{\pi}{6}\right)}=\frac{\sqrt 3}{2}\,$ og $\,\displaystyle{\sin\left(\frac{\pi}{6}\right)}=\frac{1}{2}\,.$ 
Indtegn punktet 

$$\,
\displaystyle{\left(\cos\left(\frac{\pi}{6}\right)\,,\,\sin\left(\frac{\pi}{6}\right)\right)}
\,$$ 

på en enhedscirkel og find ved hjælp af symmetribetragtninger tallene 

$$
\cos\left(p\,\frac{\pi}{6}\right)\,\,\,\mathrm{og}\,\,\,\sin\left(p\,\frac{\pi}{6}\right)
\,\,\,\mathrm{for}\,\,\,p \in \{2, 4, 5, 7, 8, 10, 11\}\,.
$$

```{hint}
:class: dropdown
Bemærkning: i Appendiks 1 fra lærebogen, som står straks efter det sidste kapitel, kan du finde en enhedscirkel, samt værdien af cosinus og sinus i visse "pæne" vinkler.
```

----

## Opgave 3: Funktionerne $\mathrm{arccos}$, $\mathrm{arcsin}$ og $\mathrm{arctan}$.

I denne opgave betragtes de inverse trigonometriske funktioner $\mathrm{arccos}$, $\mathrm{arcsin}$ og $\mathrm{arctan}$. 
Hvis du har behov for at genopfriske eller se graferne til disse funktioner, så kan du kigge på Afsnit 2.3 fra lærebogen (især underafsnittet "De inverse trigonometriske funktioner").

### Spørgsmål a

+++

Angiv tallene 
$\,\displaystyle{\mathrm{arccos}\left(\frac{1}{2}\right),\,\mathrm{arcsin}\left(-\frac{\sqrt 3}{2}\right)}$ 
og $\displaystyle{\mathrm{arctan}(-1)}\,.$


```{admonition} Svar
:class: dropdown
$\frac{1}{3} \, \pi$, $-\frac{1}{3} \, \pi$, $-\frac{1}{4} \, \pi$.
```

### Spørgsmål b

+++

Lad $x \in \mathbb{R}$ og $y \in [-1,1]$ være reelle tal. 
Lad $P$ være det logiske udsagn $\mathrm{arccos(y)}=x$ og $Q$ det logiske udsagn $y=\cos(x)$. 
Vis at $P \Rightarrow Q$ er sandt, men at $Q \Rightarrow P$ ikke behøves at være sandt.

```{hint}
:class: dropdown
Til $P \Rightarrow Q$: hvad sker der hvis man anvender $\cos$-funktionen på begge sider af lighedstegnet i $P$?

Til $Q \Rightarrow P$: kan du finde $x \in \mathbb{R}$ og $y \in [-1,1]$ således at $Q$ er sandt, men $P$ ikke?
```

----

## Opgave 4: Cosinus og sinus repetition, del 2.

Denne opgave bygger videre på Opgave 3.

### Spørgsmål a

+++

Der er givet mængderne $\,A=\left[\,0\,,\,2\pi\,\right]\,$ og $\,B=\left[\,-\pi\,,\,\pi\,\right]\,.$

Løs ligningen 
$\,\displaystyle{\cos(x)=\frac{1}{2}}\,$ inden for hver af mængderne $\,A,\,B\,$ og $\,\Bbb R\,.$
 
```{hint}
:class: dropdown
En løsning til ligningen fås direkte fra spørgsmål 3a, fordi ifølge spørgsmål 3b $\mathrm{arccos}(y)=x$ medfører at $y=\cos(x).$ 
Find nu samtlige løsninger i $\mathbb{R}$ ved at lave en skitse af grafen til $\cos$-funktionen.
```

```{admonition} Svar
:class: dropdown
Indenfor $A$ er løsningerne: $\,\frac{\pi}{3}\,$ og $\,\frac{5\pi}{3}\,.$

Indenfor $B$ er løsningerne $\,\frac{-\pi}{3}\,$ og $\,\frac{\pi}{3}\,.$

Indenfor $\mathbb{R}$ er løsningerne $\,\frac{-\pi}{3}+p\cdot 2\pi\,$ og $\,\frac{\pi}{3}+p\cdot 2\pi\,$ hvor $\,p \in \Bbb Z\,.$
```

### Spørgsmål b

+++

Løs ligningen $\,\displaystyle{\sin(x)=-\frac{\sqrt 3}{2}}\,$ inden for hver af mængderne $\,A,\,B\,$ og $\,\Bbb R\,.$
 

```{admonition} Svar
:class: dropdown
Indenfor $A$ er løsningerne: $\,\frac{4\pi}{3}\,$ og $\,\frac{5\pi}{3}\,.$

Indenfor $B$ er løsningerne: $\,\frac{-2\pi}{3}\,$ og $\,-\frac{\pi}{3}\,.$

Indenfor $\mathbb R$ er løsningerne: $\,\frac{4\pi}{3}+p\cdot 2\pi\,$ og $\,\frac{5\pi}{3}+p\cdot 2\pi\,$ hvor $\,p \in \Bbb Z\,.$
```
%
%----
%
%## Opgave 4:  $\mathrm{arccos}$, $\mathrm{arcsin}$ og trigonometriske ligninger
%
%+++
%
%Denne opgave bygger videre på Opgave 7 fra Uge 2 Store Dag. Der er givet mængderne $\, A=\left[\,0\,,\,2\pi\,\right]$ og $\, B=\left[\,-\pi\,,\,\pi\,\right]\,.$
%
%### Spørgsmål a
%
%+++
%
%Løs ligningen $\,\displaystyle{\mathrm e^{\,i\cdot v}= \frac{1}{2}-\frac{\sqrt 3}{2}\,i\,}\,$ inden for mængderne $\,A\,$ og $\,B\,.$
%
%```{admonition} Svar
%:class: dropdown
%Indenfor mængde $A$ er løsningen $\,\frac{5\pi}{3}\,.$
%
%Indenfor mængde $B$ er løsningen $\,-\frac{\pi}{3}\,.$
%```

----

## Opgave 5:  Polære koordinater

+++

### Spørgsmål a

+++

Givet tallene $z_1=1+i\sqrt{3}\,$, $z_2=-1+i\sqrt{3}\,$, $z_3=-1-i\sqrt{3}\,$ og $z_4=1-i\sqrt{3}\,$.

1. Indtegn $z_1$, $z_2$, $z_3$ og $z_4$ i den komplekse talplan og giv tallenes rektangulære koordinater.
2. Find modulus (også kendt som absolutværdi) til $z_1$, $z_2$, $z_3$ og $z_4$. Konkluder at de fire tal ligger på en cirkel med centrum i $0$. Hvad er cirklens radius?
3. Bestem hovedargumenet for $z_1$, $z_2$, $z_3$ og $z_4$ og giv tallenes polære koordinater. 

```{hint}
:class: dropdown
Angående bestemmelse af modulus og hovedargument: se Theorem 4.3.1 (og eventuelt Figur 4.5) fra lærebogen.
```

```{hint}
:class: dropdown
$\mathrm{arctan}(\sqrt{3})=\pi/3$, fordi $\tan(\pi/3)=\frac{\sin(\pi/3)}{\cos(\pi/3)}=\frac{\sqrt{3}/2}{1/2}=\sqrt{3}.$
```

```{admonition} Svar
:class: dropdown
Delvist svar: 

$z_1$: Tallets rektangulære koordinater er $(1,\sqrt{3})$, mens dets polære koordinater er $(2,\pi/3)$.

$z_2$: Tallets rektangulære koordinater er $(-1,\sqrt{3})$, mens dets polære koordinater er $(2,2\pi/3)$.

$z_3$: Tallets rektangulære koordinater er $(-1,-\sqrt{3})$, mens dets polære koordinater er $(2,-2\pi/3)$.

$z_4$: Tallets rektangulære koordinater er $(1,-\sqrt{3})$, mens dets polære koordinater er $(2,-\pi/3)$.
```

### Spørgsmål b

+++

Nogen skal finde de polære koordinater for det komplekse tal $\,-2+2i\,\,$. Vedkommende laver følgende: først beregnes

$$\sqrt{(-2)^2+2^2}$$ 

som giver $\,2\sqrt{2}\,$ til absolutværdien. Efterfølgende beregnes

$$\mathrm{arctan}\left(\frac{2}{-2}\right)$$ 

som giver svaret $\,\displaystyle{-\frac {\pi}4}\,.$

En del af svaret er forkert, men hvor ligger fejlen?


### Spørgsmål c

+++

Find absolutværdi og hovedargument for det følgende komplekse tal:

$$\displaystyle{-\frac{1}{6}+\frac{i}{2\sqrt{3}}}\,.$$

```{admonition} Svar
:class: dropdown
absolutværdi $\frac{1}{3}$, hovedargument $\frac{2}{3} \, \pi$
```


### Spørgsmål d

+++

Om tre komplekse tal $z_1$, $z_2$ og $z_3$ oplyses angående deres modulus og argument at: 

$$|z_1|=4 \quad \text{og} \quad \mathrm{arg}(z_1)=-\pi,$$

$$|z_2|=2 \quad \text{og} \quad \mathrm{arg}(z_2)=4\pi/3$$

og

$$|z_3|=6 \quad \text{og} \quad \mathrm{arg}(z_3)=21\pi/4.$$

Bemærk at tallenes hovedargument ikke er givet, men kun et muligt argument.

1. Bestem tallenes hovedargument.

2. Find tallenes rektangulære form.

```{hint}
:class: dropdown
Hovedargumentet af et komplekst tal skal ligge i intervallet $]-\pi,\pi].$ 
For hvert givet argument, læg et smart valgt multiplum af $2\pi$ til, således at resultatet ligger i $]-\pi,\pi].$ 
Læs eventuelt begyndelsen af Section 4.3 fra lærebogen for mere information om argument og hovedargument af et komplekst tal. 
```

```{hint}
:class: dropdown
Angående rektangulær form: Ligning (4.4) fra lærebogen kan bruges her.
```

```{admonition} Svar
:class: dropdown
1. Hovedargumenterne er: $\pi$, $-2\pi/3$ og $-3\pi/4$.

2. Tallene på rektangulær form: $-4$, $-1-i \, \sqrt{3}$, $-3 \, \sqrt{2} - i \, 3 \, \sqrt{2}$.
```

%----
%
%## Opgave 5: Den komplekse eksponentialfunktion
%
%### Spørgsmål a
%
%+++
%
%Skriv følgende komplekse tal på rektangulær form ved at bruge Eulers formel (Ligning (3.7) fra lærebogen) og indtegn tallene i den komplekse talplan:
%
%1. $e^{i \frac{-\pi}{4}}$
%
%2. $e^{i\frac{\pi}{2}}$
%
%3. $e^{\pi i}$
%
%4. $e^{i \frac{5\pi}{4}}$
%
%Hvad er tallenes (hoved)argumenter?
%
%```{admonition} Svar
%:class: dropdown
%1. Rektangulær form $\frac12 \sqrt{2}- \frac12 \sqrt{2} i$ og argument $-\pi/4$.
%
%2. Rektangulær form $i$ og argument $\pi/2$.
%
%3. Rektangulær form $-1$ og argument $\pi$.
%
%4. Rektangulær form $-\frac12 \sqrt{2}- \frac12 \sqrt{2} i$ og argument $5\pi/4$ (hovedargument ville være $-3\pi/4$).
%
%Opgaven illustrerer at hvis $t$ er et reelt tal, så har det komplekse tal $e^{it}$ modulus $1$ og argument $t$. 
%```
%
%### Spørgsmål b
%
%+++
%
%Skriv følgende komplekse tal på rektangulær form ved at bruge Definition 3.4.1 fra lærebogen:
%
%1. $e^{i\frac{\pi}{2}}.$
%
%2. $3e^{1+\pi i}.$
%
%```{hint}
%:class: dropdown
%Angående rektangulær form af $e^{i\frac{\pi}{2}}$: nu at man bliver bedt at bruge Definition 3.4.1, bemærk at $e^{i\frac{\pi}{2}}=e^{0+i\frac{\pi}{2}}.$
%```
%
%```{admonition} Svar
%:class: dropdown
%1. $i$. Svaret er selvfølgelig det samme som i del 2 af spørgsmål a. Faktisk er Eulers formel et specialtilfælde af Definition 3.4.1 ved at vælge $a=0$ og $b=t$ i Definition 3.4.1. 
%
%2. $-3e$.
%```
%
%### Spørgsmål c
%
%+++
%
%Givet er det kompekse tal $w=1-i\,$.
%
%1. Bestem $|\,w\,|$ og et argument $\arg(w)\,$.
%
%2. Bestem $|\,e^w\,|$ og et argument $\arg(e^w)\,$.
%
%```{hint}
%:class: dropdown
%Angående argumentet af $e^{1-i}$: En mulig fremgangsmåde er at bruge Definition 3.4.1 til at skrive tallet på rektangulær form og så at bruge Theorem 3.3.1 til at bestemme argumentet. 
%```
%
%```{hint}
%:class: dropdown
%Angående argumentet af $e^{1-i}$: Husk at $\tan(x)=\sin(x) / \cos(x)$ og at $\mathrm{arctan}$ er den inverse funktion til $\tan$. 
%```
%
%```{admonition} Svar
%:class: dropdown
%1. $|\,w\,|=\sqrt{2}$ og et muligt argument er $\arg(w)=-\frac{\pi}{4}\,.$
%
%2. $|\,e^w\,|=e$ og et muligt argument $\arg(e^w)=-1\,.$
%
%I begge tilfælde er det angivne argument faktisk hovedargumentet, fordi både $-\frac{\pi}{4}$ og $-1$ ligger i intervallet $]-\pi,\pi]$.
%```
%
%----
%
%## Opgave 3: Eulers formel
%
%+++
%
%### Spørgsmål a
%
%+++
%
%Brug Eulers formel til at omskrive $\cos(3t)\sin(2t)$ på formen $k_1 \sin(c_1t)+k_2 \sin(c_2t).$
%
%```{hint}
%:class: dropdown
%Du kan finde Eulers formel i Ligning (3.7) i lærebogen. Den beslægtede Ligning (3.9) er endnu mere nyttigt i opgavens sammenhæng. 
%```
%
%```{hint}
%:class: dropdown
%I Example 3.5.1 fra lærebogen løses et lignende problem. Eksemplet kunne give inspiration, hvis man er gået i stå.
%```
%
%```{admonition} Svar
%:class: dropdown
%$$\cos(3t)\sin(2t)=\frac12 \sin(5t)-\frac12 \sin(t).$$
%```
%
%----
%
%## Opgave 6: Afledte af den komplekse eksponentialfunktion
%
%Givet to funktioner $f_1: \mathbb{R} \to \mathbb{R}$ og $f_2: \mathbb{R} \to \mathbb{R}$, så kan man definere en funktion $f: \mathbb{R} \to \mathbb{C}$ ved forskriften $f(x)=f_1(x)+if_2(x).$ Vi antager i denne opgave at de afledte funktioner af $f_1$ og $f_2$ findes og vil betegne dem som sædvanligt med $f_1'$ og $f_2'$. I så fald definerer man funktionen $f': \mathbb{R} \to \mathbb{C}$  med forskriften
%
%$$f'(x)=f_1'(x)+i f_2'(x).$$
%
%
%### Spørgsmål a
%
%+++
%
%Lad os nu vælge $f_1(x)=\cos(x)$ og $f_2(x)=\sin(x)$. Vis at i så fald det gælder at $f(x)=e^{ix}$ og $f'(x)=i e^{ix}$ for alle $x \in \mathbb{R}.$ Med andre ord: det gælder at $(e^{ix})'=ie^{ix}.$
%
%```{hint}
%:class: dropdown
%Husk at ifølge Eulers formel $e^{ix}=\cos(x)+i \sin(x)$. 
%```
%
%### Spørgsmål b 
%
%Lad $a$ og $b$ være reelle tal. Bestem to funktioner $f_1: \mathbb{R} \to \mathbb{R}$ og $f_2: \mathbb{R} \to \mathbb{R}$ således at funktionen med forskrift $f(x)=f_1(x)+if_2(x)$ opfylder at
%
%$$f(x)=e^{(a+ib)x} \quad \text{for alle} \quad x \in \mathbb{R}.$$  
%
%```{hint}
%:class: dropdown
%Definition 3.4.1 kan bruges til at omskrive $e^{(a+ib)x}$.
%```
%
%```{admonition} Svar
%:class: dropdown
%$f_1(x)=e^{ax} \cos(bx)$ og $f_2(x)=e^{ax} \sin(bx).$
%```
%
%### Spørgsmål c
%
%Vis at $(e^{(a+ib)x})'=(a+ib)e^{(a+ib)x}.$
%
%```{hint}
%:class: dropdown
%For at beregne $(e^{(a+ib)x})'$, bliver mand nødt til at beregne de afledte funktioner $f_1'$ og $f_2'$ fra spørgsmål b. Dette kan gøres ved at bruge både produktreglen og kædereglen (hvor $a$ og $b$ betragtes som konstanter). Hvis du er i tvivl hvad produktreglen (på engelsk: product rule) og kædereglen (på engelsk: chain rule) præcist indebærer, så kan du slå dem op i Appendiks 2 af lærebogen. 
%```
