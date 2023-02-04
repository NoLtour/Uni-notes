---
aliases: ["method for evaluating shear force and bending moment diagrams"]
tags: ["Question","QFormat3"]
---

#### What is the
## Method for constructing shear force and bending moment diagrams
There are a few steps you go through:
1) Label and calcuate support reactions and moments, here we can approximate [[distrobuted force on a beam|distrobuted force]] as [[concentrated force on a beam|concentrated force]] to aid in calculation.
2) We draw a new [[Free body diagram]] with the reactions calculated and don't approximate [[distrobuted force on a beam]]
3) We go back to the beam and cut the beam into segments making [[Free body diagram]]s for each of the different loading conditions with labels using [[sign convention for beam force|sign convention]].
We then get our equalibrium equations for the section and solve them to get all our values.


### Example
Given:
![[Pasted image 20211025123655.png]]

We would:
1)
> Although the [[types of supports for beams#Types of supports for beams|pin]] can excert a horizontal reaction the lack of any horizontal forces means we know that the horizontal reaction would be zero, hence no reason to draw it.
> ![[Pasted image 20211025124200.png]]
> Also note that here we approximated the load as a point load, this would be done to figure out reaction forces but in later steps we will be calculating [[bending moment]]s and [[shearing force in beams|shearing force]]s so we will not model it as a point load then

2)
> We redraw the diagram again
> ![[Pasted image 20211025124305.png]]

3)
> Here we only need one diagram to represent the beam segment as we move in a direction away from the centre
> ![[Pasted image 20211025124649.png]]
> Vertical:
> $$ \begin{align*}
F\frac{x}{L} + Q =& 0\\
F\frac{x}{L} =& -Q
\end{align*} $$
> Rotational (taken about the cut location):
> $$ \begin{align*}
M = \frac{x}{2}*F\frac{x}{L} 
\end{align*} $$
> So:
> $$\begin{align*}
 M =& \frac{x}{2}*-Q\\
Q =& \frac{-2M}{x}
\end{align*}$$
> Hence values for Q and M along the beam