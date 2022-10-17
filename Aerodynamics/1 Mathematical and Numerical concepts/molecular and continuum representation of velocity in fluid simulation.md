---
aliases: ["central difference","forward difference","backward difference"]
tags: []
---

## Molecular and continuum representation of velocity in fluid simulation

### Molecular representation

In reality fluids are composed of many fast moving atoms, where their interactions with the environment/each other determine the forces we observe:
![[Pasted image 20221017085758.png]]
This can be represented using [[ordinary differential equation]]s, such as:
$$ \vec{V_{i}} = \frac{d\vec{x_{i}}}{dt} $$
Then just do some basic particle collision simulation for lets say $2\times 10^25$ molecules and you can simulate the forces in one cubic meter of air... of course representing each molecule with a velocity vector then crunching numbers to find useful results is practically impossible ([[it is not that hard ngl I could do it with some paper and half an hour|skill issue]]), hence why we take the other approach.


### Continuum representation
Since representing each molecules not really possible instead we take a continuum representation, in which we represent velocity as a property of units of space:

![[Pasted image 20221017091801.png]]

Here each cell represents a bunch of fluid, with the average velocity of the air in the fluid being the velocity of the cell (we also apply this average to all other properties such as density, pressure ect). For a small cell this approximation is quite accurate and of course the smaller the cell the more accurate the representation (since it's closer to the size of the individual molecules). This is essentially treating each unit as a [[control volume]].
In the diagram the average velocity of a cell is described with the vector $\vec{v}$, so now to find the value of the velocity in the box adjacent you need to add the change in velocity between the box's:

![[Pasted image 20221017090343.png]]

Which is $\frac{\delta \vec{v}}{\delta x} \times \Delta x$ (here in the [[derivative symbols|partial derivative]] we are holding $y$ constant).

#### Partial derivatives across a continuum

##### Forward/Backward difference

We can take a linear set of cells like a line relative to some reference such as $i$:
![[Pasted image 20221017093836.png]]
Each side holding $i-1,i-2,i+1,i+2...$ with $f_{i+n}$ representing some value associated at that point. Now if only there was a mathematical tool used for finding adjustment terms using a reference point plus additional derivatives \*cough\* ([[Taylor series]]). So if we write out the [[Taylor series]] for $f_{i+1}$:
$$ f_{i+1} = f_{i} + \frac{\delta f}{\delta x} \Delta x + \frac{\delta^{2} f}{\delta x^{2}} \frac{(\Delta x)^{2}}{2} + ... $$
Since in this case $\Delta x$ is tiny, $(\Delta x)^{2}$ and any other higher order terms (HOT's) are negligible with the smaller the $\Delta x$ the more exponentially insignificant the error (hence small box's):
$$ f_{i+1} = f_{i} + \frac{\delta f}{\delta x} \Delta x $$
A similar expression can be found for $f_{i-1}$:
$$ f_{i+1} = f_{i} - \frac{\delta f}{\delta x} \Delta x $$
Both of these formulas can then be rearranged to get the rate of change of some property $f$ at each point:
![[Pasted image 20221017095243.png]]
(you end up with an equation which is literally just gradient)

##### Central difference

It is possible to get a more accurate representation of the difference at the central point by averaging the gradients between $i-1 \to i$ and $i \to i+1$ to get:
$$\begin{align*}
\frac{\delta f}{\delta x} = \frac{f_{i+1} - f_{i-1}}{2\Delta x}
\end{align*}$$

We call this [[molecular and continuum representation of velocity in fluid simulation|central difference]] which can be done on numpy using "np.gradient". (It should be noted that at the boundaries of a simulation, you cannot take [[molecular and continuum representation of velocity in fluid simulation|central difference]] and instead a forward of backward difference is used)
