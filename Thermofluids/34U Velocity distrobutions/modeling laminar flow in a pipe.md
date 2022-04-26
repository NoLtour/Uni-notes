---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe the method for
## Modeling laminar flow in a pipe
### Usefull equation bit


### Derivation
First we start with the assumption that the flow is fully developed (so it's cross section/flow is uniform for its length, aka a really long pipe) so no [[boundary layer]] [[first meme since easter break lets go|shinanigins]].

![[Pasted image 20220426154544.png]]

First equation is us expressing the net force acting on the section of water, and since acceleration is zero we know that net force is zero. So pressure force equals pipe surface shear force:

$$\begin{align*}
( (p+dp) - p ) \times \pi R^{2} &= \tau_{w} \times 2R\pi dx\\
dpR &= 2 \tau_{w} dx \\
\frac{dp}{dx} \frac{R}{2} &= \tau_{w}
\end{align*}$$