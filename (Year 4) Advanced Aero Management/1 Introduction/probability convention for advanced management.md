---
aliases:
  - simple equal probability
  - simple equal probability testing
  - conditional probability
  - probability logic convention
tags:
---

## Probability convention for advanced management

There are basics of probability that should already be known from secondary school, so we go over them and show the format used in this module.

#### Equal probability

> ### $$\begin{align*} P(A)  &= \frac{n}{N}  \end{align*}$$
>> where:
>> $P(A)=$ The true chance that outcome $A$ will occur, given that there are $N$ equally possible outcomes with $n$ of them leading to $A$
>> $N=$ The number of equally possible outcomes
>> $n=$ The number of outcomes that lead to $A$ occurring

##### Equal probability testing

If we roll a dice 6 time's, it's quite unlikely each possible outcome will occur once. Say we want to find the chance that a rolled dice will produce a 1, then using the equation:

$$\begin{align*}
P(V=1) &= \frac{n_{v=1}}{N_{Tests}} &&\to& P(V=1) &= \frac{n_{v=1}}{6}
\end{align*}$$

May give us the correct value (1/6) but the correctness is left to chance, so to compensate say we try 600 tests:

$$\begin{align*}
P(V=1) &= \frac{n_{v=1}}{600}
\end{align*}$$

This will almost certainly produce a value of $P(V=1)$ very close to 1/6, as you'd expect more tests leads to more certainty in your probability values. So as number of tests approaches infinity, the true probability is found.

> ### $$\begin{align*} P(A) &= \frac{n}{N} = \lim_{N\to \infty} \left( \frac{n_{A}}{N_{Tests}} \right) \end{align*}$$
>> where:
>> $P(A)=$ The true chance that outcome $A$ will occur, given that there are $N$ equally possible outcomes with $n$ of them leading to $A$
>> $N=$ The number of equally possible outcomes
>> $n=$ The number of outcomes that lead to $A$ occurring
>> $N_{Tests}=$ The number of tests performed
>> $n_{A}=$ The number of those tests where $A$ occurred


#### Logic convention

> #### $P(A)=$ The probability of outcome $A$ occurring.
> #### $P(AB)=$ The probability of $A$ and $B$ occurring.
> #### $P(A+B)=$ The probability of $A$ or $B$ occurring.
> #### $P(A|B)=$ The probability of $A$ occurring, given that $B$ has occurred. (conditional probability)
> #### $P(\bar{A})=$ The probability that $A$ hasn't occurred.



