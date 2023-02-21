---
aliases: ["downwash","downwash angle"]
tags: []
---

## Downwash for stability analysis

We know from [[Finite wing theory overview|finite wing theory]] that induced AOA for an elliptic wing is ([[elliptic lift distrobution analysis#^cbb7e1]]):

$$\begin{align*}
\alpha_{i} &= \frac{C_{L}}{\pi A}
\end{align*}$$

Then by slapping [[Oswald efficiency factor]] we can get a more general form:


$$\begin{align*}
\alpha_{i} &= \frac{C_{L}}{\pi A e}
\end{align*}$$

Now consider downwash angle on a tail wing:

![[Pasted image 20230214233247.png]]

What is downwash angle ($\varepsilon$)? Well it's equivilent to [[Prandtls lifting line theory|induced AoA]]:

$$\begin{align*}
\varepsilon &= \frac{C_{L}}{\pi A e}
\end{align*}$$

Then if we also get an equation for lift relative to [[effective AoA on finite wings|effective AOA]] and 2D Cl:

$$\begin{align*}
C_{L} &= C_{l_{\alpha}} \alpha_{eff} \\
&=  a_{0} ( \alpha - \alpha_{0} - \alpha_{i} )
\end{align*}$$

We know $\alpha_{i}\equiv \varepsilon$, hence:

$$\begin{align*}
C_{L} &=  a_{0} \left( \alpha - \alpha_{0} - \frac{C_{L}}{\pi A e} \right)
\end{align*}$$

> ### $$\begin{align*} \varepsilon &= \frac{C_{L}}{\pi A e}\\&=  \varepsilon_{\alpha}(\alpha-\alpha_{0})  \end{align*}$$
> ### $$\begin{align*}C_{L} &=  a_{0} \left( \alpha - \alpha_{0} - \frac{C_{L}}{\pi A e} \right)\end{align*}$$
>> where:
>> $\varepsilon=$  downwash angle on tail
>> $\varepsilon_{\alpha}= \frac{d\varepsilon}{d\alpha} =$  downwash angle change with AOA change
>> $\alpha_{0}=$ no lift angle of main wing
>> $C_{L}=$ 3D [[lift coefficient]]
>> $e=$ [[Oswald efficiency factor]]
>> $A=$ [[wing aspect ratio|aspect ratio]]
>> $a_{0}= \frac{dC_{l}}{d\alpha}=$ [[lift curve slope for a finite wing|airfoils lift curve slope]]

This page is really just recap of aero stuff + getting the equations into the chapter so we can work with em.
