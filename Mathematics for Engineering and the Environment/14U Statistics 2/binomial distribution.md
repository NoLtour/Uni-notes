---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Binomial distribution
### Intro
This is a discrete version of the [[normal distribution]]. Note that [[bernoulli trial]] is applicable here as well.
![[Pasted image 20220313113209.png]]

### Probability of specific number of successes

The probability of a number of successes $k$ being equal to the actual number of successful trials for a given number of trials $n$ is given by:

> ### $$ P(N_{S}=k) = \begin{pmatrix}n  \\  k\end{pmatrix} p^{k} (1-p)^{n-k} $$ 
>> where:
>> $n=$ number of trials
>> $p=$ probability of a trials success
>> $N_{S}=$ number of successful trials for $n$ trials
>> $P(N_{S}=k)=$ probability that the number of successful trials is equal to $k$
>> $\begin{pmatrix}n  \\  k\end{pmatrix}= \frac{n!}{(n-k)k!}$

### Probability of successes in range

> ### $$ P( k_{max} \geq N_{S} \geq k_{min} ) = \sum\limits^{k_{max}}_{ k=k_{min} } \begin{pmatrix}n  \\  k\end{pmatrix} p^{k} (1-p)^{n-k} $$ 
>> where:
>> $n=$ number of trials
>> $p=$ probability of a trials success
>> $N_{S}=$ number of successful trials for $n$ trials
>> $P( k_{max} \geq N_{S} \geq k_{min} )=$ probability that the number of successful trials is equal to or between $k_{max}$ and $k_{min}$ for $n$ number of trials
>> $\begin{pmatrix}n  \\  k\end{pmatrix}= \frac{n!}{(n-k)k!}$
