---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Show that there is a
## Need for a TS diagram
### Diagram
If we use the following [[p-v diagrams|pv diagram]]:
![[Pasted image 20211212101015.png]]
We can define all it's process paths:
- 1 to 2: [[isothermal expansion or compression|isothermal expansion]] 
- 2 to 3: [[adiabatic expansion or compression|adiabetic expansion]]
- 3 to 4: [[isothermal expansion or compression|isothermal expansion]]
- 4 to 1: [[adiabatic expansion or compression|adiabetic expansion]]

#### Path $1 \to 2 \to 3$ work:
$1 \to 2$ is [[isothermal expansion or compression|isothermal expansion]] so:
$$\begin{align*}
Q_{12}&=W_{12} 
\end{align*}$$

$2 \to 3$ is [[adiabatic expansion or compression|adiabetic expansion]] so:
$$\begin{align*}
E_{u23} = - W_{23}
\end{align*}$$

So we can find $W_{13}$:
$$\begin{align*}
W_{13} &= W_{12} + W_{23}\\
&=  Q_{12} - E_{u23}
\end{align*}$$

#### Path $1 \to 4 \to 3$ work:
$1 \to 4$ is [[adiabatic expansion or compression|adiabetic expansion]] so:
$$\begin{align*}
E_{u14} = - W_{14}
\end{align*}$$

$4 \to 3$ is [[isothermal expansion or compression|isothermal expansion]] so:
$$\begin{align*}
Q_{43}&=W_{43} 
\end{align*}$$

So we can find $W_{13}$:
$$\begin{align*}
W_{13} &= W_{14} + W_{43}\\
&=  - E_{u14} + Q_{43} 
\end{align*}$$

#### Path comparision
Although the final [[state (thermodynamics)|state]] reached is the same (so pressure, internal energy ect are the same) there are differences in [[heat]] transfer and in [[internal energy]] change:
$$\begin{align*}
&&- E_{u14} + Q_{43}  &= Q_{12} - E_{u23}\\
Q_{43} &\neq Q_{12} && & E_{u14} &\neq E_{u23}
\end{align*}$$
This difference resaults in a different change in [[entropy]] depending on the path taken, hence [[entropy]] is a [[state (thermodynamics)|state]] property giving us a total of 4 state properties that define a gas: $S, P, V, T$.
According to the [[the 2 property rule|two property rule]] we must be able to define a relationship for [[entropy]] interms of the other state properties.

This leads into [[the two entropy equations]] and the need for a [[TS diagram]].