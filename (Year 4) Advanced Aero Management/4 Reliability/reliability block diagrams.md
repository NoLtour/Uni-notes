---
aliases:
  - reducing reliability block diagrams
tags:
---

## Reliability block diagrams

![[Pasted image 20241024112703.png]]

These are the blocks shown in [[complex reliability model]]s, they can be chained together to form extremely complex systems as seen above. 

Now your probably recalling [[transfer function series manipulation|reducing blocks in control theory]] and all the shit from heat transfer and electrisity, where we manipulate this sort of diagram to reduce them. Yes, that is exactly what we do.

### Reducing reliability block diagrams

By chaining together the methods from [[complex reliability model]]s for computing $R_{SYS}$, we can simplify these down into a single convenient equation.
1) Start by combining [[complex reliability model|series reliability models]]
2) Combine branches of these now singlue unit branched sections ([[complex reliability model|parallel reliability model]] and [[complex reliability model|m-out-of-n redundancy model]])
3) Repeat from step (1) till complete

### Example

Taking that diagram above, we start by doing the series paths in the parallel blocks. Then combine those in the parallel method:

![[Pasted image 20241024113236.png]]

Then we can easily reduce the [[complex reliability model|m-out-of-n redundancy model]]:

![[Pasted image 20241024113330.png]]

Now that everything is in series you just merge it all together, and boom. Ez.




