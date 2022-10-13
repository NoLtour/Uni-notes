---
aliases: [""]
tags: []
---

## Dual spin stabilising a spacecraft
### Outline
Similar to just [[spin stabilising a spacecraft]] except instead of spinning the whole thing you just spin a single section of it, you spin the craft somewhere in the range of 10 to 60 rpm which leads to stability due to [[gyroscopic rigidity]], [[gyroscopic procession]] and the fact that external influences such as drag tend to act on the body such that there is less net torque.

![[Pasted image 20221013144033.png]]

### Consequences
- Systems mounted on the spinning section have all the effects mentioned in [[spin stabilising a spacecraft#Consequences]]
- Having a stationary section means things can be mounted such that they maintain constant orientation
- When mounting stuff you still need to consider the effects on the [[moment of inertia|inertia matrix]] this applies to both the spinning and stationary parts
- Now you have a complex connection point between the two sections of your craft, makes power/information/fluid transfer between the sections much more complex as well as introducing a new mechanical failure point.

### Choice of spin axis
The spin axis can only have a constant direction if it is a [[principle axis]] (specifically either one with the maximum or minimum [[moment of linear momentum|angular momentum]] else you get [[spin vid|this issue]]).
For long term stability it's best to choose the axis of maximum inertia. (same stuff as the [[spin stabilising a spacecraft]])

### Balance
The spinning part needs to have equal inertias about axes orthogonal to the spin axis.

### Dampening
To counteract [[nutation]] you might have passive or active dampeners to counteract the nutation.
