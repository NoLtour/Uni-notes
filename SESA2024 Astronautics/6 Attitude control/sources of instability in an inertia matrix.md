---
aliases: [""]
tags: []
---

## Sources of instability in an [[moment of inertia|inertia matrix]]
### Outline
![[moment of inertia#^cc3cb6]]

The [[products of inertia]] can be interpreted as "a measure of unbalance", they lead to [[cross-coupling]]. This makes them useful for designing stable vehicles, by ensuring mass is properly distributed by properly balancing the layout of components you can reduce the natural instability of a vehicle (this of course is easier said than done).

### The ideal matrix
For long term stability such as what you want for [[spin stabilising a spacecraft]] you want the following properties in your [[moment of inertia|inertia matrix]]:

> ### $$ \begin{pmatrix} I_{xx}  & 0 & 0 \\ 0 & I_{xx} & 0 \\ 0 & 0 & I_{zz} \end{pmatrix}  $$ 
>> To achieve maximum long term stability:
>> $I_{xx}=I_{yy}=$ the non rotational axis should have equal [[moment of inertia|moments of inertia]]
>> $I_{xx} << I_{zz}$ the rotational axis [[moment of inertia]] should be larger than the other axis' [[moment of inertia|moments of inertia]]
>> $I_{zz}$ to be large
>> By having all the [[products of inertia]] be as close to zero as possible it minimises [[nutation]].