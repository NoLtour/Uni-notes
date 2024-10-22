---
aliases:
  - censored MLE
tags:
---

## Censored [[maximum likelihood estimation|MLE]]

Ok so, what do you do if you have [[interval censored data]], [[right and left censored data|right censored data]] AND [[right and left censored data|left censored data]]??? The answer is trivial, just keep compounding their probabilities.

> ### $$\begin{align*}  l(\theta)  &=\left[\sum\limits^{n}_{i=1} \log f(t_{i} ; \theta) \right] +\left[\sum\limits^{n}_{i=1} \log F(T_{L,i};\theta) \right]+ \left[\sum\limits^{n}_{i=1} \log F(T_{ub,i};\theta) - F(T_{lb,i};\theta) \right] + \left[\sum\limits^{n}_{i=1} \log R(T_{R,i};\theta) \right] \end{align*}$$
>> where:
>> $f(t;\theta)=$ some [[continuous distribution functions|continuous distribution function]] where the form is known but its parameters $\theta$ aren't known
>> $F(t; \theta)=$ the [[cumulative distribution function]] where the form is known but its parameters $\theta$ aren't known
>> $R(t; \theta)=$ the [[reliability function]] where the form is known but its parameters $\theta$ aren't known
>> $t_{i}=$ a sample value
>> $l(\theta)=$ is the log of $L(\theta)$ ([[maximum likelihood estimation|log likelihood estimation function]]) 
>> $\theta=$ the parameters associated with $f(t)$
>> $j=$ the index of the parameter ($\theta_{j}$) being found
>> $T_{L}=$ the bound of a point of left censored data
>> $T_{R}=$ the bound a point of right censored data
>> $T_{lb},T_{ub}=$ the lower and upper bounds of a point of [[interval censored data]]

This is basically just a more general form of the [[maximum likelihood estimation|MLE]] equation, since unused parts just go to zero. It's possible to define theta from just censored data, so long as there are sufficient sets to fully define the [[continuous distribution functions|continuous distribution function]]. 

Often when censored data starts existing, you'll loose the ability to analytically solve for parameters, hence having to take a numerical optimisation approach.
