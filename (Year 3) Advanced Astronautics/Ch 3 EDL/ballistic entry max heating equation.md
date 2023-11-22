---
aliases: [""]
tags: []
---

## Ballistic entry max heating equation

### Equations

> ### $$\begin{align*} \dot{q}  &= k V^{3} \sqrt{\ln \frac{V_{0}}{V} } &&& \frac{V_{peak\:\dot{Q}}}{V_{0}} &= e^{-\frac{1}{6}} &&& \dot{q}_{max} &= k V_{0}^{3}  \sqrt{\frac{ B \alpha \sin\gamma_{0}}{3e} } \end{align*}$$
>> where:
>> $\dot{q}=$ heating (I think units are $W/m^{2}$ but never clarified)
>> $k=$ some constant related to heating
>> $V_{0}=$ initial [[non-thrusting entry terms|inertal velocity magnitude]]      
>> $V=$ final [[non-thrusting entry terms|inertal velocity magnitude]]      
>> $V_{peak\:\dot{Q}}=$ [[non-thrusting entry terms|inertal velocity magnitude]] when max heating occurs
>> $\beta=2B \alpha \sin\gamma_{0}$
>> $B=$ [[ballistic coefficient]] 
>> $\gamma_{0}=\gamma=$ [[non-thrusting entry terms|flight-path angle]] (constant)
>> $\alpha^{-1}=$ [[atmospheric model for re-entry|scale height constant]]
>
>
>> assumptions:
>> - The magnitude of weight in the direction of travel is significantly smaller than drag, $W<<D\sin\gamma$ such that it can be neglected
>> - There is zero thrust and lift
>> - The entry angle is constant $\gamma=\gamma_{0}$
>> - The atmosphere can be modelled using this [[atmospheric model for re-entry]]
>> - Vehicle mass is constant

 
The $q_{max}$ is not defined nicely on slides so here is the quick derivation of my version:
$$\begin{align*}
 \dot{q}  &= k V^{3} \sqrt{\beta \ln \frac{V_{0}}{V}} & &\to &  \dot{q}_{max} &= k \left(V_{0} e^{-\frac{1}{6}}\right)^{3} \sqrt{\beta \ln \frac{V_{0}}{V_{0} e^{-\frac{1}{6}}}}  & &\to &  \dot{q}_{max} &= k V_{0}^{3}  \sqrt{\frac{\beta}{6e} }& &\to &  \dot{q}_{max} &= k V_{0}^{3}  \sqrt{\frac{ B \alpha \sin\gamma_{0}}{3e} }
\end{align*}$$

### Effect

![[Pasted image 20231121193002.png]]

![[Pasted image 20231121200042.png]]

This has significant design implications:
- Peak heating is proportional to the cube of initial velocity
- Peak heating increases with [[ballistic coefficient]]
- Peak heating increases with steeper re-entry angles

It should be noted however that the integral under a time-heating curve will produce the same total heating for any given starting velocity+altitude, which should be expected considering conservation of energy. So adjusting entry angle simply changes the duration over which heating acts.

Counterintuitively it is often desirable to heat your craft over as short a duration as possible. All heat applying at once means that thermal gradient's are much higher, which increases heat dissipation and reduced heat penetration into the spacecraft.

Something else to note is that according to the equations of peak heating and peak G force:

$$\begin{align*}
\frac{V_{peak\:\dot{Q}}}{V_{0}} &= e^{-\frac{1}{6}} &  \frac{V_{g\:max}}{V_{0}} &= e^{-\frac{1}{2}}
\end{align*}$$

We can clearly see that peak heating occurs before peak G-force, which means that:
- By the time maximum G-force is experienced most/all of the ablative heat shield would be gone
- The vehicle will be significantly lighter when max G is experienced
- We assume $m$ to be constant in all these models, this damages our validity 

![[Pasted image 20231121234905.png]]

Something to note is that the geometry also effects where heat is concentrated.