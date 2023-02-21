---
aliases: ["fixed tailplane","adjustable tailplane","all moving tailplane"]
tags: []
---

## Other methods of trim

So far we've been modelling the tail plane using a elevator, but not all aircraft control the tail that way:

![[Pasted image 20230218112340.png]]

### Fixed tail

![[Pasted image 20230218112451.png]]

Benefits:
- Lighter
- Cheaper
- Simpler
- Often safer in event of failure

Cons:
- Limited control (can't move much)
- Higher associated trim drag

When modelling $a_{2}<a_{1}$.

### Adjustable tail plane

![[Pasted image 20230218113212.png]]

To achieve trim you change the instillation angle $\alpha_{S}$, elevator control is then about the trim point.

Pros:
- High trimming power
- Increased range of stable CG locations
- Reduced drag as elevator and stabiliser aligned when in trim

Cons:
- High complexity

This is very common in airliners.

### All moving

![[Pasted image 20230218112636.png]]

Here the only thing that exists when controlling the tail is it's overall angle.

Benefits:
- High trimming power
- Can therefore move CG around more
- Lower drag 

Cons:
- Increased complexity
