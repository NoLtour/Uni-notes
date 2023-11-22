---
aliases: [""]
tags: []
---

## Ballistic entry equations velocity equation

From previous equations the following can be derived:

> ### $$\begin{align*} \\\frac{1}{V} \: dV &= \frac{1}{2B \alpha \sin\gamma_{0}} d\rho = \frac{1}{\beta} d\rho & \frac{V}{V_{0}} &= e^{- \frac{\rho}{\beta}} \end{align*}$$
>> where:
>> $V=$ [[non-thrusting entry terms|inertal velocity magnitude]]
>> $V_{0}=$ initial [[non-thrusting entry terms|inertal velocity magnitude]]
>> $\beta=2B \alpha \sin\gamma_{0}$
>> $\alpha^{-1}=$ [[atmospheric model for re-entry|scale height constant]]
>> $B=$ [[ballistic coefficient]]
>> $\rho=$ density from [[atmospheric model for re-entry]]
>> $\gamma_{0}=\gamma=$ [[non-thrusting entry terms|flight-path angle]] (constant)
>
>> assumptions:
>> - The magnitude of weight in the direction of travel is significantly smaller than drag, $W<<D\sin\gamma$ such that it can be neglected
>> - There is zero thrust and lift
>> - The entry angle is constant $\gamma=\gamma_{0}$
>> - The atmosphere can be modelled using this [[atmospheric model for re-entry]]
>> - Atmospheric density when re-entry begins ($\rho_{0}$) is negligible

The first equation shows that deceleration rate (and hence g force) can be approximated as a function of velocity and density:

$$\begin{align*}
\frac{dV}{dt} &= \frac{V}{2B \alpha \sin\gamma_{0}} \frac{d\rho}{dt}
\end{align*}$$

If you look at this equation, consider that rate of density change $d\rho/dt$ will:
- Increase with velocity
- Increase with lower altitude

This is also multiplied by the velocity $V$, meaning $g$ force's experienced by a ballistically re-entering vehicle become incredibly intense if you reach lower altitude at a high speed (as you'd expect).
