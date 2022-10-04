---
aliases: ["rank of a matrix"]
tags: ["Question","QFormat3"]
---

#### What is
## Matrix rank
Note that everything on this page only applies to [[square matrix|square matrices]].

There are some funkey definitions but just go with: "the number of rows that contain things other than zero once the matrix is in [[matrix in echelon form]]"

This is a rank 4 matrix:
$$\begin{align*}
&\begin{pmatrix} 
1 & 0 & 3 & 2 \\ 
0 & 1 & -1 & 0 \\ 
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 
\end{pmatrix}\\
\end{align*}$$

This is a rank 3 matrix:
$$\begin{align*}
&\begin{pmatrix} 
1 & 0 & 3 & 2 \\ 
0 & 1 & -1 & 0 \\ 
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 
\end{pmatrix}\\
\end{align*}$$

This is a rank 2 matrix:
$$\begin{align*}
&\begin{pmatrix} 
1 & 0 & 3 & 2 \\ 
0 & 1 & -1 & 0 \\ 
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 
\end{pmatrix}\\
\end{align*}$$

This is a rank 1 matrix:
$$\begin{align*}
&\begin{pmatrix} 
1 & 0 & 3 & 2 \\ 
0 & 0 & 0 & 0 \\ 
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 
\end{pmatrix}\\
\end{align*}$$

They can be other dimentions too, this is also a rank 2 matrix:
$$\begin{align*}
&\begin{pmatrix} 
1 & 0 & 3  \\ 
0 & 1 & -1  \\ 
0 & 0 & 0  \\
\end{pmatrix}\\
\end{align*}$$

The more accurate definition of matrix rank is: "the order of the largest square submatrix with non-zero determinant. A square submatrix is formed by deleting rows and columns to form a smaller square matrix."