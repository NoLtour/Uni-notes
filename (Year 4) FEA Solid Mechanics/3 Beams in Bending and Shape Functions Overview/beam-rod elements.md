---
aliases: [""]
tags: []
---

## Beam-rod elements

These are elements that combine bending ([[beam elements in pure bending]]) and stretching ([[PMTPE in rods]]), the two nodes will then have 6 degrees of freedom:

![[Pasted image 20241111165720.png|700]]

The resulting [[stiffness matrix]] is relatively simple to figure out, we just combine them:

![[Pasted image 20241111165846.png]]

The problem comes in appropriately identifying boundary conditions, with so many ways the system can flex we have many different means of constraining it. Correctly specifying that is important:

![[Pasted image 20241111165956.png]]


