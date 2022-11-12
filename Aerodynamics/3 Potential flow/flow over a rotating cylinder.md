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
V_{r} &= \frac{1}{r} \frac{\delta\psi}{\delta\theta} & V_{\theta} &= - \frac{\delta\osu}{\delta r}\\
...&\text{}
\end{align*}$$

