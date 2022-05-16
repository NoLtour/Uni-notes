---
aliases: ["principal value"]
tags: ["Question","QFormat3"]
---

#### How do you find the
## Logarithm of a complex number
### Equation
> ### $$ \ln( z ) = \ln|z| + i \arg z $$ 
>> where:
>> $z=$ some imaginary number
>> [[arg (complex numbers)|arg function]] is used

### Proof
Consider the equation $z = e^{w}$ if we express $z=x+iy$ and $w=u+iv$:

$$\begin{align*}
z &= e^{w} \\
 && z&=x+iy & w&=u+iv \\
 x+iy &= e^{u+iv}\\
&= e^{u}e^{iv}\\
&= e^{u} (\cos v + i\sin v)
\end{align*}$$

Hence we can separate into real and imaginary parts:
$$\begin{align*}
&& x &= e^{u} \cos v & y &= e^{u} \sin v\\
x^{2} + y^{2} &= x^{2} + y^{2}\\
&=(e^{u} \cos v)^{2} + (e^{u} \sin v)^{2}\\
&= e^{2u} ( \cos^{2} v + \sin^{2} v  )\\
&= e^{2u}\\
\frac{1}{2} \ln ( x^{2} + y^{2} ) &= u\\
\ln|z| &=
\end{align*}$$

Now we have a way to find $u$ we also want to find $v$, which can be done:

$$\begin{align*}
&& x &= e^{u} \cos v & y &= e^{u} \sin v\\
\frac{y}{x} &= \frac{e^{u} \sin v}{e^{u} \cos v}\\
&= \tan v
\end{align*}$$

Hence $v$ can be found using: $\arctan \frac{y}{x}$ note that since you are using $\arctan$ information is lost about the signs of the real and imaginary componets to ensure this data isn't lost we use the [[arg (complex numbers)|arg function]]. This gives the final equation:
$$ \ln z = \ln|z| + i \arg z $$
This is sometimes called the principle value, also note [[arg (complex numbers)|arg function]].