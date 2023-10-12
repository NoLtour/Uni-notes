---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Normal distribution ( $X \backsim N(\mu_{X},\sigma^{2}_{X})$ )
This is where a [[bernoulli trial]] is applicable, and the following equation can be used to reonably accuratly determine the fraction of the total population that rests within a given range:

> ### $$ P(x_{max}>X>x_{min}) = f_{pop} = \int^{x_{max}}_{x_{min}} \dfrac{e^{-\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^{2} } }{\sigma\sqrt{2\pi}} \cdot dx $$ 
> ### $$ \frac{P(X=x)}{dx} = \dfrac{e^{-\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^{2} } }{\sigma\sqrt{2\pi}} $$
>> where:
>> $P(x_{max}>X>x_{min}) = f_{pop} =$ The fraction of the population that has an $x$ value between $x_{max}$ and $x_{min}$, equivilent to the probability that $X$ lies between $x_{max}$ and $x_{min}$
>> $\mu=$ [[mean value by integration|mean value]]
>> $\sigma=$ [[standard deviation for probabability functions|standard deviation]]
>> $\frac{P(X=x)}{dx}=$ probability density at a value of $x$

You do not need to know how to integrate this function (that's maths degree type stuff) this is just to show you where the values come from. 

(The following is a [[normal distribution]] graph, showing the equation $\frac{e^{-\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^{2} } }{\sigma\sqrt{2\pi}}$)
![[Pasted image 20220313105429.png]]

