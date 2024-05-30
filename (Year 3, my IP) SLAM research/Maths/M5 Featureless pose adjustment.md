
Windows are masked according to the certainty present in each
$$\begin{align*}
M_{cert} &= \text{abs}(F_{r} \circ F_{t}) \:\: (38) \\\\
W_{r} &= F_{r}^{\circ 3} \circ M_{cert}\:\: (39) &&& W_{t} &= F_{t}^{\circ 3} \circ M_{cert}\:\: (40)\\

\end{align*}$$
Convolution (discrete):



Error window is extracted:


Interest mask, representing the region where both overlap:
$$\begin{align*}
M_{overlap,ij} &= (W_{r,ij} > 0) \land (W_{t,ij} > 0)\:\:(41)
\end{align*}$$
Kernels are constructed:
$$\begin{align*}
K_{dx} &= \begin{bmatrix} -1 & -1 & ... & -1 & 0 & 1 & ... & 1 & 1 \end{bmatrix} \:\: (42)&&& K_{dy} &= K_{dx}^{T}\:\:(43)\\
\end{align*}$$
Scaling multiplier:
$$\begin{align*}
l &= \min\left( \sum  [W_{r} \circ (W_{r} >0)],\:\: \sum  [W_{t} \circ (W_{t} >0)]  \right) \:\:(44)
\end{align*}$$

Convolution:

$$\begin{align*}
E_{dx} &= [(E_{dif} \:*\: K_{dx} ) \circ M_{overlap}]\: \frac{k_{x}}{l} \:\:(45)\\

E_{dy} &= [(E_{dif} \:*\: K_{dy} ) \circ M_{overlap}]\: \frac{k_{y}}{l}\:\:(46)\\
\end{align*}$$

total error:
$$\begin{align*}
e_{x} &= \sum\limits E_{dx}\:\:(47) &&& e_{y} &= \sum\limits E_{dy} \:\:(48)\\

\end{align*}$$

arrays for x and y, given in real distances and with SOMETHING as origin:

$$\begin{align*}
X_{ij} &=  \\
Y &= 
\end{align*}$$

Regions of high dx and dy errors are found


Separation from origin^2, capped at k_minSep = 0.1
$$\begin{align*}
S_{ij} &= \max( X_{ij}^{2} + Y_{ij}^{2} , k_{minSep}) \:\: (53) \\
\end{align*}$$
$$\begin{align*}
T_{x} &= Y\oslash S\:\: (54) &&& T_{y} &= X\oslash S\:\: (55)\\
\end{align*}$$

Angular error

$$\begin{align*}
E_{\alpha} &= T_{x} \circ E_{dx} + T_{y} \circ E_{dy} \:\:(56)
\end{align*}$$

This is bad because reasons, a mask is applied to remove bad

$$\begin{align*}
M_{edx,ij} &= \begin{cases}
    1 & \text{if } E_{dx,ij} \:!= 0 \\
    0 & \text{else }
\end{cases} \:\: (58)\\\\
M_{edy,ij} &= \begin{cases}
    1 & \text{if } E_{dy,ij} \:!= 0 \\
    0 & \text{else }  
\end{cases}\:\: (59)\\
\end{align*}$$
So now:
$$\begin{align*}
E_{\alpha} &= T_{x} \circ \left[E_{dx} - M_{edx} \left(  \frac{e_{x}}{\sum\limits M_{edx}} \right) \right] + T_{y} \circ \left[E_{dy} - M_{edy} \left(  \frac{e_{y}}{\sum\limits M_{edy}} \right) \right] \:\: (60)
\end{align*}$$
$$\begin{align*}
e_{\alpha} &= k_{\alpha}\sum\limits E_{\alpha} \:\: (57)
\end{align*}$$

local translation error vector:
$$\begin{align*}
v_{le} &= \begin{bmatrix} e_{lx}\\e_{ly} \end{bmatrix} \:\:(49) &&& t_{c} &=\begin{bmatrix} y/R \\ x/R\end{bmatrix} \:\:(50) &&& e_{l\alpha} &= \frac{v_{le}\cdot t_{e}}{R} \:\:(51)
\end{align*}$$

$$\begin{align*}
e_{l\alpha} &= e_{lx} \frac{y}{R^{2}} + e_{ly} \frac{x}{R^{2}} =  e_{lx} t_{x} + e_{ly} t_{y}     \:\:\:(52)
\end{align*}$$
