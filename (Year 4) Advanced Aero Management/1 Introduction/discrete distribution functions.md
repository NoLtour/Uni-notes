---
aliases:
  - binomial distribution
  - Poisson distribution
  - hypergeometric distribution
tags:
---

## Discrete distribution functions

We have covered [[continuous distribution functions]], but there are frequently cases in the real world where a discrete outcome is observed. 

### Binomial distribution

The binomial distribution with parameters $n$ and $x$ is the discrete probability distribution of the number of successes in a sequence of $n$ independent experiments

> ### $$\begin{align*} f(x)  &= \begin{pmatrix}n\\ x\end{pmatrix} p^{x} q(n-x)  =\frac{n!}{x!(n-x)!} p^{x} q(n-x)  \end{align*}$$
>> where:
>> $f(x)=$ probability function of the binomial distribution
>> $\begin{pmatrix}n\\ x\end{pmatrix}=$ [[binomial coefficient]]
>> $n=$ the number of independent experiments
>> $x=$ the number of successes


It follows a discretised [[continuous distribution functions|gaussian distribution]] in its shape.

### Poisson distribution

Here the event is occurring at a constant rate.

> ### $$\begin{align*} f(t)  &= \frac{(\lambda t)^{k}}{k!} e^{-kt} &&& (k=0,1,2,3,4,5 ...) \end{align*}$$
>> where:
>> $f(t)=$ probability density function for the poisson distribution

### Hypergeometric distribution

This models the probability in the event that there is no replacement after something is removed. Consider a box of $N$ things, $M$ of which are defective and we draw out $n$ of them at random without replacement. The probability of having $x$ defective items is:

> ### $$\begin{align*} f(x)  &=  \frac{\begin{pmatrix}M\\ x\end{pmatrix}\begin{pmatrix}N-M\\ n-x\end{pmatrix}}{\begin{pmatrix}N\\ n\end{pmatrix}} \end{align*}$$
>> where:
>> $f(t)=$ probability density function for the hypergeometric distribution
