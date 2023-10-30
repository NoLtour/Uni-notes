---
aliases: ["method of residues"]
tags: []
---

## Partial fractions fast method

### Method

Not going to show the complete [[partial fractions fast method|method of residues]], just the parts needed for this course. It's just a method for dealing with partial fractions quickly and can be summarised with:

> Input unsolved fractions:
> ### $$\begin{align*} C(s) = \frac{A}{(s-p_{1})(s-p_{2})...(s-p_{n})} &= \frac{K_{1}}{s-p_{1}} + \frac{K_{2}}{s-p_{2}} + ... + \frac{K_{n}}{s-p_{n}}  \end{align*}$$ 
> Solution method:
> ### $$\begin{align*} K_{i} &= \lim_{s\to p_{i}} (s-p_{i}) C(s)\\&\downarrow \\ K_{1} &= \lim_{s\to p_{1}} (s-p_{1}) \frac{A}{(s-p_{1})(s-p_{2})...(s-p_{n})}\\ K_{2} &= \lim_{s\to p_{2}} (s-p_{2}) \frac{A}{(s-p_{1})(s-p_{2})...(s-p_{n})}\\ &... \\ K_{n} &= \lim_{s\to p_{n}} (s-p_{n}) \frac{A}{(s-p_{1})(s-p_{2})...(s-p_{n})} \end{align*}$$ 
>> where:
>> $p_{i}=$ a [[system transfer function feature definitions|pole]] 
>> $A=$ some constant (gain factor)
>> $C(s)=$ response function in the Laplace domain
>> $K_{i}=$ partial fraction constants

It's a numerical solving method which can be done on a calculator!

### Example

Don't have time, just using slides:

![[Pasted image 20231030143744.png]]
![[Pasted image 20231030143831.png]]