---
aliases: [""]
tags: []
---

## Defining the geometry of an object in a flow
### Intro
We know from previous discussions that a streamline is effectively equivalent to a solid boundary in 2D space since mass cannot flow across streamlines. We also know that it is possible to construct complex stream geometrys from [[addition of stream functions]], combining this knowledge: it is possible to create a desired geometry using [[addition of stream functions]] then by treating one of the streamlines as the solid body we want to study we can get the characteristics of the flows interaction with it by looking at the surrounding flow.

### Describing the geometry

#### Creating an object

![[Pasted image 20221110120409.png]]

By adding the streamfunctions of a [[stream function for uniform flow|uniform flow]] and a [[stream function for line source or sink|source]] we can get the following:
![[Pasted image 20221110120539.png]]

#### Finding the streamfunction of interest

We still need to somehow find the value of the [[stream function (2D)|stream function]] which actually defines the green line, since we are taking it to be equivalent to a stationary body we know that it will have a [[stagnation point]] where the flow velocity is normal to the wall. Since the direction of flow and the source clearly oppose each other there is some point left of the origin where velocity is zero, hence using this as the boundary condition we can find the desired [[stream function (2D)|stream function]]:

$$\begin{align*}
&&\psi &= U_{\infty} r \sin\theta + \frac{Q}{2\pi} \theta \\
\frac{\delta \psi}{\delta \theta} &= U_{\infty} r \cos\theta + \frac{Q}{2\pi} &&& \frac{\delta \psi}{\delta r} &= U_{\infty}   \sin\theta 
\end{align*}$$

Then using the equations of velocity from [[stream function (2D)#^a8f4e7|stream function]]:
$$\begin{align*}
 V_{r}=0 &= \frac{1}{r} \frac{\delta \psi}{ \delta \theta } &  V_{\theta} = 0 &= - \frac{\delta \psi}{ \delta r }\\
&=  U_{\infty}   \cos\theta + \frac{Q}{2r\pi} & &= - U_{\infty}   \sin\theta \\
&& \arcsin(0) &= \theta = \pi\\
U_{\infty} &= \frac{Q}{2r\pi}\\
r &= \frac{Q}{2U_{\infty}\pi}
\end{align*}$$
Hence subbing back into streamfunction:
$$\begin{align*}
\psi &= U_{\infty}  \frac{Q}{2U_{\infty}\pi} \sin\pi + \frac{Q}{2\pi} \pi \\
&=   \frac{Q}{2 } 
\end{align*}$$

#### Finding thickness

If we then want to find some property of the shape such as thickness we can use the streamfunction we found, lets try to find $2h$ which describes the maximum thickness of our shape of interest:

![[Pasted image 20221111110435.png]]
$$\begin{align*}
 \psi &= U_{\infty} r \sin\theta + \frac{Q}{2\pi} \theta  & \psi_{SP} &= \frac{Q}{2}\\
1 &= \frac{2U_{\infty}}{Q}  r \sin\theta + \frac{1}{\pi} \theta 
\end{align*}$$
We can see on the graph that $2h$ is found as $x\to \infty$ hence it will be where $r \to \infty$ and $|\theta| \to 0$ so we can apply the $\sin$ small angle approximation:
$$\begin{align*}
1 &= \frac{2U_{\infty}}{Q}  r \theta + \frac{1}{\pi} \theta & h&=r\sin\theta=r\theta\\
1 &= \frac{2U_{\infty}}{Q}  h + \frac{\theta}{\pi}\\
\frac{1-\frac{\theta}{\pi}}{\frac{2U_{\infty}}{Q}} &=  h\\
\frac{Q-\frac{Q\theta}{\pi}}{ 2U_{\infty}} &=  h\\
\text{as }\theta \to 0:\\
\frac{Q }{ 2U_{\infty}} &=  h\\
\end{align*}$$
