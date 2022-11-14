---
aliases: [""]
tags: []
---

## Separation of variables the heat equation
#### Problem setup
Here we are going to be applying what was done from [[separation of variables]] but to the heat equation ([[parabolic partial differential equations|the prototype example for parabolic PDEs]]).

Solve:
$$ \frac{\delta y}{\delta t} = k^{2} \frac{\delta^{2} y}{\delta x^{2}} $$
With the boundary conditions:
$$\begin{align*}
\frac{\delta y}{\delta x}(0, t) &= 0, & \frac{\delta y}{\delta x}(1,t)=0  
\end{align*}$$
And initial data:
$$ y(x,0) = x(1-x) $$


#### Definition of boundary conditions
Just like last time we assume $y=T(t)\times X(x)$ hence:
$$\begin{align*}
\frac{\delta y}{\delta t} &=  k^{2} \frac{\delta^{2} y}{\delta x^{2}}\\
\frac{\delta TX}{\delta t} &=  k^{2} \frac{\delta^{2} TX}{\delta x^{2}}\\
X \dot{T} &=  k^{2} T X''\\
 \frac{X''}{X} &=k^{2} \frac{\dot{T}}{T}=\lambda 
\end{align*}$$
$$\begin{align*}
 \dot{T} - \frac{\lambda}{k^{2}} T&= 0 & X''-\lambda X &=  0
\end{align*}$$
Then we can easily define the boundary condition:
$$\begin{align*}
\frac{\delta y}{\delta x}(0, t) &= 0  & \frac{\delta y}{\delta x}(1,t)&= 0 \\
T(t) \frac{\delta X(0)}{\delta x} &= 0  & T(t) \frac{\delta X(1)}{\delta x}&= 0 \\
 \frac{\delta X(0)}{\delta x} &= X'(0) = 0  & \frac{\delta X(1)}{\delta x}&= X'(1)=0 \\
\end{align*}$$
Just like last time we are assuming that it is not $T(t)=0$ since that would lead to a [[insert self deprecating comment here|useless]] solution.

#### Solving the $X$ [[solving eigenvalue ODEs|eigenvalue]] problem
Same as [[separation of variables#Solving the x bit ($X'' - lambda X=0$)|last time]]:
$$\begin{align*}
 X''-\lambda X =  0\\
m=\pm\sqrt{\lambda}
\end{align*}$$
##### Case $(\lambda=c^{2})>0$ 
$$\begin{align*}
X &= Ae^{cx} + Be^{-cx}\\
X' &= c(Ae^{cx} - Be^{-cx})
\end{align*}$$
$$\begin{align*}
0 &= c(A - B) & 0 &= c(Ae^{c} - Be^{-c})\\
A &= B & 0 &= Ae^{c} - Be^{-c}\\
& & 0 &= A(e^{c} - e^{-c})\\
& & 0 &= A = B
\end{align*}$$
Clearly this case has a useless trivial solution.

##### Case $(\lambda=c^{2})=0$
$$\begin{align*}
X &= Ax+B\\
X' &= A
\end{align*}$$
$$\begin{align*}
0 &= A & 0&= A
\end{align*}$$
Here there no solution for $B$ but $A=0$ hence we know a possible solution is:
$$ X = B $$
##### Case $(\lambda=-c^{2})<0$
$$\begin{align*}
X &= A\sin cx + B\cos cx\\
X' &= c(A\cos cx - B\sin cx)
\end{align*}$$
$$\begin{align*}
0 &= c(A) & 0 &= c(A\cos c - B\sin c)\\
0 &= A & 0 &=  B\sin c\\
&& \arcsin(0) = n\pi &= c
\end{align*}$$
Hence a possible solution is:
$$ X = B_{n} \cos(n\pi x) $$

### Solving the $T$ problem
Well now we can see things are more complicated since there is more than 1 possible solution to $X$, so we have to consider all of them:

#### Case ($\lambda=-n^{2}\pi^{2}$<0)

