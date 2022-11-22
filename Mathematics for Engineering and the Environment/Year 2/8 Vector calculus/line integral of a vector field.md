---
aliases: [""]
tags: []
---

## Line integral of a vector field
### Intro
Integration is the same as normal, just makes use of [[dot product (vectors)|dot product]].


### Work done example
If we have a [[vector fields|vector field]] that represents the force acting on a body at some point in space then it is really easy to define the [[work done in dynamics|work done]] by that body along the path taken $\vec{r}(t)$:
$$ W = \int^{b}_{a} \vec{F}(t) \cdot \frac{d\vec{r}}{dt}dt = \int^{b}_{a} \vec{F}(t) \cdot  d\vec{r} $$
It's obvious that even in the case where the start and end of $\vec{r}$ are the same, you can get 2 different values of work done depending on path taken:
![[Pasted image 20221122144659.png]]
In the special case where the path doesn't matter as long as  the end points are the same, we call that the [[conservative force|conservative case]].
