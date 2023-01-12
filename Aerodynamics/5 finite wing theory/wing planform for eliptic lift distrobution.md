---
aliases: [""]
tags: []
---

## Wing planform for eliptic lift distrobution

### Varying the chord

We've already done all that analysis on [[elliptic lift distrobution analysis|elliptic lift distrobution characteristics]] but how do we achieve that elliptic distrobution? We can figure this out for the case where along the span:
- $\alpha_{L=0}$ is constant
- $\alpha$ is constant
  
So the only thing varying with span is chord, combining [[2D and 3D lift coefficient|2D lift coefficient]] , [[Kutta-Joukowski Theorem]] and the equation from describing circulation variation with span:

$$\begin{align*}
C_{l}\frac{1}{2} \rho V_{\infty}^{2} c  &=   L' & L' &= \rho V_{\infty} \Gamma\\
C_{l}\frac{1}{2} \rho V_{\infty}^{2} c  &=   \rho V_{\infty} \Gamma\\
c  &=     \frac{2\Gamma}{ C_{l}  V_{\infty} } & \Gamma &= \Gamma_{0} \sqrt{ 1- \left(\frac{2y_{0}}{b}\right)^{2} }  \\
c(y_{0})  &=     \frac{2 \Gamma_{0}}{ C_{l}  V_{\infty} }  \sqrt{ 1- \left(\frac{2y_{0}}{b}\right)^{2} }   \\

\end{align*}$$

So in the case where only chord is varied along the span to achieve elliptic lift distrobution we just make an elliptic wing. This has been done in many planes with one example being this little known aircraft:
![[Pasted image 20221213152200.png]]
([[very niche|almost no one knows about it]])

### Without using elliptic planform

It's actually a massive pain in the ass to manufacture elliptic wings, so when possible it's useful to use other approaches to achieve the same effect. For example using:
- [[aerodynamic twist]]
- [[geometric twist]]

To change $\alpha_{L=0}$ along the span. We can do the maths for how to achieve this by combining the equations for [[Kutta-Joukowski Theorem]], [[effective AoA on finite wings]] and the prev equation for elliptic lift distrobution:

$$\begin{align*}
C_{l} &= a_{0}( \alpha - \alpha_{i} - \alpha_{L=0} )  & \Gamma &= \Gamma_{0} \sqrt{ 1- \left(\frac{2y_{0}}{b}\right)^{2} }  & L' &= \rho V_{\infty} \Gamma & C_{l}\frac{1}{2} \rho V_{\infty}^{2} c  &=   L'
\end{align*}$$
$$\begin{align*}
&...\\
\alpha - \alpha_{L=0} &= \alpha_{i} + \frac{2\Gamma_{0}}{a_{0}cV_{\infty}}\sqrt{ 1- \left(\frac{2y_{0}}{b}\right)^{2} }
\end{align*}$$

By varying the shape of the wing to achieve that equation even square wings can have elliptic lift distrobutions:
![[Pasted image 20221213155228.png]]


### A thing that's painful

We've done all this sexy maths on lift distrobution, but you know what (>unlifts your fueseladge):
![[Pasted image 20221213155330.png]]
([[you ugly good for nothing lift disrupting turd looking asshole of a plane|undescribable rage]])

The solution is to use the fusualage to generate lift, which is easyer said than done but can be done:
![[Pasted image 20221213155535.png]]

![[Pasted image 20221213155543.png]]
