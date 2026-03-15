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

(section:uge4S)=

# Opgaver -- Store Dag

----

## Opgave 1: Den komplekse eksponentialfunktion

### Spørgsmål a

+++

Skriv følgende komplekse tal på rektangulær form ved at bruge Eulers formel (Ligning (4.7) fra lærebogen) og indtegn tallene i den komplekse talplan:

1. $e^{i \frac{-\pi}{4}}$

2. $e^{i\frac{\pi}{2}}$

3. $e^{\pi i}$

4. $e^{i \frac{5\pi}{4}}$

Hvad er tallenes (hoved)argumenter?

```{admonition} Svar
:class: dropdown
1. Rektangulær form $\frac12 \sqrt{2}- \frac12 \sqrt{2} i$ og hovedargument $-\pi/4$.

2. Rektangulær form $i$ og hovedargument $\pi/2$.

3. Rektangulær form $-1$ og hovedargument $\pi$.

4. Rektangulær form $-\frac12 \sqrt{2}- \frac12 \sqrt{2} i$ og argument $5\pi/4$ (hovedargument ville være $-3\pi/4$).

Opgaven illustrerer at hvis $t$ er et reelt tal, så har det komplekse tal $e^{it}$ modulus $1$ og argument $t$. 
```

### Spørgsmål b

+++

Skriv følgende komplekse tal på rektangulær form ved at bruge Definition 4.4.1 fra lærebogen:

1. $e^{i\frac{\pi}{2}}.$

2. $3e^{1+\pi i}.$

```{hint}
:class: dropdown
Angående rektangulær form af $e^{i\frac{\pi}{2}}$: nu at man bliver bedt at bruge Definition 4.4.1, bemærk at $e^{i\frac{\pi}{2}}=e^{0+i\frac{\pi}{2}}.$
```

```{admonition} Svar
:class: dropdown
1. $i$. Svaret er selvfølgelig det samme som i del 2 af spørgsmål a. 
Faktisk er Eulers formel (dvs. Ligning (4.7) fra lærebogen) et specialtilfælde af Definition 4.4.1 ved at vælge $a=0$ og $b=t$ i Definition 4.4.1. 

2. $-3e$.
```

----

## Opgave 2: Modulus og argument

Givet er det kompekse tal $w=1-i\,$.

1. Bestem $|\,w\,|$ og et argument $\arg(w)\,$.

2. Bestem $|\,e^w\,|$ og et argument $\arg(e^w)\,$.

```{hint}
:class: dropdown
Angående argumentet af $e^{1-i}$: 
En mulig fremgangsmåde er at bruge Definition 4.4.1 til at skrive tallet på rektangulær form og så at bruge Sætning 4.3.1 til at bestemme hovedargumentet. 
```

```{hint}
:class: dropdown
Angående argumentet af $e^{1-i}$: fra det forrige hint og Sætning 4.3.1 fås at hovedargumentet er 

$$\mathrm{arctan}\left(\frac{e\sin(-1)}{e\cos(-1)}\right).$$

Husk nu at $\tan(x)=\sin(x) / \cos(x)$ og at $\mathrm{arctan}$ er den inverse funktion til $\tan$. 
```

```{admonition} Svar
:class: dropdown
1. $|\,w\,|=\sqrt{2}$ og et muligt argument er $\arg(w)=-\frac{\pi}{4}\,.$

2. $|\,e^w\,|=e$ og et muligt argument $\arg(e^w)=-1\,.$

I begge tilfælde er det angivne argument faktisk hovedargumentet, fordi både $-\frac{\pi}{4}$ og $-1$ ligger i intervallet $]-\pi,\pi]$.
```

----

## Opgave 3: Polær form

+++

Denne opgave bygger videre på Opgave 5a fra Uge 3 Lille Dag. Givet er tallene $z_1=1+i\sqrt{3}\,$, $z_2=-1+i\sqrt{3}\,$, $z_3=-1-i\sqrt{3}\,\,$ og $\,z_4=1-i\sqrt{3}\,$.

### Spørgsmål a

+++

Angiv de fire tal på polær form.

```{hint}
:class: dropdown
Se Definition 4.6.1 hvis man vil genopfriske hvad den polære form af et komplekst tal går ud på. 
Du kan genbruge nogle resultater fra Opgave 5a fra Uge 3 Lille Dag, for at undgå dobbelt arbejde.
```

```{admonition} Svar
:class: dropdown
$z_1=2e^{\frac{\pi}{3} i}$, $z_2=2e^{\frac{2\pi}{3} i}$, $z_3=2e^{\frac{-2\pi}{3} i}$, $z_4=2e^{\frac{-\pi}{3} i}.$
```

### Spørgsmål b

+++

Brug polærformen til at beregne $z_1^{3}$, $z_2^{3}$, $z_3^{3}$ og $z_4^{3}.$ 

```{hint}
:class: dropdown
Man kan bruge sidste del af Sætning 4.6.2 fra lærebogen til at beregne modulus og argument af en heltalspotens af et komplekst tal. 
```

```{admonition} Svar
:class: dropdown
$-8,8,8,-8.$
```

### Spørgsmål c

+++

Vis at $z_2$ og $z_3$ er rødder i polynomiet $Z^3-8$.

```{hint}
:class: dropdown
Se eventuelt Definition 5.1.2 for at læse om hvad det præcist vil sige at være en rod i et polynomium.
```

### Spørgsmål d

+++

Find et polynomium $p(Z)$ i $\mathbb{C}[Z]$ af grad tre som har $z_1$ og $z_4$ som rødder.


```{admonition} Svar
:class: dropdown
$Z^3+8$ er et gyldigt svar, men der er flere muligheder.
```

----

## Opgave 4: Førstegradspolynomier

+++

Et polynomium $p(Z) \in \mathbb{C}[Z]$ er givet ved $p(Z)=(2-i)Z+i.$

### Spørgsmål a

+++

Find en rod i polynomiet $p(Z)$.

```{admonition} Svar
:class: dropdown
$\frac15-\frac25 i$.
```

### Spørgsmål b

+++

Løs polynomiumsligningerne $p(z)=2$ og $p(z)=-2+2i$.

```{admonition} Svar
:class: dropdown
Ligningen $p(z)=2$ har løsning $1$.

Ligningen $p(z)=-2+2i$ har løsning $-1$.
```

----

## Opgave 5: Andengradspolynomier

### Spørgsmål a

+++

Find samtlige rødder i polynomiet $Z^2+2Z+5\,$.

```{hint}
:class: dropdown
Sætning 5.2.1 fra lærebogen angiver hvordan man kan finde rødderne.
```

### Spørgsmål b

+++

Find samtlige rødder i polynomiet $(Z^2+2Z+5)\cdot (Z^2-4)$.

```{hint}
:class: dropdown
Man behøver ikke at gange ind i parentes først. 
Overvej derimod hvad det betyder for et komplekst tal at være rod i polynomiet $(Z^2+2Z+5)\cdot (Z^2-4).$ 
```

```{admonition} Svar
:class: dropdown
Polynomiet har fire rødder: $z_1=-1+2i$, $z_2=-1-2i$, $z_3=2$ og $z_4=-2$.
```

----

## Opgave 6: Polynomiumsaritmetik

Følgende tre polynomier i $\mathbb{C}[Z]$ er givet:

$$p_1(Z)=2Z^3-Z-1,$$

$$p_2(Z)=2+Z,$$

$$p_3(Z)=-1+0Z^{10}+(1+i)Z^5.$$

### Spørgsmål a

+++

Bestem grad og ledende koefficient af de tre givne polynomier.

```{hint}
:class: dropdown
Angående polynomiet $p_3(Z)$: bemærk at $p_3(Z)$ er det samme polynomium som $(1+i)Z^5-1$.
```

```{admonition} Svar
:class: dropdown
$p_1(Z)$ har grad $3$ og ledende koefficient $2$.

$p_2(Z)$ har grad $1$ og ledende koefficient $1$.

$p_3(Z)$ har grad $5$ og ledende koefficient $1+i$.
```


### Spørgsmål b

+++

Beregn $p_1(Z)+p_2(Z)+p_3(Z)$, $ip_3(Z)$ og $p_1(Z)p_2(Z)$.

```{admonition} Svar
:class: dropdown
$p_1(Z)+p_2(Z)+p_3(Z)=(1+i)Z^5+2Z^3.$ 

$i \cdot p_3(Z)=(-1+i)Z^5-i.$ 

$p_1(Z)p_2(Z)=2Z^4+4Z^3-Z^2-3Z-2.$
```

----

## Opgave 7: Ligninger med eksponentialfunktionen

+++

### Spørgsmål a

+++

Givet tallene $\,w_1=1\,,\,w_2=e\,$ og $\,w_3=2i\,$. For $n=1,\dots,3$, bestem mængden af samtlige løsninger i $\mathbb C$ for ligningerne 

$$e^z=w_n.$$ 

```{hint}
:class: dropdown
Lemma 4.6.1 fra lærebogen beskriver hvordan man finder løsninger til en ligning på formen $e^z=w$. 
```

```{hint}
:class: dropdown
Et vilkårligt argument af $w$ er lige med hovedargumentet af $w$ plus et heltalsmultiplum af $2\pi$.
```

```{admonition} Svar
:class: dropdown
Ifølge Lemma 4.6.1 har hver løsning til ligningen $e^z=1$ formen $z=i \mathrm{arg}(1)$. 
Hovedargumentet af $1$ er $0$, men alle andre mulige argumenter af $1$ er lige med hovedargumentet plus et heltalsmultiplum af $2\pi$. 
Derfor har ligningen $e^z=1$ løsningsmængde $\{ ip2\pi \, \mid \, p \in \mathbb{Z}\}.$ 

$e^z=e$ har løsningsmængde $\{ 1+ip2\pi \, \mid \, p \in \mathbb{Z}\}.$ 

%$e^z=i$ har løsningsmængde $\left\{ i(\frac{\pi}{2}+p2\pi) \, \mid \, p \in \mathbb{Z}\right\}.$ 

$e^z=2i$ har løsningsmængde $\left\{ \ln(2)+i(\frac{\pi}{2}+p2\pi) \, \mid \, p \in \mathbb{Z}\right\}.$ 
```

### Spørgsmål b

+++
 
Bestem mængden af samtlige løsninger for ligningen

$$(e^z-1)(e^z-2i)=0\,.$$

```{admonition} Svar
:class: dropdown
Løsningsmængden er foreningsmængden af løsningsmængderne for ligningerne svarende til $n=1$ og $n=3$ ovenfor.
```

### Spørgsmål c
Vis den første påstand i Sætning 4.4.2, nemlig at $\,e^z \neq 0\,$ for alle $\,z\in\mathbb C\,$.

```{hint}
:class: dropdown
Hvis man skriver $z=a+bi$ på rektangulær form, så medfører Definition 4.4.1 at $e^z=e^a \cdot (\cos(b)+\sin(b) i)$. 
Kan dette udtryk være nul?
```

----

## Opgave 8: Kompleks konjugering og rødder i polynomier

### Spørgsmål a

+++

1. Bestem $\overline{2-3i}$ og $\overline{10+12i}$. Angiv svarene på rektangulær form.

2. Bestem $\overline{5 e^{i\pi/3}}$. Angiv svaret på polær form,


```{hint}
:class: dropdown
$\overline{z}$ betegner den kompleks konjugerede af et komplekst tal $z$, se eventuelt Definition 4.2.3 fra lærebogen.
```

```{hint}
:class: dropdown
Angående 2.: Lemma 5.3.1 og Lemma 5.3.2 fra lærebogen kan hjælpe.
```

```{admonition} Svar
:class: dropdown
1. $\overline{2-3i}=2+3i$ og $\overline{10+12i}=10-12i$.

2. $\overline{5 e^{i\pi/3}}=\overline{5} \overline{e^{i\pi/3}}=5 e^{-i\pi/3}$.
```

+++

### Spørgsmål b

Det oplyses at det komplekse tal $1+i$ er rod i polynomiet $Z^3+(2+3i)Z+3-7i$. 
Vis at $1-i$ er rod i polynomiet $Z^3+(2-3i)Z+3+7i$ ved at bruge egenskaberne af den komplekse konjugering som beskrevet i Lemma 5.3.1 fra lærebogen.

```{hint}
:class: dropdown
Det oplyses at det komplekse tal $1+i$ er rod i polynomiet $Z^3+(2+3i)Z+3-7i$. Derfor vides at $(1+i)^3+(2+3i)(1+i)+3-7i=0.$ 
Hvad sker der hvis man tager den kompleks konjugerede af udtrykkene på begge sider af lighedstegnet?
```

+++

### Spørgsmål c

Det oplyses nu at det komplekse tal $1+i$ er rod i polynomiet $Z^4+Z^2-2Z+6$. 
Vis at $1-i$ også er rod i dette polynomium.

```{hint}
:class: dropdown
Dette gang oplyses at det komplekse tal $1+i$ opfylder $(1+i)^4+(1+i)^2 -2(1+i)+6=0.$ 
Undersøg hvad der sker hvis man tager den kompleks konjugerede af udtrykkene på begge sider af lighedstegnet.
```

%----
%
%## Opgave 7: Polynomier med reelle koefficienter
%
%### Spørgsmål a
%
%+++
%
%Check uden brug af løsningsformel at $-1+2i$ er rod i polynomiet $3Z^2+6Z+15.$
%
%```{hint}
%:class: dropdown
%Definition 5.1.2 afslører hvordan man checker at et komplekst tal er en rod.
%```
%
%### Spørgsmål b
%
%+++
%
%Find en anden rod i polynomiet $3Z^2+6Z+15$ uden at bruge løsningsformlen.
%
%```{hint}
%:class: dropdown
%Kan teorien sidst i Afsnit 5.3 bruges?
%```

----

## Opgave 9: Heltalspotenser og polær form

### Spørgsmål a

+++

Brug polærformen af det komplekse tal $-1+\sqrt{3}i$ fra Opgave 3 på lignende måde som i Eksempel 4.6.2 til at vise at 

$$(-1+\sqrt{3}i)^{10}=2^{9}(-1+\sqrt{3}i).$$ 

### Spørgsmål b

+++

Lad $n$ være et naturligt tal. Vis følgende:

$$(-1+\sqrt{3}i)^{3n}=2^{3n},$$ 

$$(-1+\sqrt{3}i)^{3n+1}=2^{3n}(-1+\sqrt{3}i),$$ 

og

$$(-1+\sqrt{3}i)^{3n+2}=2^{3n+1}(-1-\sqrt{3}i).$$ 

```{hint}
:class: dropdown
Vis først at $(-1+\sqrt{3}i)^{3}=2^3$. Hvad kan nu siges om $(-1+\sqrt{3}i)^{3n}\,$? 
```

```{hint}
:class: dropdown
Hvis $(-1+\sqrt{3}i)^{3}=2^3$, så gælder $((-1+\sqrt{3}i)^{3})^n=(2^3)^n\,$, $(-1+\sqrt{3}i)^{3n+1}=(2^3)^n(-1+\sqrt{3}i)\,$ og $(-1+\sqrt{3}i)^{3n+2}=(2^3)^n(-1+\sqrt{3}i)^2$. 
```

%----
%
%## Opgave 9: Komplekse tal og Pythagoræiske tripler
%
%Et Pythagoræisk tripel $(a,b,c)$ består ud af tre naturlige tal således at $a>b$ og $a^2+b^2=c^2$. Et eksempel er $(4,3,5).$
%
%### Spørgsmål a
%
%+++
%
%Vis at hvis et tripel $(a,b,c)$ af naturlige tal er et Pythagoræisk tripel, så gælder at det komplekse tal $z=\frac{a}{c}+\frac{b}{c}i$ opfylder $|z|=1$ og $\mathrm{Re}(z)>\mathrm{Im}(z)$.
%
%### Spørgsmål b
%
%+++
%
%Lad os nu antage at et komplekst tal $z$ af opfylder $|z|=1$ og $\mathrm{Re}(z)>\mathrm{Im}(z)$ og at $z$ kan skrives på formen $z=\frac{a}{c}+\frac{b}{c}i$, hvor $a,b$ og $c$ er naturlige tal. Vis at $(a,b,c)$ er et Pythagoræisk tripel.
%
%+++
%
%### Spørgsmål c
%
%+++
%
%Brug ovenstående indsigter og komplekse tal til at konstruere andre Pythagoræiske tripler ud fra triplet $(4,3,5).$
%
%```{hint}
%:class: dropdown
%Hvis tallet $z=\frac{a}{c}+\frac{b}{c}i$ giver anledning til det Pythagoræiske tripel $(a,b,c)$, hvad med tallet $z^2$ (eller eventuelt $i \cdot \overline{z}^2$)?
%```
%
%----
%
%## Opgave 9: Afledte af den komplekse eksponentialfunktion
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
%
%----
%
%## Opgave 6: Binome ligninger
%
%### Spørgsmål a
%
%+++
%
%Løs den binome ligning $z^3=-8i$.
%
%```{hint}
%:class: dropdown
%Binome ligninger, dvs. en ligning på formen $z^n=w$, bliver løst i Sætning 5.4.1. I dette tilfælde bliver $n=3$ og $w=-8i$.  
%```
%
%```{admonition} Svar
%:class: dropdown
%$z^3=-8i$ har løsninger $2i$, $\sqrt{3}-i$ og $-\sqrt{3}-i$.
%```
%
%----
%
%## Opgave 5: Binome andengradsligninger med reel højreside
%
%+++
%
%### Spørgsmål a
%
%+++
%
%Lad $r$ være et positivt reelt tal. Brug Sætning 5.2.1 til at gøre rede for at ligningen 
%
%$$z^2=-r$$
%
%har netop to løsninger som er givet ved $-i\sqrt{r}$ og $i\sqrt{r}$.
%
%```{hint}
%:class: dropdown
%```
%
%### Spørgsmål b
%
%+++
%
%Løs spørgsmål a igen, men nu ved at bruge Sætning 5.4.1. 
%
%```{hint}
%:class: dropdown
%Hvis du vil bruge Sætning 5.4.1, som udtaler sig om ligningen $z^n=w$, så bliver $n=2$ og $w=-r$.  
%```
%
%```{hint}
%:class: dropdown
%Hvad er hovedargumentet af et negativt reelt tal?
%```
%
%### Spørgsmål c
%
%+++
%
%Løs ligningen $z^2=-16$. 
%%Hvad er løsninger til ligningen $z^2=16$? 
%
%```{admonition} Svar
%:class: dropdown
%$z^2=-16$ har løsninger $-4i$ og $4i$.
%%
%%$z^2=16$ har løsninger $-4$ og $4$.
%```
%
%%### Spørgsmål d
%%
%%+++
%%
%%Løs ligningerne $z^2=17$ og $z^2=-17$.
%%
%%```{admonition} Svar
%%:class: dropdown
%%$z^2=17$ har løsninger $-\sqrt{17}$ og $\sqrt{17}$.
%%
%%$z^2=-17$ har løsninger $-\sqrt{17} \, i$ og $\sqrt{17}\, i$.
%%```