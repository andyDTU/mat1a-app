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

# Opgaver -- Lille Dag

----

## Opgave 1: Polynomier med reelle koefficienter

### Spørgsmål a

+++

Check uden brug af løsningsformel at $-1+2i$ er rod i polynomiet $3Z^2+6Z+15.$

```{hint}
:class: dropdown
Definition 5.1.2 afslører hvordan man checker at et komplekst tal er en rod.
```

### Spørgsmål b

+++

Find en anden rod i polynomiet $3Z^2+6Z+15$ uden at bruge løsningsformlen.

```{hint}
:class: dropdown
Kan teorien sidst i Afsnit 5.3 bruges?
```

```{admonition} Svar
:class: dropdown
Fordi polynomiet har reelle koefficienter, er den kompleks konjugerede af $-1+2i$ også rod i polynomiet. 
Med andre ord: $-1-2i$ er også rod i $3Z^2+6Z+15$.
```

----

## Opgave 2: Binome ligninger

### Spørgsmål a

+++

Løs den binome ligning $z^3=-8i$. 
Løsningerne ønskes angivet på rektangulær form.

```{hint}
:class: dropdown
Binome ligninger, dvs. en ligning på formen $z^n=w$, bliver løst i Sætning 5.4.1. I dette tilfælde bliver $n=3$ og $w=-8i$.  
```

```{admonition} Svar
:class: dropdown
$z^3=-8i$ har løsninger $2i$, $\sqrt{3}-i$ og $-\sqrt{3}-i$.
```

----

## Opgave 3: En andengradsligning

+++

Find samtlige rødder i polynomiet $Z^2+i$ indenfor de komplekse tal. Angiv rødderne både på polærform og rektangulær form.

```{hint}
:class: dropdown
En rod $z$ i polynomiet $Z^2+i$ opfylder ligningen $z^2+i=0$. Denne ligning kan omskrives til en binom ligning.
```

```{hint}
:class: dropdown
Polærformen af tallet $-i$ er $1 \cdot e^{-i \pi/2}.$
```

```{admonition} Svar
:class: dropdown
Rødderne i $Z^2+i$ på polærform er $e^{-i\pi/4}$ og $e^{i3\pi/4}$, på rektangularform $\sqrt{2}/2-i\sqrt{2}/2$ og $-\sqrt{2}/2+i\sqrt{2}/2$.
```

----

## Opgave 4: Binome andengradsligninger med reel højreside

+++

### Spørgsmål a

+++

Lad $r$ være et positivt reelt tal. Brug Sætning 5.2.1 til at gøre rede for at ligningen 

$$z^2=-r$$

har netop to løsninger som er givet ved $-i\sqrt{r}$ og $i\sqrt{r}$.

```{hint}
:class: dropdown
```

### Spørgsmål b

+++

Løs spørgsmål a igen, men nu ved at bruge Sætning 5.4.1. 

```{hint}
:class: dropdown
Hvis du vil bruge Sætning 5.4.1, som udtaler sig om ligningen $z^n=w$, så bliver $n=2$ og $w=-r$.  
```

```{hint}
:class: dropdown
Hvad er hovedargumentet af et negativt reelt tal?
```

### Spørgsmål c

+++

Løs ligningen $z^2=-16$. 
%Hvad er løsninger til ligningen $z^2=16$? 

```{admonition} Svar
:class: dropdown
$z^2=-16$ har løsninger $-4i$ og $4i$.
%
%$z^2=16$ har løsninger $-4$ og $4$.
```

%### Spørgsmål d
%
%+++
%
%Løs ligningerne $z^2=17$ og $z^2=-17$.
%
%```{admonition} Svar
%:class: dropdown
%$z^2=17$ har løsninger $-\sqrt{17}$ og $\sqrt{17}$.
%
%$z^2=-17$ har løsninger $-\sqrt{17} \, i$ og $\sqrt{17}\, i$.
%```

----

## Opgave 5: En binom ligning i et udtryk med eksponentialfunktionen

I denne opgave løses ligningen $(e^z)^4=1$ i den ubekendte $z$ indenfor de komplekse tal på to forskellige måder.

+++

### Spørgsmål a

Metode 1: Skrives $w=e^z$, så kan man omskrive ligningen $(e^z)^4=1$ til $w^4=1$. Løs nu først for $w$ og løs bagefter for $z$.

```{hint}
:class: dropdown
Ligningen $w^4=1$ er en binom ligning. Dens højresiden kan skrives som $1=1\cdot e^{0i}\,$.
```

```{hint}
:class: dropdown
Den binome ligning $w^4=1$ har løsninger $w_1=1$, $w_2=i$, $w_3=-1$ og $w_4=-i$. 
Derfor gælder $(e^z)^4=1$ hvis og kun hvis $e^z=1$ eller $e^z=i$ eller $e^z=-1$ eller $e^z=-i$.
De sidstnævnte fire ligninger kan løses vha. Lemma 4.6.1.
```

```{admonition} Svar
:class: dropdown
$e^z=1$ har løsninger $z=2\pi p i$ hvor $p \in \mathbb{Z}$

$e^z=i$ har løsninger $z=(\pi/2+2\pi p)i$ hvor $p \in \mathbb{Z}$

$e^z=-1$ har løsninger $z=(\pi+2\pi p)i$ hvor $p \in \mathbb{Z}$

$e^z=-i$ har løsninger $z=(-\pi/2+2\pi p)i$ hvor $p \in \mathbb{Z}$

Samtlige løsninger er derfor alle komplekse tal $z$ som kan skrives på én af disse fire måder.
```

+++

### Spørgsmål b

Metode 2: Bruges Sætning 4.4.2, så fås $(e^z)^4=e^{4z}$. 
Derfor kan man omskrive ligningen $(e^z)^4=1$ til $e^{4z}=1$. 
Brug nu Lemma 4.6.1 for at finde løsningerne og tjek at svarene fra spørgsmål a og b giver de samme løsninger.

```{admonition} Svar
:class: dropdown
Man får løsningerne $z=(2\pi p i)/4=\pi p i/2$ hvor $p \in \mathbb{Z}$. 
Når $p$ gennemløber alle hele tal i $\mathbb{Z}$, fås de samme løsninger som i spørgsmål a.
```