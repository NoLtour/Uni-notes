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

### Method

1) Split $y(x,t)$ into $y(x,t)=X(x)\times T(t)$ 
2) Determine the boundary conditions for $X$ and $T$ from the information about the boundary conditions of $y$
3) Solve the [[solving eigenvalue ODEs|eigenvalue]] problem for $X$ and $T$ to obtain $X_{n}$ and $T_{n}$
4) Combine solutions to get $y$, then apply superposition: $y(x,t)=\sum\limits X_{n}T_{n}$
5) If needed apply initial conditions, this often requires [[defining the fourier series|Fourier series]]

### Example (wave equation)
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
X &=  Ae^{k x} + Be^{-kx} 
\end{align*}$$
$$\begin{align*}
X(0) &= 0 & X(L) &= 0\\
0&=  Ae^{k 0} + Be^{-k0}  & 0 &=  Ae^{k L} + Be^{-kL}\\
0&=  A + B &  - A &=  B e^{-2kL} \\
A &= -B\\
&& B &= Be^{-2kL}\\
&& &\therefore B=A=0
\end{align*}$$
This is a trivial solution and useless.

##### Case $(\lambda=k^{2})\:\:=0$

$$\begin{align*}
X &=  Ax+B
\end{align*}$$
$$\begin{align*}
0 &=  A0+B & 0 &=  AL+B\\ 
0 &= B\\
& & 0 &=  AL\\ 
\end{align*}$$
This is a trivial solution and useless.

##### Case $(\lambda=-k^{2})\:\:<0$

$$\begin{align*}
X &=   A\cos(kx) + B\sin(kx)
\end{align*}$$
$$\begin{align*}
0 &=   A\cos(k0) + B\sin(k0) & 0&=   A\cos(kL) + B\sin(kL)\\
0 &=   A \\
& & 0&= B\sin(kL)\\
& & \arcsin(0)=0,\pi,2\pi,3\pi,4\pi...=n\pi&= kL & \text{where }n\text{ is some integer}\\
& & \frac{n\pi}{L} &= k\\
\end{align*}$$
$$\begin{align*}
\therefore \:\: X &= B_{n} \sin\left(\frac{n\pi}{L}x\right)
\end{align*}$$
[[these take fuckin ages|Finally]] a non trivial solution. In this case $\lambda=-k^{2}$ hence:
$$\begin{align*}
\lambda_{n} &= - \left(\frac{n\pi}{L}\right)^{2}
\end{align*}$$
It is important to note that since there are infinite solutions depending on the value of $n$ there are infinite corresponding solutions of the equation $y$ and hence value's of $\lambda$ so you need to make sure to clearly show this with variables such as $\lambda_{n}$.

#### Solving the t bit ($\ddot{T} - c^{2} \lambda T=0$)
Well it's the same constant $\lambda$ for both $T$ and $X$ equations, hence from [[separation of variables#Solving the x bit ($X'' - lambda X=0$)|the result above]] we actually know the value of $\lambda$, which is:
$$\begin{align*}
\lambda_{n} &= - \left(\frac{n\pi}{L}\right)^{2}
\end{align*}$$
$$\begin{align*}
\ddot{T} - c^{2} \lambda T &=0 &&\to& \ddot{T} + c^{2} \left(\frac{n\pi}{L}\right)^{2} T &=0 
\end{align*}$$
Then we can solve [[solving eigenvalue ODEs|eigenvalue ODE]]:
$$\begin{align*}
m &= \frac{0^{2}\pm\sqrt{ 0^{2} - 4 c^{2} \left(\frac{n\pi}{L}\right)^{2} }}{2} = 0\pm j \frac{cn\pi}{L}\\
\end{align*}$$
This is expected since we are just taking $\lambda$ and multiplying by a real constant $c$, so the solution for $T$ is:
$$\begin{align*}
T_{n}(t) &= A_{n} \cos\left( \frac{cn\pi}{L}t \right) + B_{n} \sin\left( \frac{cn\pi}{L}t \right) 
\end{align*}$$
Of course without more information this is the most precise solution we can get.

### Combining our solutions
So now we just combine using our original definition of $y$ in terms of $T$ and $X$:
$$\begin{align*}
y(x,t) &=  X(x) \times T(t)\\
  &=  \left[B_{Xn} \sin\left(\frac{n\pi}{L}x\right)\right] \times \left[ A_{Tn} \cos\left( \frac{cn\pi}{L}t \right) + B_{Tn} \sin\left( \frac{cn\pi}{L}t \right)  \right]\\\\
&(\text{merging constants})\\\\
y(x,t)  &=   \left[ A_{ n} \cos\left( \frac{cn\pi}{L}t \right) + B_{ n} \sin\left( \frac{cn\pi}{L}t \right)  \right]\sin\left(\frac{n\pi}{L}x\right) 
\end{align*}$$
Now although this is a valid solution, since this is a linear [[partial differential equation|PDE]] we can sum 2 or more solutions to get another still valid solution (in the same way we can for normal linear [[ordinary differential equation|ODE]]s) hence since there are solutions for each of the infinite values of $n$:

$$\begin{align*}
y(x,t)  &=  \sum\limits^{\infty}_{n=1} \left[ A_{ n} \cos\left( \frac{cn\pi}{L}t \right) + B_{ n} \sin\left( \frac{cn\pi}{L}t\right)  \right]\sin\left(\frac{n\pi}{L}x\right) 
\end{align*}$$
Which is clearly the most general form possible.

#### Additional initial data
The solution can be defined further if given additional boundary conditions, such as:
$$\begin{align*}
y(x,0) &= v(x) & \frac{\delta y}{\delta t}(x, 0)=u(x)
\end{align*}$$
Then we take our solution, differentiate and substitute:
$$\begin{align*}
y(x,t)  &=  \sum\limits^{\infty}_{n=1} \left[ A_{ n} \cos\left( \frac{cn\pi}{L}t \right) + B_{ n} \sin\left( \frac{cn\pi}{L}t\right)  \right]\sin\left(\frac{n\pi}{L}x\right)  & \frac{\delta y(x,t)}{\delta t}  &=  \sum\limits^{\infty}_{n=1} \left[ -A_{ n} \frac{cn\pi}{L} \sin\left( \frac{cn\pi}{L}t \right) + B_{ n} \frac{cn\pi}{L}\cos\left( \frac{cn\pi}{L}t\right)  \right]\sin\left(\frac{n\pi}{L}x\right) \\
y(x,0) = v(x)  &=  \sum\limits^{\infty}_{n=1}  A_{ n}  \sin\left(\frac{n\pi}{L}x\right)  & \frac{\delta y(x,0)}{\delta t} = u(x) &=  \sum\limits^{\infty}_{n=1}   B_{ n} \frac{cn\pi}{L} \sin\left(\frac{n\pi}{L}x\right) 
\end{align*}$$
This is clearly just [[defining the fourier series|Fourier series]], with a period of $\frac{n\pi}{L}$ so it's clear that $L_{p}= \frac{2n\pi}{L}$ also $a_{n}=0$ and $a_{0}=0$, hence to bind $A_{n},B_{n}$ which are similar to $b_{n}$ in this context:
$$\begin{align*}
f(x) &=  \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ a_{n} \cos \left( \frac{n\pi}{L_{p}} x \right) + b_{n} \sin \left(\frac{n\pi}{L_{p}} x\right) \right]\\
f(x) &=  \sum\limits^{\infty}_{n=1}  b_{n} \sin \left(\frac{n\pi}{L_{p}} x\right) \\
\end{align*}$$
$$\begin{align*}
A_{n} &= b_{n} & B_{n} \frac{cn\pi}{L} & = b_{n} \\
A_{n}&= \frac{1}{\frac{2n\pi}{L}} \int^{\frac{n\pi}{L}}_{-\frac{n\pi}{L} } u(x) \sin\left(\frac{n\pi}{\frac{2n\pi}{L}} x\right) \cdot dx  & B_{n} &= \frac{L}{cn\pi} \frac{1}{\frac{2n\pi}{L}}  \int^{\frac{n\pi}{L}}_{-\frac{n\pi}{L} } v(x) \sin\left(\frac{n\pi}{\frac{2n\pi}{L}} x\right) \cdot dx \\
A_{n}&= \frac{L}{ 2n\pi} \int^{\frac{n\pi}{L}}_{-\frac{n\pi}{L} } u(x) \sin\left(\frac{ L}{2} x\right) \cdot dx  &  B_{n} &= \left(\frac{L}{cn\pi}\right)^{2} \frac{1}{2}   \int^{\frac{n\pi}{L}}_{-\frac{n\pi}{L} } v(x) \sin\left(\frac{ L}{2} x\right) \cdot dx\\
\end{align*}$$
Which for known functions of $v$ and $u$ are solvable (I think this is what's meant, still kinda confused on this last bit).