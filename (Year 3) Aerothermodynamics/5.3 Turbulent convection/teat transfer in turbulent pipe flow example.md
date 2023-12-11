---
aliases: [""]
tags: []
---

## Teat transfer in turbulent pipe flow example

![[Pasted image 20231211204651.png]]

The mean outlet temperature can be found if we consider the gasses [[constant pressure specific heat]], additionally using the [[first law of thermodynamics]] and [[enthalpy]] we know that $\dot{\Delta\mathcal{H}}=\dot{Q}$:

$$\begin{align*}
c_{p} &= \frac{d\mathcal{H}}{dT} \frac{1}{m} &&\to&  c_{p} &= \frac{\Delta\mathcal{H}}{\Delta T} \frac{1}{m} &&\to& \Delta T &= \frac{\dot{\Delta\mathcal{H}}}{c_{p}} \frac{1}{\dot{m}} &&\to& \Delta T &= \frac{\dot{Q}}{c_{p}} \frac{1}{\dot{m}}
\end{align*}$$

The complication comes from the fact that we can't just take $c_{p}$ as a constant like we do typically, since we have [[Prandtl number]] we can find $c_{p}$:
$$\begin{align*}
\text{Pr}  &= \frac{c_{p} \mu}{k} &&\to &  \frac{\text{Pr}k}{\mu}  &= c_{p} =1014.51
\end{align*}$$
So then:
$$\begin{align*}
\Delta T &= \frac{\dot{Q}}{c_{p}} \frac{1}{\dot{m}}=141.93K&&&\therefore T_{0}&= 241.93\degree C
\end{align*}$$


Then to find Reynolds number:

$$\begin{align*}
\dot{m}&= \pi \frac{d^{2}}{4}\rho V &&\to & \frac{4\dot{m}}{\pi d^{2}} & =   \rho V\\

&&\text{Re} &= \frac{\rho V d}{\mu} & &\to& \text{Re} &= \frac{4\dot{m} d}{\mu \pi d^{2}} & &\to& \text{Re} &= \frac{4\dot{m}  }{\mu \pi d }=14261
\end{align*}$$

Generally the method's are quite different compared to when dealing with the [[laminar-turbulent thermal boundary layer example]], since in a pipe the boundary layer is fully developed and can be assumed to be in steady state.


First we need [[convection heat transfer coefficient]].

$$\begin{align*}
&& \text{Nu}&= \frac{hd}{k}\\
\text{Nu} &= 0.023\:\text{Re}_{x}^{\frac{4}{5}}\:\text{Pr}^{0.4} &&\to&  \frac{hd}{k}&= 0.023\:\text{Re}_{x}^{\frac{4}{5}}\:\text{Pr}^{0.4} &&\to&  h&= \frac{0.023k}{d}\:\text{Re}_{x}^{\frac{4}{5}}\:\text{Pr}^{0.4}=307.1
\end{align*}$$

Using this we can get the wall temperature from [[thermal boundary layer|thermal boundary layer heating equation]], taking the fact that the rate of heat transfer is constant along the pipe hence $T_{pipe,x}-T_{fliud,x}=\Delta T$ is constant:

$$\begin{align*}
\dot{Q} &= hA\Delta T &&\to& \frac{1}{h}\frac{\dot{Q}}{A} &= \Delta T &&\to& \frac{1}{h}\frac{\dot{Q}}{d\pi L} &= \Delta T =82.91K
\end{align*}$$

Temp is highest at the outlet, hence:

$$\begin{align*}
T_{max} &= T_{o} + \Delta T =324.8\degree C
\end{align*}$$
