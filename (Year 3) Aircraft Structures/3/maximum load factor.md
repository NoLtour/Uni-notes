---
aliases: [""]
tags: []
---

## Maximum load factor

### Useful bit

> ![[Pasted image 20240301174321.png]]
> ### $$\begin{align*} n_{max} &= \frac{\frac{1}{2} \rho S C_{L,max} V^{2}}{W}   \end{align*}$$
> ### $$\begin{align*} C_{L,max} &= C^{wing}_{L,max}\left(1+\frac{a}{l}\right) + C_{m0}\frac{\bar{c}}{l}   \end{align*}$$
>> where:
>> $n_{max}=$ The maximum [[load factor]]
>> $C_{L,max}=$ [[stalling speed|max lift coefficient]]
>> $C_{L,max}^{wing}=$ [[stalling speed|max lift coefficient]] experienced by the main wing
>> $V=$ [[true airspeed]]
>> $C_{m0}=$ [[pitching moment coefficient]]
>> $a=$ distance from centre of mass to [[aerodynamic centre]]
>> $l=$ distance from centre of mass to tail [[aerodynamic centre]]
>> $\bar{c}=$ [[Mean chord|mean aerodynamic chord]]

### Derivation

![[Pasted image 20240301174321.png]]

Consider a simple aircraft in steady level flight, we can easily relate [[load factor]] to the various [[lift equation|lift]] values and net acceleration:

$$\begin{align*}
&&N_{z} = L + P &= \sum\limits F\\
&&  &= W +M a_{z}\\
n &= \frac{N_{z}}{W} &&\to& nW &= L + P=W+Ma_{z}
\end{align*}$$

Obviously a higher net lift increases load factor, and the resultant force ($L+P>W$) means we experience higher upward acceleration ([[aka primary school physics|duh]]). 

Taking the equilibrium for moments, we can easily express the net lift:

$$\begin{align*} 
M_{0} + La &= lP &&\to& P&= \frac{M_{0}}{l} + L \frac{a}{l} \\
&& L+P &=L+P &&\to&  L+P=& L + \frac{M_{0}}{l} + L \frac{a}{l} &&\to& L+P &= L\left(1+\frac{a}{l}\right) + \frac{M_{0}}{l}  
\end{align*}$$

This equation can then be rewritten interms of non-dimensionalised coefficients:

$$\begin{align*}
L+P=L_{net} &= L\left(1+\frac{a}{l}\right) + \frac{M_{0}}{l}   &&\to&  C_{L,max} &= C^{wing}_{L,max}\left(1+\frac{a}{l}\right) + C_{m0}\frac{\bar{c}}{l}  
\end{align*}$$

Noting the use of $C_{L,max}=C_{L,max}^{wing}+C_{L,max}^{tail}$ and [[Mean chord|mean aerodynamic chord]]. We can then relate it back to $n$ easily, peak [[load factor]] will occur at maximum lift aka the limit of stall:

$$\begin{align*}
n_{max} &= \frac{L_{max}}{W}  &&\to&  n_{max} &= \frac{\frac{1}{2} \rho S C_{L,max} V^{2}}{W} 
\end{align*}$$




RETURN TO N_MAX