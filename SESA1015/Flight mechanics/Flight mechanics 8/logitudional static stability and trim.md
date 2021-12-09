---
aliases: ["logitudional static stability","logitudional trim"]
tags: ["Question","QFormat3"]
---

#### Describe how to achieve
## Logitudional static stability and trim
### Intro

This is where you get [[static stability]] in the pitch axis of the aircraft, expressed mathamatically:

$$\begin{align*}
\frac{dC_{mG}}{d\alpha} &< 0 
\end{align*}$$
$dC_{mG}$ being the pitching moment about the centre of gravity
$\alpha$ being the [[Angle of attack]]

So to calculate this we will need an expression for $C_{mG}$ interms of $\alpha$. Introducing "maths":

### Maths
We will use the following diagram:

![[aircraft controls and dimentions for calculating longitudional stability#^267a4d]]

Now if we take moments about the centre of gravity:
$$\begin{align*}
 M_G &=  M_0 + L_W(h-h_0)c - P( l_T - (h-h_0)c )
\end{align*}$$
Here the $M_0 + L_W(h-h_0)c$ is from the wing and $- P( l_T - (h-h_0)c )$ is from the tailplane.

#### Desired diagram
So we can see by the equation that $P(...)$ is counteracting $L_W(...)$, which is desireable for static stability. But the important bit is how they change with changing $\alpha$ (angle of attack), to get an automatic return to the correct $\alpha$ we will need:
- $M_G<0$ when pitched upward
- $M_G>0$ when pitched downward

Hence:
- $M_0+L_W(...) < P(...)$ when pitched upward
- $M_0+L_W(...) > P(...)$ when pitched downward

![[Pasted image 20211206143540.png]]

#### Back to maths
Now we can convert everything into coefficients:
$$\begin{align*}
 \frac{M_G}{\frac{1}{2}\rho V^{2}S_c} &=  \frac{M_0 + L_W(h-h_0)c - P( l_T - (h-h_0)c )}{\frac{1}{2}\rho V^{2}S_c}\\
C_{mG} &=  C_{mo} + (h-h_0)\left(C_{Lw}+\frac{C_{LT}S_T}{S}\right) - \left(\frac{S_T l_T}{ Sc }\right)C_{LT}\\
& & \bar{V}&= \frac{S_T l_T}{ Sc }\\
C_{mG} &=  C_{mo} + (h-h_0)\left(C_{Lw}+\frac{C_{LT}S_T}{S}\right) - \bar{V}C_{LT}
\end{align*}$$

Note that $\bar{V}$ is known as the [[tail volume coefficient]].
We can use verticle equalibrium to simplify further $L=L_W+P=W=\frac{1}{2}\rho V^{2}SC_L$:
$$\begin{align*}
&&L&=L_W+P & W&=\frac{1}{2}\rho V^{2}SC_L\\
&&C_L &= C_{Lw} + C_{LT} \frac{S_T}{S}  &  \frac{2W}{\rho V^{2}S} &= C_L\\
C_{mG} &=  C_{mo} + (h-h_0)\left(C_{Lw}+\frac{C_{LT}S_T}{S}\right) - \bar{V}C_{LT} &C_L - C_{LT} \frac{S_T}{S}&= C_{Lw} \\
C_{mG} &=  C_{mo} + (h-h_0)\left(C_L - C_{LT} \frac{S_T}{S}+\frac{C_{LT}S_T}{S}\right) - \bar{V}C_{LT}\\
C_{mG} &=  C_{mo} + (h-h_0)C_L - \bar{V}C_{LT}
\end{align*}$$

Well now we have hit a wall, since we don't know how to determine $C_{LT}$, if only there was some sort of "[[tailplane lift coefficient|how do you determine the tailplane lift coefficient]]" document... wait that embeded?! Guess we have unhit said wall.

From [[tailplane lift coefficient]] we get:

![[tailplane lift coefficient#^d6f08f]]

Which we can now sub back:
$$\begin{align*}
C_{mG} &=  C_{mo} + (h-h_0)C_L - \bar{V}C_{LT} & C_{LT} &= a_{1T} \alpha_T + a_{2T} \eta \\
C_{mG} &=  C_{mo} + (h-h_0)C_L - \bar{V}(a_{1T} \alpha_T + a_{2T} \eta) &&& \alpha_T &= \alpha\left(1 - \frac{d\varepsilon}{d\alpha}\right)+\alpha_S\\
C_{mG} &=  C_{mo} + (h-h_0)C_L - \bar{V}\left(a_{1T} \left(\alpha\left(1 - \frac{d\varepsilon}{d\alpha}\right)+\alpha_S\right) + a_{2T} \eta\right)\\
& & at\:C_{mG}&=0\\
0 &=  C_{mo} + (h-h_0)C_L - \bar{V}a_{1T} \left(\alpha\left(1 - \frac{d\varepsilon}{d\alpha}\right)+\alpha_S\right) - \bar{V} a_{2T} \bar{\eta} &&& C_L&= a_1 \alpha \\
\bar{V} a_{2T} \bar{\eta} &=  C_{mo} + (h-h_0)a_1 \alpha - \bar{V}a_{1T} \left(\alpha\left(1 - \frac{d\varepsilon}{d\alpha}\right)+\alpha_S\right)\\
\end{align*}$$

### Achieving trim

#### Equations

We now have a final resault for the elevator angle needed for trim:
> ### $$ \bar{V} a_{2T} \bar{\eta} =  C_{mo} + (h-h_0)a_1 \alpha - \bar{V}a_{1T} \left(\alpha\left(1 - \frac{d\varepsilon}{d\alpha}\right)+\alpha_S\right) $$ 
> ### $$ \bar{\eta} =  \frac{C_{mo}}{\bar{V}a_{2T}} + \frac{(h-h_0)a_1 }{\bar{V} a_{2T}}\alpha - \frac{a_{1T} }{ a_{2T}}\left(\alpha\left(1 - \frac{d\varepsilon}{d\alpha}\right)+\alpha_S\right) $$ 
>> where:
>> $a_{1T}= \dfrac{dC_{LT}}{d\alpha_T}=$ lift curve slope of tailplane (for a constant value of $\eta$) 
>> $a_{2T}= \dfrac{dC_{LT}}{d\eta}=$ constant (for a value constant of $\alpha_T$)
>> $\alpha_S=$ angle between tailplane and main wing datum line
>> $\alpha=$ angle of attack
>> $\frac{d\varepsilon}{d\alpha}=$ downwash angle rate of change with angle of attack
>> $\bar{V}=$ [[tail volume coefficient]]
>> $h=$ fraction of the wing chord from the leading edge to centre of gravity
>> $h_0=$ fraction of the wing chord from the leading edge to aerodynamic centre
>> $\bar{\eta}=$ tailplane elevator angle for trim
>> $C_{mo}=$ [[aircraft controls and dimentions for calculating longitudional stability|pitching moment at zero lift coefficient ]]


In some cases instead of trimming by adjusting the tailplanes elevator ange, you will adjust the whole tailplanes planes angle (rotate the entire back wingy bit), if that is the case then to achieve trim you do:
> ### $$ \bar{V} a_{1T} \bar{\alpha_S} = C_{mo} + (h-h_0)a_1 \alpha - \bar{V} a_{1T} \alpha \left(1-\frac{d\varepsilon}{d\alpha}\right) $$ 
>> where: 
>> $a_{1T}= \dfrac{dC_{LT}}{d\alpha_T}=$ lift curve slope of tailplane (for a constant value of $\eta$) 
>> $a_{2T}= \dfrac{dC_{LT}}{d\eta}=$ constant (for a value constant of $\alpha_T$)
>> $\bar{\alpha_S}=$ angle between tailplane and main wing datum line required for trim
>> $\alpha=$ angle of attack
>> $\frac{d\varepsilon}{d\alpha}=$ downwash angle rate of change with angle of attack
>> $\bar{V}=$ [[tail volume coefficient]]
>> $h=$ fraction of the wing chord from the leading edge to centre of gravity
>> $h_0=$ fraction of the wing chord from the leading edge to aerodynamic centre
>> $C_{mo}=$ [[aircraft controls and dimentions for calculating longitudional stability|pitching moment at zero lift coefficient ]]

Note we are assuming that the controls are fixed. (the angle of elevators and such are constant)

#### Implications
There is a maximum that the elevator can angle too and hence a maximum negative trim, this determines the furthest forward that the centre of mass can go. 
It should also be noted that there is extra drag created by the tailplane, hence greater air deflection will create more drag this is known as [[trim drag]].

### 