---
aliases: ["del","nabla"]
tags: []
---

## Del operator ($\nabla$)

### Def

This is quite simple:

> $$\begin{align*}(n)D:&\:\:\:\nabla = \sum\limits^{n}_{i=1} \vec{e}_{i} \frac{\delta}{\delta x_{i}}\\&\:\:\:\nabla f = \sum\limits^{n}_{i=1} \vec{e}_{i} \frac{\delta f}{\delta x_{i}} \\3D:&\:\:\: \nabla f = \left( \frac{\delta f}{\delta x}, \frac{\delta f}{\delta y}, \frac{\delta f}{\delta z} \right) = \vec{e}_{x} \frac{\delta}{\delta x} + \vec{e}_{y} \frac{\delta}{\delta y} + \vec{e}_{z} \frac{\delta}{\delta z}\end{align*}$$
>> where:
>> $\nabla=$ [[del operator]]
>> $f=$ some function
>> $x_{i}=$ $i_{th}$ dimension
>> $\vec{e}_{i}=$ $i_{th}$ [[unit vector]]

All this means is that for some function $f$, if you apply the [[del operator]] you get the rate of change of each of it's components, this results in a vector which points in the direction of increase.

### Example
> Take the [[del operator]] of $p=x^{2} + 7yx + e^{3z}$ where $p$ represents pressure:

$$\begin{align*}
\nabla f = \left( \frac{\delta f}{\delta x}, \frac{\delta f}{\delta y}, \frac{\delta f}{\delta z} \right)
\end{align*}$$