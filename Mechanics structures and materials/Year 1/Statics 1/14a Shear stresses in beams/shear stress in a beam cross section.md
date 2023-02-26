---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you find
## Shear stress in a beam cross section
### Equations

> ### $$\sigma_{xy} = \frac{Q}{Ib} \int^{0}_{A_s} y \cdot dA$$ 
> ### $$ \sigma_{xy} = \frac{Q}{Ib} A_s y_c $$ 
> ### $$ \sigma_{xy} = \sigma_{yx} $$ 
>> where:
>> $=$ 
>> $=$
>> $=$


### Proof
#### Getting expressions for the left and right sides
To find the shear stress at a specific point we are going to have to do some maeth, consider the following:
![[Pasted image 20211207232317.png]]
You can see that:
$$\begin{align*}
M_{left} &= M & M_{right} &= M + \frac{dM}{dx}dx 
\end{align*}$$


#### Determining local stresses
Now remember how we showed in previous notes that $Q$ at any point along a beam could be expressed by starting from one side and moving to the other (see [[method for constructing shear force and bending moment diagrams]]), basically we are going to employ a simular method to calculate the sum of the shear forces on a cut face starting from the bottom:
![[Pasted image 20211207233037.png]]

First lets use this diagram and the previous section to find expressions for the stresses at given points on the faces. We know that the stress at a given point along the face is given in [[engineer's bending theory]]:
$$\begin{align*}
\sigma_{xx} = \frac{My}{I} 
\end{align*}$$

So we can determine the left and right stresses:
$$\begin{align*}
Left : \sigma_{xx} &= \frac{My}{I} & Right: \sigma_{xx}+ \frac{\Delta \sigma_{xx}}{\Delta x} dx= \frac{\left(M+ \frac{dM}{dx} dx\right) y}{I}
\end{align*}$$
Also note that $M$ is a function of x, as it varys along the length of the beam.

Now if we consider how these equations look on a diagram:
![[Pasted image 20211207234541.png]]
We can see that the difference in stresses would resault in non equalibrium conditions, hence we introduce $\sigma_{xy}$ to balence the internal forces hence:
$$\begin{align*}
left&\: \: :\: right\\
\int (\sigma_{xx})\cdot dA + (\sigma_{xy}\times bdx) &= \int \left(\sigma_{xx}+ \frac{\Delta \sigma_{xx}}{\Delta x} dx\right)\cdot dA\\
\end{align*}$$
The integration is due to the basic fact that $\sigma=F/A$ and when finding equalibrium we use forces.

Now drawing the diagram 3D:
![[Pasted image 20211207235231.png]]

$$\begin{align*}
\int^{0}_{A_s} (\sigma_{xx})\cdot dA + (\sigma_{xy} \times bdx) &= \int^{0}_{A_s} \left(\sigma_{xx}+ \frac{\Delta \sigma_{xx}}{\Delta x} dx\right)\cdot dA\\
 \sigma_{xy} \times bdx &= \int^{0}_{A_s} \left(\frac{\Delta \sigma_{xx}}{\Delta x} dx\right)\cdot dA\\
 \sigma_{xy} \times bdx &= dx \int^{0}_{A_s} \left(\frac{\Delta \sigma_{xx}}{\Delta x} \right)\cdot dA\\
 \sigma_{xy} &= \frac{1}{b} \int^{0}_{A_s} \left(\frac{\Delta \sigma_{xx}}{\Delta x} \right)\cdot dA & \sigma_{xx} &= \frac{My}{I} \\
& & \frac{\Delta \sigma_{xx}}{\Delta x} &= \frac{dM}{dx}\frac{y}{I}\\
 \sigma_{xy} &= \frac{1}{b} \int^{0}_{A_s} \frac{dM}{dx}\frac{y}{I}\cdot dA
\end{align*}$$
We also know that $\frac{dM}{dx} = Q$ from [[proof of the differential relationship between load, shear force and bending moment]]:
$$\begin{align*}
 \therefore \sigma_{xy} &= \frac{1}{b} \int^{0}_{A_s} Q \frac{y}{I}\cdot dA \\
\sigma_{xy} &= \frac{Q}{Ib} \int^{0}_{A_s} y \cdot dA
\end{align*}$$
This is useful, but so far we have been using $y$ which represents the top of our focused section, if we want it relative to the ceteroid of our focused section (as shown below):

![[Pasted image 20211208102702.png]]

We get the form:

$$\begin{align*}
\sigma_{xy} &= \frac{Q}{Ib} A_s y_c 
\end{align*}$$

