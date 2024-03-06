---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Load factor ($n,n_{z}$)

### Simple description

The load factor is the ratio of the lift of an aircraft to its weight and represents a global measure of the stress ("load") to which the structure of the aircraft is subjected.

> ### $$\begin{align*} n &=  \frac{L_{total}}{W} &&& n&= \frac{L+P}{W}  \end{align*}$$ 
> ### $$ \sqrt n = \frac{V_{Sr}}{V_S} $$ 
>> where:
>> $n=$ [[load factor]]
>> $L_{total}=$ Total lift
>> $L=$ main wing lift
>> $P=$ tail plane lift
>> $W=$ Weight
>> $V_{Sr}=$ [[stalling speed]] during a [[co-ordinated turn]]
>> $V_S=$ [[stalling speed]] during steady level flight

In a [[co-ordinated turn]] the resaulting vector of the weight and centrafugal forces act "down" relative to the passengers. 
Basically when someone says "I'm experiencing 69g's" then $n=69$, and I'm not sure how they survived pulling 69 fucking g's, like fuck they must be a pancake, and a somehow sentient pancake at that? 

### More accurate

![[Pasted image 20240301173905.png]]

It is the net vertical force (ignoring weight) divided by weight, which can be usually simplified to net lift divided by weight.

> ### $$\begin{align*} n_{z} &= \frac{N_{z}}{W} &&& n_{z} &= \frac{(\sum\limits F_{z})+ W}{W} = \frac{\sum\limits F_{z}}{W} +1  &&& n_{z} &= \frac{Mg + Ma_{z}}{W}= \frac{ Ma_{z}}{W} + 1 \end{align*}$$
>> where:
>> $n_{z}=$ [[load factor]] in z direction
>> $N_{z}=$ net force in z direction (ignoring weight)
>> $W=$ weight
>> $a_z=$ acceleration

### Circular motion

Load factor is often considered in the context of pitching manoeuvres, taking some constant pitch rate - constant speed manoeuvre, it's obvious the aircraft travels in a circular arc:
![[Pasted image 20240302145917.png]]

So load factor will be:

$$\begin{align*}
&&\frac{L}{W}&= n\\ 
L - W\cos\alpha &= M \frac{V^{2}}{R} &&\to&  nW - W\cos\alpha &= M \frac{V^{2}}{R}  &&\to&  n   &=   \frac{V^{2}}{Rg} + \cos\alpha
\end{align*}$$

This can be further expanded by defining manoeuvre radius interms of pitching rate:

$$\begin{align*}
\frac{dx}{dt} &= R \frac{d\alpha}{dt} &&\to& \frac{V}{\dot\alpha} &= R   \\
&& n   &=   \frac{V^{2}}{Rg} + \cos\alpha &&\to& n   &=   \frac{V \dot\alpha}{g} + \cos\alpha
\end{align*}$$

> ### $$\begin{align*} && \frac{V}{\dot\alpha} &= R \\ n   &=   \frac{V^{2}}{Rg} + \cos\alpha &&\to& n &=   \frac{V \dot\alpha}{g} + \cos\alpha \end{align*}$$
>> where:
>> $n=$ [[load factor]]
>> $R=$ radius of pitching manoeuvre
>> $V=$ [[true airspeed]]
>> $\alpha=$ [[angle of attack]]
>> $\dot\alpha=$ pitching rate (radians)

What this shows is that load factor is:
- At a maximum when $\alpha=0\degree$ (at bottom of loop)
- At a minimum when $\alpha=180\degree$ (at top of loop) 

