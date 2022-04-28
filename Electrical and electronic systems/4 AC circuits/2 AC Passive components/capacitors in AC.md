---
aliases: ["capacitor impedance"]
tags: ["Question","QFormat3"]
---

#### How do we deal with
## Capacitors in AC
### Capacitor [[impedance]]
> ### $$ Z_{C} = \frac{1}{j\omega C} = \frac{1}{\omega C} \angle -90 $$ 
>> where:
>> $Z_{C}=$ [[capacitors in AC|capacitor impedance]]
>> $j=\sqrt{-1}$
>> $C=$ [[capacitance]]

### Theory
It's the usual, take the equation for [[capacitors#^e6fedd|capacitors]] then the equation for [[complex numbers for representing AC|representing AC with complex numbers]]:
$$\begin{align*}
V(t) &= \frac{1}{C} \int^{t}_{t_{0}} I(t) \cdot dt + V(t_{0}) & I &= I_{p}\cos(\omega t + \phi ) \\
 &=  \frac{1}{C} \int^{t}_{t_{0}} I_{p}\cos(\omega t + \phi ) \cdot dt + V(t_{0}) \\
 && &at\:t=\frac{-\phi}{\omega},V=0\\
&=  \frac{I_{p}}{C \omega} \sin(\omega t + \phi ) \\
&=  \frac{I_{p}}{C \omega} \cos(\omega t + \phi - 90 ) \\
\end{align*}$$