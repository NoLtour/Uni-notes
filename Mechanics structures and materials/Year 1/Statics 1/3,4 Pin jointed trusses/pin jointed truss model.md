---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is a
## Pin jointed [[truss]] model
It is a simplified model of reality, where:
- Each beam of the truss is modelled as a bar
- All bars are connected by pins
- It's assumed bars can rotate around the pins with no friction
- All external forces and reactions are applied only in the joints
- It's assumed all deformation is minimal so the geometrys consistant enough not to need recalculation
- the weight of the structure might be ignored (depends)

These assumtions make it so that there are only axial forces acting through the bar, but each bar has no moments.
![[Pasted image 20211022210326.png]]

In reality the model is only valid if the joints are flexable enough to approximate moments to be negligible.

### Supports for trusses
There are 2 types of supports for trusses:
- Pinned
- Rolling
![[Pasted image 20211022210726.png]]

As can be seen rolling supports only exert a reaction force vertically, while pinned supports have reactions in both directions.

(Also note that since the supports touch at pins the bars connected to them are free to rotate like normal {duh})