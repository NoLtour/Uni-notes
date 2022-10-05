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

#### The case where k is real and has 2 solutions

> ### $$ x^{2} \frac{d^{2}y}{dx^{2}} + bx \frac{dy}{dx} + c y = 0 $$ 
> ### $$ k_{1,2} = \frac{ (b-1) \pm \sqrt{ (b-1)^{2} - 4c } }{ 2 } $$ 
> ### $$ y = A x^{k_{1}} + B x^{k_{2}} $$ 
>> solving:
>> Simply sub the values of $k_{1},k_{2}$ 
>> $=$
>> $=$

#### The case where k is complex or duplicate

> ### $$ x^{2} \frac{d^{2}y}{dx^{2}} + bx \frac{dy}{dx} + c y = 0 $$ 
> ### $$  \frac{d^{2}y}{dt^{2}} + (b-1) \frac{dy}{dt} + c y = 0 $$ 
> ### $$ t=\ln x $$ 
>> solving:
>> $=$ 
>> $=$
>> $=$

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

If the values of $k$ are not complex or duplicates every thing's easy (note this part still works with complex it's just really painful): 

$$\begin{align*}
y &= A y_{1} + B y_{2} & y_{1} &= x^{k_{1}} & y_{2} &= x^{k_{2}} \\
y &= A x^{k_{1}} + B x^{k_{2}}
\end{align*}$$

Else in the case where $k_{1} = k_{2}$ or is complex instead of using $y=x^{k}$ substitute $t=\log(x)$:

$$\begin{align*}
x^{2} \frac{d^{2}y}{dx^{2}} + bx \frac{dy}{dx} + c y &= 0 & t &= \log(x) \\
&...\\
 \frac{d^{2}y}{dt^{2}} + (b-1) \frac{dy}{dt} + c y &= 0 
\end{align*}$$

([[UNFINISHED STUFF]] need to figure out intermediate steps)

Then from this step onwards it's just solving the same as [[solving linear homogeneous constant-coefficient equations]].


