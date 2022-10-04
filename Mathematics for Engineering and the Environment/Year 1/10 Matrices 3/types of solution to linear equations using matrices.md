---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can we determine the
## Types of solution to linear equations using matrices
### Messy (shit) explenation
![[Pasted image 20211223162423.png]]

If we have a [[matrix in echelon form]] as shown above that is acompanyed by a [[column vector]] containing solutions (here we have it in [[adjoint matrix]] form) then the following rules apply (here this is for solving sets of linear equations):
1) If the rank of the [[augmented matrix]] is greater than the rank of the coefficient matrix the set of linear equations are [[inconsistant equations|inconsistant]].
2) If the ranks of these matrices are equal then the system has one set of solutions and is [[consistant equations|consistant]].
3) If the rank of the coefficient matrix is higher than the [[augmented matrix]] then the equations has infinate solutions and is [[consistant equations|consistant]].

Note that:
Rank of [[augmented matrix]] = $u$
Rank of coefficient matrix = rank of the matrix containing the single numerical equivilences of each equation (not sure if I phrased that well, the skinny matrix that goes on the right, though you will need to go from [[augmented matrix]] back to the origional split form [[augmented matrix#^5130a9|example]])

### Better explenation
I think trying to adapt what the book says is confusing so I'll phrase it in a nice way:

> In form (cofactor matrix is the right most one):
> ### $$ FU=C $$
> ### $$ \begin{pmatrix} a_{11} &  a_{12} & ... \\ a_{21} & a_{22} & ... \\ ... & ... & ... \end{pmatrix} \begin{pmatrix}  x_1 \\ x_2 \\ ... \end{pmatrix} = \begin{pmatrix} c_{1}  \\ c_{2} \\ ... \end{pmatrix} $$
> Solutions:
> ### $$ \begin{align*}R_F < R_C &:\: no\:solutions,\:not\:consistant\\R_F = R_C &:\: single\:set\:of solutions \\R_F > R_C &:\: infinate\:solutions\end{align*} $$
>> where:
>> $R_F=$ [[matrix rank|Rank]] of the fat matrix
>> $R_C=$ [[matrix rank|Rank]] of the cofactor matrix
>> $F_{rows} \geq U_{rows}$ The cofactor matrix/fat matrix has more or equal rows as the unknown's matrix

^25079b

Note that this can actually be applied to non square matrices as well, plug: [[solving linear equations with non square matricies]]
Though secondary note if $F_{rows} < U_{rows}$ then there will alwayse be infinate solutions.

### Example
> Given the following matrix, determine how many sets of solutions exist.
> $$ \begin{pmatrix} 0 & 1 & 1 & 0 \\ 1 & 0 & 3 & 2 \\ 2 & 1 & 5 & 4 \\ 1  & -2 & 0 & 2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} = \begin{pmatrix}1 \\ 3 \\ 7 \\ 2\end{pmatrix} $$

(Imagine I have lots of working here (it's the same as [[matrix in echelon form#Example]] but modifieng the coefficient matrix as well during [[elementary row operations with constant solutions|elementary row operations]]))

$$\begin{align*}
 \begin{pmatrix}1 & \frac{1}{2} & \frac{5}{2} & 2 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}\begin{pmatrix}x_1 \\ x_2 \\ x_3 \\ x_4\end{pmatrix} &= \begin{pmatrix} \frac{7}{2} \\ \frac{3}{5} \\ - \frac{1}{5} \\ \frac{2}{5}\end{pmatrix}
\end{align*}$$
The rank of the main matrix is 3 while the coefficient matrix is 4, hence there are no solutions.