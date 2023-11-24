---
aliases: [""]
tags: []
---

## Critical Mach number pressure

### Derivation
  
Making use of [[supersonic flow properties equations]]:

$$\begin{align*}
 &&\frac{p_{0}}{p} &= \left(1 + \frac{\gamma-1}{2} Ma^{2}\right)^\frac{\gamma}{\gamma-1} \\
\frac{p}{p_{\infty}} &= \frac{\frac{p_{0}}{p_{\infty}}}{\frac{p_{0}}{p} } 
& &\to & \frac{p}{p_{\infty}} &= \frac{ \left(1 + \frac{\gamma-1}{2} Ma_{\infty}^{2}\right)^\frac{\gamma}{\gamma-1} }{  \left(1 + \frac{\gamma-1}{2} Ma^{2}\right)^\frac{\gamma}{\gamma-1}  } 
& &\to & \frac{p}{p_{\infty}} &= \left( \frac{ 1 + \frac{\gamma-1}{2} Ma_{\infty}^{2} }{   1 + \frac{\gamma-1}{2} Ma^{2}  }   \right)^\frac{\gamma}{\gamma-1}
\end{align*}$$

(Don't forget that this particular supersonic flow equation assumes [[isentropic process|isentropic]] relations)

By definition [[2D CFD for supersonic airfoil examples|critical Mach number]] occurs when the local Mach number is 1 because the free stream is at $M_{crit}$, using this in [[pressure coefficient]]:

$$\begin{align*}
&&\frac{p}{p_{crit}} &= \left( \frac{ 1 + \frac{\gamma-1}{2} Ma_{crit}^{2} }{   1 + \frac{\gamma-1}{2}   }   \right)^\frac{\gamma}{\gamma-1}\\
C_{p} &=   \frac{2}{\gamma M^{2}_{\infty}} \left(\frac{p}{p_{\infty}} - 1\right) & &\to &
C_{p} &=   \frac{2}{\gamma M^{2}_{crit}} \left(  \left( \frac{ 1 + \frac{\gamma-1}{2} Ma_{crit}^{2} }{   1 + \frac{\gamma-1}{2}   }   \right)^\frac{\gamma}{\gamma-1} - 1\right)
\end{align*}$$


This can then be subbed into the [[Prandtl-Glauert transformation]] of the pressure coefficient for working with high speed potential flows:

$$\begin{align*}
C_{p} &=  \frac{C_{p0}}{\sqrt{1-M_{\infty}^{2}}} 
& &\to & \frac{2}{\gamma M^{2}_{crit}} \left(  \left( \frac{ 1 + \frac{\gamma-1}{2} Ma_{crit}^{2} }{   1 + \frac{\gamma-1}{2}   }   \right)^\frac{\gamma}{\gamma-1} - 1\right) &=  \frac{C_{p0}}{\sqrt{1-M_{crit}^{2}}} 
\end{align*}$$

Now if we find where on our shape the lowest $C_{p0}$ is, we can use that value to determine the [[2D CFD for supersonic airfoil examples|critical Mach number]] for that shape!

That being said, looking at that equation.... good luck rearranging for $M_{crit}$, this is where iterative method's come in lmao. 

### Example
Lazy:

![[Pasted image 20231123220342.png]]

