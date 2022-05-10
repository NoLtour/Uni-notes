---
aliases: ["Thevenin equivalent circuits","I still dislike that name, so he dons't be to be the file name","Thevinins theorem"]
tags: ["Question","QFormat3"]
---

#### What's the method for
## Simplifying simple circuits
### Method
#### Requirements
- Must be represented in a way that it has 2 terminals
- Must only consist of resistors (that obey [[Ohms law]]), voltage sources and current sources

#### Theory
The method is based on the fact that any "black box" circuit that meets the above requirements can be represented as just a single voltage source and resistor in series:
![[Pasted image 20211114114408.png]]

#### Method
1) Identify the part of the circuit you are going to simplify
2) Find it's resistance between the two terminals by ignoring voltage sources and current sources
3) Find the [[potential difference|voltage]] of the representative voltage source ($V_{TH}$) by finding it's open circuit voltage

### Example
 ![[Pasted image 20211114115018.png]]
 
 1) > First we identify the circuit we want to simplify
 > ![[Pasted image 20211114115154.png]]
> Which is baiscall everything except that resistor

2) > Start by ignoring current sources and voltage sorces 
> ![[Pasted image 20211114115356.png]]
> So: 
> $$\begin{align*}
R=&\dfrac{1}{\dfrac{1}{4+6}+ \dfrac{1}{2}}  \\
=& \frac{5}{3} \Omega
\end{align*}$$

3) > Now cutting $\vec{AB}$ so that $R_{AB} = \inf$
> ![[Pasted image 20211114120431.png]] 
> Now we can use [[Kirchov's voltage law]] on the outside loop:
> $$\begin{align*}
12 - 2I -4I -6 -6I =& 0\\
6 =& 12I\\
I=&0.5A
\end{align*}$$
> We also can use [[Kirchov's voltage law]] on the left half of the circuit treating it as it's own loop:
> $$ \begin{align*}
12 - 2I - V_{AB} &= 0\\
12 - \frac{2}{2} &= V_{AB}\\
&= 11V 
\end{align*} $$

Hence (also note that the current from earlyer is gone, that's because it was only valid during those specific calculations):
![[Pasted image 20211114121052.png]]