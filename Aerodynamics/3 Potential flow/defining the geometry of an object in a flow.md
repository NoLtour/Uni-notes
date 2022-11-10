---
aliases: [""]
tags: []
---

## Defining the geometry of an object in a flow
### Intro
We know from previous discussions that a streamline is effectively equivalent to a solid boundary in 2D space since mass cannot flow across streamlines. We also know that it is possible to construct complex stream geometrys from [[addition of stream functions]], combining this knowledge: it is possible to create a desired geometry using [[addition of stream functions]] then by treating one of the streamlines as the solid body we want to study we can get the characteristics of the flows interaction with it by looking at the surrounding flow.

### Creating a object

![[Pasted image 20221110120409.png]]

By adding the streamfunctions of a [[stream function for uniform flow|uniform flow]] and a [[stream function for line source or sink|source]] we can get the following:
![[Pasted image 20221110120539.png]]
We still need to somehow find the value of the [[stream function (2D)|stream function]] which actually defines the green line, since we are taking it to be equivalent to a stationary body we know that it will have a [[stagnation point]] where the flow velocity is normal to the wall. Since the direction of flow and the source clearly oppose each other there is some point left of the origin where velocity is zero, hence using this as the boundary condition we can find the desired [[stream function (2D)|stream function]]:

$$\begin{align*}
\psi &= U_\ing
\end{align*}$$

