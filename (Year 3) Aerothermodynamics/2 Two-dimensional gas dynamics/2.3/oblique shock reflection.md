---
aliases: [""]
tags: []
---

## Oblique shock reflection
### Setup
Ok so going back to [[intro to engine intake design in supersonic flow]], we can see that it involves lot's of shock reflections. So for intake design we'll have to understand how to calculate these... which is what this is about.

![[Pasted image 20231025110629.png]]

It can be seen that the streamlines for $M_{2}$ will collide with the top surface now that they are inclined, this will result in a secondary [[oblique shocks|oblique shock]]:
- The first oblique shock has [[oblique shock angles|a turning angle]] of $\theta$, by defenition the flow $M_{2}$ will follow this angle. Then apon hitting a "flat" surface it will have a [[oblique shock angles|turning angle]] of $\theta$. Hence both have the same turning angle.
- Although the turning angle is the same the [[oblique shock angles|shock angle]] is not the same, since that is a function of Mach number and $M_{1}\neq M_{2}$

With the outline of the problem established, lets work towards getting $M_{3}$ by starting with $M_2$, assume the following values:
$$\begin{align*}
M_{1} &= 3.6 & \theta &= 10\degree & p_{1} &= 40\text{kPa}
\end{align*}$$

### Solving

Going back to [[oblique shock equations#Equation|solving oblique problems]] we can apply the method described there.

##### Find $\beta$

Practically, we've got to use either [[oblique shock chart]]s or the online calculator, doing this get's you:
$$\begin{align*}
\beta &= 23.9\degree
\end{align*}$$

##### Find $M_{2}$

Can use the equation from [[oblique shock equations#^774680]] or a [[normal shock table]] using the method discussed there (we're using that method):

We'll get $M_{n1}$ using:
$$\begin{align*}
M_{n1} &= M_{1} \sin \beta & &\to & M_{n1} &= 3.6 \sin 23.9\degree\\
&& && &= 1.458
\end{align*}$$

Then looking that up in the normal shock table, get's $M_{n2}$ which is about 0.716. Now to get $M_{2}$ we use the inversion formula from [[oblique shock equations]]:

$$\begin{align*}
M_{2} &= \frac{M_{n2}}{\sin(\beta-\theta)}\\
&= 2.98
\end{align*}$$

##### Find $\phi$
Same method as for $\beta$, recall that [[oblique shock angles|flow turning angle]] is the same $\theta=10\degree$:

$$\begin{align*}
\phi &= 27.5 \degree
\end{align*}$$

##### Find $M_{3}$

Let's use the alternative method, that equation we derived:

$$\begin{align*}
M^{2}_{3}  &= \frac{1}{\sin^{2}(\phi-\theta)}   \frac{(\gamma - 1) M^{2}_{2} \sin^{2} \phi + 2}{2\gamma M^{2}_{2} \sin^{2} \phi - (\gamma - 1)}\\
&= 6.22\\
M_{3} &= 2.49
\end{align*}$$

And that's it, [[yipeee|we found]] $M_{3}$!
 