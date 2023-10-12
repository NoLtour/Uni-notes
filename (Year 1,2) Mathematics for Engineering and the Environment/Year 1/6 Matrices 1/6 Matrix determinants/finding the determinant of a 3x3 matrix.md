---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the method for
## Finding the determinant of a 3x3 matrix

To find the determinant of the following matrix ($B$):

$$\begin{align*}
B &= \begin{pmatrix} a_{11} &  a_{12} &  a_{13} \\  a_{21} &  a_{22} &  a_{23} \\  a_{31} &  a_{32} &  a_{33} \end{pmatrix}
\end{align*}$$

You use this equation:

> ### $$ det\:B = a_{11}\cdot det\:\begin{pmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{pmatrix} - a_{12}\cdot det\:\begin{pmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{pmatrix} + a_{13} \cdot det\:\begin{pmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{pmatrix} $$ 

Note that you need to use [[finding the determinant of a 2x2 matrix]] for each. (I know it's a pain)
This equation is basically the sum of [[minors and cofactors (matrices)|cofactor]]s multiplied by the thing


There is an easy way to remember it though.

![[Pasted image 20211205200114.png]]

Also note that it is possible to find the determinant using other rows, but you will probably figure that out for yourself later.