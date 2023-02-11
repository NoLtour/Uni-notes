---
aliases: [""]
tags: []
---

## Calculating crack life using [[AHHHHHHHHHHHHH FRENCH|paris]] law

### Derivation

Starting with [[crack propagation rate (material fatigue)#Crack propigation rate equation (paris rule)|paris rule]]:
$$\frac{da}{dN} = A (\Delta K)^{m}$$
It's obvious that to find $N$ we'll need some integration, further we need a equation for $\Delta K$, K so let's grab the equation for [[stress intensity factor]]:

$$\begin{align*}
\Delta K &= Q \Delta \sigma \sqrt{\pi a}
\end{align*}$$

Then we just combine and do some maths magic:

$$\begin{align*}
 \frac{da}{dN} &=  A (\Delta K)^{m}\\
 \frac{da}{dN} &=  A (Q \Delta \sigma \sqrt{\pi a})^{m}\\
 \int \frac{1}{\sqrt{a}^{m}} da &=  A (Q \Delta \sigma \sqrt{\pi })^{m} \int dN \\
\end{align*}$$
Now we just need limits, these will be the crack at the start and the crack at the end. By definition the crack at the end should be [[critical crack radius]], so:
- At the start $a=a_{i}$, $N=0$
- At the end $a=a_{c}$, $N=N_{f}$

Subbing in and integrating:
$$\begin{align*}
\int^{a_{c}}_{a_{i}} \frac{1}{\sqrt{a}^{m}} da &=  A (Q \Delta \sigma \sqrt{\pi })^{m} \int^{N_{f}}_{0} dN\\
\frac{1}{1-\frac{m}{2}}\left(a_{c}^{1- \frac{m}{2}} - a_{i}^{1- \frac{m}{2}}\right) &= A (Q \Delta \sigma \sqrt{\pi })^{m} N_{f}
\end{align*}$$

> ### $$\begin{align*}  \frac{1}{1-\frac{m}{2}}\left(a_{c}^{1- \frac{m}{2}} - a_{i}^{1- \frac{m}{2}}\right) &= A (Q \Delta \sigma \sqrt{\pi })^{m} N_{f}  \end{align*}$$
>> where:
>> $m,A=$  material constants related to [[crack propagation rate (material fatigue)|paris rule]]
>> $a_{c}=$ [[critical crack radius]]
>> $a_{i}=$ initial crack radius (often found using advanced electronic devices, ultrasound sensors, X rays ect)
>> $Q=$ [[stress intensity factor|shape factor]]
>> $\Delta \sigma=$ stress range
>> $N_{f}=$ cycles to failure

Something to keep in mind is that not all geometrys/materials follow [[crack propagation rate (material fatigue)|paris rule]]! So this is as always an estimation that can sometimes be used.