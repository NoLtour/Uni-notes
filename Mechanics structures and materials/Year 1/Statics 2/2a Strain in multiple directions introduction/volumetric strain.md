---
aliases: ["strains in 3D"]
tags: ["Question","QFormat3"]
---

#### Whats the equation for
## Volumetric strain
### Main bit
If we consider some material element, and define it's strain in 3D:

![[Pasted image 20220213094856.png]]

We can then use this with the following equation to find volumetric strain, assuming that the strains are small:

> ### $$\varepsilon_{V} =\varepsilon_{xx}+ \varepsilon_{yy} + \varepsilon_{zz} $$ 
>> where:
>> $\varepsilon_{V}= \frac{\Delta V}{V_{0}} =$ [[volumetric strain|volumetric strain]]
>> $\varepsilon_{xx},\varepsilon_{yy},\varepsilon_{zz}=$ strain in each axis

### Proof

If we start with it's strain in the x,y,z directions:

$$\begin{align*}
\varepsilon_{xx} &= \frac{\Delta L_{x}}{L_{x0}} & \varepsilon_{yy} &= \frac{\Delta L_{y}}{L_{y0}} & \varepsilon_{zz} &= \frac{\Delta L_{z}}{L_{z0}} 
\end{align*}$$

Now if we want some measure of volumetric strain, we can use these strains to calculate that:

$$\begin{align*}
\varepsilon_{V} &= \frac{\Delta V}{V_{0}} & V_{0} &= L_{x0} L_{y0} L_{z0}\\
 &= \frac{ V - V_{0} }{L_{x0} L_{y0} L_{z0}}\\
& = \frac{ V - L_{x0} L_{y0} L_{z0} }{L_{x0} L_{y0} L_{z0}} & V &= ( L_{x0} + \Delta L_{x})( L_{y0} + \Delta L_{y})( L_{z0} + \Delta L_{z})\\
& & &= L_{x0}L_{y0}L_{z0}( 1 + \varepsilon_{xx})( 1 + \varepsilon_{yy})( 1 + \varepsilon_{zz})\\
& & &= L_{x0}L_{y0}L_{z0}( 1+ \varepsilon_{xx} + \varepsilon_{zz} + \varepsilon_{yy} + \varepsilon_{xx}\varepsilon_{yy} + \varepsilon_{xx}\varepsilon_{zz} + \varepsilon_{yy}\varepsilon_{zz} + ... )\\
&& & \varepsilon\:is\:small\:\therefore\varepsilon\times\varepsilon\:is\:negligible\therefore \varepsilon + \varepsilon\varepsilon \approx \varepsilon \\
&&&= L_{x0}L_{y0}L_{z0}( 1+\varepsilon_{xx}+ \varepsilon_{yy} + \varepsilon_{zz} )\\
& = \frac{ L_{x0}L_{y0}L_{z0}(1+ \varepsilon_{xx}+ \varepsilon_{yy} + \varepsilon_{zz} ) - L_{x0} L_{y0} L_{z0} }{L_{x0} L_{y0} L_{z0}}\\
& = \frac{ (1+ \varepsilon_{xx}+ \varepsilon_{yy} + \varepsilon_{zz} ) - 1 }{1}\\
&=\varepsilon_{xx}+ \varepsilon_{yy} + \varepsilon_{zz}
\end{align*}$$