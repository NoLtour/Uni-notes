---
aliases: [""]
tags: []
---

## Rankine oval

We can get a shape called a [[Rankine oval]] by placing a source and a sink in a uniform flow:
![[Pasted image 20221111113621.png]]
To simplify things it's best to place the source and sink on the x axis with equal distance $b$ from the origin.

The maths to get the [[stream function (2D)|stream function]] can be recycled from [[stream function for a doublet]]:
$$\begin{align*}
\psi_{doublet}(x,z) &=  \frac{Q}{2\pi} \left(\arctan \left(\frac{z }{x+B}\right) - \arctan \left(\frac{z }{x- B}\right)\right) & \theta_{1} &= \arctan \left(\frac{z }{x+ B}\right) & \theta_{2} &= \arctan \left(\frac{z }{x- B}\right)\\
\psi_{doublet}(x,z) &=  \frac{Q}{2\pi} \left(  \theta_{1} - \theta_{2} \right)
\end{align*}$$

Then adding the streamfunction of [[stream function for uniform flow|uniform flow]] in the positive x direction:
$$\begin{align*}
\psi(x,z) &=  \frac{Q}{2\pi} \left(  \theta_{1} - \theta_{2} \right) + U_{\infty} z
\end{align*}$$

Following the same procedure previously used to find the shape of interest (used in [[defining the geometry of an object in a flow#Finding the streamfunction of interest]]), we need to find functions of $u,w$ so that we can get the [[stagnation point]]:
$$\begin{align*}
 V_{x} &=  \frac{\delta \psi}{ \delta z } & V_{z} &=  - \frac{\delta \psi}{ \delta x } 
\end{align*}$$
Thing is doing this for the streamfunction we have would be a major pain in the ass, so (let's just use [[the hero we need but dont deserve|wolfram alpha]]) which will get:
$$\begin{align*}
 V_{x} &=  \frac{\delta \psi}{ \delta z } = U_{\infty}+ \frac{Q}{2\pi}\left( \frac{x+b}{(x+b)^{2}+z^{2}} - \frac{x-b}{(x-b)^{2}+z^{2}} \right) & V_{z} &=  - \frac{\delta \psi}{ \delta x } = \frac{Qz}{2\pi} \left( \frac{1}{(x+b)^{2}+z^{2}} - \frac{1}{(x-b)^{2}+z^{2}} \right) & 
\end{align*}$$
Finding where both equal zero is a bit of a pain analytically, so to simplify we can guess the stagnation point lies on $z=0$ by observation:
$$\begin{align*}
V_{x} = 0 &=  U_{\infty}+ \frac{Q}{2\pi}\left( \frac{x+b}{(x+b)^{2} } - \frac{x-b}{(x-b)^{2} } \right) & V_{z} = 0 &=    \frac{Q0}{2\pi} \left( \frac{1}{(x+b)^{2} } - \frac{1}{(x-b)^{2} } \right)\\
 - \frac{2\pi U_{\infty}}{Q}  &= \frac{x+b}{(x+b)^{2} } - \frac{x-b}{(x-b)^{2} } & &= 0 \\
&...\:\:\text{(math's magic)}\\
x=\pm \sqrt{    b^{2}  + \frac{bQ}{\pi U_{\infty}} }
\end{align*}$$

