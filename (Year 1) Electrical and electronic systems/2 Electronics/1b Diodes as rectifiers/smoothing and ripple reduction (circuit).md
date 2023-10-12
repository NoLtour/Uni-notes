---
aliases: ["wave smoothing and ripple reduction"]
tags: ["Question","QFormat3"]
---

#### What is
## Smoothing and ripple reduction (circuit)
### Introduction
So if we look at [[full-wave rectification]] and [[half-wave rectification]] we can see that even though the voltage sign is constant the magnitude is constantly changing, even the glorious [[full-wave rectification|FULL BRIDGE RECTIFIER!!!!]] suffers from this problem, and yes I am leaving exclamation points mid sentence.
So we use [[smoothing and ripple reduction (circuit)|wave smoothing and ripple reduction]] by using components that have useful time dependent properties.

### Using [[Capacitors|Capacitors]]
It is possible to make a [[full-wave rectification|FULL BRIDGE RECTIFIER!!!!]] even more perfect by adding a smoothing [[Capacitors|capacitor]] as shown:
![[Pasted image 20211217162252.png]]
Since the capacitor charges and discharges depending on the cycle position it leads to a pd/time graph like:
![[Pasted image 20211217162455.png]]
As the [[capacitance]] of the capacitor increases the $\Delta V$ decreases, consequently if the $\Delta t$ increases the $\Delta V$ increases. So we can reduce peaks with stronger [[Capacitors|Capacitors]] or by increasing the frequency of the AC.
In reality you don't need a perfect constant supply voltage, your use case will have an acceptable range of voltages, currents and rate of change of these, so basically we just need the ripple reduction to be "good enough".

Note that the following equations are an approximation.
> ### $$ C = \frac{i_{DC}}{2f(\Delta V)} $$ 
> ### $$ C = \frac{i_{DC}}{4f(V_p - V_{average})} $$ 
>> where:
>> $C=$ [[capacitance]] 
>> $\Delta V=$ variation between max and min voltage
>> $f=$ AC frequency
>> $i_{DC}=$ charge flow in the visinity of the capacitor
>> $V_{average}=$ average voltage
>> $V_p=$ max voltage

#### Deriving equations
If we want nice equations to calculate the expected smoothing we can derive them.
Starting with the capacitor equation:

$$\begin{align*}
Q &= CV\\
\frac{dQ}{dt} &= C \frac{dV}{dt}\\
i_{DC} &= C \frac{dV}{dt}
\end{align*}$$

If you look back at our ripple graph, the shape can be approximated as triangular so to make working ez we are going to do just that:

$$\begin{align*}
i_{DC} &= C \frac{\Delta V}{ \Delta t }
\end{align*}$$

We also know that $\Delta t$ will be equivilent to half of the AC period ($T$) so $\Delta t = \frac{1}{2}T$ subbing that in:

$$\begin{align*}
i_{DC} &= C \frac{\Delta V}{ \frac{1}{2}T } & f = \frac{1}{T}\\
i_{DC} &= C 2f(\Delta V)\\
\therefore C &= \frac{i_{DC}}{2f(\Delta V)}
\end{align*}$$

We can also get this interms of average voltage by subracting $\Delta V \frac{1}{2}$ from $V_p$, where $V_p$ is peak voltage ($V_{average}=V_p - \Delta V \frac{1}{2}$):
$$\begin{align*}
C &= \frac{i_{DC}}{2f(\Delta V)} & 2(V_p - V_{average}) &= \Delta V\\
C &= \frac{i_{DC}}{2f(2(V_p - V_{average}))}\\
\therefore C &= \frac{i_{DC}}{4f(V_p - V_{average})}
\end{align*}$$