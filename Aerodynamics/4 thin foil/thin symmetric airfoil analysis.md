---
aliases: [""]
tags: []
---

## Thin symmetric airfoil analysis
### Lift coefficient
#### Result
> ### $$C_{l} =  2\pi\alpha $$
> ### $$ \frac{dC_{l}}{d\alpha}= 2\pi$$
>> where:
>> $C_{l}=$ [[2D and 3D lift coefficient|2D lift coefficient]]
>> $\alpha=$ angle of attack

Hence we can see for all symetric airfoils they have zero lift at $\alpha=0$ and their lift increases linearly with increasing angle of attack, this is also reflected in real life (with limit of stall + some slight error).


![[Pasted image 20221205145621.png]]



#### Proof
So to start we take the [[fundemental equation of thin aerofoil theory]] and slap a zero camber condition on it, aka $\frac{dz}{dx}=0$ reulting in:

$$\begin{align*}
 V_{\infty} \left(\alpha -\frac{dz}{dx}\right) &= \frac{1}{2\pi}\int^{\pi}_{0} \frac{\gamma(\theta) \sin\theta }{\cos \theta - \cos\theta_{0}} d\theta & &\to &  V_{\infty} \alpha  &= \frac{1}{2\pi}\int^{\pi}_{0} \frac{\gamma(\theta) \sin\theta }{\cos \theta - \cos\theta_{0}} d\theta 
\end{align*}$$

Then if you solve the equation above for $\gamma(\theta)$ you will get:

$$\begin{align*}
\gamma(\theta) &= 2 V_{\infty} \alpha \frac{1+\cos\theta}{\sin\theta}
\end{align*}$$
The intermidiate steps required to figure this out are [[because it is really really hard|outside the scope]] of the course so just accept it.

Now we can start to find some useful numbers, such as lift. Taking the [[Kutta-Joukowski Theorem]], the equation above and the defenition of [[vortex sheet strength]]:
$$\begin{align*}
L' &= \rho V_{\infty} \Gamma  & \gamma(\theta) &= 2 V_{\infty} \alpha \frac{1+\cos\theta}{\sin\theta}& \Gamma &= \int^{c}_{0} \gamma(\xi) d\xi
\end{align*}$$
Before we can actually get anywhere we've got to convert our equation of $\Gamma$ into a angular form:
$$\begin{align*}
&& \xi &= \frac{c}{2} (1-\cos \theta) & x &= \frac{c}{2} (1-\cos \theta_{0})\\
&& \frac{d\xi}{d\theta} &= \frac{c}{2}\sin\theta
\end{align*}$$

^4c804c

$$\begin{align*}
\Gamma &= \int^{c}_{0} \gamma(\xi) d\xi & &\to & \Gamma &= \int^{\pi}_{0} \gamma(\theta) \frac{d\xi}{d\theta} d\theta \\
&& &&  &=  \alpha\int^{\pi}_{0} 2 V_{\infty} \frac{1+\cos\theta}{\sin\theta} \frac{d\xi}{d\theta} d\theta \\
&& &&  &=  2 V_{\infty} \alpha\int^{\pi}_{0} \frac{1+\cos\theta}{\sin\theta}\frac{c}{2}\sin\theta d\theta \\
&& &&  &=  V_{\infty} \alpha c\int^{\pi}_{0}( 1+\cos\theta) d\theta \\
\end{align*}$$

Now we can continue with finding the lift:
$$\begin{align*}
 L' &= \rho V_{\infty} \Gamma\\
  &=  \rho V_{\infty}^{2}   \alpha c\int^{\pi}_{0}( 1+\cos\theta) d\theta\\
  &=  \pi\rho V_{\infty}^{2}  c   \alpha
\end{align*}$$

It's then trivial to find the [[2D and 3D lift coefficient|2D lift coefficient]] and it's corresponding lift coefficient AOA gradient:
$$\begin{align*}
C_{l} = \frac{L'}{\frac{1}{2} \rho V_{\infty}^{2}c}&= 2\pi\alpha\\
\frac{dC_{l}}{d\alpha}&= 2\pi
\end{align*}$$

### Analysis of vortex distrobution

![[Pasted image 20221208125332.png]]

This is the result of plotting the vortex equation we used earlyer, once converted into cartesian form (right graph) you get a more intuitive look at the distrobution. Something that should be kept in mind is as shown in previous section ([[vortex sheet strength#Sheet strength and pressure]]) we know that:
$$ \gamma \propto \Delta P $$
Meaning according to our gamma function the pressure difference decreases from infinity to zero along the length of the foil, (of course this isn't the case in real life but a simular shape is followed). This extreme pressure distrobution actually leads to boundary layer seperation (if you include [[viscosity]]) on the leading edge:
![[Pasted image 20221208125817.png]]

The area where flow is detached leads to a region where the pressure does not follow the distrobution predicted by $\gamma$ and reduces lift.

### Pitching moment

#### Equations

> ### $$\begin{align*}   C_{m,LE} &= - \frac{C_{l}}{4}  \end{align*}$$
> ### $$\begin{align*}   C_{m,c/4} &= C_{m,LE}+ \frac{C_{l}}{4}  \end{align*}$$
>> where:
>> $=$ 
>> $=$
>> $=$

#### Proof

![[Pasted image 20221207215540.png]]

The pitching moment at some distance away from the leading edge is $dM_{LE}'=-\xi dL'$ which can be rearranged into a more useful form by substituting in the formula from [[Kutta-Joukowski Theorem|Kutta-Joukowski]] then converting to angular form using [[thin symmetric airfoil analysis#^4c804c|here]]:
$$\begin{align*}
M_{LE}' &= - \int^{c}_{0} \xi dL' & &\to &M_{LE}' &= - \int \xi \rho V_{\infty} d\Gamma  & &\to &M_{LE}' &= - \int^{c}_{0} \xi \rho V_{\infty} \gamma(\xi)  \: d\xi 
\end{align*}$$

$$\begin{align*}
M_{LE}' &= - \int^{c}_{0} \xi \rho V_{\infty} \gamma(\xi)  \: d\xi  & \xi &= \frac{c}{2}(1-\cos \theta)\\
 &= - \int^{\pi}_{0} \frac{c}{2}(1-\cos \theta) \rho V_{\infty} \gamma(\xi)  \: \frac{d\xi}{d\theta} d\theta & \frac{d\xi}{d\theta} &= \frac{c}{2}\sin\theta\\
&= - \int^{\pi}_{0} \frac{c}{2}(1-\cos \theta) \rho V_{\infty} \gamma(\theta)  \frac{c}{2}\sin\theta \: d\theta  &&& \gamma(\theta) &= 2 V_{\infty} \alpha \frac{1+\cos\theta}{\sin\theta}\\
&= - \int^{\pi}_{0} \frac{c}{2}(1-\cos \theta) \rho V_{\infty} 2 V_{\infty} \alpha \frac{1+\cos\theta}{\sin\theta}  \frac{c}{2}\sin\theta \: d\theta \\
&= - \frac{1}{2}\rho V_{\infty}^{2} c^{2}\alpha \int^{\pi}_{0} (1-\cos^{2}\theta) \: d\theta\\
&= - \frac{\pi}{4}\rho V_{\infty}^{2} c^{2}\alpha 
\end{align*}$$

To find the coeffcient of moments from the leading edge is simple:
$$\begin{align*}
C_{m,LE} = \frac{M_{LE}'}{\frac{1}{2} \rho V^{2}_{\infty}c^{2} }  &= \frac{- \frac{\pi}{4}\rho V_{\infty}^{2} c^{2}\alpha }{\frac{1}{2} \rho V^{2}_{\infty}c^{2} } \\
&= - \frac{\pi\alpha}{2}
\end{align*}$$
Recall that for a symetric airfoil the coefficient of lift is simply $C_{l}=2\pi\alpha$ hence:
$$\begin{align*}
C_{m,LE} &= - \frac{\pi\alpha}{2} & &\to & C_{m,LE} &= - \frac{C_{l}}{4}
\end{align*}$$
So for a symetric airfoil moment coefficient around the leading edge is directly proportional to the lift coefficient!

![[Pasted image 20221207222013.png]]

We can also calculate the [[aerodynamic centre]], simply :
$$\begin{align*}
\frac{d}{d\alpha} (x C_{l} - c C_{m,LE}) &= 0\\
\frac{d}{d\alpha} \left( x C_{l} - c\frac{C_{l}}{4} \right) &= & C_{l} =  2\pi \alpha \\
\frac{d}{d\alpha} 2\pi \alpha \left( x-\frac{c}{4}   \right) &= \\
  \frac{c}{4}   &= x
\end{align*}$$
Hence the [[aerodynamic centre]] is at $\frac{c}{4}$ ([[very nice indeed|neat]] we just proved a result from first year).
