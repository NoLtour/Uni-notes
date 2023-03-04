---
aliases: ["shear flow"]
tags: []
---

## Calculating shear stress in open sections

### Equation


### Derivation

Lets say instead of a nice closed loop we have some horrible cross section such as:
![[Pasted image 20230304102349.png]]

To calculate the shear stress we can take the equation from [[shear force in a arbitrary symmetric cross section]]:

$$\begin{align*}
\tau_{yx} &=  \frac{1}{t} \int_{A} \frac{d\sigma_{xx}}{dx} \: d A
\end{align*}$$

Then combine it with the equation from [[bending a beam with assymetric cross sections|bending a beam with asymmetric cross sections]]:

$$\begin{align*}
\sigma_{xx}  &= \frac{ (M_{zz} I_{yy} - M_{yy} I_{yz}) y  + (M_{yy} I _{zz} - M_{zz} I_{yz}) z }{I_{yy} I_{zz} - I_{yz}^{2}} \\
\frac{d\sigma_{xx}}{dx}  &= \frac{ (\frac{M_{zz}}{dx} I_{yy} - \frac{M_{yy}}{dx} I_{yz}) y  + (\frac{M_{yy}}{dx} I _{zz} - \frac{M_{zz}}{dx} I_{yz}) z }{I_{yy} I_{zz} - I_{yz}^{2}} \\
  &= \frac{ (Q_{yy} I_{yy} - Q_{zz} I_{yz}) y  + (Q_{zz} I _{zz} - Q_{yy} I_{yz}) z }{I_{yy} I_{zz} - I_{yz}^{2}} \\
\end{align*}$$

$$\begin{align*}
\tau_{yx} &=  \frac{1}{t} \int_{A} \frac{d\sigma_{xx}}{dx} \: d A & &\to & \tau_{yx} &=  \frac{1}{t} \int_{A} \frac{ (Q_{yy} I_{yy} - Q_{zz} I_{yz}) y  + (Q_{zz} I _{zz} - Q_{yy} I_{yz}) z }{I_{yy} I_{zz} - I_{yz}^{2}} \: d A\\
&&&&&=  \frac{1}{t} \frac{1}{I_{yy} I_{zz} - I_{yz}^{2}} \left[ (Q_{yy} I_{yy} - Q_{zz} I_{yz})\int_{A}  y \:dA + (Q_{zz} I _{zz} - Q_{yy} I_{yz}) \int_{A}  z  \: d A \right]\\
&&&& \tau_{yx}  t &=   \frac{(Q_{yy} I_{yy} - Q_{zz} I_{yz}) \bar{y}A + (Q_{zz} I _{zz} - Q_{yy} I_{yz}) \bar{z}A}{I_{yy} I_{zz} - I_{yz}^{2}}  \\
\end{align*}$$

We then let $\tau_{yx}  t=q$ where $q$ is called "shear flow", think of it as the overall shear acting through a 2D slice of the cross section.
