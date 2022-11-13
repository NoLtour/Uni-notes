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

#### Separation
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
The final line is simply me showing that both sides are entirely dependent on a single independent variable, but at the same time also always equal;  they must be equal to the same constant! Hence this can be expressed as:
$$\begin{align*}
 \frac{1}{c^{2}} \frac{\ddot{T}}{T}=\frac{1}{c^{2}} \hat{f}_{1}(t) &= \lambda & \frac{X''}{X}=\hat{f}_{2}(x) &= \lambda\\
\ddot{T}  - c^{2} \lambda T &= 0 &  X''  - \lambda X &= 0\\
\end{align*}$$
#### Boundary conditions
In this form it becomes obvious that this is just a [[solving eigenvalue ODEs|eigenvalue ODE]] so we can just apply that method to both of them. If we look at the set of boundary conditions given at the start:
$$\begin{align*}
y(0,t)&=0 & y(L,t)&=0\\
X(0)T(t)&= 0 & X(L)T(t)&= 0
\end{align*}$$
In this case we know that for $X(0)T(t)$ either $X(0)=0$ or $T(t)=0$, to get any useful solutions we assume that $T(t)=?$ and $X(0)=0$ (if we took $T(t)=0$ then $y=0$ and no useful information can be gathered) this is also done with $X(L)T(t)=0$ hence we get:
$$\begin{align*}
X(0) &= 0 & T(t) &= ? &&\text{and} & X(L) &= 0 & T(t) &= ? & 
\end{align*}$$
It quickly becomes apparent that we only have boundary conditions for $x$, this is a future problem though so let's start by solving $X$'s [[solving eigenvalue ODEs|eigenvalue ODE]].

#### Solving the x bit ($X'' - \lambda X=0$)

##### Case $(\lambda=k^{2})\:\:>0$
$$\begin{align*}
y &=  Ae^{k x} + Be^{-kx} 
\end{align*}$$
$$\begin{align*}
y(0) &= 0 & y(\pi) &= 0\\
0&=  Ae^{k 0} + Be^{-k0}  & 0 &=  Ae^{k \pi} + Be^{-k\pi}\\
0&=  A + B &  - A &=  B e^{-2k\pi} \\
A &= -B\\
&& B &= Be^{-2k\pi}\\
&& &\therefore B=A=0
\end{align*}$$
This is a trivial solution and useless.
