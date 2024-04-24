
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
M_{overlap} &= (W_{r} > 0) \land (W_{t} > 0)
\end{align*}$$

Scaling multiplier:
$$\begin{align*}
l &= \min\left( \sum  [W_{r} \circ (W_{r} >0)],\:\: \sum  [W_{t} \circ (W_{t} >0)]  \right) 
\end{align*}$$

Convolution:

$$\begin{align*}
E_{dx} &= [(E_{dif} \:*\: K_{dx} ) \circ M_{overlap}]\:lk_{x} \\

E_{dy} &= [(E_{dif} \:*\: K_{dy} ) \circ M_{overlap}]\:lk_{y}\\
\end{align*}$$

total error:
$$\begin{align*}
e_{x} &= \sum\limits E_{dx}\\
e_{y} &= \sum\limits E_{dy}
\end{align*}$$

arrays for x and y, given in real distances and with SOMETHING as origin:

$$\begin{align*}
X &= \\
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
M_{edx} &= (E_{dx} !=0)\circ e_{x}\\
M_{edy} &= (E_{dy} !=0)\circ e_{y}
\end{align*}$$
So now:
$$\begin{align*}
E_{\alpha} &= T_{x} \circ (E_{dx} - M_{edx}) + T_{y} \circ (E_{dy} - M_{edy})
\end{align*}$$
$$\begin{align*}
e_{\alpha} &= - \sum\limits E_{\alpha}
\end{align*}$$

