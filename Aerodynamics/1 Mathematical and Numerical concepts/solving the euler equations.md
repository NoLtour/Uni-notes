---
aliases: [""]
tags: []
---

## Solving the [[euler equations for inviscid and incompressible flow|euler equations]]

These equations are still too complex to be solved analytically so we simplify them. (yes even further)

[[putting this away since I dont know why its needed|ignore]]

### Assuming irrotational flow

Start by assuming the flow is irrotational [[curl of a vector|vorticity]] is zero:

$$\begin{align*}
0&=\left(\frac{\delta V_{y}}{\delta x} - \frac{\delta V_{x}}{\delta y} \right) \hat{e}_{z}\\
\frac{\delta V_{y}}{\delta x} &= \frac{\delta V_{x}}{\delta y}
\end{align*}$$

Now we can take [[momentum balance in inviscid incompressible flow#^da19ae|these equations]] and sub into them:
$$\begin{align*}
V_{x} \frac{\delta V_{x}}{\delta x} + V_{y} \frac{\delta V_{x}}{\delta y} &= - \frac{1}{\rho} \frac{\delta p}{\delta x}  & V_{x} \frac{\delta V_{y}}{\delta x} + V_{y} \frac{\delta V_{y}}{\delta y}  &= - \frac{1}{\rho} \frac{\delta p}{\delta y}\\
V_{x} \frac{\delta V_{x}}{\delta x} + V_{y} \frac{\delta V_{y}}{\delta x} &= - \frac{1}{\rho} \frac{\delta p}{\delta x}  & V_{x} \frac{\delta V_{x}}{\delta y} + V_{y} \frac{\delta V_{y}}{\delta y}  &= - \frac{1}{\rho} \frac{\delta p}{\delta y}\\
p + \frac{1}{2} \rho( V_{x}^{2}+ V_{y}^{2}  ) &= f(y) & p + \frac{1}{2} \rho( V_{x}^{2}+ V_{y}^{2}  ) &= g(x)\\
f(y) &= g(x)
\end{align*}$$

The only way that the unkown functions $f(y)$ and $g(x)$ can be equal is if they are just equal to some constant, hence:
$$p + \frac{1}{2} \rho( V_{x}^{2} +V_{y}^{2}  )  =C$$
Here there is nothing linking the equation to a specific streamline, which means that in a irrotational flow [[Bernouillis equation]] (ignoring gravity) the bernoulli constant is the same everywhere.
