---
aliases: ["Helmholtz theorum","Biot-Savart law","induced veloicty from a infinite vortex filiment","induced veloicty from a semi-infinite vortex filiment"]
tags: []
---

## Helmholtz theorem and Biot-Savart law
### Helmholtz theorum
This states two things:
- A vortex filiment cannot have a defined end, they must either be closed loops or infinitely long
- Circlulation is constant around any cross sectional plane of the filiment

### Biot-Savart law

To find the induced velocity at some point we'll have to rely on the [[biot-savart law]]:

> ### $$\begin{align*} d\vec{V}   &= \frac{\Gamma}{4\pi} \frac{d\vec{l}\times\vec{r}}{|\vec{r}|^{3}}   \end{align*}$$
>> where:
>> $d\vec{V}=$ change in velocity over some small distance
>> $\vec{r}=$ seperation between veloicty sample and filiment (vector is perpendicular to filiment)
>> $\Gamma=$ [[circulation]]
>> $d\vec{l}=$ small vector along vortex filiment
>> ![[Pasted image 20221210141723.png]]

#### Applying it to a strait line
> Find the velocity induced at point $P$ by the section of the vortex filiment $A\to B$:
>![[Pasted image 20221211135333.png]]

To get the velocity at $P$ we need to integrate the [[biot-savart law]] to get the summed effect of the vortex filiment over some section:
$$\begin{align*}
 d\vec{V}   &= \frac{\Gamma}{4\pi} \frac{d\vec{l}\times\vec{r}}{|\vec{r}|^{3}} \\
\vec{V}   & = \frac{\Gamma}{4\pi} \int^{?}_{?} \frac{d\vec{l}\times\vec{r}}{|\vec{r}|^{3}} \\
   & = \frac{\Gamma}{4\pi} \int^{?}_{?} \frac{ -\hat{e}_{z} |d\vec{l}| |\vec{r}| \sin\theta  }{|\vec{r}|^{3}} \\
   & = \frac{\Gamma}{4\pi} \int^{?}_{?} \frac{ -\hat{e}_{z}     \sin\theta  }{ r ^{2}} d l \\
\end{align*}$$

Before we get any further we need to figure out some relationship between $\theta$ and $l$ because else this integrations not getting anywhere:

$$\begin{align*}
 & & l\tan(\pi-\theta) &= h \\
& & l &= \frac{h}{\tan(\pi-\theta)}\\
r \sin(\pi-\theta ) &= h & &= -\frac{h}{\tan(\theta)}\\
r &= \frac{h}{\sin\theta} & dl &= \frac{h}{\sin^{2}\theta } d\theta
\end{align*}$$

Subbing back into the integral:
$$\begin{align*}
\vec{V} & = \frac{\Gamma}{4\pi} \int^{?}_{?} \frac{ -\hat{e}_{z}     \sin\theta  }{ r ^{2}} d l \\
 & = \frac{\Gamma}{4\pi} \int^{?}_{?} \frac{ -\hat{e}_{z}     \sin\theta  }{ \left(\frac{h}{\sin\theta}\right) ^{2}} \frac{h}{\sin^{2}\theta } d\theta\\
  & = -\hat{e}_{z}\frac{\Gamma}{4h\pi} \int^{\theta_{2} }_{\theta_{1}}   \sin\theta     d\theta\\
  & =  \hat{e}_{z}\frac{\Gamma}{4h\pi} (\cos\theta_{2}- \cos\theta_{1})  
\end{align*}$$
Here $\theta_{1}$ and $\theta_{2}$ are simply the clockwise angle between the vortex filiment and the line connecting to $P$, if we take the limit to infinity then we can calculate the total velocity due to the influence of the entire filiment:
$$\begin{align*}
\theta_{2} &= \pi & \theta_{1}&= 0
\end{align*}$$
$$\begin{align*}
\vec{V}_{\text{infinite}} & =  \hat{e}_{z}\frac{\Gamma}{4h\pi} (\cos\pi- \cos0)\\
 & =  \hat{e}_{z}\frac{\Gamma}{4h\pi} (-1- 1) \\
 & = - \hat{e}_{z}\frac{ \Gamma}{2h\pi}
\end{align*}$$

Something intresting to note is that this equation is identical to the [[stream function for a vortex#^c7a30d|vortex velocity equation from potential flow]], which makes sense.

It's also clear that if we have a semi-infinite fililement (cut in half) so one theta is $\pi/2$ then it's just half the veloicty:
$$\begin{align*}
 \vec{V}_{\text{semi infinite}}  & = - \hat{e}_{z}\frac{ \Gamma}{4h\pi}
\end{align*}$$

^568c65



