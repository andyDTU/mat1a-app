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

(section:uge1L)=

## Opgaver -- Lille Dag

### Opgave 1: Repetitionsopgave: Negation

Betragt igen de logiske udsagn $u$, $v$ og $w$ fra Opgave 1 på Store Dag.

#### Spørgsmål a

+++

Opskriv sandhedstabeller for $\neg u$, $\neg v$ og $\neg w$.

```{hint}
:class: dropdown
Brug sandhedstabellerne som du beregnede i Opgave 1 på Store Dag, frem for at starte helt forfra.
```

#### Spørgsmål b

+++

Lad nu $P$ og $Q$ betegne negationen af de logiske udsagn:

"6 er et ulige tal" og "3<7".

Hvad er sandhedsværdien af de tre udsagn $u$, $v$ og $w$?

```{admonition} Svar
:class: dropdown
u: T (dvs. Sand), v: T og w: T
```

----


### Opgave 2: Implikation

#### Spørgsmål a

+++

Lad $P$ være et logisk udsagn.
Opskriv sandhedstabellerne for $(P \Rightarrow P) \Rightarrow P$ og $P \Rightarrow (P \Rightarrow P)$.



#### Spørgsmål b
Er ovenstående to logiske udsagn ækvivalente?

+++

```{admonition} Svar
:class: dropdown
Nej.
```

---

### Opgave 3: Implikation/Biimplikation


#### Spørgsmål a

+++

Løs førstegradsligningen $x-2 = 3$.


#### Spørgsmål b

+++


Nogen løser ovenstående førstegradsligning på mere omstændig måde, og glemmer samtidig at sætte implikationspile mellem sine udregninger. Udregningerne fremgår af nedenstående:

$x-2=3$

$(x-2)^2 =3^2$

$x^2 -4x+4=9$

$x^2 -4x -5 =0$

$x=-1 \vee x=5$


Mellem hvilke udregninger kan vi sætte biimplikationspile og mellem hvilke kun en implikationspil? Forklar hvorfor ikke hver mulighed for $x$ i den sidste udregning behøves at være en løsning til den oprindelige ligning.

```{hint}
:class: dropdown
Ifølge Ligning (1.22) i Sætning 1.3.4 kan man sætte en biimplikationspil mellem to logiske udsagn $P$ og $Q$ præcist hvis $P$ medfører $Q$ og $Q$ medfører $P$. 
```

#### Spørgsmål c

+++

En anden person løser ligningssystemet på en anden (og også ret omstændig) måde:

$x-2=3$

$x-5 =0$

$(x-5)^2 =0$

$x^2 -10x +25 =0$

$x=5$ (der er kun en løsning til andengradsligningen)

Mellem hvilke udregninger kan vi sætte biimplikationspile og mellem hvilke kun en implikationspil? Forklar hvorfor denne gang hver mulighed for $x$ i den sidste udregning er en løsning til den oprindelige ligning.

```{admonition} Svar
:class: dropdown
Der gælder biimplikationspile mellem samtlige udregninger.
```

---


### Opgave 4: Tautologi

Betragt det logiske udsagn: $(P \vee Q)\vee (\neg P \wedge \neg Q)$.

#### Spørgsmål a

+++

Vis ved hjælp af sandhedstabeller at det er en tautologi.

```{hint}
:class: dropdown
Hvis du er i tvivl om hvad en tautologi er, se teksten i lærebogen mellem Definition 1.3.1 og Eksempel 1.3.1.
```

#### Spørgsmål b

+++

Forklar i ord at ovenstående er en tautologi.

```{hint}
:class: dropdown
Med ord kan man udtale $\neg P \wedge \neg Q$ som "ikke $P$ og heller ikke $Q$". Alternativt kunne man også sige "hverken $P$ eller $Q$". Prøv nu på lignende måde at fortolke $(P \vee Q)\vee (\neg P \wedge \neg Q)$ sprogligt.
```

#### Spørgsmål c

+++

Samme spørgsmål som i spørgsmål a, men med udsagnet $(P \Rightarrow Q)\vee (Q \Rightarrow P)$.


#### Spørgsmål d

+++

Samme spørgsmål som i spørgsmål a, men nu med udsagnet $(P \Rightarrow Q)\vee (\neg P \Rightarrow Q)$.


---

### Opgave 5: Ligninger

Løs følgende fire ligninger ved først at indføre en tautologi.

#### Spørgsmål a

+++

1. Løs ligningen $|x|=-x+1$.


2. Løs ligningen $|x|=2x+1$.


3. Løs ligningen $3|2x-1|=-4x+3$.


4. Løs ligningen $|2x+1|=|-5x+3|$.


```{hint}
:class: dropdown
Se Eksempel 1.4.2 i lærebogen til inspiration.
```

```{hint}
:class: dropdown
Omskriv ligningen til $|x|=-x+1 \wedge ( x<0 \vee x \ge 0)$.
```


```{admonition} Svar
:class: dropdown
1. $x=\frac{1}{2}$

2. $x=-\frac{1}{3}$

3. $x=0 \vee x=\frac{3}{5}$

4. $x=\frac{4}{3} \vee x=\frac{2}{7}$
```

----
%### Opgave 6: Python opgave
%
%I denne opgave får du behov for command console Python på din computer. 
%
%#### Spørgsmål a
%Python kan bestemme sandhedsværdien af nogle enkele logiske udtryk. Kør for eksempel følgende Pythonkode. Bemærk at Python bruger `True` og `False`, hvor man i lærebogen ville have brugt T og F.
%
%`2>5`
%
%`3>1`
%
%`1==1`
%
%+++
%
%#### Spørgsmål b
%De logiske operationer $\neg$, $\wedge$ og $\vee$ skrives i Python som `not`, `and` og `or`. Kør for eksempel følgende Pythonkode og check om outputtet giver det rigtige.
%
%`2>5 and 3>1`
%
%`2>5 or 3>1`
%
%`not (2>5 and 3>1)`
%
%`True or False`
%
%`not (True and False)`
%
%+++
%
%#### Spørgsmål c
%
%I stedet for `True` og `False` kan man skrive `1` og `0` i Python. Kør for eksempel følgende Pythonkode. 
%
%`True == 1`
%
%`False == 0`
%
%`0 or 1`
%
%#### Spørgsmål d
%Udfyld nu sandhedstabellen i lærebogens Example 1.3.2 ved hjælp af Python, brug eventuelt denne kortere skrivemåde med `0` og `1` istedet for `False` og `True`.
%
%+++
%
%
%```{hint}
%:class: dropdown
%Første linje i tabellen: `1 or (1 and (not 1))`
%```
%below two exercises from 2023
%---
%
%### Opgave 6: Modstridsbevis
%
%#### Spørgsmål a
%
%+++
%
%Vis at der ikke findes et $n \in \Bbb{Z}$ så $4$ er en divisor i tallet $n^2+6$
%
%
%---
%
%### Opgave 7: Modstrid 2
%
%
%#### Spørgsmål a
%
%+++
%
%Vis at der ikke findes hele tal $x,y\in \Bbb{Z}$ så $49x+21y=1$
