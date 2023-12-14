---
aliases: [""]
tags: []
---

## Time steps

Something to note is that just as $\Delta x$ resolution matters, the $\Delta t$ resolution is very significant. Recall how [[1D discretised time variant heat diffusion]] creates equations where the state of a cell is only dependent on ones adjasent:

![[Pasted image 20231214115902.png]]

This means that the maximum rate at which information can propagate is $\frac{\Delta x}{\Delta t}$, which means that it's possible to have such a high time step that heat propagates in the system slower than it actually can! Which leads to all sorts of problems, generally making the equations unstable and preventing them from converging.

To solve this a bunch of analysis has to be done to determine the largest possible timestep before this occurs, in the specific case of [[1D discretised time variant heat diffusion]] the equation would be:

$$\begin{align*}
\Delta t &\leq \frac{\Delta x^{2}}{2\alpha} &&\equiv& F &\leq \frac{1}{2} 
\end{align*}$$

If that condition is met, then the system in [[1D discretised time variant heat diffusion]] would converge. Of course this stability criteria is dependent on the model, this example only works for our highly specific case.
