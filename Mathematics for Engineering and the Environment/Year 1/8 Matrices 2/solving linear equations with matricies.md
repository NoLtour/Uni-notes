---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Solving linear equations with matricies
We commonly need to find the unkowns in a set of linear equations:

> Given $x+5y-z=7$, $-2x+23y+21z=5$ and $y+4z=0$ find $x,y,z$.

If we rewrite the given equations in the form:
$$\begin{align*}
+1x+5y-1z&=7\\
-2x+23y+21z&=5\\
+0x+1y+4z&=0\\
\end{align*}$$
Then it becomes clear that this can be rewritten using matricies:
$$\begin{align*}
\begin{pmatrix} 1 & 5 & -1 \\ -2 & 23 & 21 \\ 0 & 1 & 4 \end{pmatrix} \begin{pmatrix}x \\ y \\ z\end{pmatrix} &= \begin{pmatrix}7  \\ 5 \\ 0\end{pmatrix} 
\end{align*}$$
Hence solving it requires finding the [[inverse matrix]] of the 3x3:
$$\begin{align*}
 \begin{pmatrix}x \\ y \\ z\end{pmatrix} &= \begin{pmatrix} 1 & 5 & -1 \\ -2 & 23 & 21 \\ 0 & 1 & 4 \end{pmatrix}^{-1} \begin{pmatrix}7  \\ 5 \\ 0\end{pmatrix} \\
&= \begin{pmatrix} \frac{392}{113} \\ \frac{76}{113} \\ - \frac{19}{113} \end{pmatrix}
\end{align*}$$
This is basically the method for [[solving linear equations with matricies]], this works with 2,3,4,5,6, ... n unkowns. ([[I am calling you stupid if you do not understand|me saying unlimited unknowns ok]]) With the number of unknowns being the dimentions of your [[square matrix]].

Of course the limitations on when it is possible to find a [[inverse matrix]] still applies, this is actually quite useful as we can now use matricies to prove if a set of linear equations has solutions that can be determined based on whether or not it's [[square matrix]] form has a non zero [[determinant]].