---
aliases: [""]
tags: []
---

## Flow over a rotating cylinder
### Stream function
We've already done lots of analysis on [[Flow past a circular cylinder]], but things get interesting once we add a [[stream function for a vortex|vortex]] into the mix:
![[Pasted image 20221112144936.png]]
For convenience we add in the term $\epsilon$ such that the stream function for the stagnation point is zero, since when dealing with stream functions we only really work with the derivative adding any constant to the stream function won't change any outputs, hence we can do this without negative consequence.

Since we know from [[pressure coefficients for a stream function in a potential flow|previous working]] that at $r=R$ the streamfunction passes through the stagnation point and follows this circle, we can write:
$$\begin{align*}
\psi &= V_{\infty} r \sin\theta \frac{1- R^{2}}{r^{2}} + \frac{\Gamma}{2\pi}\ln r + \varepsilon\\
\text{at:}&r=R,\psi=0\\
0 &= V_{\infty} R \sin\theta \frac{1- R^{2}}{R^{2}} + \frac{\Gamma}{2\pi}\ln R + \varepsilon\\
\varepsilon &= - \frac{\Gamma}{2\pi}\ln R\\\\
\therefore \psi &= V_{\infty} r \sin\theta \frac{1- R^{2}}{r^{2}} + \frac{\Gamma}{2\pi}\ln \frac{r}{R}
\end{align*}$$
This is simply a form of the stream function such that at $R=r$, $\psi=0$ for convenience. Depending on how we vary $\Gamma$ ([[circulation]]) we get different results:
![[Pasted image 20221112150117.png]]

### Veloicty
The method to get velocity components is of course the same as done previously making use of the identity of [[stream function (2D)|stream function]]:

$$\begin{align*}
V_{r} &= \frac{1}{r} \frac{\delta\psi}{\delta\theta} & V_{\theta} &= - \frac{\delta\psi}{\delta r}\\
...&\text{wolfram alpha}\\
V_{r} &=  V_{\infty} \cos\theta \left( 1 - \frac{R^{2}}{r^{2}} \right) & V_{\theta} &= - V_{\infty} \sin \theta \left(1 + \frac{R^{2}}{r^{2}}\right) - \frac{\Gamma}{2\pi r}
\end{align*}$$

### Stagnation points
Stagnation points can be found by finding where $|V|=0$ hence if we assume $r=R$:
$$\begin{align*}
 0 &=  V_{\infty} \cos\theta \left( 1 - \frac{R^{2}}{r^{2}} \right) & 0 &= - V_{\infty} \sin \theta \left(1 + \frac{R^{2}}{r^{2}}\right) - \frac{\Gamma}{2\pi r}\\
&... \text{(some algebraic magic)}
\end{align*}$$
$$\begin{align*}
\theta &= \arcsin\left( - \frac{\Gamma}{4\pi RV_{\infty}} \right) & \text{where: }& |\Gamma| \leq 4\pi R V_{\infty}\\
r &= R
\end{align*}$$
We can see that there are values of $\Gamma$ such that there are no stagnation points on the circumference of the circle, this case coincides with when the flow starts to get [[loss of sanity|trippy]]:
![[Pasted image 20221112151419.png]]
From looking at the diagram it can be determined that when $|\Gamma|>4\pi R V_{\infty}$ the stagnation point will lie somewhere on this centre line, aka $\theta= \frac{\pi}{2}$ or $\theta= -\frac{\pi}{2}$ the value $\theta$ will take turns out to depend on whether $\Gamma$ is greater or less than zero (since this determines the direction of rotation) such that for $\Gamma>0,\theta_{st}= -\frac{\pi}{2}$ and $\Gamma<0,\theta_{st}= \frac{\pi}{2}$. Now we can once again solve the veloicty equations to find where the stagnation point is:

$$\begin{align*}
 0 &=  V_{\infty} \cos\theta \left( 1 - \frac{R^{2}}{r^{2}} \right) & 0 &= - V_{\infty} \sin \theta \left(1 + \frac{R^{2}}{r^{2}}\right) - \frac{\Gamma}{2\pi r}\\
&... \text{(some algebraic magic where: }\Gamma=\pm k, \:\:\:\theta= \mp \frac{\pi}{2} )
\end{align*}$$
$$\begin{align*}
\theta &= \pm \frac{\pi}{2} & \text{where: }& |\Gamma| \leq 4\pi R V_{\infty}\\
r &= \mp \frac{\Gamma}{4\pi V_{\infty}} + \sqrt{ \left( \frac{\Gamma}{4\pi V_{\infty}} \right)^{2} - R^{2} } \:\:\: and \:\:\: r = \mp \frac{\Gamma}{4\pi V_{\infty}} - \sqrt{ \left( \frac{\Gamma}{4\pi V_{\infty}} \right)^{2} - R^{2} }
\end{align*}$$

### Lift and drag
#### Pressure coefficient on the surface
If we take the stream function where $\psi=0$, hence $r=R$ then we know that:
$$\begin{align*}
V_{r} &=  V_{\infty} \cos\theta \left( 1 - \frac{R^{2}}{R^{2}} \right) & V_{\theta} &= - V_{\infty} \sin \theta \left(1 + \frac{R^{2}}{R^{2}}\right) - \frac{\Gamma}{2\pi R}\\
  &= 0 & &= - 2 V_{\infty} \sin \theta   - \frac{\Gamma}{2\pi R}
\end{align*}$$
Subbing into the pressure coefficient equation we get:
$$\begin{align*}
 C_{p}  &=  1-\frac{  V_{\theta}^{2} + V_{r}^{2}  }{ V^{2}_{\infty} }\\
 C_{p}  &=  1-\frac{  \left(2 V_{\infty} \sin \theta  + \frac{\Gamma}{2\pi R} \right)^{2}  }{ V^{2}_{\infty} }
\end{align*}$$

#### Drag
This is quite easy, it simply  requires us to integrate over $\theta=0\to 2\pi$ to get drag coefficient:
$$\begin{align*}
D' &= \int_{C} P\times(-\hat{n}\cdot \hat{i})ds & &\to & c_{d}&=   \frac{1}{2R} \int_{C} C_{p}\times(-\hat{n}\cdot \hat{i})ds
\end{align*}$$
Here $\hat{n}$ is the unit vector normal to the surface and $\hat{i}$ is the unit vector in the direction of flow, hence the [[dot product (vectors)|dot product]] of these gets the magnitude of the pressure acting in the direction of the free stream, multiplying by -1 gets against the free stream (drag) and integrating gets this drag over the whole object (net drag), hence the equation seen here. The specifics don't matter much but this becomes:
$$\begin{align*}
c_{d} &= 0
\end{align*}$$
This is interesting :think: there is no drag at all for this body.

#### Lift
The working here is the same as what was done for drag only now we use the unit vector $\hat{j}$ which represents the vector perpendicular to $i$ hence it's perpendicular to the free stream velocity:
$$\begin{align*}
L' &= \int_{C} P\times(-\hat{n}\cdot \hat{j})ds & &\to & c_{l}&=   \frac{1}{2R} \int_{C} C_{p}\times(-\hat{n}\cdot \hat{j})ds
\end{align*}$$
Once again the specifics of solving [[this is doable using current knowledge but loooooooooooong and not needed|don't matter]], but subbing in the equation for $C_{p}$ results in:
$$\begin{align*}
C_{l} &= \frac{\Gamma}{RV_{\infty}}\\
\therefore\:L' &= \frac{1}{2}\rho V^{2}_{\infty}S \frac{\Gamma}{RV_{\infty}} & S &= 2R \\
&= \rho V_{\infty} \Gamma
\end{align*}$$
This equation pretty much implies that in a potential flow lift is a direct product of the interaction between [[circulation]] and the freestream. This is basically the [[magnus effect]] when we are working with real flows:
![[Pasted image 20221112160741.png]]