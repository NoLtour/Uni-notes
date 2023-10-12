---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can we use
## Operator notation to define linear equations

Any equation that can satisfy the following is a [[linear differential equation]]:

> ### $$ L[ax_1 + bx_2] = aL[x_1] + bL[x_2] $$ 
>> where:
>> $x_1,x_2=$ all functions of x 
>> $a,b=$ any constant
>> $L[...]=$ a function function

^785a09

### Example
> Prove that $\frac{d^{2}x}{dt^{2}} + 4t \frac{dx}{dt} - (\sin t)x = \cos t$ is a [[linear differential equation]].

$$\begin{align*}
L = \frac{d^{2}}{dt^{2}} + 4t \frac{d}{dt} - (\sin t)
\end{align*}$$

$$\begin{align*}
L[ax_1 + bx_2] &= L[ax_1 + bx_2]\\
&= (ax_1 + bx_2)\frac{d^{2}}{dt^{2}} + (ax_1 + bx_2)4t \frac{d}{dt} - (ax_1 + bx_2)(\sin t)\\
&= a\frac{d^{2}x_1}{dt^{2}} + b\frac{d^{2}x_2}{dt^{2}} + a4t \frac{dx_1}{dt} + b 4t \frac{dx_2}{dt} - ax_1 \sin t - bx_2 \sin t\\
&= a\left( \frac{d^{2}x_1}{dt^{2}} + 4t \frac{dx_1}{dt} - x_1 \sin t \right) + b\left( \frac{d^{2}x_2}{dt^{2}} + 4t \frac{dx_2}{dt} - x_2 \sin t \right)\\
&= aL[x_1] + bL[x_2]\\
\therefore L[ax_1 + bx_2] &= aL[x_1] + bL[x_2]\\
\end{align*}$$

$\therefore \frac{d^{2}x}{dt^{2}} + 4t \frac{dx}{dt} - (\sin t)x = \cos t$   is a [[linear differential equation]].