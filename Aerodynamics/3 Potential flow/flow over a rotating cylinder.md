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

### Pressure coefficient

The method to get velocity components is of course the same as done previously making use of the identity of [[stream function (2D)|stream function]]:

$$\begin{align*}
V_{r} &= \frac{1}{r} \frac{\delta\psi}{\delta\theta} & V_{\theta} &= - \frac{\delta\psi}{\delta r}\\
...&\text{wolfram alpha}\\
V_{r} &=  V_{\infty} \cos\theta \left( 1 - \frac{R^{2}}{r^{2}} \right) & V_{\theta} &= - V_{\infty} \sin \theta \left(1 + \frac{R^{2}}{r^{2}}\right) - \frac{\Gamma}{2\pi r}
\end{align*}$$

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
From looking at the diagram it can b
