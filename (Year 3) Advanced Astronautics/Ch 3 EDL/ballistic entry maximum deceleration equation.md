---
aliases: [""]
tags: []
---

## Ballistic entry maximum deceleration equation

Making use of previous equations:
- Velocity as a function of density
- Acceleration as a function of density

It becomes possible to derive an expression for rate of change of velocity during ballistic re-entry:

> ### $$\begin{align*} \frac{dV}{dt}  &=  \frac{\beta}{2B} V^{2} \ln \frac{V}{V_{0}} &&& \ln \frac{V_{g\:max}}{V_{0}} &= -\frac{1}{2} &&& \left(\frac{dV}{dt}\right)_{max}  &=  \frac{  \alpha \sin\gamma_{0} }{2e}  V_{0}^{2} \\ & &&& & &&& \left( \frac{\dot{V}}{g} \right)_{max}  &=  \frac{  \alpha \sin\gamma_{0} }{2eg}  V_{0}^{2} \end{align*}$$
>> where: 
>> $V_{g max}=$ [[non-thrusting entry terms|inertal velocity magnitude]] at maximum decceleration
>> $V=$ final [[non-thrusting entry terms|inertal velocity magnitude]]
>> $V_{0}=$ initial [[non-thrusting entry terms|inertal velocity magnitude]]
>> $\left(\frac{dV}{dt}\right)_{max}=$ maximum deceleration
>> $\left( \frac{\dot{V}}{g} \right)_{max}=$ max G force
>> $\beta=2B \alpha \sin\gamma_{0}$
>> $B=$ [[ballistic coefficient]] 
>> $\gamma_{0}=\gamma=$ [[non-thrusting entry terms|flight-path angle]] (constant)
>> $\alpha^{-1}=$ [[atmospheric model for re-entry|scale height constant]] 
>
>> assumptions:
>> - The magnitude of weight in the direction of travel is significantly smaller than drag, $W<<D\sin\gamma$ such that it can be neglected
>> - There is zero thrust and lift
>> - The entry angle is constant $\gamma=\gamma_{0}$
>> - The atmosphere can be modelled using this [[atmospheric model for re-entry]]
>> - Vehicle mass is constant


Rewriting for clarity:
$$\begin{align*}
\ln \frac{V_{g\:max}}{V_{0}} &=- \frac{1}{2} & &\to & V_{g\:max}  &= V_{0}e^{-\frac{1}{2}}
\end{align*}$$

The velocity that max deceleration is just a function of initial velocity, we can find a function for magnitude subbing back in:

$$\begin{align*}
&& V_{g\:max}  &= V_{0}e^{-\frac{1}{2}}\\
\frac{dV}{dt}  &=  \frac{\beta}{2B} V^{2} \ln \frac{V}{V_{0}} & &\to & \left(\frac{dV}{dt}\right)_{max}   &=  \frac{\beta}{2B}  V_{0}^{2}(e^{- \frac{1}{2}})^{2} \ln \frac{ V_{0}e^{-\frac{1}{2}}}{V_{0}} & &\to & \left(\frac{dV}{dt}\right)_{max}  &=  \frac{\beta }{4eB}  V_{0}^{2}   & &\to & \left(\frac{dV}{dt}\right)_{max}  &=  \frac{  \alpha \sin\gamma_{0} }{2e}  V_{0}^{2}
\end{align*}$$

Now we can see that the magnitude of maximum deceleration:
- Increases by initial velocity squared
- Is independent of ballistic coefficient
- Increases with entry angle

(Note that this is for a highly simplified model)

The independence of [[ballistic coefficient]] is demonstrated here, increased ballistic coefficient just leads to peak deceleration occurring lower in the atmosphere rather than changing peak magnitude. Something worth noting however is that the increased density at lower altitudes will obviously effect heating intensity.

![[Pasted image 20231121234703.png]]