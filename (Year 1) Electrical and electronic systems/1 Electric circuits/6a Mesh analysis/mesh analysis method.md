---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Mesh analysis method
### Method

1) > Draw "loop currents" around each loop (these arn't real currents but help with analysis, at any given point the sum of adjacent loop currents will equal the real current). They should all be clockwise.

2) > For each loop repeat the following steps (note that $I_x$ refers to the focused loop current and $I_n$ refers to non focused currents and $R_n$ is any resistor on the focused loop current): 
> 1) Add all known p.ds together on the right side of the equation taking direction relative to the focused loop current
> 2) Add the $I_x \cdot (\sum\limits R_n)$ to the left side of the equation
> 3) Subtract all of the adjasent loop currents $I_n \cdot (\sum\limits R_n)$ from the left side of the equation
As an equation:
>> ### $$ I_x \cdot \sum\limits \left(R_n\right)- \sum\limits \left(I_n \cdot \sum\limits \left(R_n\right) \right) = \sum\limits \left(V_n\right) $$ 
>>> where:
>>> $I_x=$ The focused loop current 
>>> $I_n=$ Any loop current that touches the focused loop current
>>> $R_n=$ All components between the focused loop current and the other selected loop current
>>> $V_n=$ Any known pds, taking direction relative to $I_x$

3) > Now form a matrix using all your equations and solve it, (With practice you don't even need to write the equations tbh)

4) > Now you know your loop currents you can sum them at any point to give the real local current at that point

### Example
Find expressions for the resistances in this circuit:
![[Pasted image 20211107153425.png]]

1) > We draw loop currents.
> ![[Pasted image 20211113235757.png]]

2) 
> Selecting $I_1$:
> 1) There are no known p.d's on this loop current so it is just 0
$$ ? = 0 $$
> 2) $I_1$ is adjasent to all it's resitors so it's the sum of all of them
$$ I_1( R_4 + R_2 + R_1 ) + ? = 0 $$
> 3) $I_2,I_3$ each only share one component with $I_1$
$$ I_1( R_4 + R_2 + R_1 ) - I_2(R_1) - I_3(R_2) = 0 $$
> This will take too long if I give a detailed desc for each so I'm going to skip steps for $I_2,I_3$:
> $$ I_2( R_1 + R_3 ) - I_1 (R_1) - I_3( R_3 ) = V $$
> $$ I_3( R_2 + R_5 + R_3 ) - I_1(R_2) - I_2(R_3) = 0 $$


3) > Pog
> $$\begin{align*}
\begin{pmatrix}
( R_4 + R_2 + R_1 ) & -(R_1) & -(R_2) \\ 
-(R_1) & ( R_1 + R_3 ) & -( R_3 ) \\ 
-(R_2) & -(R_3) & ( R_2 + R_5 + R_3 )
\end{pmatrix}\begin{pmatrix} 
 I_1 \\ I_2 \\ I_3 
\end{pmatrix}  &= 
\begin{pmatrix} 0 \\ V \\ 0 \end{pmatrix}\\
\begin{pmatrix} 
 I_1 \\ I_2 \\ I_3 
\end{pmatrix}  &= \begin{pmatrix}
( R_4 + R_2 + R_1 ) & -(R_1) & -(R_2) \\ 
-(R_1) & ( R_1 + R_3 ) & -( R_3 ) \\ 
-(R_2) & -(R_3) & ( R_2 + R_5 + R_3 )
\end{pmatrix}^{-1}
\begin{pmatrix} 0 \\ V \\ 0 \end{pmatrix}
\end{align*}$$
> And done, holy shit that took ages to write out. 