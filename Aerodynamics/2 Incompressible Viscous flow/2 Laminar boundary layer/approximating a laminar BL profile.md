---
aliases: [""]
tags: []
---

## Approximating a laminar BL profile
We know from [[similarity in boundary layer velocity profiles]] that for flow over a plate if you know the flow profile at one point in the flow, you can scale it for any other point in the flow (as long as it's the same type of flow). It is therefore possible to derive equations defining flow at any point on the plate and subsequently characteristics of the flow if you have a accurate model for flow profile; here we are going to assume the following flow profile:
![[Pasted image 20221030151008.png]]
Or expressed mathematically:
$$ u(y) = \begin{dcases} U_{\infty} \frac{y}{\delta} & for\:\: y<\delta \\ U_{\infty}  & for\:\:y\geq\delta \end{dcases} $$
Plugging this into the equations of [[boundary layer momentum thickness|momentum thickness]] and [[boundary layer displacement thickness|displacement thickness]] results in the following:
$$\begin{align*}
\theta & = \int^{\infty}_{0} \frac{U(y)}{U_{\infty}}\left( 1 - \frac{U(y)}{U_{\infty}} \right) dy& \delta * &= \int^{\infty}_{0} \left( 1 - \frac{U(y)}{U_{\infty}} \right) dy\\
  & = \int^{\delta}_{0} \frac{ U_{\infty} \frac{y}{\delta} }{U_{\infty}}\left( 1 - \frac{U_{\infty} \frac{y}{\delta}}{U_{\infty}} \right)dy &    &= \int^{\delta}_{0} \left( 1 - \frac{U_{\infty} \frac{y}{\delta}}{U_{\infty}} \right) dy\\
&... & &...\\
\theta & =\delta \frac{1}{6} & \delta * & =\delta \frac{1}{2}\\
6\theta & =\delta  & 2\delta * & =\delta 
\end{align*}$$
The [[boundary layer shape factor|shape factor]] can then easily be calculated, which gives us $H=3$. We can also use the formula for [[momentum integral equation for a flat plate|MIE]]:  
$$\begin{align*}
\frac{d\theta}{dx} &= \frac{\nu}{U_{\infty}^{2}} \left. \frac{du}{dy} \right|_{y=0} & u(y) &= U_{\infty} \frac{y}{\delta}\\
& & \frac{du}{dy} &= U_{\infty} \frac{1}{\delta}\\
\frac{d\theta}{dx} &= \frac{\nu}{U_{\infty}^{2}}  \frac{U_{\infty}}{\delta}\\
&= \frac{\nu}{U_{\infty} \delta} = \frac{\nu}{U_{\infty} 6\theta}  \\
\int^{\theta}_{0} \theta d\theta &= \int^{x}_{0} \frac{\nu}{6 U_{\infty}}dx\\
&...\\
\frac{\theta^{2}}{x} &=  \frac{\nu}{3 U_{\infty}}\\
\frac{\theta}{x } &= \sqrt \frac{\nu}{3 x U_{\infty}} & Re &= \frac{UL}{\nu}\\
 &= \sqrt \frac{1}{3 Re_{x}}  \\
 &\approx \frac{0.577}{\sqrt{Re_{x}}}
\end{align*}$$
Then using the identity $3\theta = \delta *$ and the definition of [[viscous drag coefficient|local viscous drag coefficient]] we can also get the following identities from the above quite easily:
$$\begin{align*}
\frac{\delta*}{x} &= \frac{3\theta}{x} &&& C_{f} = 2 \frac{d\theta}{dx} = 2\frac{\nu}{U_{\infty} 6\theta} &=  \frac{\nu}{U_{\infty} 3\theta}  & \frac{\theta^{2}}{x} &=  \frac{\nu}{3 U_{\infty}}\\
&\approx \frac{1.732}{\sqrt{Re_{x}}} &&&  &  & \frac{\theta }{x} &=  \frac{\nu}{3 U_{\infty}\theta}   \\ 
&&&& C_{f} &\approx \frac{0.577}{\sqrt{Re_{x}}}
\end{align*}$$
The process for deriving these for a more accurate and complex profile is basically the same as above but more a pain in the ass, hence the results [[parabolic laminar BL profile]].