---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Using elementary row operations to get the upper-triangular form
Fuck I don't have any illuminati memes, ok this sucks I need to find some one moment. [[yes I am using a meme from the stone age fucking cope|found one]]

Ok so we know that [[elementary row operations with constant solutions|elementary row operations]] can be used to manipulate matrices representing linear equations without changing the solution, so what we are doing here is using these methods to get it the [[square matrix]] in the equation matrix thing into a [[upper-triangular matrix]] where elements along the diaganal are all 1.

### Example
$$\begin{align*}
\begin{pmatrix} 1 & 5 & -1 \\ -2 & 23 & 21 \\ 0 & 1 & 4 \end{pmatrix} \begin{pmatrix}x  \\ y \\ z\end{pmatrix}  &= \begin{pmatrix} 7 \\ 5 \\ 0 \end{pmatrix}
\end{align*}$$
Subtract 2x(row 1) from row 2:

$$\begin{align*}
\begin{pmatrix} 1 & 5 & -1 \\ 0 & 33 & 19 \\ 0 & 1 & 4 \end{pmatrix} \begin{pmatrix}x  \\ y \\ z\end{pmatrix}  &= \begin{pmatrix} 7 \\ 19 \\ 0 \end{pmatrix}
\end{align*}$$

Divide row 2 by 33 to get the diaganal to equal 1:

$$\begin{align*}
\begin{pmatrix} 1 & 5 & -1 \\ 0 & 1 & \frac{19}{33} \\ 0 & 1 & 4 \end{pmatrix} \begin{pmatrix}x  \\ y \\ z\end{pmatrix}  &= \begin{pmatrix} 7 \\ \frac{19}{33} \\ 0 \end{pmatrix}
\end{align*}$$

Subtract 1x(row 2) from row 3:
$$\begin{align*}
\begin{pmatrix} 1 & 5 & -1 \\ 0 & 1 & \frac{19}{33} \\ 0 & 0 & \frac{113}{33} \end{pmatrix}\begin{pmatrix}x  \\ y \\ z\end{pmatrix}   &= \begin{pmatrix} 7 \\ \frac{19}{33} \\ -\frac{19}{33} \end{pmatrix}
\end{align*}$$

Divide row 3 by $\frac{113}{33}$:

$$\begin{align*}
\begin{pmatrix} 1 & 5 & -1 \\ 0 & 1 & \frac{19}{33} \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix}x  \\ y \\ z\end{pmatrix}  &= \begin{pmatrix} 7 \\ \frac{19}{33} \\ -\frac{19}{113} \end{pmatrix}
\end{align*}$$

Now the equations in [[upper-triangular matrix]] form with 1's on the diaganal. And the solution to the matrix is the same.