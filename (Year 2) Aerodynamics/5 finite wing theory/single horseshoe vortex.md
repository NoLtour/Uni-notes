---
aliases: [""]
tags: []
---

## Single horseshoe vortex
### Model
By interpreting the fact that [[tip vortecies and downwash|tip vorticies]] exist and that [[Helmholtz theorem and Biot-Savart law|Helmholtz theorum]] theorum lays out conditions requireing vortex filiments to not have defined endpoints we can arrive at the following model of a finite wing:

![[Pasted image 20221211144808.png]]

Here we represent the lifting strength of the wing  as a "bound vortex" (from [[Kutta-Joukowski Theorem]]), then we represent the [[tip vortecies and downwash|tip vorticies]] as trailing vortecies on the edges. 

### Veloicty function

![[Pasted image 20221211145454.png]]

We can find the veloicty at some point along the bound vortex $y_{0}$ by summing the effect of both free trailing vortecies and the bound vortex. Since we are taking veloicty from inside the bound vortex we know it's contribution will be zero so we just need to velocity caused by the trailing vortecies:
$$\begin{align*}
w &= V_{1} + V_{2} & \vec{V}_{\text{semi infinite}}  & = - \hat{e}_{z}\frac{ \Gamma}{4h\pi} \\
&= - \frac{\Gamma}{4\pi h_{1}} - \frac{-\Gamma}{4\pi (-h_{2}) } \\
&...\\
w &= - \frac{\Gamma}{4\pi} \frac{h_{1}+h_{2}}{h_{1}h_{2}}
\end{align*}$$

![[Pasted image 20221211150453.png]]

We can now get this in terms of $y_{0}$ by subbing in the defenitions of $h_{1}$ and $h_{2}$:
$$\begin{align*}
h_{1} &= \frac{b}{2} - y_{0} & h_{2} &= y_{0} + \frac{b}{2} 
\end{align*}$$
$$\begin{align*}
w &= - \frac{\Gamma}{4\pi} \frac{h_{1}+h_{2}}{h_{1}h_{2}} &&\to& w(y_{0}) &= - \frac{\Gamma}{4\pi} \frac{\left(\frac{b}{2} - y_{0}\right)+\left(y_{0} + \frac{b}{2} \right)}{\left(\frac{b}{2} - y_{0}\right)\left(y_{0} + \frac{b}{2} \right)} \\
&& && &...\\
&& && w(y_{0}) &= - \frac{\Gamma}{4\pi} \frac{b}{\left(\frac{b}{2}\right)^{2} - y_{0}^{2}}
\end{align*}$$

This can then be used to find the induced velocity along the wing, allowing us to then find the induced drag along the wing! Don't celebrate yet though, because at the edges this model falls appart and tends to infinity... so it's useless ([[I love wasting time and effort YAY|poggers]]), meaning we will need to figure out something better before we can continue.
