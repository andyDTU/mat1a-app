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

(section:uge8L)=

# Opgaver -- Lille Dag

----

+++

## Opgave 1: Ordnede baser i $\mathbb{C^2}$

Er 

$$\left(\left[\begin{array}{r}1\\i\end{array}\right],\left[\begin{array}{r}1+i\\-1+i\end{array}\right]\right) $$

en ordnet basis for $\mathbb{C}^2$?

```{hint}
:class: dropdown
Er de to vektorer i den givne liste $\beta$ lineært uafhængige?
```

```{admonition} Svar
:class: dropdown
De to vektorer i den givne list $\beta$ er lineært afhængige over $\mathbb{C}$, fordi

$$(1+i)\left[\begin{array}{r}1\\i\end{array}\right]=\left[\begin{array}{r}1+i\\-1+i\end{array}\right].$$

Derfor kan $\beta$ ikke være en ordnet basis. 
```

+++

----

+++

## Opgave 2: Koordinater mht. den ordnede standardbasis

Den ordnede standardbasis for $\mathbb{R}^3$ er givet som $\epsilon=({\mathbf e}_1,{\mathbf e}_2,{\mathbf e}_3)$, hvor

$$
{\mathbf e}_1=\left[\begin{array}{r}1\\0\\0\end{array}\right],\,
{\mathbf e}_2=\left[\begin{array}{r}0\\1\\0\end{array}\right],\,
{\mathbf e}_3=\left[\begin{array}{r}0\\0\\1\end{array}\right]\, .$$

Hvorfor gælder at 

$$
\left[\begin{array}{r}a\\b\\c\end{array}\right]_\epsilon = \left[\begin{array}{r}a\\b\\c\end{array}\right]
$$

for alle $a,b,c \in \mathbb{R}$?

Overvej hvorfor mere generelt $[{\mathbf v}]_\epsilon={\mathbf v}$ for alle $\mathbf v \in \mathbb{F}^m$, hvis $\epsilon$ er den ordnede standardbasis for $\mathbb{F}^m$ beskrevet i Eksempel 9.2.1.

```{hint}
:class: dropdown
Ifølge Definition 9.5.1 er de tre indgange i $\epsilon$-koordinatvektoren af en vektor $\mathbf v \in \mathbb{R}^3$ løsningen til det inhomogene lineære ligningssystem 

$$c_1\cdot{\mathbf e}_1+c_2\cdot{\mathbf e}_2+c_3\cdot{\mathbf e}_3={\mathbf v} \, .$$ 

Skriv nu 

$$
{\mathbf v}=\left[\begin{array}{r}a\\b\\c\end{array}\right]
$$

og prøv at løse for $c_1,c_2,c_3$.
``` 

```{admonition} Svar
:class: dropdown
Se Eksempel 9.5.1 fra lærebogen for det generelle tilfælde nævnt i bemærkningen. 
```

+++

----

+++

## Opgave 3: Udspænding, ordnet basis og koordinater

Vi betragter $W=\mathrm{Span}({\mathbf w}_1,{\mathbf w}_2,{\mathbf w}_3,{\mathbf w}_4)$ i $\mathbb{C}^4$ hvor 

$$
{\mathbf w}_1=\left[\begin{array}{r}0\\0\\0\\0\end{array}\right],\,
{\mathbf w}_2=\left[\begin{array}{r}0\\i\\0\\-2\end{array}\right],\,
{\mathbf w}_3=\left[\begin{array}{r}0\\-i\\0\\2\end{array}\right],\, 
{\mathbf w}_4=\left[\begin{array}{r}1\\1\\-1\\2i\end{array}\right], \, 
\, .$$

+++

### Spørgsmål a

Bestem en ordnet basis for $W$.

```{admonition} Svar
:class: dropdown
Bruges Sætning 9.2.1 fra lærebogen, så fås at $\beta=({\mathbf w}_2,{\mathbf w}_4)$ er en ordnet basis for $W$.
```

+++

### Spørgsmål b

Der skrives 

$${\mathbf w}=\left[\begin{array}{r}1\\i\\-1\\-2\end{array}\right] \, .$$

Beregn $[{\mathbf w}]_\beta$, hvor $\beta=({\mathbf w}_2,{\mathbf w}_4)$.

```{hint}
:class: dropdown
Hvilket lineær ligningssystem i de ubekendte $c_1,c_2$ giver Definition 9.5.1 fra lærebogen anledning til?
```

```{admonition} Svar
:class: dropdown

$$
[{\mathbf w}]_\beta=\left[\begin{array}{r}1+i\\1\end{array}\right] \, .
$$

```

+++

### Spørgsmål c

Det oplyses for en hvis vektor $\mathbf u \in \mathbb{C}^4$ at ligningen $c_1 {\mathbf w}_2 + c_2 {\mathbf w}_4 =  {\mathbf u}$ i de ubekendte $c_1,c_2$ ingen løsninger har.
Må man konkludere at ${\mathbf u}$ ikke er i $W$?

```{admonition} Svar
:class: dropdown
Ja.
```

+++

----

+++


## Opgave 4: Ordnede baser og koordinater i $\mathbb{R}^4$

I $\mathbb{R}^4$ er der givet fem vektorer:

$$
{\mathbf v}_1=\left[\begin{array}{r}1\\-1\\2\\1\end{array}\right],\,
{\mathbf v}_2=\left[\begin{array}{r}0\\1\\1\\3\end{array}\right],\,
{\mathbf v}_3=\left[\begin{array}{r}1\\-2\\2\\-1\end{array}\right],\, 
{\mathbf v}_4=\left[\begin{array}{r}0\\1\\-1\\3\end{array}\right], \, 
{\mathbf v}=\left[\begin{array}{r}1\\-2\\2\\-3\end{array}\right] \, .$$

Det oplyses at 

$$\mathrm{det}\left( \left[\begin{array}{rrrr}1 & 0 & 1 & 0\\-1 & 1 & -2 & 1\\2 & 1 & 2 & -1\\1 & 3 & -1 & 3\end{array}\right] \right) = 2.$$

+++

### Spørgsmål a

Gør rede for at $\beta=({\mathbf v}_1,{\mathbf v}_2,{\mathbf v}_3,{\mathbf v}_4)$ er en ordnet basis for $\mathbb{R}^4\,$. 

```{hint}
:class: dropdown
Kan den givne determinant bruges til noget?
```

+++


### Spørgsmål b

Bestem $\beta$-koordinatvektoren $[{\mathbf v}]_\beta$, hvor $\beta=({\mathbf v}_1,{\mathbf v}_2,{\mathbf v}_3,{\mathbf v}_4)$ er den ordnede basis fra Spørgsmål a.


```{hint}
:class: dropdown
Ifølge Definition 9.5.1 er de fire indgange i $\beta$-koordinatvektoren for $\mathbf v$ løsningen til det inhomogene lineære ligningssystem 

$$c_1\cdot{\mathbf v}_1+c_2\cdot{\mathbf v}_2+c_3\cdot{\mathbf v}_3+c_4\cdot{\mathbf v}_4={\mathbf v} \, .$$ 

Prøv derfor at løse dette ligningssystem.
``` 

```{admonition} Svar
:class: dropdown
$$
[{\mathbf v}]_\beta=\left[\begin{array}{r}2\\-1\\-1\\-1\end{array}\right]\, .
$$
```

+++

----

+++


## Opgave 5: Koordinater mht. en ordnet basis

Givet vektoren 

$${\mathbf u}=\left[\begin{array}{r}1\\2\\3\end{array}\right]$$

i $\mathbb{C^3}$, find en ordnet basis $\gamma$ for $\mathbb{C}^3$ således at 

$$[{\mathbf u}]_\gamma=\left[\begin{array}{r}1\\1\\1\end{array}\right].$$

+++

----

+++


## Opgave 6: Eksempler på udspændinger

Givet er et naturligt tal $n$ og et helt tal $d$ som opfylder at $0 \le d \le n$. 
Find $d$ vektorer i $\mathbb{R}^n$ således at deres udspænding har dimension $d$.
