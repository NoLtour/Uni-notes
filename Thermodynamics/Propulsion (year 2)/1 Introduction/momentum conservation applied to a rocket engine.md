---
aliases: [""]
tags: []
---

## Momentum conservation applied to a rocket engine

The way literally anything moves is conservation of momentum, apply this principle to a [[control volume]] and suddenly you'll find yourself modelling a thruster. So lets do exactly that, with a rocket engine. We can use equations of momentum flux to get force (conservation of momentum boi):

$$\begin{align*}
\dot{M}_{out} - \dot{M}_{in} &= \sum\limits F
\end{align*}$$

(These should be vectors but I'm taking everything in the direction of thrust because lazy)

For a rocket engine there is no flow into the engine since it carries it's own fuel and oxidiser ($\dot{M}_{in}=0$) so:

$$\begin{align*}
\dot{M}_{out} &= \sum\limits F\\
&& \dot{M}_{out} &= \dot{m} V_{ex}\\
\dot{m} V_{ex} &= \sum\limits F\\

\end{align*}$$
Sum of forces is just resultant force + pressures, $\sum\limits F=  P_{A} A_{j} - P_{j} A_{j} + F$ so subbing that in and rearranging:
$$\begin{align*}
\dot{m} V_{ex} &= P_{A} A_{j} - P_{j} A_{j} + F & &\to &  \dot{m} V_{ex} + A_{j}( P_{j} - P_{A} ) &= F
\end{align*}$$

(I find it annoying that we use $F$ for thrust instead of $T$, but I'm doing that since it seems to be the convention in this module)

> ### $$\begin{align*}  F &=  \dot{m} V_{ex} + A_{j}( P_{j} - P_{A} )  \end{align*}$$
>> where:
>> $\dot{m}=$  mass flow rate through rocket nozzle
>> $V_{ex}=$ exhaust velocity from rocket nozzle
>> $A_{j}=$ cross sectional area of end of rocket nozzle
>> $P_{j}=$ pr
