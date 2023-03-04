---
aliases: [""]
tags: []
---

## Shear force in a arbitrary symmetric cross section

### Equation

> Generic case:
> ### $$\begin{align*} \tau_{yx} &=  \frac{Q_{yy}}{ I_{zz}} \int_{A} \frac{y}{t}  \: d A \end{align*}$$
> Rectangular case:
> ### $$\begin{align*} \tau_{yx} &= \frac{Q_{yy}}{2I_{zz}} \left(\frac{h^{2}}{4} - y^{2}\right)  \end{align*}$$
> ### $$\begin{align*} \frac{ Q_{y} }{ th } &= \bar{\tau}_{xy} &&& \tau_{xy,max} &= 1.5 \bar{\tau}_{xy} \end{align*}$$
>> where:
>> $\tau_{yx}=$ shear force in the $yx$ plane
>> $Q_{yy}=$ shear force acting in the pure $y$ direction
>> $I_{zz}=$ [[second moment of area]]
>> $t=$ thickness of section
>> $A=$ cross sectional area 
>> $\bar{\tau}_{xy}=$ average shear force in the $yx$ plane
>> ${\tau}_{xy,max}=$ max shear force in the $yx$ plane
>> $h=$ height of the rectangular cross section
>> ![[Pasted image 20230303203315.png]]


### Proof

Ok so lets take a lil slice from a big beam, which is $x$ away from some refrence and $\delta x$ long:
![[Pasted image 20230303203200.png]]

The total shear acting on the upper surface of this element will be equal to the shear stress times the area on the top:
![[Pasted image 20230303203315.png]]

Giving the equation:
$$\begin{align*}
Q_{yx} &= \tau_{yx} t \: \delta x
\end{align*}$$
Where $t$ is thickness.

Then consider the forces acting on this section, you've got the shear force along the top and then the tensile/compressive stress acting on each side:

![[Pasted image 20230303203512.png]]

For this thing to be in equilibrium (only considering $x$ direction) we'll need these forces to sum to zero:

$$\begin{align*}
Q_{yx} &= \sigma_{xx}(x+\delta x) \: \delta A - \sigma_{xx}(x) \: \delta A\\
\tau_{yx} t \: \delta x &= \sigma_{xx}(x+\delta x) \: \delta A - \sigma_{xx}(x) \: \delta A\\
\end{align*}$$

This element is being considered from the edge, if we replace $\delta A$ with $dA$ and let $\delta x \to 0$ (aka $\delta x \to dx$) we get something that looks like an integration problem:

$$\begin{align*}
\tau_{yx} t \: \delta x &= \sigma_{xx}(x+\delta x) \: \delta A - \sigma_{xx}(x) \: \delta A & &\to & \tau_{yx} t \: d x &= \sigma_{xx}(x+d x) \: d A - \sigma_{xx}(x) \: d A\\
&& && \tau_{yx} t \: d x &= (\sigma_{xx}(x+d x) - \sigma_{xx}(x)) \: d A\\
&& && && \sigma_{xx}(x+d x) - \sigma_{xx}(x) &= d\sigma_{xx}\\
&& && \tau_{yx} t \: d x &=  d\sigma_{xx} \: d A\\
&& && \tau_{yx} &= \frac{1}{t} \int_{A} \frac{d\sigma_{xx}}{dx} \: d A\\
\end{align*}$$

So the shear stress at the top of some area from the edge of the cross section is the area integral of the point $\frac{d\sigma_{xx}}{dx}$ (the rate of change of tensile stress along the beams length). This is assuming that the stress along the thickness of the beam are constant.

Then by substituting the equation from [[engineer's bending theory]] we can get the following form:

$$\begin{align*}
&& \sigma_{xx} &= \frac{M_{z}y}{I_{z}}\\
&& d\sigma_{xx} &= \frac{y}{I_{z}} dM_{z}\\
\tau_{yx} &= \frac{1}{t} \int_{A} \frac{d\sigma_{xx}}{dx} \: d A & &\to & \tau_{yx} &=  \frac{1}{t I_{z}} \int_{A} y \frac{ dM_{z}}{dx} \: d A\\
\end{align*}$$

Then recalling [[basic properties shear force and bending moment graphs|this relationship between shear force and moments]] $\frac{dM_{z}}{dx} = Q_{y}$ we can sub this into the equation above and get our final form:

$$\begin{align*}
\tau_{yx} &=  \frac{Q_{y}}{t I_{z}} \int_{A}y  \: d A\\
 &=  \frac{Q_{y}A\bar{y}}{t I_{z}}\\
\end{align*}$$

### Rectangular case

![[Pasted image 20230303210217.png]]

K let's try and figure out what this equation means by using a rectangular beam example, $dA=t\:dy$ so subbing that in:

$$\begin{align*}
\tau_{yx} &=  \frac{Q_{y}}{t I_{z}} \int_{A}y  \: d A\\
 &=  \frac{Q_{y}}{t I_{z}} \int_{\frac{h}{2}}^{y} y t \: d y\\
 &= \frac{Q_{y}}{ I_{z}} \left[\frac{y^{2}}{2}\right]_{\frac{h}{2}}^{y}\\
&...\\
\tau_{yx} &= \frac{Q_{y}}{2I_{z}} \left(\frac{h^{2}}{4} - y^{2}\right) 
\end{align*}$$

This tells us that (in a rectangular case) interlayer shear will be maximum at the centre and decay in a parabola, being zero at the edges:

![[Pasted image 20230303210739.png]]

It then becomes trivial to derive mean shear using properties of a paraballa and the [[proof of second moment of area of a rectangle|equation for second moment of area for a rectangle]]:

$$\begin{align*}
\tau_{xy,max} &= 1.5 \bar{\tau}_{xy}\\
\frac{Q_{y} h^{2}}{8 I_{z}} &= & I_{z} &= \frac{th^{3}}{12}\\
\frac{3 Q_{y} }{2 th } &= \frac{3}{2} \bar{\tau}_{xy}\\
\frac{ Q_{y} }{ th } &= \bar{\tau}_{xy}
\end{align*}$$

You may have noticed that it is [[that is because it is|seemingly arbitrary]] when I use $\to$ to make substitutions/transformations clearer compared to just spreading working over multiple lines and there is no consistent format in how I do it.