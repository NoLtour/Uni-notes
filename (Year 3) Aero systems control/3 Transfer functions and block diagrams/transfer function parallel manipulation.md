---
aliases: ["reducing parallel blocks","parallel transfer function reduction"]
tags: []
---

## Transfer function parallel manipulation

Just like [[transfer function series manipulation]] allows for series elements to be combined, a similar thing can be done for parallel connections:

> ![[Pasted image 20231029115621.png]]
> ### $$\begin{align*} G_{eq} &= \pm G_{1} \pm G_{2} ... \pm G_{n}  \end{align*}$$
>> where:
>> $G_{eq}=$ the equivalent [[Laplace transform representation of a system|Laplace domain transfer function]] for all the blocks in series
>> $\pm G_{x}=$ one of the parallel blocks, the $\pm$ is because the sign get's determined at the [[block diagram parts|summing junction]] (set by user)

Unlike [[transfer function series manipulation]] where blocks get multiplied, in parallel they get summed.
