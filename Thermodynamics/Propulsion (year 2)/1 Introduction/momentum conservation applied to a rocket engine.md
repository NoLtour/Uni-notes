---
aliases: [""]
tags: []
---

## Momentum conservation applied to a rocket engine

The way litterally anything moves is conservation of momentum, apply this principle to a [[control volume]] and suddenly you'll find yourself modelling a thruster. So lets do exactly that, with a rocket engine. We can use equations of momentum flux to get force (conservation of momentum boi):

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

