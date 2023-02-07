---
aliases: ["thrust limit"]
tags: ["Question","QFormat3"]
---

#### What is the
## Limit on the thrust during a co-ordinated turn

### Intro
For everything so far we have basically just been assuming that the engines can keep up, but here's a real shocker... engines can't output infinate thrust.
So thrust becomes a limiting factor.

This especially becomes an issue when you consider that during a [[co-ordinated turn]] lift tends to exceed weight, with higher turns having even higher lifts required.
(as we know drag tends to increase with lift due to its [[induced drag coefficient]] component).

### Math time
Lets just assume we have a term called $T_{max}$, which is the max thrust the aircraft can produce.

$$\begin{align*}
T_{max} &= D & D&=\frac{1}{2}\rho V^{2} S C_D & C_D &= C_{Do} + kC_L^{2} & R_{min}&= \frac{V^{2}}{g} \frac{1}{\sqrt{ \left(\frac{L_{max}}{W}\right)^{2} - 1}} \\
&= \frac{1}{2}\rho V^{2} S (C_{Do} + kC_L^{2}) &&&&& \frac{V^{2}}{gR_{min}} &= \sqrt{ \left(\frac{L_{max}}{W}\right)^{2} - 1} \\
&= \frac{1}{2}\rho V^{2} S C_{Do} + \frac{1}{2}\rho V^{2} S kC_L^{2} & L &= \frac{1}{2}\rho S V^{2} C_L &&& W\sqrt{\left(\frac{V^{2}}{gR_{min}}\right)^{2} + 1} &= L_{max}\\
& &&&&& W\sqrt{\left(\frac{V^{2}}{gR_{min}}\right)^{2} + 1} &= \frac{1}{2}\rho S V^{2} C_L\\
& &&&&&  \frac{2W}{\rho S V^{2}} \sqrt{\left(\frac{V^{2}}{gR_{min}}\right)^{2} + 1} &= C_L

\end{align*}$$
Ok it's become so phat that I need to shift it:
$$\begin{align*}
T_{max} &=  \frac{1}{2}\rho V^{2} S C_{Do} + \frac{1}{2}\rho V^{2} S k\left(\frac{2W}{\rho S V^{2}} \sqrt{\left(\frac{V^{2}}{gR_{min}}\right)^{2} + 1}\right)^{2} \\
&=  \frac{1}{2}\rho V^{2} S C_{Do} + \frac{4W^{2}\rho V^{2} S k}{2\rho^{2} S^{2} V^{4}}\left( \left(\frac{V^{2}}{gR_{min}}\right)^{2} + 1\right)\\
&=  \frac{1}{2}\rho V^{2} S C_{Do} + \frac{2W^{2} k}{\rho S V^{2}}\left( \left(\frac{V^{2}}{gR_{min}}\right)^{2} + 1\right)\\
&=  \frac{1}{2}\rho V^{2} S C_{Do} + \frac{2W^{2} k}{\rho S V^{2}}\frac{V^{4}}{g^{2}R_{min}^{2}} + \frac{2W^{2} k}{\rho S V^{2}}\\
&=  \frac{1}{2}\rho V^{2} S C_{Do} + \frac{2W^{2} kV^{2}}{\rho S g^{2}R_{min}^{2}} + \frac{2W^{2} k}{\rho S V^{2}}\\
\end{align*}$$
We also have the equation for drag in steady level flight ($D_L$) and for our $D_L$ we can assume that $L=W$
$$\begin{align*}
&& D_{L} &= \frac{1}{2}\rho V^{2}S ( C_{Do} + kC_L^{2} ) & W = L &= \frac{1}{2}\rho V^{2} S C_L\\
&& D_{L} &= \frac{1}{2}\rho V^{2}S C_{Do} + kC_L^{2} \frac{1}{2}\rho V^{2}S & \frac{2W}{\rho V^{2} S} &=C_L\\
&& &= \frac{1}{2}\rho V^{2}S C_{Do} + k\left(\frac{2W}{\rho V^{2} S}\right)^{2} \frac{1}{2}\rho V^{2}S\\
T_{max} &=  \frac{1}{2}\rho V^{2} S C_{Do}+ \frac{2W^{2} k}{\rho S V^{2}} + \frac{2W^{2} kV^{2}}{\rho S g^{2}R_{min}^{2}}  & &= \frac{1}{2}\rho V^{2}S C_{Do} + \frac{2W^{2}k}{\rho V^{2} S}\\
T_{max} &= D_L + \frac{2W^{2} kV^{2}}{\rho S g^{2}R_{min}^{2}}\\
R_{min}^{2} &= \frac{2W^{2} kV^{2}}{\rho S g^{2}} \frac{1}{(T_{max} - D_L)}\\
R_{min} &= \sqrt\frac{2W^{2} kV^{2}}{\rho S g^{2}} \frac{1}{\sqrt{T_{max} - D_L}}
\end{align*}$$

### Final equation

[[vent hahahahha amongus funny|vent]] open this link pussy.

> ### $$ R_{min} = \sqrt\frac{2W^{2} kV^{2}}{\rho S g^{2}} \frac{1}{\sqrt{T_{max} - D_L}}  $$ 
>> where:
>> $D_L=\frac{1}{2}\rho V^{2}S C_{Do} + \frac{2W^{2}k}{\rho V^{2} S}$ 
>> $R_{min}=$ min turning radius
>> $T_{max}=$ max thrust

#### Implications

It produces a graph that looks like this:
![[Pasted image 20211129225849.png]]

Now if we consider what this looks like when including the [[limit on the lift during a co-ordinated turn|stall limit]]:
![[Pasted image 20211129230004.png]]
We get two situations, with the top one being desireable for training aircraft because the pilot is unable to stall the plane inside their thrust limit when turning. But the second one they can so is dangerous.