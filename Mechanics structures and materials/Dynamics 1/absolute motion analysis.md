---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe
## Absolute motion analysis
### Intro
Basically this is just when you have one or more [[rigid body|rigid bodies]] and create a bunch of equations relating how variables describing their motion/position. 

By creating a bunch of equations to describe how things move relative to each other it then becomes possible to find constraints on movement which has lots of uses:
- Calculating part dimensions necessary to allow movement
- Determining range of motion
- Assessing forces acting on components

### Basic wheel
Really simple example, a wheel that doesn't slip:
![[Pasted image 20220427111552.png]]
An equation can easily be defined that relates the position of $\underline{G}$ and the rotation of $\theta$.
$$\begin{align*}
s_{G} &= r\theta 
\end{align*}$$
It is then possible to also derive equations for velocity and acceleration:
$$\begin{align*}
v_{g} &= r\dot{\theta} \\
a_{g} &= r\ddot{\theta} 
\end{align*}$$

### Window
Here is a more complex problem where multiple parts are moving together:
> ![[Pasted image 20220427113754.png]]
> Get an equation that describes the $\theta$ in terms of $s$. Then get an expression describing the absolute position of the end point of the window.

This is quite simple to solve when you realise the motion is basically just a triangle:
![[Pasted image 20220427114023.png]]
So you can use the cosine rule $a^{2}=b^{2}+c^{2}-2bc\cos A$ so yeah ezz:
$$\begin{align*}
(P+s)^{2} &= H^{2} + (W-E)^{2} - 2 H (W-E) \cos \theta\\
 \frac{H^{2} + (W-E)^{2} - (P+s)^{2}}{2 H (W-E)} &= \cos \theta\\
 \cos^{-1} \left(\frac{H^{2} + (W-E)^{2} - (P+s)^{2}}{2 H (W-E)}\right) &= \theta
\end{align*}$$
The endpoint of the window is basic trig:
$$\begin{align*}
\begin{pmatrix} x_{E} \\ y_{E} \end{pmatrix} &= \begin{pmatrix} W\cos\theta \\ W\sin\theta \end{pmatrix}
\end{align*}$$