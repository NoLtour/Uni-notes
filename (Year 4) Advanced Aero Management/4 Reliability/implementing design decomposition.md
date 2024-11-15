---
aliases:
  - design decomposition
  - coordination through interfaces
tags:
---

## Implementing design decomposition

### Decomposition

This is critical in the design of well... anything. We need to break a complex design into manageable parts, aka decompose it into sub-systems to:
- Make effective use of specialists 
- Reduce the number of design variables to resonable numbers
- Reduce the scope of the models required

Of course we still have the problem of:
- Treating sub-systems separately fundamentally contradicts the fact they function as a part of a system, hence they are all coupled
- Sub-systems often have conflicting requirements
- Sub-systems have varying levels of system level performance contribution, they shouldn't be treated equally

### Interfaces

This is a traditional method for coordinating between sub-systems. Effectively we are defining each point of interaction between sub-systems, which could be actual communication like digital signals or thing's like mass flows, temperatures, pressures or stresses:

![[Pasted image 20241113160452.png|600]]

Interfaces may be agreed on at the start of the design process, based on the preliminary system level design. Hence there's a requirement for a system-level preliminary design for this to be implemented. These offer early constraints for sub-systems, forcing the designers to meet these interfacing targets. 

There are some problems with this approach:
- Constraints may not be possible on a component or system level, insufficient info in the preliminary design may have created impossible targets
- System level responses are rarely checked, since doing so requires a system level model which may be nearly impossible to do
- It may be too rigid, with changes in other subsystems not being reflected in the interface values

In real systems we rarely treat interface values as single values, instead defining them with a distribution. This is often some sort of mean with bounds, possibly as simple as $\bar{x}\pm \sigma$ or something more complex like:

![[Pasted image 20241113164417.png|550]]

### Robust Interfaces

Although upper and lower bounds are useful, it may be better to instead recast this as a [[Optimisation for robustness Overview|robust design]] problem, replacing simple bounds with a [[probability density function|PDF]] representing the possible bounds of the sub-system.

We do need a way to construct this PDF, generally that is done from past experience and/or [[expert elicitation]]. Just like with traditional interfaces, we should expect this [[probability density function|PDF]] to be updates as the design iteration progresses. We may even want to include the uncertainty in "how much could the interface change" in the [[probability density function|PDF]] by making it more conservative.

The downside of this method is it may be excessive, it's more expensive to implement than simpler interfacing methods, so it must be implemented only when doing so's sufficiently useful.


