
Windows are masked according to the certainty present in each
$$\begin{align*}
M_{cert} &= \text{abs}(F_{r} \circ F_{t})\\\\
W_{r} &= F_{r}^{\circ 3} \circ M_{cert}\\
W_{t} &= F_{t}^{\circ 3} \circ M_{cert}\\
\end{align*}$$
Convolution (discrete):

$$\begin{align*}
 (A * B)[i,j] = \sum_{m} \sum_{n} A[m,n] \cdot B[i-m, j-n]
\end{align*}$$

Kernels are constructed:
$$\begin{align*}
K_{dx} &= \begin{bmatrix} -1 & -1 & ... & -1 & 0 & 1 & ... & 1 & 1 \end{bmatrix}\\
K_{dy} &= K_{dx}^{T}
\end{align*}$$

Error window is extracted:
$$\begin{align*}
E_{dif} &= W_{r} - W_{t} \\
\end{align*}$$

Interest mask, representing the region where both overlap:
$$\begin{align*}
M_{overlap,ij} &= (W_{r,ij} > 0) \land (W_{t,ij} > 0)
\end{align*}$$

Scaling multiplier:
$$\begin{align*}
l &= \min\left( \sum  [W_{r} \circ (W_{r} >0)],\:\: \sum  [W_{t} \circ (W_{t} >0)]  \right) 
\end{align*}$$

Convolution:

$$\begin{align*}
E_{dx} &= [(E_{dif} \:*\: K_{dx} ) \circ M_{overlap}]\: \frac{k_{x}}{l} \\

E_{dy} &= [(E_{dif} \:*\: K_{dy} ) \circ M_{overlap}]\: \frac{k_{y}}{l}\\
\end{align*}$$

total error:
$$\begin{align*}
e_{x} &= \sum\limits E_{dx}\\
e_{y} &= \sum\limits E_{dy}
\end{align*}$$

arrays for x and y, given in real distances and with SOMETHING as origin:

$$\begin{align*}
X_{ij} &=  \\
Y &= 
\end{align*}$$

Regions of high dx and dy errors are found


Separation from origin^2, capped at k_minSep = 0.1
$$\begin{align*}
S_{ij} &= \max( X_{ij}^{2} + Y_{ij}^{2} , k_{minSep})\\
T_{x} &= Y\oslash S\\
T_{y} &= X\oslash S\\

\end{align*}$$

Angular error

$$\begin{align*}
E_{\alpha} &= T_{x} \circ E_{dx} + T_{y} \circ E_{dy}
\end{align*}$$

This is bad because reasons, a mask is applied to remove bad

$$\begin{align*}
M_{edx,ij} &= \begin{cases}
    1 & \text{if } E_{dx,ij} \:!= 0 \\
    0 & \text{else }
\end{cases}\\\\
M_{edy,ij} &= \begin{cases}
    1 & \text{if } E_{dy,ij} \:!= 0 \\
    0 & \text{else }  
\end{cases}\\
\end{align*}$$
So now:
$$\begin{align*}
E_{\alpha} &= T_{x} \circ \left[E_{dx} - M_{edx} \left(  \frac{e_{x}}{\sum\limits M_{edx}} \right) \right] + T_{y} \circ \left[E_{dy} - M_{edy} \left(  \frac{e_{y}}{\sum\limits M_{edy}} \right) \right]
\end{align*}$$
$$\begin{align*}
e_{\alpha} &= k_{\alpha}\sum\limits E_{\alpha}
\end{align*}$$

local translation error vector:
$$\begin{align*}
v_{le} &= \begin{bmatrix} e_{lx}\\e_{ly} \end{bmatrix} \:\:(?) &&& t_{c} &=\begin{bmatrix} y/R \\ x/R\end{bmatrix} \:\:(?) &&& e_{l\alpha} &= \frac{v_{le}\cdot t_{e}}{R} \:\:(?)
\end{align*}$$

$$\begin{align*}
e_{l\alpha} &= e_{lx} \frac{y}{R^{2}} + e_{ly} \frac{x}{R^{2}} =  e_{lx} t_{x} + e_{ly} t_{y}     \:\:\:(?)
\end{align*}$$
