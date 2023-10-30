---
aliases: ["supersonic wind tunnel"]
tags: []
---

## Ideal supersonic wind tunnel

![[Pasted image 20231028160317.png]]

Wind tunnels are useful for flow experimentation, but supersonic ones introduce lot's of challenges.

One is ensuring the normal shock occurs in the correct location, the only location in an empty wind tunnel that should have a normal shock is where we want supersonic flow to transition to subsonic.
So we want the normal shock to occur in the second throat.


The problem comes in starting it. When it start's there is a tendency for a shock to form in the test section, if the second throat is smaller than the first it's possible it could become choked forcing the first throat into a subsonic regime due to the backpressure. To prevent this the second throat's made larger.

![[Pasted image 20231028160511.png]]

An additional consideration is the effect of pressure losses, recall the [[mass flowrate through a choked nozzle]] equation:

$$ \dot{m}  = p_{0}  A^{*} \sqrt{\frac{\gamma}{RT_{0}}} \left(\frac{2}{\gamma+1}\right)^{\frac{\gamma+1}{2(\gamma-1)}} $$

If stagnation pressure drops through the test section a larger second throat would be needed to maintain the same mass flow rate. It seems necessary to have some sort of variable geometry to ensure correct shock formation, as the initial conditions vs operating conditions are different.
