
$$\begin{align*}
w_{p} &= w_{e} r_{cell} \:\: (6)
\end{align*}$$

$$\begin{align*}
F_{pr} = (F_{pd} * K_{circ}) * K_{g} \:\: (7)
\end{align*}$$


$$\begin{align*}
M_{nd,ij} &=  \begin{cases}
    1 & \text{if } F_{pr,ij} \:> F_{nd} k_{sh} \\
    0 & \text{else }
\end{cases} \:\:\:\:\: (8)
\end{align*}$$

$$\begin{align*}
F_{ps} &= F_{pr} \circ M_{nd} \:\:(9)
\end{align*}$$

$$\begin{align*}
F_{e,ij} &= \text{max} (\text{min}( F_{ps,ij}, \:1 ), \: F_{pd} ) - F_{nd} \:\:(10)
\end{align*}$$
