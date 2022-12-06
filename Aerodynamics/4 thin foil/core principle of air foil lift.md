---
aliases: [""]
tags: []
---

## Core principle of air foil lift

For thin airfoil theory it all simply boils down to [[Kutta-Joukowski Theorem]], with that in mind if you know the [[circulation]] around any shape foil you know it's lift. So to model an we can just distrobute it's circulation across it's entire length using lots of tiny little [[stream function for a vortex|vortecies]]:
![[Pasted image 20221204150954.png]]
By doing so we can figure out other useful information about them, the issues with attempting this are:
- There is a specific distrobution for each foil that must be used to get useful information
- The complex shape leads to REALLY complex maths if you want to solve it [[numerical and analytical solutions|analytically]] 

So basically what the entire purpose of [[Thin airfoil theory Overview|thin airfoil theory]] is just trying to simplify the problem ^ and get useful info. Some of the info we are trying to get is pressure distrobution:
![[Pasted image 20221204151802.png]]
Which will then be useful for finding things such as [[aerodynamic centre]] and [[Centre of pressure]], remember these thing's from year 1? Well most of the equations from then which we pulled out of our [[and the maths is going to be fun|asses]] at the time will now be derived.
