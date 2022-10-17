---
aliases: [""]
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

Here each cell represents a bunch of fluid, with the average velocity of the air in the fluid being the velocity of the cell (we also apply this average to all other properties such as density, pressure ect). For a small cell this approximation is quite accurate and of course the smaller the cell the more accurate the representation (since it's closer to the size of the individual molecules). 
In the diagram the average velocity of a cell is described with the vector $\vec{v}$, so now to find the value of the velocity in the box adjasent you need to add the change in velocity between the box's:

![[Pasted image 20221017090343.png]]

Which is $\frac{\delta \vec{v}}{\delta x} \times \Delta x$ (here in the [[derivative symbols|partial derivative]] we are holding $y$ constant).

#### Partial derivatives across a continuum
We can take a linear set of cells like a line numbere

