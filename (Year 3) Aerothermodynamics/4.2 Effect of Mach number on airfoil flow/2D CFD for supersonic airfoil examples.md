---
aliases: ["critical Mach number"]
tags: []
---

## 2D CFD for supersonic airfoil examples

Here we look at the same generic airfoil in a compressible, inviscid flow over a range of Mach numbers.

### Subsonic

#### "Low" subsonic ($M_{\infty}=0.6$)

![[Pasted image 20231123183331.png]]

Observations:
- No supersonic regions
- Speed increases on foil (as expected) above freestream

Aka: nothing interesting happens

#### Transonic ($M_{\infty}=0.8$)

![[Pasted image 20231123183403.png]]

Observations:
- The increasing velocity lead to $M>1$ on the foil
- There is a shock which allows transition back to freestream 

#### Critical Mach number

![[Pasted image 20231123184245.png]]

The critical mach number is the freestream Mach that will produce a supersonic region somewhere on the foil. (this is typically about 0.8)


### Supersonic

#### Mach 1 ($M_{\infty}=1$)

![[Pasted image 20231123185520.png]]

Observations:
- No normal shock on trailing, expected since freestream isn't subsonic
- [[oblique shocks|Oblique shocks]] still occur at the trailing edge
- There is a [[detached shock]], this is expected since the [[kutta condition]] requires a front stagnation point

#### Low supersonic ($M_{\infty}=1.2$)

![[Pasted image 20231123190016.png]]

Observations:
- No normal shock on trailing, expected since freestream isn't subsonic
- [[oblique shocks|Oblique shocks]] still occur at the trailing edge
- There is a [[detached shock]], this is expected since the [[kutta condition]] requires a front stagnation point
- (not much change, just slightly more curved)


#### Lowish supersonic ($M_{\infty}=1.4$)

![[Pasted image 20231123190219.png]]

Observations:
- No normal shock on trailing, expected since freestream isn't subsonic
- [[oblique shocks|Oblique shocks]] still occur at the trailing edge
- There is a [[detached shock]], this is expected since the [[kutta condition]] requires a front stagnation point
- Even more curved and [[detached shock]] get's tighter

### Angle of attack

![[Pasted image 20231123190438.png]]

Here the $\alpha=5.7\degree$, there are clearly significant differences between the transonic and supersonic cases:
- In the transonic case a shockwave forms on the top only
- The angle and geometry is such that the gas is in compression along the entire lower surface
