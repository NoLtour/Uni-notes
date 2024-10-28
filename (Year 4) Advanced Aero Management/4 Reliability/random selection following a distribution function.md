---
aliases: [""]
tags: []
---

## Random selection following a distribution function

### Method

We have these [[continuous distribution functions|distribution functions]], but what if we want to get a random sample that has the same distribution as the function in question? 

When working with random numbers, we generally use random number generations. These usually give a value between zero and one, with a equal probability of being anywhere between em, effectively just a [[continuous distribution functions|uniform distribution function]]. For instance, plotting a couple thousand samples from one we get:

![[Pasted image 20241023160701.png]]

Getting it to follow our target distributions actually quite simple, we just feed the output of our random function into a inverse [[cumulative distribution function|CDF]]:

![[Pasted image 20241023160828.png]]

> ### $$\begin{align*} F^{-1}(\text{Random}(i)) &= t_{i} \end{align*}$$
>> where:
>> $F(t)=$ the [[cumulative distribution function]] in terms of $t$
>> $\text{Random}(i)=$ a random number generator, this one takes an index
>> $t_{i}=$ the $i_{th}$ value of $t$ (outputs following the [[cumulative distribution function|CDF]])

### Example

Ok so let's invert the [[continuous distribution functions|exponential distribution]]:

$$\begin{align*}
F(t)  &=  e^{-\lambda t} &&\to& - \frac{\ln(F(t))}{\lambda} &= t 
\end{align*}$$

Then just feed in value's of $F$, taking that [[continuous distribution functions|uniform distribution function]]:

![[Pasted image 20241023161626.png]]
