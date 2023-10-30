---
aliases: [""]
tags: []
---

## Properties of linear Laplace transforms

### Linearity consequence

Due to linearity a bunch of useful properties hold even after we've transformed the original functions as a consequence of [[linear systems|linearity]]:

> ### $$\begin{align*} f_{1}(t) + f_{2}(t)  &&\to &  &F_{1}(s)+F_{2}(s) \\ f_{1}(t) - f_{2}(t)  &&\to &  &F_{1}(s)-F_{2}(s) \\ af_{1}(t)  &&\to &  &aF_{1}(s) \\ a[f_{1}(t) - bf_{2}](t)  &&\to &  &a[F_{1}(s)-bF_{2}(s)] \end{align*}$$
>> where:
>> $f_{1},\:f_{2}=$ linear time domain functions
>> $F_{1},\:F_{2}=$ linear Laplace domain functions
>> $a,b=$ constants

### Time shifts

Something that needs to be kept in mind is that most changes don't transfer so cleanly, take a time shift:

> ![[Pasted image 20231029131725.png]]
> ### $$\begin{align*} f(t)  &\to F(s) \\ f(t-t_{d}) &\to e^{-t_{d} s} F(s)   \end{align*}$$
>> where:
>> $f  =$ time domain functions
>> $F =$ Laplace domain functions
>> $t_{d}=$ time delay constant

There is fucky stuff that occurs in the [[Laplace transform]].

### Other changes

There are lot's of other ones (recall [[Laplace Transform overview]] from year 2). For the exam learn to make use of the standard results table:

![[Laplace transform table]]
