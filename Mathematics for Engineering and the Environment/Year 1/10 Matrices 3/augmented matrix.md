---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is a
## Augmented matrix
An augmented matrix is a matrix obtained by appending the columns of two given matrices, usually for the purpose of performing the same [[elementary row operations with constant solutions|elementary row operations]] on each of the given matrices.

You can define an augmented matrix using the notation $(X:Y)$
> ### $$ (A:b) = \begin{pmatrix} a_{11} & a_{12} & a_{13} & b_{11} \\ a_{21}  & a_{22} & a_{23} & b_{21} \\ a_{31} & a_{32} & a_{33} & b_{31} \end{pmatrix} $$ 
>> where:
>> $A=\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21}  & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}$ 
>> $b=\begin{pmatrix} b_{11} \\b_{21} \\ b_{31} \end{pmatrix}$
>> $A_{row\:count}=b_{row\:count}$
>> Note that in reality A and b can be matrices of any width

### Example
> Solve:
> $$\begin{align*}
2x+0y+1z &=6\\
4x+1y-1z&=3 \\
0x+1y+1z&= 1
\end{align*}$$

$$\begin{align*}
\begin{pmatrix} 2 & 0 & 1 \\ 4 & 1 & -1 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix}x \\ y \\ z\end{pmatrix} &= \begin{pmatrix}  6  \\ 3 \\ 1\end{pmatrix}
\end{align*}$$

Expressing it as an [[augmented matrix]]:
$$\begin{align*}
\begin{pmatrix} 2 & 0 & 1 & 6 \\ 4 & 1 & -1 & 3 \\ 0 & 1 & 1 & 1 \end{pmatrix}
\end{align*}$$
(Just makes [[elementary row operations with constant solutions|elementary row operations]] more convenient.)
$$\begin{align*}
&\begin{pmatrix} 
2 & 0 & 1 & 6 \\ 
4 & 1 & -1 & 3 \\ 
0 & 1 & 1 & 1 
\end{pmatrix}\\\\

&\begin{pmatrix} 
1 & 0 & \frac{1}{2} & 3 \\ 
4 & 1 & -1 & 3 \\ 
0 & 1 & 1 & 1 
\end{pmatrix}\\\\

&\begin{pmatrix} 
1 & 0 & \frac{1}{2} & 3 \\ 
0 & 1 & -3 & -9 \\ 
0 & 1 & 1 & 1 
\end{pmatrix}\\\\

&\begin{pmatrix} 
1 & 0 & \frac{1}{2} & 3 \\ 
0 & 1 & -3 & -9 \\ 
0 & 0 & 4 & 10 
\end{pmatrix}\\\\

&\begin{pmatrix} 
1 & 0 & \frac{1}{2} & 3 \\ 
0 & 1 & -3 & -9 \\ 
0 & 0 & 1 & \frac{5}{2}
\end{pmatrix}\\

\end{align*}$$
Split it out again:

$$\begin{align*}
\begin{pmatrix} 
1 & 0 & \frac{1}{2} \\ 
0 & 1 & -3  \\ 
0 & 0 & 1 
\end{pmatrix} \begin{pmatrix}x \\ y \\ z\end{pmatrix} = \begin{pmatrix} 3 \\ -9 \\ \frac{5}{2} \end{pmatrix}
\end{align*}$$

^5130a9

