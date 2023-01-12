---
aliases: [""]
tags: []
---

## Max lift to drag ratio in finite wing theory
### Equation
> ### $$\begin{align*}  C_{L\:\text{(at max L/D)}} &= \sqrt{\pi e A C_{Do}}  \end{align*}$$
> ### $$ \left(\frac{C_{L}}{C_{D}}\right)_\text{max} = \frac{1}{2} \sqrt{ \frac{\pi e A}{C_{Do}} } $$
>> where:
>> $C_{L}=$ lift coefficient
>> $C_{D}=$ total drag coefficient
>> $C_{Do}=$ [[form drag coefficient]]
>> $A=$ [[wing aspect ratio|aspect ratio]]
>> $e=$ [[Oswald efficiency factor]]

Also note that this equation doesn't work if the plane has multiple wings (such as a bi plane), this fact applies to basically everything in [[Finite wing theory overview|finite wing theory]].

### Derivation
This is pretty ezz, just take the equation for drag and slap in the equation for induced drag from [[general lift distrobution for a finite wing#Equations]]:

$$\begin{align*}
C_{D} &= C_{Do} + C_{Di} & C_{Di} &=  \frac{C_{L}^{2}}{\pi eA}\\
C_{D} &= C_{Do} + \frac{C_{L}^{2}}{\pi eA}
\end{align*}$$

Now simply sub into the lift drag ratio ($C_{L}/C_{D}$) and take the derivative and find where it is zero to get the minimum:

$$\begin{align*}
&&\frac{C_{L}}{C_{D}} &= \frac{C_{L}}{C_{Do} + \frac{C_{L}^{2}}{\pi eA}}\\
&&\frac{d}{dC_{L}}\left(\frac{C_{L}}{C_{D}}\right) &= \frac{d}{dC_{L}} \frac{C_{L}}{C_{Do} + \frac{C_{L}^{2}}{\pi eA}}\\
&&&= \frac{\pi eA (\pi eA C_{Do} - C_{L}^{2})}{(\pi eA C_{Do} + C_{L}^{2})^{2}}\\
&\text{let: } \frac{d}{dC_{L}}\left(\frac{C_{L}}{C_{D}}\right) = 0\\
&&0&= \frac{\pi eA (\pi eA C_{Do} - C_{L}^{2})}{(\pi eA C_{Do} + C_{L}^{2})^{2}}\\
&& &...\\
&&C_{L} &= \sqrt{\pi e A C_{Do}}
\end{align*}$$
Then just sub this back into the lift drag ratio equation and we can get max lift drag ratio:
$$\begin{align*}
\left(\frac{C_{L}}{C_{D}}\right)_\text{max} &= \frac{\sqrt{\pi e A C_{Do}}}{C_{Do} + \frac{C_{L}^{2}}{\pi eA}}\\
&= \frac{1}{2} \sqrt{ \frac{\pi e A}{C_{Do}} }
\end{align*}$$
This tells us a bunch about how to maximise efficiency and it will also remind you of [[max lift to drag ratio|year 1 max lift to drag ratio]] because the equations are basically the same, so yeah [[this is why I like using obsidian|neat]] huh?

