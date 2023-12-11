---
aliases: ["thermal resistance","1D parallel heat conduction","1D series heat conduction"]
tags: []
---

## Parallel and series 1D heat conduction

If we have a multi-material medium that heat is conducting through, it is actually possible to treat it in a very similar way to [[resistors in parallel]]/series.

> ![[Pasted image 20231210135735.png]]
> ### $$ \dot{Q} = \frac{1}{R}(T_{A} - T_{B}) $$
> ### $$\begin{align*} R_{i} &= \frac{L_{i}}{k_{i}A_{i}} \end{align*}$$
>> where:
>> $\dot{Q}=$ [[heat transfer rate]] from $A$ to $B$
>> $T_{A},T_{B}=$ temperature of heat reservoirs
>> $R_{i}=$ thermal resistance of material section
>> $L_{i}=$ length of material section
>> $k_{i}=$ [[material thermal conductivity|thermal conductivity]] of material section
>> $A_{i}=$ cross sectional area of material section

Since the heat only conducts in one direction, it's still a 1D heat conduction case.

### Example

![[Pasted image 20231210140211.png]]

First we make the observation that this is a system in series, so we use the series equation:

$$\begin{align*}
R_{A} = R_{C} &= \frac{L_{A}}{Ak_{A}} & R_{B} &= \frac{L_{B}}{Ak_{B}}
\end{align*}$$
$$\begin{align*}
R_{T} &= R_{A} + R_{B} + R_{C} &&\to& R_{T} &= 2\frac{L_{A}}{Ak_{A}}+\frac{L_{B}}{Ak_{B}} \\\\
&& \dot{q} &= \frac{1}{A} \frac{1}{R_{T}}(T_{1} - T_{4}) & &\to & \dot{q} &= \frac{1}{A} \frac{1}{2\frac{L_{A}}{Ak_{A}}+\frac{L_{B}}{Ak_{B}} }(T_{1} - T_{4})& &\to & 
\dot{q} &=  \frac{T_{1} - T_{4}}{2\frac{L_{A}}{k_{A}}+\frac{L_{B}}{k_{B}} }\\
&&&&&&&&&&&= 100.36\:Wm^{-2}s^{-1}
\end{align*}$$

Getting overall heat flux. Then to get heat transfer for each region is slightly more difficult but not so hard.

$$\begin{align*}
\dot{q}_{AB} &= \dot{q}_{BC}=\dot{q}_T
\end{align*}$$
$$\begin{align*}
r_{A} = r_{C}&= \frac{R_{A}}{A} =0.625& r_{B}&= \frac{R_{B}}{A} = \frac{10}{69}
\end{align*}$$
So:

$$\begin{align*} 
&\begin{aligned} 
\dot{q} &= \frac{1}{r_{A}}(T_{1}-T_{2}) \\
\dot{q} &= \frac{1}{r_{C}}(T_{3}-T_{4}) \\
\end{aligned}
&&\to&
&\begin{aligned} 
T_{1} -r_{A} \dot{q}  &=   T_{2}    \\
r_{A} \dot{q}+ T_{4}  &=  T_{3}   \\
\end{aligned} 
&&\to&
&\begin{aligned} 
T_{2} &= 87.275\:\degree C\\
T_{3} &= 72.725\:\degree C
\end{aligned}
\end{align*}$$
