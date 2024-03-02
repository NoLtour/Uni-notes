---
aliases: [""]
tags: []
---

## P-n diagram

![[Pasted image 20240302154751.png]]

Starting from equilibrium around the AC, where some load factor is in effect:

$$\begin{align*}
M_{0} + a nW &= (a+l) P &&\to& \frac{M_{0} + a nW}{a+l} &= P
\end{align*}$$

Then using the definition of [[Pitching moment equation]]:

$$\begin{align*}
 && M_{0} &= \frac{1}{2} \rho V^{2} S \bar{c} C_{m0} \\
P &= \frac{M_{0} + a nW}{a+l} &&\to& P &= \frac{\frac{1}{2} \rho V^{2} S \bar{c} C_{m0} + a nW}{a+l} &&\to& P &= n\frac{ a  W}{a+l} + V^{2} \frac{\frac{1}{2} \rho S \bar{c} C_{m0} }{a+l}
\end{align*}$$

If we look at the parts of the equation that are constant, then the tail force can be described as:

$$\begin{align*}
P &= n\frac{ a  W}{a+l} + V^{2} \frac{\frac{1}{2} \rho S \bar{c} C_{m0} }{a+l} &&\to& P&= \beta_{1} n + \beta_{2} V^{2}
\end{align*}$$

> ### $$\begin{align*}  P &= n\frac{ a  W}{a+l} + V^{2} \frac{\frac{1}{2} \rho S \bar{c} C_{m0} }{a+l} &&\to& P&= \beta_{1} n + \beta_{2} V^{2} \end{align*}$$
>> where:
>> $P=$ tail lift
>> $V=$ velocity
>> $l=$ distance between tail and main wing centres of lift
>> $a=$ distance between main wing centre of lift and centre of mass
>> $n=$ [[load factor]]
>> $W=$ aircraft weight
>> $C_{m0}=$ [[pitching moment coefficient]]
>> $\bar{c}=$ [[Mean chord|mean aerodynamic chord]]
>> $\rho=$ atmospheric density

Consider the fact that generally $C_{m0}$ is negative, then we will have a negative $\beta_{2}$. Now compare the relationship between load factor and total lift vs tail lift:

$$\begin{align*}
P&= \beta_{1} n + \beta_{2} V^{2} &&& L &= nW
\end{align*}$$

This allows us to draw a P-n for the tail using the [[V-n diagram]] transformed by the above defined tail lift equation:

![[Pasted image 20240302160148.png]]

We can see the negative curvature on the load factor lines caused by $\beta_{1}$ being negative. Recalling the definition of load factor:

$$\begin{align*}
\frac{L_{Total}}{W} &= n &&\to& L_{main} &= nW - P
\end{align*}$$

We can see that for a pitch up manoeuvre main wing loading will be at a maximum at D, where the [[load factor]] is at a maximum and tail lift is at a minimum.
