---
aliases: [""]
tags: []
---

## Fundemental equation of thin aerofoil theory
### The equation we care about

> ### $$\begin{align*} V_{\infty} \left(\alpha -\frac{dz}{dx}\right) &= \frac{1}{2\pi}\int^{\pi}_{0} \frac{\gamma(\theta) \sin\theta }{\cos \theta - \cos\theta_{0}} d\theta  \end{align*}$$
> ### $$\begin{align*}\xi &= \frac{c}{2} (1-\cos \theta) & x &= \frac{c}{2} (1-\cos \theta_{0})\end{align*}$$
>> where:
>> $\theta=$  dummy variable stand in for $\xi$ 
>> $\theta_{0}=$ dummy variable stand in for $x$
>> $x=$ a position along the chord hence $0\leq x \leq c$ 
>> $\xi=$ position along the chord for a constant $x$ (used during integration)
>> $V_{\infty}=$ freestream velocity
>> $\frac{dz}{dx}=$ the gradient of the mean camber
>> $\alpha=$ angle of attack
>> $\gamma=$ [[vortex sheet strength]]

### Cartesian derivation
![[Pasted image 20221205115933.png]]
If we want to find the induced velocity $w$ at some point along the chord then we can derive it using the equation of induced velocity from [[vortex sheet strength#Induced velocity from the vortex sheet|induced velocity from the vortex sheet]]:
$$\begin{align*}
dV_{\theta} &=  - \frac{\gamma  ds }{2\pi r}
\end{align*}$$
We just need to substitute in variables which are appropriate for the situation in this case:
$$\begin{align*} 
dV_{\theta} &=  - \frac{\gamma  ds }{2\pi r} & &\to & dw &= - \frac{\gamma(\xi)}{2\pi(x-\xi)} d\xi
\end{align*}$$
This can then be integrated from $\xi=0 \to \xi=c$:
$$\begin{align*}
w &= - \frac{1}{2\pi} \int^{c}_{0} \frac{\gamma(\xi)}{x-\xi} d\xi
\end{align*}$$

Then by substituting in the equation of $w$ from [[thin airfoil problem definition#Flow tangency|flow tangency assumption]] we get the fundemental equation of thin aerofoil theory (in a really [[aka the useless form|hard to use]] form):
$$\begin{align*}
V_{\infty} \left(\alpha -\frac{dz}{dx}\right) &= \frac{1}{2\pi} \int^{c}_{0} \frac{\gamma(\xi)}{x-\xi} d\xi
\end{align*}$$

^75d590

### Angular domain version
Basically the cartesian one is a pain in the ass to calculate so we are going to introduce some equations which can be used to convert the equation into an angular version interms of some new dummy variables $\theta$ and $\theta_{0}$:
$$\begin{align*}
&& \xi &= \frac{c}{2} (1-\cos \theta) & x &= \frac{c}{2} (1-\cos \theta_{0})\\
&& \frac{d\xi}{d\theta} &= \frac{c}{2}\sin\theta
\end{align*}$$
Subbing these into the cartesian integration bit of the equation:
$$\begin{align*}
\int^{c}_{0} \frac{\gamma(\xi)}{x-\xi} d\xi &= \int^{\pi}_{0} \frac{\gamma(\theta)}{\frac{c}{2}(1-cos\theta_{0})-\frac{c}{2}(1-cos\theta)} \frac{d\xi}{d\theta}d\theta \\
&= \int^{\pi}_{0} \frac{\gamma(\theta)}{\frac{c}{2}(1-cos\theta_{0})-\frac{c}{2}(1-cos\theta)} \frac{c}{2} \sin\theta \: d\theta \\
&...\\
&= \int^{\pi}_{0} \frac{\gamma(\theta) \sin\theta }{\cos \theta - \cos\theta_{0}} d\theta
\end{align*}$$
Which can be substituted into [[fundemental equation of thin aerofoil theory#^75d590|the cartesian form of the equation]] to get our final angular form:

$$\begin{align*}
V_{\infty} \left(\alpha -\frac{dz}{dx}\right) &= \frac{1}{2\pi} \int^{c}_{0} \frac{\gamma(\xi)}{x-\xi} d\xi & &\to & V_{\infty} \left(\alpha -\frac{dz}{dx}\right) &= \frac{1}{2\pi}\int^{\pi}_{0} \frac{\gamma(\theta) \sin\theta }{\cos \theta - \cos\theta_{0}} d\theta
\end{align*}$$
Due to the many identities that exist for solving trigometric integrations this form of the equation is much more convenient to integrate!