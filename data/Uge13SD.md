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


(section:uge13S)=

# Opgaver -- Store Dag

----

+++


## Opgave 1: Homogen eller inhomogen?

Er følgende differentialligninger og systemer af differentialligninger homogene eller inhomogene?

1. $f''(t)=f'(t)-2f(t)$.

2. $f'(t)-t\cdot f(t)-e^{-3t}=0$.

3. $\left[\begin{array}{c} f'_1(t)\\ f'_2(t) \end{array}\right] =\left[\begin{array}{cc} 4 & 6 \\ -2 & 7 \end{array}\right] \cdot \left[\begin{array}{c} f_1(t)\\ f_2(t) \end{array}\right]+\left[\begin{array}{c} 1\\ 1\end{array}\right].$

4. $\left\{ \begin{array}{lcr} f'_1(t) & = & f_2(t)\\ f'_2(t) & = & f_1(t)-f_2(t)\\ \end{array} \right.$

```{admonition} Svar
:class: dropdown
1. Ligningen kan omskrives til $f''(t)-f'(t)+2f(t)=0$. Differentialligningen er derfor homogen (se eventuelt Definition 13.3.1 fra lærebogen).

2. Ligningen kan omskrives til $f'(t)-t\cdot f(t)=e^{-3t}$. Differentialligningen er derfor inhomogen.

3. Differentialligningssystemet er inhomogent (se eventuelt Definition 13.2.1 fra lærebogen).

4. Differentialligningssystemet kan omskrives til 

$$\left[\begin{array}{c} f'_1(t)\\ f'_2(t) \end{array}\right] =\left[\begin{array}{cc} 0 & 1\\1 & -1 \end{array}\right] \cdot \left[\begin{array}{c} f_1(t)\\ f_2(t) \end{array}\right].$$

Derfor er differentialligningssystemet homogent.
```

+++

----

+++


## Opgave 2: En homogen andenordens differentialligning

Givet den homogene reelle differentialligning

$$f''(t)+3f'(t)-4f(t)=0.$$

Find dens fuldstændige løsning.

```{hint}
:class: dropdown
Find først rødderne i ligningens karakteristiske polynomium. 
Se Afsnit 13.3 fra lærebogen for flere oplysninger og eksempler.
```

```{admonition} Svar
:class: dropdown
$$f(t)=c_1 \cdot e^t+c_2 \cdot e^{−4t}, \quad c_1,c_2 \in \mathbb{R}.$$
```

+++

----

+++

## Opgave 3: Flere homogene andenordens differentialligninger

Givet følgende homogene reelle differentialligninger. Find deres fuldstændige løsning.

1. $$f''(t)-6f'(t)+9f(t)=0.$$

2. $$f''(t)+2f'(t)+5f(t)=0.$$

```{hint}
:class: dropdown
Alt afhængig af om det karakteristiske polynomium har to reelle rødder, to ikke-reelle rødder eller en dobbeltrod, skal man bruge Scenarie 1, Scenarie 2, Scenarie 3 på sider 262 og 263 i Afsnit 13.3 fra lærebogen.
```

```{admonition} Svar
:class: dropdown
1. $f(t)=c_1 \cdot e^{3t}+c_2 \cdot te^{3t}, \quad c_1,c_2 \in \mathbb{R}.$
2. $f(t)=c_1 \cdot e^{−t}\mathrm{cos}(2t)+c_2\cdot e^{−t} \mathrm{sin}(2t), \quad c_1,c_2 \in \mathbb{R}.$
```

+++

----

+++


## Opgave 4: En inhomogen andenordens differentialligning

Givet den inhomogene differentialligning 

$$f''(t)-6f'(t)+9f(t)=e^{2t}.$$

+++

### Spørgsmål a

Bestem et reelt tal $a$ således at funktionen $f(t)=a\cdot e^{2t}$ er en partikulær løsning til den givne differentialligning.

```{hint}
:class: dropdown
Indsæt funktionen $f(t)=a\cdot e^{2t}$ i differentialligningen. 
Hvilken ligning skal $a$ opfylde for at funktionen er en løsning til differentialligningen?
```

```{admonition} Svar
:class: dropdown
Funktionen $f(t)=e^{2t}$ er en partikulær løsning.
```

+++

### Spørgsmål b

Beskriv nu den fuldstændige løsning til den givne inhomogene differentialligning. 
Bemærk at den tilhørende homogene differentialligning allerede blev undersøgt i Opgave 3. 

```{hint}
:class: dropdown
Den fuldstændige løsning til den tilhørende homogene differentialligning $f''(t)-6f'(t)+9f(t)=0$
blev fundet i Opgave 3 til at være $f(t)=c_1 \cdot e^{3t}+c_2 \cdot te^{3t}, \quad c_1,c_2 \in \mathbb{R}.$
```

```{admonition} Svar
:class: dropdown
Den ønskede fuldstændige løsning er summen af en partikulær løsning og den fuldstændige løsning til den tilhørende homogene differentialligning. Derfor er svaret:

$$f(t)=e^{2t}+c_1 \cdot e^{3t}+c_2 \cdot te^{3t}, \quad c_1,c_2 \in \mathbb{R}.$$
```

+++

----

+++


## Opgave 5: Omskrivning af en højere ordens differentialligning til et system

En lineær andenordens differentialligning med konstante koefficienter kan omskrives til et system af førsteordens differentialligninger (se Afsnit 13.3 fra lærebogen). 
I denne opgave betragtes et eksempel.


+++

### Spørgsmål a

Givet differentialligningen $f''(t)+2f'(t)+f(t)=\mathrm{cos}(t)$. 
Omskriv denne differentialligning til et system af to førsteordensdifferentialligninger i funktionerne $f_1(t)$ og $f_2(t)$, hvor $f_1(t)=f(t)$ og $f_2(t)=f'(t)$.

```{admonition} Svar
:class: dropdown
Vælges $f_1(t)=f(t)$ og $f_2(t)=f'(t)$, så gælder at $f'_1(t)=f'(t)=f_2(t)$ og $f'_2(t)=f''(t)=-2f'(t)-f(t)+\mathrm{cos}(t)=-2f_2(t)-f_1(t)+\mathrm{cos}(t)$. 
Derfor fås differentialligningssystemet 

$$\left[\begin{array}{c} f'_1(t)\\ f'_2(t) \end{array}\right] =\left[\begin{array}{cc} 0 & 1 \\ -1 & -2 \end{array}\right] \cdot \left[\begin{array}{c} f_1(t)\\ f_2(t) \end{array}\right]+\left[\begin{array}{c} 0\\ \mathrm{cos}(t)\end{array}\right].$$

```

+++

### Spørgsmål b

Tjek at Ligning (13.13) i Sætning 13.3.1 fra lærebogen ville have givet det samme system. 

```{admonition} Svar
:class: dropdown
Bruges Ligning (13.13) med $a_0=1$, $a_1=2$ og $q(t)=\mathrm{cos}(t)$, så fås det samme differentialligningssystem som i svaret til Spørgsmål a.
```

+++

----

+++

## Opgave 6: Endnu en inhomogen andenordens differentialligning

Givet den inhomogene differentialligning 

$$f''(t)+3f'(t)-4f(t)=e^{t}.$$

+++

### Spørgsmål a

Inspireret af Opgave 4, kunne man håbe at der findes et reelt tal $a$ således at $f(t)=a\cdot e^t$ er en partikulær løsning til den givne differentialligning. 
Vis at der faktisk ikke findes nogen funktion på formen $f(t)=a\cdot e^t$, som er en løsning. 
Hvad er problemet?

```{admonition} Svar
:class: dropdown
Indsættes en funktion på formen $f(t)=a \cdot e^{t}$ i differentialligningen, så fås $0=e^t$, som aldrig er opfyldt. 
Problemet er at funktioner på formen $f(t)=a \cdot e^{t}$ allerede er løsning til den tilhørende homogene differentialligning $f''(t)+3f'(t)-4f(t)=0.$
```

+++

### Spørgsmål b

Prøv nu at finde en partikulær løsning på formen $f(t)=a \cdot t\cdot e^{t}$. 
Tjek eventuelt først at $(t\cdot e^{t})'=e^t+t\cdot e^{t}$ og $(t\cdot e^{t})''=2e^t+t\cdot e^{t}$.

```{admonition} Svar
:class: dropdown
Indsættes funktionen $f(t)=a\cdot t\cdot e^{t}$ i differentialligningen, så fås efter nogle mellemregninger at $2a e^t+3ae^t=e^t$. 
Denne ligning er opfyldt præcist hvis $a=1/5$. Derfor er funktionen $f(t)=(1/5)te^t$ en partikulær løsning til den givne differentialligning.
```

+++

### Spørgsmål c

Beskriv nu den fuldstændige løsning til den givne inhomogene differentialligning. 
Bemærk at den tilhørende homogene differentialligning allerede blev undersøgt i Opgave 2. 

```{hint}
:class: dropdown
Den fuldstændige løsning til den tilhørende homogene differentialligning $f''(t)+3f'(t)-4f(t)=0$
blev fundet i Opgave 2 til at være $f(t)=c_1 \cdot e^{t}+c_2 \cdot e^{-4t}, \quad c_1,c_2 \in \mathbb{R}.$
```

```{admonition} Svar
:class: dropdown
Den ønskede fuldstændige løsning er summen af en partikulær løsning og den fuldstændige løsning til den tilhørende homogene differentialligning. 
Derfor er svaret:

$$f(t)=(1/5)te^{t}+c_1 \cdot e^{t}+c_2 \cdot e^{-4t}, \quad c_1,c_2 \in \mathbb{R}.$$

```


+++

----

+++

## Opgave 7: Fra løsning til differentialligning

Det oplyses at den fuldstændige reelle løsning til en homogen lineær andenordens differentialligning med konstante reelle koefficienter er 

$$f(t)=c_1e^{−t}\mathrm{cos}(2t)+c_2e^{−t}\mathrm{sin}(2t), \quad c_1,c_2 \in \mathbb{R}.$$

Opskriv differentialligningen.

```{hint}
:class: dropdown
Fordi $0$ er en løsning (sæt $c_1=0$ og $c_2=0$ i den fuldstændige løsning), er differentialligningen man leder efter en homogen differentialligning. Differentialligningen kan derfor skrives på formen $f''(t)+a_1 f'(t)+a_0 f(t)=0$ for visse reelle tal $a_0,a_1$. 
```

```{hint}
:class: dropdown
Hvilke rødder skal det karakteristiske polynomium $Z^2+a_1Z+a_0$ have?
```

```{admonition} Svar
:class: dropdown
Fra den givne fuldstændige løsning ses at det karakteristiske polynomium $Z^2+a_1Z+a_0$ har rødder $-1+2i$ og $-1-2i$. Derfor gælder 
$Z^2+a_1Z+a_0=(Z-(-1+2i))\cdot (Z-(-1-2i))$. Ganger man ind i parentes så fås at $Z^2+a_1Z+a_0=Z^2+2Z+5.$ Derfor $a_1=2$ og $a_0=5$. Den ønskede differentialligning er: $f''(t)+2f'(t)+5f(t)=0.$
```



+++

----

+++


## Opgave 8: Fra løsning til differentialligning, del 2

Det oplyses at den fuldstændige reelle løsning til en inhomogen lineær andenordens differentialligning er 

$$f(t)=c_1e^{−t}\mathrm{cos}(2t)+c_2e^{−t}\mathrm{sin}(2t)+7+3t+5e^t, \quad c_1,c_2 \in \mathbb{R}.$$

Opskriv differentialligningen.

```{hint}
:class: dropdown
Hvad er den fuldstændige løsning til den tilhørende homogene differentialligning? Kan den tilhørende homogene differentialligning bestemmes ved hjælp af svaret til Opgave 7?
```

```{hint}
:class: dropdown
Den tilhørende homogene differentialligning er ifølge Opgave 7 givet som $f''(t)+2f'(t)+5f(t)=0.$ Den inhomogene differentialligning der er efterspurgt i denne opgave kan derfor skrives på formen $f''(t)+2f'(t)+5f(t)=q(t).$  
```

```{hint}
:class: dropdown
Funktionen $f(t)=7+3t+5e^t$ er en partikulær løsning til den ønskede differentialligning. Hvad får man hvis man indsætter denne funktion i sidstnævnte differentialligningen fra forrige hint?
```

```{admonition} Svar
:class: dropdown
Den ønskede differentialligning er $f''(t)+2f'(t)+5f(t)=41+15t+40e^t.$
```

+++

----

+++


## Opgave 9: Begyndelsesbetingelser

Givet den homogene reelle differentialligning

$$f''(t)+3f'(t)-4f(t)=0.$$

Bemærk at differentialligningen er den samme som i Opgave 2. 
Målet med opgaven er at finde løsningen til differentialligningen som opfylder begyndelsesbetingelserne $f(0)=1$ og $f'(0)=2$.

+++

### Spørgsmål a

I Opgave 2 var resultatet at den givne differentialligning har den fuldstændige løsning 

$$f(t)=c_1 \cdot e^t+c_2 \cdot e^{−4t}, \quad c_1,c_2 \in \mathbb{R}.$$

Hvilken ligning skal $c_1$ og $c_2$ opfylde for at det gælder at $f(0)=1$?

```{admonition} Svar
:class: dropdown
Fra Opgave 2 vides at 

$$f(t)=c_1 \cdot e^t+c_2 \cdot e^{−4t}, \quad c_1,c_2 \in \mathbb{R}.$$

Indsættes $t=0$ og bruges begyndelsesbetingelsen $f(0)=1$, så fås at $1=c_1+c_2.$
```

+++

### Spørgsmål b

Hvilken ligning skal $c_1$ og $c_2$ opfylde for at det gælder at $f'(0)=2$?

```{hint}
:class: dropdown
Ligesom i spørgsmål a, vides fra Opgave 2 at 

$$f(t)=c_1 \cdot e^t+c_2 \cdot e^{−4t}, \quad c_1,c_2 \in \mathbb{R}.$$

Tag nu den afledte på begge sider af lighedstegnet og indsæt bagefter $t=0$.
```

```{hint}
:class: dropdown
Udfra den fuldstændige løsning

$$f(t)=c_1 \cdot e^t+c_2 \cdot e^{−4t}, \quad c_1,c_2 \in \mathbb{R}$$

fås ved differentiation på begge sider af lighedstegnet at:

$$f'(t)=c_1 \cdot e^t-4c_2 \cdot e^{−4t}, \quad c_1,c_2 \in \mathbb{R}.$$

Brug nu sidste del af forrige hint.
```

```{admonition} Svar
:class: dropdown
$2=c_1-4c_2$
```

+++

### Spørgsmål c

Find nu den løsning $f(t)$ til differentialligningen som opfylder $f(0)=1$ og $f'(0)=2$.

```{hint}
:class: dropdown
Bestem $c_1$ og $c_2$ ved at løse de to ligninger man fandt i spørgsmål a og b. 
```

```{admonition} Svar
:class: dropdown
Løses de to ligninger $1=c_1+c_2$ og $2=c_1-4c_2$, så fås $c_1=6/5$ og $c_2=-1/5$. 
Den ønskede løsning er derfor:

$$f(t)=(6/5) \cdot e^t-(1/5) \cdot e^{−4t}.$$
```

## Bemærkning

Der åbnes en Möbius test om forrige ugens Pythonopgave kl. 15:30