---
aliases: ["single vortex sheet assumption","flow tangency assumption","small camber assumption"]
tags: []
---

## Thin airfoil problem definition

### Single sheet assumption
So we've seen how we assume the airfoil to be 2 sheets from [[vortex sheet strength|the vortex sheet assumption]], thing is since the airfoil is thin these sheets are so close to eachother we can just approximate it using a single sheet with voticity equal to the sum of the top and bottom vortex strength at that point.
![[Pasted image 20221205110857.png]]
We distribute this resultant vortex sheet along the camber line.

### Small camber assumption
To simplify further we assume that due to the airfoil having a small angle of attack, a small thickness and a small camber we can approximate the vortex sheet position with a strait line along the chord instead of along the camber line:
![[Pasted image 20221205111330.png]]
We represent distance along this line using $\xi$, the verticle veloicty $w\approx w'$  due to the smallness of what was mentioned previously

### Freestream velocity approximation
Since we are taking $\alpha$ to be small (using [[I do not have a page on these since they are so easy lol|small angle approximations]]):

$$\begin{align*}
\vec{V}_{\infty} &= V_{\infty} ( \hat{{i}}\cos\alpha + \hat{{k}}\sin\alpha ) & &\to & \vec{V}_{\infty} &\approx V_{\infty} ( \hat{{i}} + \hat{{k}}\alpha ) 
\end{align*}$$


### Flow tangency
Basically this is the assumption that there is no flow normal to the foil:
$$ \vec{V}\cdot\vec{n}=0 $$
So that some effect of the camber line is still taken into account we take the normal relative to the camber line not the chord line. From this we can define vectors for the tangent and normal if we have the gradient of the camber line at some aritrary point along it ($\frac{dz}{dx}$):

![[Pasted image 20221205113255.png]]

Now we just need to work out the velocity at some point along the camber, which will be the sum of freestream and the effect of vorticity then just dot product it with the normal to camber:
$$\begin{align*}
\vec{n} &= \hat{k} - \hat{i} \frac{dz}{dx} & \vec{V} + w \hat{k} &= V_{\infty} ( \hat{{i}} + \hat{{k}}\alpha ) + w \hat{k}\\
&& &= \hat{i}(V_{\infty}) + \hat{k}(V_{\infty} \alpha + w)
\end{align*}$$
$$\begin{align*}
\vec{V}\cdot\vec{n}&= 0\\
( 1\times(V_{\infty}\alpha+w) ) + \left( -\frac{dz}{dx} \times V_{\infty} \right) &= \\
w + V_{\infty} \left(\alpha -\frac{dz}{dx}\right)   &= \\
-V_{\infty} \left(\alpha -\frac{dz}{dx}\right)   &= w
\end{align*}$$
