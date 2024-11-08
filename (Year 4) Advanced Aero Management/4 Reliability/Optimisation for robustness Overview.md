---
aliases: 
tags:
  - NotesPage
---

# Optimisation for robustness Overview

#### Intro and contents

If we have some performance characteristic, which we quantify with the function $f(x)$, then how do we optimize our parameter $x$ to get best performance? The obvious analysis is look at minima:

![[Pasted image 20241107165704.png]]

That said, the greatest minima isn't necessarily the best minima. Although $A$ has better peak performance, if $x$ is subject to uncertainty $B$ may actually be better. We may also place a intrinsic value on certainty above performance, at that point $B$ is the clear winner. What we will cover here is comparable to previous [[Taguchi optimisation analysis]] where we balance performance and robustness.

- [[aleatory and epistemic uncertainty]]
- [[optimisation under uncertainty]]
- [[surrogate modelling]]

Something to also keep in mind is the existence of constraints, generally better systems cost more. We may place constraints on the parameters values based on things like "mass" or "cost":

![[Pasted image 20241107190643.png]]


## Expanded articles
![[aleatory and epistemic uncertainty]]
![[optimisation under uncertainty]]
![[surrogate modelling]]