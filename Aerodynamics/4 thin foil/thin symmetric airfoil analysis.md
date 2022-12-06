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
\end{align*}$$$$\begin{align*}
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

### ejhytgfhg

#### Proof




