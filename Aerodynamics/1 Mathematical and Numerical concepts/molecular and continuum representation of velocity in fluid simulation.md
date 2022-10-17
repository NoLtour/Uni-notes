---
aliases: [""]
tags: []
---

## Molecular and continuum representation of velocity in fluid simulation

### Molecular representation

In reality fluids are composed of many fast moving atoms, where their interactions with the environment/eachother determine the forces we observe:
![[Pasted image 20221017085758.png]]
This can be represented using [[ordinary differential equation]]s, such as:
$$ \vec{V_{i}} = \frac{d\vec{x_{i}}}{dt} $$
Then just do some basic particle collision simulation for lets say 
But of course representing each molecule with a velocity vector then crunching numbers to find useful results is practically impossible.


### Continuum representation
Since representing each molecules not really possible instead we take a continuum representation, in which we represent velocity as a property of units of space:

![[Pasted image 20221017090343.png]]

Here each cell represents a bunch of fluid, with the average velocity of the air in the fluid being the velocity of the cell. For a small cell this approximation is quite accurate and of course the smaller the cell the more accurate the representation.
Since we need to isolate changes in 