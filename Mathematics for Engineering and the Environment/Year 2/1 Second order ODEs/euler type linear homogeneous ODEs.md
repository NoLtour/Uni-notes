---
aliases: ["solving euler type linear homogeneous ODEs"]
tags: []
---

## Euler type linear homogeneous ODEs

### What it is

So these are actually quite cool (and common), as you'll see in a bit this is a [[homogeneous and nonhomogeneous differential equations|homogeneous]] Euler type:

> ### $$ x^{2} \frac{d^{2}y}{dx^{2}} + bx \frac{dy}{dx} + c y = 0 $$ 

What you'll note is the difference between this and a [[solving linear homogeneous constant-coefficient equations|linear second order homogeneous ODE]] is the multiplication by decreasing powers of $x$, these actually cancel out with the differentials leading to a dimensionless equation.

### Solving it



### Theory to solve it

So basically if you recall the method from [[solving linear homogeneous constant-coefficient equations#Proofing solving linear homogeneous constant-coefficient equations Method the method|this proof]], it's the same(ish). We need to find 2 [[linearly dependent and independent functions|linearly independent functions]] that solve the equation.

Of course the first step is to guess what this function is, since this is a proof [[I am omnipitent ghuahahhd|my guess is right]]. Lets guess $y = x^{k}$:

$$\begin{align*}
x^{2} \frac{d^{2}y}{dx^{2}} + bx \frac{dy}{dx} + c y &= 0 & y &= x^{k} \\
& & \frac{dy}{dx} &= k x^{k-1}\\
& & \frac{d^{2}y}{dx^{2}} &= k (k-2) x^{k-2}\\
x^{2} k (k-2) x^{k-2} + bx k x^{k-1} + c x^{k} &= 0\\
k (k-2) x^{k} + bx x^{k} + c x^{k} &= 0\\
k^{2} + (b-1)k + c &= 0\\
k &= \frac{ (b-1) \pm \sqrt{ (b-1)^{2} - 4c } }{ 2 }
\end{align*}$$

If the values of $k$ are n
