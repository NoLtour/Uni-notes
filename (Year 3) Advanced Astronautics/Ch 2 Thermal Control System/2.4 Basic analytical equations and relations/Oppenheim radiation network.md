---
aliases: [""]
tags: []
---

## Oppenheim radiation network

It's best explained through an example so here you go.

### Example

Two flat disks of identical dimensions exist in a otherwise empty vacuum. 

![[Pasted image 20231120221418.png]]

- [[view factor]] is $F_{A\to B}=0.7176$
- temp $T_{A}=150C$
- [[useful spacecraft surface characteristics|IR emissivity]] $\varepsilon_{IR}=0.4$ (for both)

Questions:
1) What is the view factor of A to space
2) What is the Oppenheim network
3) Estimate the energy input needed for A to maintain it's temp
4) Calculate B's temp

#### 1 Calculate view factor

This is quite simple, in this scenario there only exists these two disk's and the infinite expanse of space. By definition sum of view factor's for a object equal 1:

$$\begin{align*}
\sum\limits F_{A\to ?} &= 1 & &\to & F_{A\to B} + F_{A\to S} &= 1 & &\to &  F_{A\to S} &= 1 - F_{A\to B}= 0.2824
\end{align*}$$

#### 2 Oppenheim network

![[Pasted image 20231120225145.png]]

#### 3 Energy needed for A to maintain temp

The "resistance"

$$\begin{align*}
R_{1} &= \frac{\varepsilon_{IR}}{1-\varepsilon_{IR}} A_{A} & R_{2} &= \frac{\varepsilon_{S}}{1-\varepsilon_{S}} A_{S} & R_{3} &= \frac{\varepsilon_{IR}}{1-\varepsilon_{IR}} A_{B}\\
&= 0.754 &&=(not\:used)& &= 0.754
\end{align*}$$

others:

$$\begin{align*}
R_{4} &= A_{A} F_{A\to S} & R_{5} &= A_{B} F_{B\to S} & R_{6} &= A_{A} F_{A\to B}\\
&= 0.319 & &= 0.319 & &= 0.812
\end{align*}$$

Then we can create set's of simultaneous equations for nodes:
$$\begin{align*} 
&\begin{aligned} 
\sum\limits \dot{Q}_{in} - \sum\limits \dot{Q}_{out}&= 0\\\\
\dot{Q}_{A} + R_{1} J_{A} - R_{1} T_{A}^{4} \sigma &= 0 \\
T_{A}^{4} \sigma R_{1} + R_{6} J_{B} + R_{4} J_{S} - J_{A}(R_{1} + R_{6} + R_{4}) &= 0 \\
T_{B}^{4} \sigma R_{3} + R_{6} J_{A} + R_{5} J_{S} - J_{B}(R_{6} + R_{5} + R_{3}) &= 0 \\
J_{B} R_{3} - T_{B}^{4} \sigma R_{3} &= 0 \\
\end{aligned}&\to&& 
\begin{array}{ccc} \\\\\\
&\dot{Q}_{A} &+ J_{A} R_{1}&&& &= T_{A}^{4} \sigma R_{1} \\
 &&- J_{A}(R_{1} + R_{6} + R_{4}) &&+ J_{B} R_{6} &&= -T_{A}^{4} \sigma R_{1} \\
&& J_{A} R_{6} &+T_{B}^{4} \sigma R_{3}  &- J_{B}(R_{6} &+ R_{5} + R_{3}) &= 0 \\
&&&- T_{B}^{4} \sigma R_{3} &+J_{B} R_{3} & &= 0
\end{array}
\end{align*}$$

These can then be easily solved using matrices or calculator functions:

$$\begin{align*}
\dot{Q}_{A} &= 576\\
{J}_{A} &= 1050\\
{T}_{B}^{4} &= 1.33\times10^{10} & T_{B}&= 340\\
{J}_{B} &= 753\\
\end{align*}$$
 

 