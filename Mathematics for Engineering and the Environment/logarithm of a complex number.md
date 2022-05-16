---
aliases: ["principal value"]
tags: ["Question","QFormat3"]
---

#### How do you find the
## Logarithm of a complex number

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

Hence $v$ can be found using: $\arctan \frac{y}{x}$ note that since you are using $\arctan$ acceptable answers can have $\pm n\pi$. This gives the final equation:
$$ \ln z = \ln|z| + j \arg z $$
This is sometimes called the principle value, also note [[arg (complex numbers)|arg function]].