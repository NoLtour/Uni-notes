---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## General solution of a linear nonhomogeneous equation

Let $L[x] = f(t)$ be a [[homogeneous and nonhomogeneous differential equations|nonhomogeneous]] [[linear differential equation]].

Now let $x*$ be a solution of $L[x]$ so $L[x*] = f(t)$.

Now conider the related [[homogeneous and nonhomogeneous differential equations|homogeneous equation]] $L[x]=0$, and let the solution of this be $x_c$ so $L[x_c]=0$.

If $L[x]$ is a [[linear differential equation]] then ([[operator notation to define linear differential equations|from this]]) $L[ax_1 + bx_2] = aL[x_1] + bL[x_2]$ and since $x_c$ and $x*$ are solutions to $L[x]$ then:
$$\begin{align*}
L[x_c + x*] &= L[x_c] + L[x*]  & L[x_c]&=0 & L[x*] &= f(t)\\
L[x_c + x*] &= 0 + f(t)\\
\therefore L[x_c + x*] &= f(t)
\end{align*}$$

^d8709d

So $x_c + x*$ is a solution of $L[x]=f(t)$

> ### $$ L[x_c + x*] = f(t) $$ 
>> where:
>> $x_c=$ a solution of the homogeneous version of $L[x] = f(t) \rightarrow L[x] =0$ (also known as [[complementary function]])
>> $x*=$ any solution of $L[x] = f(t)$ (also known as [[particular integral]])
>> $L[x]=$ a [[linear differential equation]]

^50b2a4

Note that we define the [[particular integral]] and [[complementary function]] from $x_c$ and $x*$: ^3fefb1
- $x*$ the "any solution" is the [[particular integral]] ^eaa815
- $x_c$ is the [[complementary function]] ^a0a99f

It follows from this that finding the general solution of a nonhomogeneous linear differential equation can be reduced to the problem of finding any solution of thenonhomogeneous equation and adding to it the general solution of the equivalent homogeneous equation.

In the event that you are totally confused we can do some examples.

### Examples

Find the general solution of $\frac{d^{2}x}{dt^{2}}+ \lambda^{2}x = 4t^{3}$
![[Pasted image 20211219172823.png]]