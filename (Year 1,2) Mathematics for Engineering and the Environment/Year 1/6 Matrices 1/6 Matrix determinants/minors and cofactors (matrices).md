---
aliases: ["cofactor","minor"]
tags: ["Question","QFormat3"]
---

#### What is a
## Minors and cofactors (matrices)
### Minors
If we take the following 3x3:
$$\begin{align*}
B &= \begin{pmatrix} a_{11} &  a_{12} &  a_{13} \\  a_{21} &  a_{22} &  a_{23} \\  a_{31} &  a_{32} &  a_{33} \end{pmatrix}
\end{align*}$$

The minor at position $a_{ij}$ can be found by crossing out the row $i$ and column $j$ then [[finding the determinant of a 2x2 matrix|finding the determinant of the remaining 2x2]]. 

#### Example for $a_{11}$:

$$\begin{align*}
B =& \begin{pmatrix} a_{11} &  a_{12} &  a_{13} \\  a_{21} &  a_{22} &  a_{23} \\  a_{31} &  a_{32} &  a_{33} \end{pmatrix}\\
 & \begin{pmatrix} * &  * &  * \\  * &  a_{22} &  a_{23} \\  * &  a_{32} &  a_{33} \end{pmatrix}\\
minor_{11}=& det\: \begin{pmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{pmatrix}
\end{align*}$$

#### Example for $a_{22}$:

$$\begin{align*}
B =& \begin{pmatrix} a_{11} &  a_{12} &  a_{13} \\  a_{21} &  a_{22} &  a_{23} \\  a_{31} &  a_{32} &  a_{33} \end{pmatrix}\\
 & \begin{pmatrix} a_{11} &  * &  a_{13} \\  * &  * &  * \\  a_{31} &  * &  a_{33} \end{pmatrix}\\
minor_{11}=& det\: \begin{pmatrix} a_{11} & a_{13} \\ a_{31} & a_{33} \end{pmatrix}
\end{align*}$$

### Cofactors ($A_{ij}$)
The cofactor for a specific element in a matix is represented using $A_{ij}$, it is calculated using the same method used for finding minors except you adjust the sign according to:
![[Pasted image 20211205210430.png]]

So if we take the following 3x3 (again):
$$\begin{align*}
B &= \begin{pmatrix} a_{11} &  a_{12} &  a_{13} \\  a_{21} &  a_{22} &  a_{23} \\  a_{31} &  a_{32} &  a_{33} \end{pmatrix}
\end{align*}$$

If we made a matrix of all of it's minors (m):
$$\begin{align*}
B_{minors} &= \begin{pmatrix} m_{11} &  m_{12} &  m_{13} \\  m_{21} &  m_{22} &  m_{23} \\  m_{31} &  m_{32} &  m_{33} \end{pmatrix}
\end{align*}$$
Then a matrix of its cofactors (c) would be:
$$\begin{align*}
B_{cofactors} &= \begin{pmatrix} c_{11} &  c_{12} &  c_{13} \\  c_{21} &  c_{22} &  c_{23} \\  c_{31} &  c_{32} &  c_{33} \end{pmatrix}= \begin{pmatrix} m_{11} &  -m_{12} &  m_{13} \\  -m_{21} &  m_{22} &  -m_{23} \\  m_{31} &  -m_{32} &  m_{33} \end{pmatrix}
\end{align*}$$
You can see that the only difference for a cofactor and a minor at any poisiton in the matrix is that mask we apply to it.