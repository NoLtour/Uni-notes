---
aliases: ["inverse matricies"]
tags: ["Question","QFormat3"]
---

#### How can you find an
## Inverse matrix

For a matrix to have an inverse it must be a [[square matrix]] and be a [[singular matrix|non-singular matrix]].

> ### $$ A^{-1} = \frac{1}{|A|} adj\:A $$ 
>> where:
>> $A^{-1}=$ [[inverse matrix]] 
>> $|A|=$ [[determinant]] of A
>> $adj\:A=$ [[adjoint matrix]]
>> $AA^{-1} = I$
>> $I=$ [[unit matrix]]
>> $|A|\neq 0$

If you look back at the [[adjoint matrix]] page you can see under it's strange properties how it can easily be manipulated to give an inverse matrix.

### Example
#### 2x2 matrix
> Find the inverse of $A=\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$

$$\begin{align*}
A^{-1}&= \frac{1}{det\:A} adj\:A \\
&= \frac{1}{det\:A} (cofactors\:A)^{T} \\
&= \frac{1}{det\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}} (cofactors\:\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix})^{T}\\
&= \frac{1}{1*3-2*2} \begin{pmatrix} 3 & -2 \\ -2 & 1 \end{pmatrix}^{T}\\
&= \frac{1}{-1} \begin{pmatrix} 3 & -2 \\ -2 & 1 \end{pmatrix}\\
&= \begin{pmatrix} -3 & 2 \\ 2 & -1 \end{pmatrix}
\end{align*}$$

#### 3x3 matrix
> Find the inverse of $A=\begin{pmatrix} 5 & 2 & 4 \\ 3 & -1 & 2 \\ 1 & 4 & -3 \end{pmatrix}$

$$\begin{align*}
A^{-1}&= \frac{1}{det\:A} adj\:A \\
&= \frac{1}{det\:A} (cofactors\:A)^{T} \\
&= \frac{1}{det\:A} \left(cofactors\:\begin{pmatrix} 5 & 2 & 4 \\ 3 & -1 & 2 \\ 1 & 4 & -3 \end{pmatrix} \right)^{T}\\
&= \frac{1}{5det \begin{pmatrix} -1 & 2 \\ 4 & -3 \end{pmatrix} -2det \begin{pmatrix} 3 & 2 \\ 1 & -3 \end{pmatrix} +4 det\begin{pmatrix} 3 & -1 &  \\ 1 & 4 \end{pmatrix}} \begin{pmatrix} det \begin{pmatrix} -1 & 2 \\ 4 & -3 \end{pmatrix} & -det \begin{pmatrix} 3 & 2 \\ 1 & -3 \end{pmatrix} & det\begin{pmatrix} 3 & -1 &  \\ 1 & 4 \end{pmatrix} \\ -det\begin{pmatrix} 2 & 4 \\ 4 & -3 \end{pmatrix} & det\begin{pmatrix} 5 & 4 \\ 1 & -3 \end{pmatrix} & -det\begin{pmatrix} 5 & 2 &  \\ 1 & 4 \end{pmatrix} \\det \begin{pmatrix} 2 & 4 \\ -1 & 2 \end{pmatrix} & -det\begin{pmatrix} 5 & 4 \\ 3 & 2 \end{pmatrix} &det \begin{pmatrix} 5 & 2 &  \\ 3 & -1 \end{pmatrix} \end{pmatrix}^{T}\\
&= \frac{1}{49} \begin{pmatrix} -5 & 11 & 13 \\ 22 & -19 & -18 \\ 8 & 2 & -11 \end{pmatrix}^{T}\\
&= \frac{1}{49} \begin{pmatrix} -5 & 22 & 8 \\ 11 & -19 & 2 \\ 13 & -18 & -11 \end{pmatrix}\\
\end{align*}$$