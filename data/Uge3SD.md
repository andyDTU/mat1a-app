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

(section:uge3S)=

# Opgaver -- Store Dag

## Opgave 1: Tallet i

+++

I denne opgave får du nogle indledende erfaringer med de komplekse tal. 

### Spørgsmål a

+++

Hvad er $i^2$, $i^3$, $i^4$, $i^5$, $(-i)^2$, $(-i)^3$, $(-i)^4$ og $(-i)^{-5}\,$?

```{hint}
:class: dropdown
Hvis du er i tvivl hvordan man simplificerer $i^2$, se Definition 4.1.1 fra lærebogen.
```

```{admonition} Svar
:class: dropdown
$$-1,-i,1,i,-1,i,1,i$$
```

### Spørgsmål b

+++

Hvad er realdelen og imaginærdelen af de komplekse tal $10+i$, $3$ og $i$? 
Hvad med realdelen og imaginærdelen af tallet $-5-i7\,$?

```{hint}
:class: dropdown
Hvis du er i tvivl hvad real- og imaginærdelen af et komplekst tal er, så kan du læse om det i lærebogen mellem Definition 4.1.1. og Eksempel 4.1.1.
```

```{admonition} Svar
:class: dropdown
$10+i$: realdelen er $10$ og imaginærdelen er $1$.

$3$: realdelen er $3$ og imaginærdelen er $0$.

$i$: realdelen er $0$ og imaginærdelen er $1$.

$-5-i7$: realdelen er $-5$ og imaginærdelen er $-7$.
```


### Spørgsmål c

+++

Hvad er $\mathrm{Re}(-5-7i)$ og $\mathrm{Im}(-5-7i)$?


```{admonition} Svar
:class: dropdown
$\mathrm{Re}(-5-7i)=-5$ og $\mathrm{Im}(-5-7i)=-7.$
```

### Spørgsmål d

+++

Skriv de komplekse tal $\,7i-5\,$, $\,i(7i-5)\,$ og $\,i(7i-5)i\,$ på rektangulær form.

```{hint}
:class: dropdown
I Definition 4.2.2 bliver forklaret hvordan man ganger to komplekse tal sammen.
```

```{admonition} Svar
:class: dropdown
$$-5+7i \, \, , \, \, -7-5i \, \, \text{og} \, \, 5-7i.$$
```

----

## Opgave 2: Den komplekse talplan

+++

### Spørgsmål a

+++

Betragt de følgende ti tal: $-2,\,0,\,i,\,2-i,\,1+2i,\,1,\,-2+3i,\,-5i,\,3\,$ og $\,-1-2i\,.$

Hvilke af dem er komplekse, hvilke er reelle, og hvilke er rent imaginære?

Indtegn de ti tal i den komplekse talplan.

```{hint}
:class: dropdown
Hvis du vil genopfriske hvordan man indtegner tal i den komplekse talplan eller hvad "rent imaginær" betyder, så kan du finde det i lærebogens Afsnit 4.1, især i teksten efter Definition 4.1.1.
```

```{admonition} Svar
:class: dropdown
Alle ti tal er komplekse tal, tallene $-2,0,1,3$ er reelle tal, tallene $0,i,-5i$ er rent imaginære tal. Bemærk at $0$ kan opfattes både som reelt tal og som ren imaginært tal, fordi $0$ ligger på både den reelle akse og den imaginære akse. 
```

### Spørgsmål b

+++

Givet tallet $z=4+i\,$.

1. Indtegn de fire tal $\,z\,,\,iz\,,\,i^2z\,$ og $\,i^3z\,$ i den komplekse talplan.
2. Hvad sker der geometrisk i den komplekse talplan når et komplekst tal bliver ganget med $i\,$?
3. Og divideret med $i\,$?


----

## Opgave 3: Grundlæggende udregninger

+++

### Spørgsmål a

+++

Find ved hjælp af elementære udregninger den rektangulære form for de følgende komplekse tal.

1. $(5+i)(1+9i).$

2. $i+i^2+i^3+i^4.$

3. $\displaystyle{\frac{1}{1+3i}+\frac{1}{(1+3i)^2}}.$

4. $\displaystyle{\frac{1}{(1+i)^4}}.$

5. $\displaystyle{\frac{5+i}{2-2i}}.$

6. $\displaystyle{\frac{3i}{4}}\,$ og $\displaystyle{\frac{i2}{4}}.$

```{hint}
:class: dropdown
Hvis man vil simplificere en brøk hvor både tæller og nævner er komplekse tal på rektangulær form, så er Ligning (4.2) fra lærebogen nyttig. 
Se eventuelt også Eksempel 4.2.3 fra lærebogen.
```

```{admonition} Svar
:class: dropdown
1. $-4+46i$, 2. $0$, 3. $\frac{1}{50} -\frac{9}{25} i$, 4. $- \frac{1}{4}$, 5. $1+ \frac{3}{2}i$, 6. $\frac{3}{4} i$ og $\frac{1}{2} i$.
```

### Spørgsmål b

+++

Givet er to reelle tal $a$ og $b\,$, ikke begge to lig med $0$.

1. Hvorfor er tallet $\,\,\displaystyle{\frac{1}{a+ib}}\,\,$ ikke på rektangulær form?

2. Udregn $\mathrm{Re}\displaystyle{\left(\frac{1}{a+ib}\right)}\,$ og $\mathrm{Im}\displaystyle{\left(\frac{1}{a+ib}\right)}\,\,$.



```{admonition} Svar
:class: dropdown
$\mathrm{Re}\displaystyle{\left(\frac{1}{a+ib}\right)}\, = \frac{a}{a^2+b^2}$ og $\mathrm{Im}\displaystyle{\left(\frac{1}{a+ib}\right)} = -\frac{b}{a^2+b^2}$.
```

----

## Opgave 4: Konjugering


I Definition 4.2.3 blev den komplekst konjugerede $\overline{z}$ af et komplekst tal $z$ defineret. 
Læs eventuelt denne definition først hvis du er i tvivl om hvad $\overline{z}$ præcist betyder.

+++

### Spørgsmål a

+++

Vis at $\overline{\overline{2+3i}}=2+3i$ og at $\overline{(2+3i)\cdot (2+3i)}=\overline{2+3i}\cdot \overline{2+3i}$. Vis nu at mere generelt $\,\overline{\overline{z}}=z\,$ og at $\,\overline{z_1\cdot z_2}=\overline{z_1}\cdot\overline{z_2}\,$ for all komplekse tal $z_1$ og $z_2$. 

```{hint}
:class: dropdown
Hvis $z=a+bi$ er et komplekst tal på rektangulær form, hvad sker der hvis man anvender komplekst konjugering to gang i træk? På lignende måde, prøv at beregne både $\,\overline{z_1\cdot z_2}$ og $\overline{z_1}\cdot\overline{z_2}\,$ hvis $z_1=a+bi$ og $z_2=c+di$ er tallene $z_1$ og $z_2$ skrevet på rektangulær form.
```

### Spørgsmål b

+++

Lad $z=a+ib\neq 0$ være et givet komplekst tal. 
Hvilket komplekst tal svarer til spejlbilledet af $z$ i

1. nulpunktet af den komplekse plan,

2. den reelle akse,

3. den imaginære akse,

4. linjen med hældning $1$ gennem nulpunktet?

Angiv facit både på rektangulær form og ved hjælp af formler hvor $z$, $\overline{z}$ og $i$ kan indgå. 

```{hint}
:class: dropdown
Det kan give et godt overblik først at tegne det hele ind i den komplekse talplan.
```

```{admonition} Svar
:class: dropdown
1. Rektangulær form: $-a-bi$. Formel: $-z$. 

2. Rektangulær form: $a-bi$. Formel: $\overline{z}$.

3. Rektangulær form: $-a+bi$. Formel:  $-\overline{z}$.

4. Rektangulær form: $b+ai$. Formel: $i\cdot  \overline{z}$.
```
----

## Opgave 5: Absolutværdi

+++

Ved absolutværdien $\,\left|z\right|\,$ af et komplekst tal $z$ forstås afstand mellem $0$ og $z$ i den komplekse talplan. 
Se eventuelt Figur 4.4. Absolutværdien kaldes også for modulus.

### Spørgsmål a

+++

Givet er reelle tal $a,b$ og et komplekst tal på rektangulær form $\,z=a+ib\,.$  Bestem $\,\left|z\right|\,.$ Mere konkret, hvad er $|2+3i|$?


```{admonition} Svar
:class: dropdown
$|z|=\sqrt{a^2+b^2}$ og $|2+3i|=\sqrt{2^2+3^2}=\sqrt{13}$.
```

### Spørgsmål b

+++

Undersøg hvilken geometrisk betydning for to vilkårlige komplekse tal $\,z_1\,$ og $\,z_2$ absolutværdien $\,\left|z_1-z_2\right|\,$ har. 
Illustrér gerne med eksempler.


```{admonition} Svar
:class: dropdown
$\,\left|z_1-z_2\right|\,$ giver afstanden mellem $z_1$ og $z_2$ i den komplekse talplan.
```

### Spørgsmål c

+++

En mængde i den komplekse talplan er givet ved 

$$\big\{z \in {\mathbb C} \, \mid \,  |z-1|\, = \, 3\big\}\,.$$

Giv en geometrisk beskrivelse af mængden.


```{admonition} Svar
:class: dropdown
Mængden beskriver en cirkel i den komplekse talplan med centrum i $1$ og radius $3$.
```

----

## Opgave 6: Mængder i den komplekse talplan

+++

I den komplekse talplan betragter vi talmængden $\,M=\left\{z \,\, | \,\, |z-1+2i|\leq 3\,\right\}\,.$

### Spørgsmål a

+++

Beskriv $M$ og indtegn $M$ i den komplekse talplan.


### Spørgsmål b

+++

Bestem $M \cap \mathbb{R}$, dvs. den delmængde af $\,M\,$ bestående af alle reelle tal i $M$.

```{hint}
:class: dropdown
Indtegn først $M \cap \mathbb{R}$ i tegningen fra spørgsmål a.
```

```{admonition} Svar
:class: dropdown
$M \cap \mathbb{R}=\left[\,1-\sqrt 5\,,\,1+\sqrt 5\,\right]\,.$
```

----

## Opgave 7: Parenteser og regnearternes hierarki

+++

### Spørgsmål a

+++

Givet tallet $\,\,z=3(i-10)-5(7-2i)-i(3i-5)+3i(i-5)\,.\,$ Find den rektangulære form for $z\,.$

```{hint}
:class: dropdown
I udtryk hvor både multiplikation og addition/subtraktion indgår, udregnes multiplikationerne først.
```

```{admonition} Svar
:class: dropdown
$$z=-65 +3i.$$
```

### Spørgsmål b

+++

Givet er tallene 

$$a=5-i(3-i)+6i\,\,\, \mathrm{og} \,\,\,b=-5-4(-2i+1)\,.$$ 

Skriv tallet $\,z=a+ib\,$ på rektangulær form.


```{admonition} Svar
:class: dropdown
$$z=-4-6i.$$
```

----

## Opgave 8: Brøker

+++

### Spørgsmål a

+++

Bestem realdelen og imaginærdelen af $(-2+3i)/i$ og skriv tallet på rektangulær form.

```{hint}
:class: dropdown
Du kan finde nogle eksempler på hvordan man skriver en brøk af komplekse tal på rektangulær form i Example 4.2.3 fra lærebogen. 
```


```{admonition} Svar
:class: dropdown
$$(-2+3i)/i=3+2i.$$
```

### Spørgsmål b

+++

Reducér det følgende udtryk og skriv det på rektangulær form.
$\displaystyle{\frac{3}{5}- \frac{3-2i}{2+i}}$ 

```{hint}
:class: dropdown
Det er nok nemmest først at skrive den sidste brøk på rektangulær form. Hertil kan man bruge en lignende fremgangsmåde som i spørgsmål a.
```

```{admonition} Svar
:class: dropdown
$$\frac{3}{5}- \frac{3-2i}{2+i}=-\frac{1}{5} + \frac{7}{5} i.$$
```

### Spørgsmål c

+++

Lad $b,c$ og $d$ være følgende reelle tal:

$$b=5 \,,\, \, c=\frac{6}{7} \,,\, \, d=\frac{2}{3} \,$$

Find følgende tal:

$$c+d\,,\, \, d \cdot b\,,\, \,\frac{b}{d}, \, \, \, \frac{d}{c}.$$


### Spørgsmål d

+++

Lad $k,n,m$ og $s$ være følgende komplekse tal:

$$k=1+i \cdot \sqrt{3} \,,\, \,  n=5 \cdot  i \,,\, \,  m=1+i \,,\, \, s=i \cdot 4 +3.$$

Skriv følgende komplekse tal på rektangulær form:

$$\frac{m}{n} \,,\, \, \frac{k}{s} \,,\, \,  \frac{1}{m} + s.$$


----


## Opgave 9:  Ordning af komplekse tal

+++

I de reelle tal har vi den velkendte *mindre end* ordningsrelation $\,<\,$ som for alle $\,a,b\,$ og $\,c\,$ i $\mathbb R$ opfylder:

1. Kun én af påstandene $\,a<b,$ $\,b<a$ eller $\,a=b\,$ er sand.

2. Hvis $\,a<b\,$ og $\,b<c\,$ så er $\,a<c\,.$

3. Hvis $\,a<b\,$ så er $\,a+c<b+c\,.$ 

4. Hvis $\,a<b\,$ og $\,0<c\,$ så er $\,ac<bc\,.$


### Spørgsmål a

+++

Afprøv de fire påstande med nogle eksempler.


### Spørgsmål b

+++

Vis at ordningsrelationen $\,<\,$ fra de reelle tal IKKE kan udvides til at gælde for alle komplekse tal. Mere præcist, vis at der ikke findes en ordningsrelationen $\,<\,$ på $\mathbb C$ som udvider ordningsrelationen $\,<\,$ fra de reelle tal og som opfylder de fire punkter ovenfor for alle $\,a,b\,$ og $\,c\,$ i $\mathbb C$.  

```{hint}
:class: dropdown
Forsøg at finde et modstridsbevis. Det vil sige: antag at udvidelsen findes og forsøg at nå frem til en modstrid.
```

```{hint}
:class: dropdown
Hvis udvidelsen findes, så gælder enten $0<i$ eller $i<0$ pga. egenskab 1. Forsøg at nå frem til en modstrid i hvert tilfælde.
```
