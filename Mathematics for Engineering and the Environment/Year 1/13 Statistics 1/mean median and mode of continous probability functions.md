---
aliases: ["median of a continous probability function","mode of a continous probability function","mean of a continous probability function"]
tags: ["Question","QFormat3"]
---

#### What is the equation for the
## Mean median and mode of continous probability functions

### Mean

This is easy enough:

> ### $$ \bar{x} = \mu = \int^{\infty}_{-\infty} x \times f_{X}(x) \cdot dx $$ 
>> where:
>> $\mu=\bar{x}=$ mean value of $x$
>> $f_{X}(x)=$ a [[probablility function]] for $x$

### Mode

Super easy:

> ### $$ f_{X}(x_{mode}) = P_{max} $$
>> where:
>> $f_{X}(x)=$ [[probablility function]] of $x$
>> $x_{mode}=$ mode value
>> $P_{max}=$ highest probability (usually on a turning point)

If the highest probability is located at a turning point you can just [[differentiation|differentiate]] $f_{X}$ to find the maximums and choose the highest.

### Median

This is less intuitive but also not that bad, the median is just the value of $x$ where 50% of outcomes lie on either side of $x_{median}$:

> ### $$ \int^{\infty}_{x_{median}} f_{X}(x) dx = \int^{x_{median}}_{-\infty} f_{X}(x) dx $$ 
>> where:
>> $f_{X}(x)=$ [[probablility function]] of $x$
>> $x_{median}=$ meadian value