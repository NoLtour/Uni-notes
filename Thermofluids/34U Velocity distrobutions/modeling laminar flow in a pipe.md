---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe the method for
## Modeling laminar flow in a pipe
### Usefull equation bit


### Derivation
We make some assumptions: 
- flow is fully developed (so it's cross section/flow is uniform for its length, aka a really long pipe) so no [[boundary layer]] [[first meme since easter break lets go|shinanigins]].
- Flow is incompressible
- No mass accumulation (flow rate is constant for the length of the pipe)

![[Pasted image 20220426154544.png]]

First equation is us expressing the net force acting on the section of water, and since acceleration is zero we know that net force is zero. So pressure force equals pipe surface shear force:

$$\begin{align*}
( (p+dp) - p ) \times \pi R^{2} &= \tau_{w} \times 2R\pi dx\\
dpR &= 2 \tau_{w} dx \\
\frac{dp}{dx} \frac{R}{2} &= \tau_{w}
\end{align*}$$

Now we have an expression relating the shear force and rate of change of pressure. Next we can model this as a [[newtonian fluids]]
