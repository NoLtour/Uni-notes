---
aliases: ["integration substitution method","integration by substitution"]
tags: ["Question","QFormat3"]
---

#### What is
## Integration using the general composite rule

> ### $$ \int f^{'}(g(x))\times g^{'}(x)\cdot dx = f(g(x))+k $$ 
>> where:
>> $f(x),g(x)=$ a function 
>> $k=$ a constant

The hard part of using this is getting/seeing that the equation is in that format.

Alternatively you can replace g(x) with t (or some other letter) and use:

> ### $$ \int f^{'}(g(x))\times g^{'}(x)\cdot dx = \int f^{'}(t) \frac{dt}{dx} dx = \int f^{'}(t) dt = f(t) + k $$ 
>> where:
>> $f(t)=$ a function 
>> $k=$ a constant

^11dcf7

(This second one is the way you really use it tbh)

##### Important note! Remember to adjust limits appropirately when using this method!!

### Examples
#### Example 1
> Find the [[Indefinate integral]] of $\int 2x\sqrt{x^{2}+2}\cdot dx$

$$\begin{align*}
&\int 2x\sqrt{x^{2}+2}\cdot dx \\
&& t &= x^{2}+2\\
&& \frac{dt}{dx} &= 2x\\
&\int \frac{dt}{dx} \sqrt{t}\cdot dx\\
&\int \sqrt{t} \cdot dt\\
& \frac{2}{3} t^{\frac{3}{2}} + k\\
& \frac{2}{3} (x^{2}+2)^{\frac{3}{2}} + k
\end{align*}$$

#### Example 2
> Find the [[Indefinate integral]] of $\int \frac{x+1}{x^{2}+2x +2}\cdot dx$
$$\begin{align*}
&\int \frac{x+1}{x^{2}+2x +2}\cdot dx \\
&& t &= x^{2}+2x +2\\
&& \frac{dt}{dx} &= 2x+2\\
&\int \frac{\frac{1}{2} \frac{dt}{dx}}{t}\cdot dx\\
&\frac{1}{2}\int \frac{1}{t} \frac{dt}{dx}\cdot dx\\
& \frac{1}{2} \ln(t) + k\\
& \frac{1}{2} \ln(x^{2}+2x +2) + k\\
\end{align*}$$

#### Example 3
> Find $\int^{2}_{-2} \frac{\sqrt{x+2}}{x+6}\cdot dx$

$$\begin{align*}
\int^{2}_{-2} \frac{\sqrt{x+2}}{x+6}\cdot dx & &  u &= \sqrt{x+2}\\
& & u^{2}-2 &= x\\
& & 2u &= \frac{dx}{du}\\
&= \int^{2}_{0} \frac{u}{u^{2}+4}\cdot 2u \frac{du}{dx} dx\\
&= \int^{2}_{0} \frac{2u^{2}}{u^{2}+4}\cdot du\\
&& \frac{2u^{2}}{u^{2}+4} &= A + \frac{B}{u^{2}+4}\\
&& 2u^{2} &= A(u^{2} +4) + B\\
&& 2&=A & 0&= 4A + B\\
&& & & B&=-8\\
&= \int^{2}_{0} 2 - \frac{8}{u^{2}+4} \cdot du\\
&= \left[ 2u - 4\tan^{-1} \frac{u}{2} \right]^{2}_0 = 4-\pi
\end{align*}$$

