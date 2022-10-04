---
aliases: ["eigenvalue","eigenvalues","eigenvector","eigenvectors"]
tags: ["Question","QFormat3"]
---

#### What are
## Eigenvalues and eigenvectors

### Eigenvalues
These are values that induce the equivilent transformation as a specific square matrix for a specific column vector: 
> ### $$ Au = \lambda u $$ 
>> where:
>> $A=$ some matrix 
>> $u=$ a [[column vector]] (the [[eigenvalues and eigenvectors|eigenvector]])
>> $\lambda=$ the [[eigenvalues and eigenvectors|eigenvalue]]

The eigenvalues of a [[square matrix]] can be found using:
> ### $$ 0 = \det ( \lambda I - A) $$ 
>> where:
>> $\lambda=$ [[eigenvalues and eigenvectors|eigenvalues]] 
>> $I=$ [[unit matrix]]
>> $A=$ some [[square matrix]]
>> $\det(X)=$ [[determinant]] function

#### Example
> Find the [[eigenvalues and eigenvectors|eigenvalues]] for:
> $$ \begin{pmatrix} -2 & 1 \\ 1 & -2 \end{pmatrix} $$

$$\begin{align*}
0 & =\det \left( \lambda \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - \begin{pmatrix} -2 & 1 \\ 1 & -2 \end{pmatrix} \right) \\
&= \det \begin{pmatrix} \lambda+2 & -1 \\ -1 & \lambda+2 \end{pmatrix} \\
&= (\lambda+2)^{2} - 1\\
&= \lambda^{2} + 4\lambda + 3\\
&& \lambda &= -1 & \lambda &= -3
\end{align*}$$

[[eigenvalues and eigenvectors|Eigenvalues]] are -1, -3

### Eigenvectors
Basically this is the [[column vector]] that goes with a [[eigenvalues and eigenvectors|eigenvalue]]. Using all the same definitions as above.

Note: The method shown below also works for when eigenvalues are complex numbers, which is very common though annoying.

Also note: [[matrices are tools of the devil invented to torture the living|I love matrices]].

#### Examples
> Find the eigenvectors and eigenvalues for the following matrix:
> $$ A = \begin{pmatrix} 1 & 1 & -2 \\ -1 & 2 & 1 \\ 0 & 1 & -1 \end{pmatrix} $$

First you find the eigenvalues:
$$\begin{align*}
0 &= \det\: \begin{pmatrix} \lambda & 0 & 0 \\ 0 & \lambda & 0 \\ 0 & 0 & \lambda \end{pmatrix} - \begin{pmatrix} 1 & 1 & -2 \\ -1 & 2 & 1 \\ 0 & 1 & -1 \end{pmatrix}\\
&= \det\:  \begin{pmatrix} \lambda-1 & -1 & 2 \\ 1 & \lambda-2 & -1 \\ 0 & -1 & \lambda+1 \end{pmatrix}\\
&= 0 \det\begin{pmatrix} -1 & 2 \\ \lambda-2 & -1 \end{pmatrix} + 1\det\begin{pmatrix} \lambda-1 & 2 \\ 1 & -1 \end{pmatrix} + (\lambda+1)det\begin{pmatrix} \lambda-1 & -1 \\ 1 & \lambda-2 \end{pmatrix}\\
&= \lambda^{3}-2\lambda^{2}-\lambda+2\\
\lambda &= 2,\:1,\:-1
\end{align*}$$

Now for each eigenvalue you need to find the corresponding [[eigenvalues and eigenvectors|eigenvector]], we can use the identity $Au = \lambda u$:
$$\begin{align*}
\begin{pmatrix} 1 & 1 & -2 \\ -1 & 2 & 1 \\ 0 & 1 & -1 \end{pmatrix} \begin{pmatrix}a  \\ b \\ c\end{pmatrix} &= \lambda \begin{pmatrix}a \\ b \\ c\end{pmatrix} \\
&& a+b-2c&=\lambda a & -a +2b +c &= \lambda b
\end{align*}$$
We then sub in our eigenvalues and solve.
$$\begin{align*}\\
 \lambda &= 2 \\
a+b-2c&=2a & -a +2b +c &= 2 b \\
b-2c&=a & -a  +c &= 0\\
& & a &= c\\
b &= 3c
\end{align*}$$
Hence our [[eigenvalues and eigenvectors|eigenvector]] for our [[eigenvalues and eigenvectors|eigenvalue]] of 2 is:
$$\begin{align*}
\begin{pmatrix} c \\ 3c \\ c \end{pmatrix} &= \beta \begin{pmatrix} 1 \\ 3 \\ 1 \end{pmatrix}\\
&&  \begin{pmatrix} 1 & 1 & -2 \\ -1 & 2 & 1 \\ 0 & 1 & -1 \end{pmatrix} \beta \begin{pmatrix} 1 \\ 3 \\ 1 \end{pmatrix} &= 2 \times \beta \begin{pmatrix} 1 \\ 3 \\ 1 \end{pmatrix}
\end{align*}$$
Now to do the same for $\lambda=1$:
$$\begin{align*}\\
 \lambda &= 1 \\
a+b-2c&=a & -a +2b +c &= b \\
b&=2c & -a +b +c &= 0\\
&& 2c +c &= a\\
&& 3c &= a
\end{align*}$$
$$\begin{align*}
\begin{pmatrix} 3c \\ 2c \\ c \end{pmatrix} &= \beta \begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix}\\
&&  \begin{pmatrix} 1 & 1 & -2 \\ -1 & 2 & 1 \\ 0 & 1 & -1 \end{pmatrix} \beta \begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix} &= 1 \times \beta \begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix}
\end{align*}$$
Now to do the same for $\lambda=-1$:
$$\begin{align*}\\
 \lambda &= 1 \\
a+b-2c&=-a & -a +2b +c &= -b \\
2a+b-2c&=0 & 3b +c &= a \\
2(3b +c)+b-2c&=0\\
7b&=0\\
&& c &= a
\end{align*}$$
$$\begin{align*}
\begin{pmatrix} a \\ 0 \\ a \end{pmatrix} &= \beta \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}\\
&&  \begin{pmatrix} 1 & 1 & -2 \\ -1 & 2 & 1 \\ 0 & 1 & -1 \end{pmatrix} \beta \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} &= -1 \times \beta \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}
\end{align*}$$

Hence the [[eigenvalues and eigenvectors]] for matrix A are:
1) >$$ 2 , \begin{pmatrix} 1 \\ 3 \\ 1 \end{pmatrix} $$
2) >$$ 1 , \begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix} $$
3) >$$ -1 , \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} $$

Notice the $\beta$ is excluded, it's kinda just not needed as you can multiply/divide both sides by any constant.