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

(section:uge1)=
# Opgaver -- Store Dag

## Opgave 1: Udsagn

+++

Lad $P$ og $Q$ være logiske udsagn.


Vi danner nu tre nye udsagn:

$u:$ "Mindst et af udsagnene $P$ og $Q$ er sande"

$v:$ "Netop et af udsagnene $P$ og $Q$ er falsk"

$w:$ "$P$ er sandt og $Q$ er falsk"

### Spørgsmål a

+++

Opskriv sandhedstabeller for de logiske udsagn $u$, $v$ og $w$.

```{hint}
:class: dropdown
Ligesom i Eksempel 1.2.1 fra lærebogen, starter man med at lave en sandhedstabel hvor alle mulige kombinationer af sandhedsværdierne at de "atomiske" logiske udtryk som indgår i udsagnet er givet. I dette tilfælde er der kun to sådanne udtryk, nemlig $P$ og $Q$. Derfor start med at skrive følgende sandhedstabellen. 

%![](../media/uge1_1.png)

| $P$ | $Q$ | $...$ |
|:---:|:---:|:---:|
| T | T |  |
| F | T |  |
| T | F |  |
| F | F |  |

Udfyld nu den sidste søjle til hvert at de givne udsagn $u$, $v$ og $w$.
```

```{admonition} Svar
:class: dropdown
Sandhedstabellen for $u$ er:

%![](../media/uge1_2.png)

| $P$ | $Q$ | $u$ |
|:---:|:---:|:---:|
| T | T | T |
| F | T | T |
| T | F | T |
| F | F | F |

Sandhedstabellerne for $v$ og $w$ kan fås på lignende måde.
```

### Spørgsmål b

+++

Lad nu $P$ og $Q$ betegne de logiske udsagn:

$P$: "6 er et ulige tal" og $Q$: "3<7"

Brug tabellerne fra forrige spørgsmål til at afklare sandhedsværdien af de tre udsagn $u$, $v$ og $w$:


```{admonition} Svar
:class: dropdown
u: T (dvs. Sand), v: T og w: F (dvs. Falsk). 
```

### Spørgsmål c

+++

Hvilket af følgende logiske udsagn  $P \wedge  Q$ eller $P \vee Q$ er logisk ækvivalent med $u$?


```{hint}
:class: dropdown
Se teksten i bogen lige før Sætning 1.3.1 hvis du er i tvivl om hvad det betyder for to logiske udsagn til at være logisk ækvivalente.
```
+++


## Opgave 2: Eller

I udsagnslogikken benytter vi symbolet $\vee$ som udtales "eller".

Lad $P$ og $Q$ være udsagn.


### Spørgsmål a

Opskriv sandhedstabellen for $P \vee Q$


```{hint}
:class: dropdown
Se Definition 1.2.2 i lærebogen.
```
+++


### Spørgsmål b

Opskriv sandhedstabellen for $(P \vee Q) \wedge \neg(P \wedge Q)$.

```{hint}
:class: dropdown
Hvis du er i tvivl hvordan man opbygger en sandhedstabel for et mere indviklet udtryk som $(P \vee Q) \wedge \neg(P \wedge Q)$, så kan du få inspiration fra Eksempel 1.2.2 fra lærebogen.
```

### Spørgsmål c

+++

Giv eksempler på brug af ordet "eller" i almindeligt talesprog og analyser om betydningen af ordet "eller" er ligesom i spørgsmål a eller ligesom i spørgsmål b.

```{admonition} Svar
:class: dropdown
I almideligt talesprog betyder "P eller Q" tit det samme som det logiske udtryk fra spørgsmål b og ikke det matematiske "eller" fra spørgsmål a. Et eksempel er "Jeg har matematik i morgen eller i overmorgen." Det matematiske "eller" vil ikke udelukke muligheden at man har matematik både i morgen og i overmorgen, men sprogligt er det som regel ikke det man mener. Til orientering: i logik kalder man "eller" som brugt i almindeligt talesprog for "exclusive or", tit betegnet kort med "xor".
```

---

## Opgave 3: Sandhedstabeller

+++

Lad $P$, $Q$ og $R$ være logiske udsagn.

### Spørgsmål a
Opskriv sandhedstabellen for det logiske udsagn: $P \wedge ( Q \vee R)$.



```{hint}
:class: dropdown
Følg en lignende fremgangsmåde som Eksempel 1.2.1 i lærebogen.
```
+++

### Spørgsmål b
Opskriv sandhedstabellen for det logiske udsagn: $(P \wedge  Q) \vee R$.

+++

### Spørgsmål c
Er de logiske udsagn  $P \wedge ( Q \vee R)$ og $(P \wedge  Q) \vee R$ logisk ækvivalente?

+++

```{admonition} Svar
:class: dropdown
Nej
```



---

## Opgave 4: Negation

Lad $P$ og $Q$ være logiske udsagn.

### Spørgsmål a

+++

Opskriv sandhedstabellen for det logiske udsagn: $\neg P$.


### Spørgsmål b

+++

Opskriv sandhedstabellen for det logiske udsagn: $\neg (P \wedge Q)$.


### Spørgsmål c

+++

Opskriv sandhedstabellen for det logiske udsagn: $\neg P \vee \neg Q$.


### Spørgsmål d

+++

Er de logiske udsagn $\neg (P \wedge Q)$ og  $\neg P \vee \neg Q$ logisk ækvivalente?


```{admonition} Svar
:class: dropdown
Ja
```

### Spørgsmål e

+++

Brug nu forrige svar på de logiske udsagn $\neg P$ og $\neg Q$, og udled et logisk ækvivalent udtryk for $\neg (P \vee Q)$

```{hint}
:class: dropdown
Hvis man bruge spørgsmål d på de logiske udsagn $\neg P$ og $\neg Q$, så fås at $\neg (\neg P \wedge \neg Q)$ og $\neg(\neg P) \vee \neg(\neg Q)$ er logisk æquivalente. Simplificer nu udtrykket $\neg(\neg P) \vee \neg(\neg Q)$.
```

```{admonition} Svar
:class: dropdown
$\neg (P \vee Q)$ er logisk ækvivalent med $\neg P \wedge \neg Q$
```


---

## Opgave 5: Negation sproglig

### Spørgsmål a

+++

%Lad $P$ være udsagnet "Studerende på DTU er gode til matematik!" og $Q$ være udsagnet "Studerende på DTU er gode til fysik!".
Lad $P$ være udsagnet "Solen skinner." og $Q$ være udsagnet "Jeg er i dårligt humør.".
Forklar sprogligt hvad nedenstående udsagn dækker over:

1. $\neg P$

2. $P \vee \neg Q$

3. $\neg P \wedge \neg Q$

4. $P \Rightarrow \neg Q$

5. $(\neg P \wedge \neg Q) \Rightarrow (\neg P)$

```{admonition} Svar
:class: dropdown
4. Sprogligt betyder $P \Rightarrow \neg Q$ følgende: "Hvis solen skinner, så er jeg ikke i dårligt humør." Der er flere muligheder, for eksempel: "Hvis solen skinner, så er jeg i godt humør."
```
---

## Opgave 6: Implikation

### Spørgsmål a

+++

Hvilke af nedenstående udtryk er logisk ækvivalent med $P \Rightarrow Q$?

1) $Q \Rightarrow P$

2) $\neg P \Rightarrow \neg Q$

3) $\neg Q \Rightarrow P$

4) $\neg Q \Rightarrow \neg P$


### Spørgsmål b

+++

Vis at udsagnet $P \Leftrightarrow Q$ er logisk ækvivalent med $\neg P \Leftrightarrow \neg Q$

----

%
%#### Spørgsmål a
%
%+++
%
%Vis ovenstående sætning både med et direkte bevis og et modstridsbevis
%
%

## Opgave 7: Kontraposition

Et helt tal $a$ kaldes lige, hvis $a=2b$ for et givet helt tal $b$. På lignende måde kaldes et helt tal $a$ ulige, hvis man kan skrive $a=1+2c$ for et givet helt tal $c$. 

Sætning: Lad $a$ være et helt tal. Hvis $a^2$ er lige så er $a$ lige.

Målet med opgaven er at vise denne sætning ved brug af udsagnslogik. 

### Spørgsmål a

+++

Ovenstående sætning indeholder en implikation. Formuler logiske udsagn $P$ og $Q$, således at implikationen i sætningen kan skrives som $P \Rightarrow Q$. 

```{admonition} Svar
:class: dropdown
$P$ er udsagnet at "$a^2$ er lige", mens $Q$ er udsagnet at "$a$ er lige". Med disse valg kan udsagnet "Hvis $a^2$ er lige så er $a$ lige.", skrives som "$P \Rightarrow Q$." 
```

### Spørgsmål b

+++

Med $P$ og $Q$ som i spørgsmål a, beskriv med ord det logiske udsagn $\neg Q \Rightarrow \neg P$ 

```{hint}
:class: dropdown
Hvis et hel tal ikke er et lige tal er ensbetydende med at sige at et hel tal er ulige.
```

```{admonition} Svar
:class: dropdown
"Hvis $a$ er ulige, så er $a^2$ ulige."
```

### Spørgsmål c

+++

Ifølge den forrige opgave er de logiske udsagn $P \Rightarrow Q$ og $\neg Q \Rightarrow \neg P$ logisk ækvivalente. Derfor kan vi vise sætningen i opgaven ved at vise at udsagnet "Hvis $a$ er ulige, så er $a^2$ ulige." er sandt for ethvert helt tal $a$. Vis dette udsagn.

```{hint}
:class: dropdown
Hvis $a$ er ulige, så gælder $a=1+2b$ for et givet helt tal $b$. Hvad kan der nu siges om $a^2$?
```

----


## Opgave 8: NAND operatoren

Den logiske operator $\uparrow$, som kaldes **NAND** har følgende sandhedstabel:  

| $A$ | $B$ | $A \uparrow B$ |
|:---:|:---:|:---:|
| T | T | F |
| F | T | T |
| T | F | T |
| F | F | T |

Man kan også betragte en NAND operator som en del af et elektrisk netværk som tager to inputstrøm $A$ og $B$ som hver for sig kan være slået til eller slået fra, og producerer en outputstrøm. Hvis $A$ har værdi $T$ (hhv. $F$), så kan det fortolkes i et elektrisk netværk med at sige at $A$ er slået til (hhv. slået fra). Sandhedsværdien for $B$ og outputtet $A \uparrow B$ har en lignende fortolkning. 
I sammenhængen af elektriske netværk kalder man **NAND**-operatoren en **NAND**-gate. Den tegnes i elektriske netværk som følger:

![](../media/uge1_sd_nand1.PNG)

Også andre logiske operatorer som $\neg$, $\wedge$ og $\vee$ kan fortolkes som gates i elektriske netværk (see wikipedia-siden "Logic gate" hvis du vil læse mere).

### Spørgsmål a

+++

Vis at de to logiske udsagn $A \uparrow B$ og $\neg (A \wedge B)$ er logisk ækvivalente. Det forklarer navnet **NAND**: det står for **not and**.  

### Spørgsmål b

+++

Gør rede for at følgende elektriske netværk har den samme effekt som $\neg A$ ved at vise at de to logiske udsagn $A \uparrow A$ og $\neg A$ er logisk ækvivalente.

![](../media/uge1_sd_nand2.PNG)

%Show that the logical expression $\neg P$ can be written in terms of the **NAND** operator only. More concretely: show that the %logical propositions $\neg P$ and $P \uparrow P$ are logically equivalent.

### Spørgsmål c

+++

Gør rede for at følgende elektriske netværk har den samme effekt som $A \wedge B$. 

![](../media/uge1_sd_nand3.PNG)

```{hint}
:class: dropdown
Vis at de to logiske udsagn $A \wedge B$ og $(A \uparrow B)\uparrow(A \uparrow B)$ er logisk ækvivalente.
```
%Show that the logical expressions $P \wedge Q$ and $P \vee Q$ can be written in terms of the **NAND** operator only. Background: %digital computers have inbuilt hardware devices called **gates**, that can perform the logical operators $\neg, \wedge, \vee$. All of %these are constructed using one particular gate only, namely one corresponding to the **NAND** operator.

### Spørgsmål d

+++

Find et elektrisk netværk med to inputstrømme $A$ og $B$ som kun bruger **NAND**-gates og som har den samme effekt som $A \vee B$.

```{admonition} Svar
:class: dropdown
![](../media/uge1_sd_nand4.PNG)
```
----
%
%### Opgave 9: NAND
%
%På figuren nedenfor ses en NAND operator. De to ben A og B er til input.
%![Nand.png](uploads/opgfig/Nand.png)
%
%#### Spørgsmål a
%
%+++
%
%
%```{hint}
%:class: dropdown
%Opskriv sandhedstabeller for hver operator.  
%```
%
%```{admonition} Svar
%:class: dropdown
%1) Negation, 2) and og 3) or
%```
%
%#### Spørgsmål b
%
%+++
%
%Kontruer en NOR (not or) operator, udelukkende ved brug ad NAND operatorer
%
%```{hint}
%:class: dropdown
%Brug forrige spørgsmål
%```
%
%
%----
## Opgave 9: Modstridsbevis

Betragt andengradsligningen $x^2+bx+c=0$ hvor $b,c \in \Bbb{Z}$. Som kendt, har denne ligning diskriminant $D=b^2-4c.$ Lad $P$ være udsagnet at $D$ aldrig kan antage værdien $2$ for $b,c \in \Bbb{Z}$.

### Spørgsmål a

+++

Hvad siger det logiske udsagn $\neg P$ om diskriminanten $D$? 

```{hint}
:class: dropdown
$\neg P$ er negationen af udsagnet at $D$ aldrig kan antage værdien $2$ for $b,c \in \Bbb{Z}$. Prøv at formulere det lidt pænere og kortere ren sprogligt.
```

```{admonition} Svar
:class: dropdown
$\neg P$ er udsagnet at $D=2$ for visse hele tal $b$ og $c$.
```
### Spørgsmål b

+++

Vis at udsagnet $P$ er sandt ved hjælp af et modstridsbevis.

```{hint}
:class: dropdown
Et modstridsbevis af et udsagn $P$ er baseret på Ligning (1.23) fra Sætning 1.3.4 i lærebogen. Antag derfor at $\neg P$ er sandt og prøv at finde en modstrid.
```

----

## Opgave 10: Gåde 
### Spørgsmål a

+++

Prøv selv at løse gåden i Eksempel 1.5.2 fra lærebogen. Alternativt læs og forstå Eksempel 1.5.2. 
