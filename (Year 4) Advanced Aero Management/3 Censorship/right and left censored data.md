---
aliases:
  - right censored data
  - left censored data
tags:
---

## Right and left censored data

Ok so what if instead of [[interval censored data]], we have all data beyond a certain limit have exact measurements not available? This is right and left censored data.

This is what left censored data looks like:

![[Pasted image 20241018170033.png]]

I'll leave it up to your imagination whata leftt censored data looks like.

### [[maximum likelihood estimation|MLE]] with left/right censored data

Ok so this is why I did [[interval censored data|MLE with interval censored data]] first, in reality right/left censored data is just interval censored data where the interval goes to infinity. So well... just do that:

$$\begin{align*} 
\text{Left:}&&
l(\theta)  &= \left[\sum\limits^{n}_{i=1} \log f(t_{i} ; \theta) \right] + \left[\sum\limits^{n}_{i=1} \log F(T_{L};\theta) - F(\infty;\theta) \right] &&\to& 

l(\theta)  &= \left[\sum\limits^{n}_{i=1} \log f(t_{i} ; \theta) \right] + \left[\sum\limits^{n}_{i=1} \log F(T_{L};\theta) \right]\\\\
\text{Right:}&&
l(\theta)  &= \left[\sum\limits^{n}_{i=1} \log f(t_{i} ; \theta) \right] + \left[\sum\limits^{n}_{i=1} \log F(\infty;\theta) - F(T_{R};\theta) \right] &&\to& 

l(\theta)  &= \left[\sum\limits^{n}_{i=1} \log f(t_{i} ; \theta) \right] + \left[\sum\limits^{n}_{i=1} \log R(T_{R};\theta) \right]

\end{align*}$$

Yeah, it's quite easy.


