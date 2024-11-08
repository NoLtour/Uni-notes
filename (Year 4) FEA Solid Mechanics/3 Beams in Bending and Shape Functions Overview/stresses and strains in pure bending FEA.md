---
aliases:
  - B matrix
tags:
---

## Stresses and strains in pure bending FEA

Although we've discussed finding reaction forces and deformations in [[beam elements in pure bending]], we have no discussion of solving for stress. Recalling previous work [[calculating the deflection of a beam]] and [[engineer's bending theory]]:

$$\begin{align*}
&&&&E &= \frac{\sigma_{xx}}{\varepsilon_{xx}} &&\to& \varepsilon_{xx} &= \frac{\sigma_{xx}}{E}\\
\sigma_{xx} &=  \frac{My}{I} &&\to& \frac{\sigma_{xx}}{y} &=  \frac{M}{I} \\
&&M &=  -EI \frac{\partial^{2}w}{\partial x^{2}} &&\to&   \frac{\sigma_{xx}}{y} &=  -E \frac{\partial^{2}w}{\partial x^{2}} &&\to&   \varepsilon_{xx} &=  -y \frac{\partial^{2}w}{\partial x^{2}}
\end{align*}$$

We have a definition of deflection $w$ from [[beam elements in pure bending]]:

$$\begin{align*}
w(x) &= f_{1}(x) q_{1} + f_{2}(x) q_{2}+ f_{3}(x) q_{3}+ f_{4}(x) q_{4} &&\to& \{w\} &= \begin{pmatrix} f_{1}(x)& f_{2}(x)& f_{3}(x) & f_{4}(x) \end{pmatrix}  \begin{pmatrix} q_{1} \\ q_{2} \\ q_{3} \\ q_{4} \end{pmatrix}
\end{align*}$$

In this form we can easily state the expression for strain:

$$\begin{align*}
\varepsilon_{xx} &=  -y \frac{\partial^{2}w}{\partial x^{2}} &&\to& \varepsilon_{xx} &=  -y\: \frac{\partial^{2}}{\partial x^{2}} \: \{w\}
&&\to& \varepsilon_{xx} &=  -y\: \begin{pmatrix} f''_{1}(x)& f''_{2}(x)& f''_{3}(x) & f''_{4}(x) \end{pmatrix}  \begin{pmatrix} q_{1} \\ q_{2} \\ q_{3} \\ q_{4} \end{pmatrix}
\end{align*}$$

If we then sub in the shape functions, we'll end up with:

$$\begin{align*}
\varepsilon_{xx} &=  -y\: \begin{pmatrix} f''_{1}(x)& f''_{2}(x)& f''_{3}(x) & f''_{4}(x) \end{pmatrix}  \begin{pmatrix} q_{1} \\ q_{2} \\ q_{3} \\ q_{4} \end{pmatrix}  &&\to&

\varepsilon_{xx} &=  -y\: \begin{pmatrix}  -  \dfrac{6}{L^{2}} +  \dfrac{12x}{L^{3}} \\  - \dfrac{4}{L} + \dfrac{6x}{L^{2}} \\  \dfrac{6}{L^{2}} -  \dfrac{12x}{L^{3}} \\ - \dfrac{2}{L} + \dfrac{6x }{L^{2}}  \end{pmatrix}^{T}  \begin{pmatrix} q_{1} \\ q_{2} \\ q_{3} \\ q_{4} \end{pmatrix} &&\to& -y\: \begin{pmatrix}  -  \dfrac{6}{L^{2}} +  \dfrac{12x}{L^{3}} \\  - \dfrac{4}{L} + \dfrac{6x}{L^{2}} \\  \dfrac{6}{L^{2}} -  \dfrac{12x}{L^{3}} \\ - \dfrac{2}{L} + \dfrac{6x }{L^{2}}  \end{pmatrix}^{T}&=  [B]\\\\
\end{align*}$$

This describes local axial strain, we often call this the "B matrix" (creatively named I know). We can then get stress by adding the "D matrix", which in our case is just Youngs modulus:

$$\begin{align*}
\sigma_{x} (x,y) &= [D][B]\{q\} &&\to& \sigma_{x} (x,y) &=-yE\: \begin{pmatrix}  -  \dfrac{6}{L^{2}} +  \dfrac{12x}{L^{3}} \\  - \dfrac{4}{L} + \dfrac{6x}{L^{2}} \\  \dfrac{6}{L^{2}} -  \dfrac{12x}{L^{3}} \\ - \dfrac{2}{L} + \dfrac{6x }{L^{2}}  \end{pmatrix}^{T}  \begin{pmatrix} q_{1} \\ q_{2} \\ q_{3} \\ q_{4} \end{pmatrix} 
\end{align*}$$
