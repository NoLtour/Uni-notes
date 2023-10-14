---
aliases: ["linear","nonlinear","linear function","linearity","linear system"]
tags: []
---

## Linear systems

### Checking linearity

#### Linear case

Linearity can be a bit of a confusing subject, but fundamentally a equation is linear if it obeys the [[principle of superposition]].

$$\begin{align*}
y(t) &= 3t + 12  & &\to & y(t) &= 3(t + 4)& &\to & y(x) &= 3 x
\end{align*}$$

So then by superposition $y(x_{1} + x_{2}) = y(x_{1}) + y(x_{2})$, testing this:

$$\begin{align*}
y(x_{1} + x_{2}) =& y(x_{1}) + y(x_{2})\\
3(x_{1} + x_{2}) =&  (3x_{1}) + 3(x_{2})\\
 x_{1} + x_{2}  \equiv&   x_{1} +  x_{2} 
\end{align*}$$

#### Non-linear case

Doesn't take much to find a non linear case:
$$\begin{align*}
y(t) &= t^{2} + t
\end{align*}$$

Here you can just test using $x=2$, no need to do fancy variable shite. So lets check superposition:

$$\begin{align*}
y(2 + 2) &=  y(2) + y(2)\\
(2 + 2)^{2} + (2+2) &=  (2^{2} + 2) + (2^{2} + 2)\\
20 &\neq  12\
\end{align*}$$
 
There is no coordinate transform that is able to make this equation linear. ([[I suggest a proof by exhaustion|Proof is left as a exercise to the reader]])

### Linear systems

We know that [[block diagram]]s effectively just provide nice representations of systems which are really just "piles of math", so in the event all the functions are linear then the system is linear. So we can apply [[principle of superposition]] to them, in a block diagram this looks like:

![[Pasted image 20231014181009.png]]


