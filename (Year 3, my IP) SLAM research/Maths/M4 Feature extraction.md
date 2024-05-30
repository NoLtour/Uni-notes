
Gradients of an image:

$$\begin{align*}
   \begin{bmatrix} I_{x}(x,y) \\ I_{y}(x,y) \end{bmatrix} &= \nabla f(x,y) \:\:(1)
\end{align*}$$

Structure tensor

$$\begin{align*}
M &= \begin{bmatrix} \sum\limits I_{x}^{2} &  \sum\limits I_{x} I_{y} \\ \sum\limits I_{x} I_{y} & \sum\limits I_{y}^{2}  \end{bmatrix} =  \begin{bmatrix} m_{1} & m_{2}\\m_{2} & m_{3} \end{bmatrix} \:\:(2)
\end{align*}$$

Eigenvalues:

$$\begin{align*}
\lambda_{1} &= \frac{m_{1} + m_{3} + \sqrt{ (m_{1} - m_{3})^{2} + 4 m_{2}^{2} }}{2}\:\:(3) &&& \lambda_{2} &= \frac{m_{1} + m_{3} - \sqrt{ (m_{1} - m_{3})^{2} + 4 m_{2}^{2} }}{2}\:\:(4)
\end{align*}$$

R val:
$$\begin{align*}
R &= \lambda_{1} \lambda_{2} - k_{R} (\lambda_{1} + \lambda_{2})^{2}\:\:(5)
\end{align*}$$

NEW

$$\begin{align*}
I_{x} &= \frac{d}{dx} F \:\:(17) &&& I_{y} &= \frac{d}{dy} F \:\:(18) &&&
\end{align*}$$

$$\begin{align*}
M_{1} &= (I_{x}^{\circ2} * K)  \:\:(19)&&& M_{2} &= ([I_{x}\circ I_{y} ]* K)  \:\:(20)&&& M_{3} &= (I_{y}^{\circ2} * K) \:\:(21)
\end{align*}$$

$$\begin{align*}
\Lambda_{1} &= \frac{M_{1} + M_{3} + \sqrt{ (M_{1} - M_{3})^{\circ2} + 4 M_{2}^{\circ2} }}{2}\:\:(22)  &&& \Lambda_{2} &= \frac{M_{1} + M_{3} - \sqrt{ (M_{1} - M_{3})^{\circ2} + 4 M_{2}^{\circ2} }}{2}\:\:(23)
\end{align*}$$

$$\begin{align*}
R &= \Lambda_{1} \Lambda_{2} - k_{R} (\Lambda_{1} + \Lambda_{2})^{\circ2}\:\:(24)
\end{align*}$$

### Gradient hist

$$\begin{align*}
F_{A,ij} &= \begin{cases}
    -1 & \text{if } F_{ij} \:< 0 \\
    1 & \text{else }
\end{cases} \:\:\:\:\: (25)
\end{align*}$$
$$\begin{align*}
F_{K} &= F_{A} * K_{3\times3}\:\:\:\: (26)
\end{align*}$$

$$\begin{align*}
F_{Kdx} &= \frac{d}{dx} F_{K} \:\: (27) &&& F_{Kdy} &= \frac{d}{dy} F_{K} \:\: (28)
\end{align*}$$

$$\begin{align*}
W_{dx} &= \{F_{Kdx,ij} \:|\: c_{x}-R \leq i \leq c_{x}+R, c_{y}-R \leq j \leq c_{y}+R \} \:\: (29)\\
W_{dy} &= \{F_{Kdy,ij} \:|\: c_{x}-R \leq i \leq c_{x}+R, c_{y}-R \leq j \leq c_{y}+R \} \:\: (30) \\
\end{align*}$$

$$\begin{align*}
W_{Cdx} &= W_{dx} * M_{circ} \:\:(31)&&& W_{Cdy} &= W_{dy} * M_{circ} \:\:(32)
\end{align*}$$
$$\begin{align*}
W_{\alpha,ij} &= \text{atan2}( W_{Cdy,ij}, \:W_{Cdx,ij} ) \:\:\: (33)
\end{align*}$$
$$\begin{align*}
W_{m,ij} &= \sqrt{ W_{Cdy,ij}^{2} + W_{Cdx,ij}^{2} } \:\:\: (34)
\end{align*}$$

$$\begin{align*}
\alpha_{cm} &= \text{atan2}\left(  \sum\limits W_{Cdy,ij}^{3}, \: W_{Cdx,ij}^{3}\right) \:\: (35)
\end{align*}$$

eucild

$$\begin{align*}
s &= \sum\limits_{n} (D_{1,n} - D_{2,n})^{2} \:\:\:(36)
\end{align*}$$
$$\begin{aligned}
i_{min} = \underset{i}{\text{argmin}}   \sum\limits_{n} (D_{x,n} - D_{i,n})^{2} \:\: (37)
\end{aligned}$$

