---
aliases:
  - robust regularisation
  - expectancy measures
tags:
---

## Optimisation under uncertainty

If we consider both [[aleatory and epistemic uncertainty]] it's clear that margins are needed, highly optimised models are often extremely fragile if they even work at all (the optimiser may achieve a false optimum by exploiting your model, yielding no useful result). 

This is where we account for uncertainty in the optimisation process of whatever performance metrics we look at, and depending on how it's incorporated certainty in performance can be a performance metric itself.

### Robust regularisation
This works for attempting to compensate for [[aleatory and epistemic uncertainty|epistemic uncertainty]] or [[aleatory and epistemic uncertainty|aleatory uncertainty]], effectively we slap an expected error on it. This is a way of searching $f(x)$ for a "worst case" within a $\pm \varepsilon$ of target $x$. 

> ### $$\begin{align*} f_{r}(x)  &= \min_{x}(\max[f(x\pm\varepsilon)])  \end{align*}$$
>> where:
>> $f_{r}(x)=$ the definition for [[optimisation under uncertainty|robust regularisation]] when minimising $f(x)$ is desirable
>> $\underset{x}{\min}(...)=$ is a minimisation function, that finds the $x$ that yields the lowest value of some function
>> $\max(...)=$ a function which returns the highest value out of some set
>> $f(x\pm\varepsilon)=$ the performance metric being minimised, returning all values as a set in the range of $x\pm\varepsilon$

If we apply this to some function, it'll look something like:
![[Pasted image 20241107172703.png|500]]

This method is quite easy to implement, but it often suffers from being too conservative especially if the selected range is large. 

### Expectancy Measures
Given the issues with robust regularisation it might be better to consider robustness based on a probability. In such a case the inputs become random and based on a PDF which reflects prior knowledge, hence this strategy is more suited for [[aleatory and epistemic uncertainty|aleatory uncertainty]].

#### Aggregation

##### Robust solutions

This is basically [[convolution]] between our [[probability density function|PDF]] describing the variation of some input parameter ($x$) and the performance function ($f(x)$):

> ### $$\begin{align*} F(x)  &=  \int f(x+\varepsilon) P(\varepsilon) \: d\varepsilon \end{align*}$$
>> where:
>> $F(x)=$ the "effective fitness", how fit it is considering the inputs actually vary about the [[probability density function|PDF]]
>> $P(x)=$ the [[probability density function|PDF]] defining the variation of $x$ ([[convolution|kernel]])
>> $f(x)=$ our fitness function

Plotted it would look something like:
![[Pasted image 20241107184107.png|500]]

##### Consistent solutions

Alternatively we may actually want to measure overall consistency rather than performance, then something like the following would work:

> ### $$\begin{align*} F(x)  &=  \int [f(x+\varepsilon)-f(x)]^{2} P(\varepsilon) \: d\varepsilon \end{align*}$$
>> where:
>> $F(x)=$ the deviation experienced by $f(x)$ given some pdf
>> $P(x)=$ the [[probability density function|PDF]] defining the variation of $x$
>> $f(x)=$ our fitness function

Plotted it would look something like:
![[Pasted image 20241107184212.png|700]]

Here the metric is only consistency, which is reflected in the "fitness".

##### Reconciling both

If we plot both consistency and a robust optimum on the same plot, we can see that the optima are clearly different.

![[Pasted image 20241107184414.png|500]]

We might use something like a [[Pareto front]] to find the desired trade off between these, but regardless we will have to make a trade off.

![[Pasted image 20241107185902.png|700]]
![[Pasted image 20241107185931.png|800]]

#### Randomised Sampling

The methods outlined in [[optimisation under uncertainty#Aggregation]] may not be possible to implement analytically, so we can use [[Monte Carlo simulation]] to implement them. 


