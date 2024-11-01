---
aliases:
  - reliability models for load sharing
  - load dependent reliability models
  - load dependent reliability model
  - the Daniels Model
  - Daniels Model
tags:
---

## Load-sharing systems

### Equation

> ### $$\begin{align*} G_{n}(L)  &=  \sum\limits^{n}_{r=1} \begin{pmatrix} n\\r \end{pmatrix}\: (-1)^{r+1} \:F^{r}(L)\:G_{n-r}\left(\frac{nL}{n-r}\right) \end{align*}$$
>> where [[recursion]] is used:
>> $G_{n}(L)=$ [[load-sharing systems|Daniels Model]] for a system under load $L$ shared between $n$ identical components in [[complex reliability model|parallel]], the resulting overall [[cumulative distribution function|CDF]].
>> $n=$  the total number of components in [[complex reliability model|parallel]]
>> $r=$ the number of components that have failed
>> $F(L)=$ the [[cumulative distribution function]] for a component under load $L$
>> $\begin{pmatrix} n\\r \end{pmatrix}=$ [[binomial coefficient]]

Something to note about this formula is that it can be very hard to compute for large values of $n$ (above like 30), due to [[numerical instability]]. In such cases other approximations may be better suited than the [[load-sharing systems|Daniels Model]]. 

### Explanation

Let's try and model the chance of a system of power plants failing, starting with their probability function $F(L)$ which is the [[cumulative distribution function|CDF]] with reference to $L$ (load). 

We have a target load $L$ which must be met, calculating the failure chance when the system is 1 power plant's simple enough:

$$\begin{align*}
G_{1}(L) &= F(L)
\end{align*}$$

Congrats lol.

Now let's consider 2 or 3 power plants, once one fails the other(s) now have increased loading and there are many combinations for failure. For the 2 plant case it's not soo bad, we fail when all plants have broken which occurs if:
- Plant 1 fails, then 2 fails
- Plant 2 fails, then 1 fails

Hence its a simple [[basic rules of probability#General rules|or statement]]
$$\begin{align*}
&& F=F_{1} &= F_{2}\\
G_{2}(L) &= F_{1}(L) F_{2}\left(\frac{L}{2}\right) + F_{1}\left(\frac{L}{2}\right) F_{2}(L)  - F_{1}(L)F_{2}(L) &&\to&
G_{2}(L) &= 2F(L) F\left(\frac{L}{2}\right) - F^{2}(L)

\end{align*}$$


Ok so what about 3 plants? Now to fail we have:
- Plant 1 fails, then 2, then 3
- Plant 1 fails, then 3, then 2
- Plant 2 fails, then 1, then 3
- Plant 2 fails, then 3, then 2
- Plant 3 fails, then 1, then 2
- Plant 3 fails, then 2, then 1

Accounting for this takes a while, but you'll eventually end up with:

$$\begin{align*}
G_{3}(L) &= 6\:F(L)\: F\left(\frac{4L}{2}\right) \:F(3L) -\: 3\:F(L) \:F^{2}\left(\frac{3L}{2}\right) - \:3\:F^{2}(L)\: F(3L) + \:F^{3}(L)
\end{align*}$$

Deriving this is aids, now consider deriving with 4+.... if your hoping there's a general formula then congrats on noticing the first section of this page lol.
