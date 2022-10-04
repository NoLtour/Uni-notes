---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Binomial distribution
### Intro
This is a discrete version of the [[normal distribution]]. Note that [[bernoulli trial]] is applicable here as well.
![[Pasted image 20220313113209.png]]

Something to note is that as number of trials approaches infinity the [[normal distribution]] becomes a more and more accurate approximation of the [[binomial distribution]]. Hence why for large populations we use a [[normal distribution]].

### Probability of specific number of successes

The probability of the actual number of successful trials for a given number of trials $n$ being equal to a value $k$ is given by:

> ### $$ P(N_{S}=k) = \begin{pmatrix}n  \\  k\end{pmatrix} p^{k} (1-p)^{n-k} $$ 
>> where:
>> $n=$ number of trials
>> $p=$ probability of a trials success
>> $N_{S}=$ number of successful trials for $n$ trials
>> $P(N_{S}=k)=$ probability that the number of successful trials is equal to $k$
>> $\begin{pmatrix}n  \\  k\end{pmatrix}= \frac{n!}{(n-k)k!}$

### Probability of successes in range

The probability of the actual number of successful trials for a given number of trials $n$ being in a range is:

> ### $$ P( k_{max} \geq N_{S} \geq k_{min} ) = \sum\limits^{k_{max}}_{ k=k_{min} } \begin{pmatrix}n  \\  k\end{pmatrix} p^{k} (1-p)^{n-k} $$ 
> ### $$ P( k_{max} \geq N_{S} ) = \sum\limits^{k_{max}}_{ k=-\infty } \begin{pmatrix}n  \\  k\end{pmatrix} p^{k} (1-p)^{n-k} $$ 
> ### $$ P( N_{S} \geq k_{min} ) = \sum\limits^{\infty}_{ k=k_{min} } \begin{pmatrix}n  \\  k\end{pmatrix} p^{k} (1-p)^{n-k} $$ 
> ### $$ P( k_{max} \geq N_{S} ) = P( k_{max}+1 > N_{S} ) $$
> ### $$ P( N_{S} \geq k_{min} ) = P( N_{S} > k_{min}-1 ) $$
> ### $$ P( \infty \geq N_{S} \geq -\infty ) = 1 $$
>> where: 
>> $n=$ number of trials
>> $p=$ probability of a trials success
>> $N_{S}=$ number of successful trials for $n$ trials
>> $P( k_{max} \geq N_{S} \geq k_{min} )=$ probability that the number of successful trials is equal to or between $k_{max}$ and $k_{min}$ for $n$ number of trials
>> $\begin{pmatrix}n  \\  k\end{pmatrix}= \frac{n!}{(n-k)k!}$

You probably wont be asked to manuall sum these, most calculators will have binomial distorbution specific functions so learn how to use those, else find something online that does it.