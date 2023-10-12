---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe how you solve
## Doube integrals with dependent limits
### Why limits matter
So you know how I said that [[double integrals with independent limits|double integrals]] are easy, they only become difficult when limits get fucky well that's what this is about. What it essentially comes down to is the fact that to integrate something you have to fully expand all variables that can be defined interms of the variable your integrating for. For example if you have a function $y(x)$ where $y = x+2$ if you have to integrate $\int xy dx$ then:
$$\begin{align*}
\int xy \cdot dx &\\
\int x(x+2) \cdot dx &\\
\int x^{2}+2x \cdot dx &\\
\frac{x^{3}}{3} + x^{2} & 
\end{align*}$$
It would be wrong to do:
$$\begin{align*}
\int xy \cdot dx &\\
y\int x \cdot dx &\\
y \frac{x^{2}}{2} &\\
\end{align*}$$
This is what I mean by fully expanding all variables that can be defined interms of what's being integrated for, since y can be defined interms of x it must be accounted for. So in this exact same way given the following example:
> Solve:
> $$ V = \int^{x=X}_{x=0} \int^{y=g}_{y=0} yx+1 \cdot dy \cdot dx $$
> where: $g = x^{2}$

Here although y is an independent variable from x you can rewrite the integral as:

$$ \int^{X}_{0} f(x) \cdot dx $$

where: $f(x) = \int^{g}_{0} yx+1 \cdot dy= \int^{x^{2}}_{0} yx+1 \cdot dy$ so by thinking about it that way you can clearly see that integration order matters in these situations. Now if for some reason you wanted to integrate for x first you would need to change the limits so that your dy integral is no longer a function of x. Which isn't possible for this particular example but if there was a way to relate $y$ and $x$ directly then it would be possible.

### Implications of dependent limits
Imagine the following graph as a top down view of a 3D graph, hence it is not currently possible to see the 3rd axis hieght due to the perspective:
![[Pasted image 20220227122916.png]]
If we take the 3rd axis as hieght ($H(x,y) = x^{2} + 2xy$) then this shape is confusing, since with [[double integrals with independent limits]] we only dealt with rectangular shapes (limits such as $\int^{x=1}_{x+0}\int^{y=3}_{y=1}dy\cdot dx$, for this a top down view would be rectangular bound by those lines), the thing is limits on an integration function are actually just lines that define an area inside to integrate for, so it stands to reason that if these lines can be defined as constants then they can also be defined as functions, this is what is done in the diagram above, further as discussed in [[double integrals with dependent limits#Why limits matter|in the previous section]] if you define your limits in this mannor the integration order starts to matter.

Now going back to the graph being used as an example, it's integral would be written as:
$$\begin{align*}
V &= \int^{x=x_{2}}_{x=x_{1}} \int^{y=g_{2}(x)}_{y=g_{1}(x)} x^{2} + 2xy \cdot dy\cdot dx
\end{align*}$$

^dce0e0

Something important to note is if the line $x=x_{2}$ was before the interception point of $g_{2}(x)$ and $g_{1}(x)$:
![[Pasted image 20220227123318.png]]
Then [[double integrals with dependent limits#^dce0e0|the equation described above]] would still work, of course it is also possible to move $x_{1}$ inwards in the same fashion and it would still be valid, this means you can define quite complex geometrys using integral limits.

### Example
> Let $I$ denote the intagral:
> $$ I = \int\int_{A} \frac{x}{y} \cdot dx \cdot dy $$
> Where $A$ is the inside of the triangle bound by lines $x=1,y=2,y=x$
> Expand and simplify $I$

As described previously, limits are just the lines defining some shape in this case:
![[Pasted image 20220227124245.png]]

So we can then write the integral as:
$$\begin{align*}
I &= \int^{x=?}_{x=1} \int^{y=2}_{y=x} \frac{x}{y} \cdot dy\cdot dx
\end{align*}$$
But what do we put as the second limit on $x$ to ensure it's defining the area inside the triangle? What we need is a line that doesn't change the area enclosed, such a line can be found by finding where $y=2$ and $y=x$ intecept and then define a limit that passes through that point. In this case that's quite easy, it's just $x=2$:
![[Pasted image 20220227124959.png]]
Now we can solve the equation, noting that since the limits on y are defined interms of x the dy intagral needs to be solved first:
$$\begin{align*}
I &= \int^{x=2}_{x=1} \int^{y=2}_{y=x} \frac{x}{y} \cdot dy\cdot dx\\
&= \int^{x=2}_{x=1} \left(\int^{y=2}_{y=x} \frac{x}{y} \cdot dy\right)\cdot dx\\
&= \int^{x=2}_{x=1} \left[ x \ln(y) \right]^{y=2}_{y=x}\cdot dx\\
&= \int^{x=2}_{x=1} x\ln(2) - x\ln(x) \cdot dx\\
&= \left[ \frac{x^{2}}{2} \ln\left(2\right) - \frac{x^{2} \ln(x)}{2} + \frac{x^{2}}{4} \right]^{x=2}_{x=1}\\
&= \frac{2^{2}}{2} \ln\left(2\right) - \frac{2^{2} \ln(2)}{2} + \frac{2^{2}}{4} - \frac{1^{2}}{2} \ln\left(2\right) + \frac{1^{2} \ln(1)}{2} - \frac{1^{2}}{4} \\
&= 2 \ln(2) - 2 \ln(2) + 1 - \frac{1}{2} \ln(2) - \frac{1}{4} \\
&= \frac{3}{4} - \frac{1}{2}\ln2 \\
\end{align*}$$
If you want to know how I integrated $x\ln x$ I used [[single-page-integral-table.pdf]], I could marry this pdf [[its so fucking useful|ngl]]. Note that it would have been much simpler to instead use the limits:
$$ I = \int^{y=2}_{y=1} \int^{x=y}_{x=1} \frac{x}{y} \cdot dx\cdot dy $$
Which would have also worked, but I wanted to show the hard way.