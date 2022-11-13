---
aliases: ["eigenvalue ODE"]
tags: []
---

## Solving eigenvalue ODEs

### Intro

Now your asking "what the fuck are those they sound painful" and the answer is they are not that bad! A eigenvalue ODE is just where you only have 2 terms in the ODE eg:

$$ \frac{d^{2}y}{dx^{2}} + \lambda y = 0 $$

We call them eigenvalue problems since they can be rearranged into:
$$ \frac{d^{2}y}{dx^{2}}  = -\lambda y $$
Which indicates it is possible to find derivatives/integrals simply by multiplying by $\lambda$.

### Example
> Solve:
> $$ \frac{d^{2}y}{dx^{2}} + \lambda y = 0 $$
> Where $y(0)=0$ and $y(\pi)=0$

We solve this using the same method [[solving linear homogeneous constant-coefficient equations#Method (for constant coefficients)|solving linear second order ODEs]] hence we will start with step 1:
$$\begin{align*}
m&=  \frac{0\pm\sqrt{0^{2}-4\times1\times\lambda}}{2\times1} &&\to& m&= \pm\sqrt{-\lambda}
\end{align*}$$
This becomes 3 separate problems, depending on the value of $\lambda$ hence our 3 cases are:
1) $(\lambda=-k^{2})\:\:<0$ so there is 2 real roots, so we use $y = Ae^{m_1 x} + Be^{m_2 x}\:\to\: y = Ae^{k x} + Be^{-kx}$
2) $(\lambda=k^{2})\:\:=0$ so there is 1 real roots, so we use $y = (Ax+B)e^{m_1 x}\:\to\:y = Ax+B$
3) $(\lambda=k^{2})\:\:>0$ so there is 2 complex roots, so we use $y = e^{ax} ( A\cos(bx) + B\sin(bx) ) \:\to\: y =  A\cos(kx) + B\sin(kx)$

For all of these $k$ is just some real constant which makes working cleaner since we don't need to write $\sqrt{\lambda}$ everywhere. The next step is to just solve it for each case, since $\lambda$ is unknown we need to treat this as a general case situation.

#### Case $(\lambda=-k^{2})\:\:<0$

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

#### Case $(\lambda=k^{2})\:\:=0$

$$\begin{align*}
y &=  Ax+B
\end{align*}$$
$$\begin{align*}
0 &=  A0+B & 0 &=  A\pi+B\\ 
0 &= B\\
& & 0 &=  A\pi\\ 
\end{align*}$$
This is a trivial solution and useless.


#### Case $(\lambda=k^{2})\:\:>0$

$$\begin{align*}
y &=   A\cos(kx) + B\sin(kx)
\end{align*}$$
$$\begin{align*}
0 &=   A\cos(k0) + B\sin(k0) & 0&=   A\cos(k\pi) + B\sin(k\pi)\\
0 &=   A \\
& & 0&= B\sin(k\pi)\\
& & \arcsin(0)=n\pi&= k\pi\\
& & n &= k\\
\therefore
\end{align*}$$
This is a trivial solution and useless.



