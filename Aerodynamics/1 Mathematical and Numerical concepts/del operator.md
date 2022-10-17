---
aliases: ["del","nabla","grad"]
tags: []
---

## Del operator ($\nabla$)

Also referred too as nabla or grad.

### Def

This is quite simple:

> $$\begin{align*}(n)D:&\:\:\:\nabla = \sum\limits^{n}_{i=1} \vec{e}_{i} \frac{\delta}{\delta x_{i}}\\&\:\:\:\nabla f = \sum\limits^{n}_{i=1} \vec{e}_{i} \frac{\delta f}{\delta x_{i}} \\3D:&\:\:\: \nabla f = \left( \frac{\delta f}{\delta x}, \frac{\delta f}{\delta y}, \frac{\delta f}{\delta z} \right) = \vec{e}_{x} \frac{\delta}{\delta x} + \vec{e}_{y} \frac{\delta}{\delta y} + \vec{e}_{z} \frac{\delta}{\delta z}\end{align*}$$
>> where:
>> $\nabla=$ [[del operator]]
>> $f=$ some function
>> $x_{i}=$ $i_{th}$ dimension
>> $\vec{e}_{i}=$ $i_{th}$ [[unit vector]] in the $i_{th}$ dimension

All this means is that for some function $f$, if you apply the [[del operator]] you get the rate of change of each of it's components, this results in a vector which points in the direction of increase.
So the [[del operator]] will give you a vector representing the direction of increase in a [[Scalars and vectors|scalar]] field.

### Example
> Take the [[del operator]] of $p=x^{2} + 7yx + e^{3z}$ where $p$ represents pressure:

$$\begin{align*}
\nabla f &= \left( \frac{\delta f}{\delta x}, \frac{\delta f}{\delta y}, \frac{\delta f}{\delta z} \right) & p&=x^{2} + 7y^{3}x + e^{3z}\\
\nabla p &= \left( p \frac{\delta }{\delta x}, p \frac{\delta  }{\delta y}, p \frac{\delta  }{\delta z} \right)\\
&= \left( 2x,\: 21y^{2}x,\: 3e^{3z} \right)
\end{align*}$$

### Vid bit (graphical representation of [[del operator]])
![youtube](https://youtu.be/ynzRyIL2atU?t=82#t=82)