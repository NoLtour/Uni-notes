---
aliases: [""]
tags: []
---

## Separation of variables
### Intro

Ok so we have the abomination from [[classification of partial differential equations|classification of PDEs]], so how the fuck are we supposed to solve it? 
$$ a \frac{\delta^{2} u}{ \delta x^{2} } + 2b \frac{\delta^{2}u}{\delta x \delta y} + c \frac{\delta^{2} u}{\delta y^{2}} + d \frac{\delta u}{\delta x} + e \frac{\delta u}{\delta y} + fu = 0 $$
Turns out it's not so bad, we start by assuming the solution is:
$$ y(x,t) = X(x) \times T(t) $$
Now you see we've [[see what I did there so funny|separated the variables]] into two simpler functions, theoretically these functions are just [[ordinary differential equation|ODE]]s so they can be solved as such!

### Example
> Given the PDE:
> $$ \frac{\delta^{2}y}{\delta t^{2}} = c^{2} \frac{\delta^{2}y}{\delta x^{2}} $$
> Such that $y(0,t)=0$ and $y(L,t)=0$ find the solution.

Use the substitution $y(x,t) = X(x) \times T(t)$:
$$\begin{align*}
\frac{\delta^{2}y}{\delta t^{2}} &=  c^{2} \frac{\delta^{2}y}{\delta x^{2}} & y(x,t) &=  X(x) \times T(t)\\
\frac{\delta^{2} (XT) }{\delta t^{2}} &=  c^{2} \frac{\delta^{2}(XT)}{\delta x^{2}}
\end{align*}$$
Since $X$ and $T$ are purely dependent on $x$ and $t$ respectively, when being differentiated in terms of another independent variable it is clear they are effectively just constants:
$$\begin{align*}
\frac{\delta^{2}X(x)}{\delta t^{2}} &= 0 & \frac{\delta^{2}T(t)}{\delta x^{2}} &= 0\\
\therefore\:\: \frac{\delta^{2} (XT) }{\delta t^{2}} & =  X \frac{\delta^{2} T }{\delta t^{2}} & \frac{\delta^{2} (XT) }{\delta x^{2}} & =  T \frac{\delta^{2} X }{\delta x^{2}}
\end{align*}$$
Hence the previous complicated derivative can be simplified to:
$$\begin{align*}
X \frac{\delta^{2} T }{\delta t^{2}} &=  c^{2} T \frac{\delta^{2} X }{\delta x^{2}}\\
X \ddot{T} &=  c^{2} T X''\\
\frac{1}{c^{2}} \frac{\ddot{T}}{T} &=  \frac{X''}{X}\\
\frac{1}{c^{2}} \hat{f}_{1}(t) &= \hat{f}_{2}(x)
\end{align*}$$
The final line is simply me showing that both sides are entirely dependent on a single independent variable, but at the same time also always equal; hence they muse be equal to the same constant! Hence this can be expressed as:
$$\begin{align*}
 \frac{1}{c^{2}} \frac{\ddot{T}}{T}=\frac{1}{c^{2}} \hat{f}_{1}(t) &= \lambda & \frac{X''}{X}=\hat{f}_{2}(x) &= \lambda\\
 \frac{1}{c^{2}} \frac{\ddot{T}}{T} - \lambda &= 0 & \frac{X''}{X} - \lambda &= 0\\
\end{align*}$$ 
In this form it becomes obvious that this is just a [[eigenvalue ]]