---
aliases: ["two input system manipulation"]
tags: []
---

## Multiple input system manipulation

### Method

Although it may seem daunting, it's actually not that hard to solve block diagrams with multiple inputs. The method is as follows:
1) Use [[transfer function junction manipulation|junction manipulation]] till all inputs take a single path which meet at a [[block diagram parts|summing junction]]
2) Combine those into an "input equation"
3) Finish completing normally

Alternative layout for simplifying multi input systems

### 2 Input example

![[Pasted image 20231029154249.png]]

#### 1 Merging the paths

In this particular case it's quite simple, we just [[transfer function junction manipulation|move G1 over the summing junction]]:

![[Pasted image 20231029154344.png]]

#### 2 Combining into an input

Then we express both those inputs as a single equation:

![[Pasted image 20231029154534.png]]

#### 3 Finish solving

Now we can just continue normally, next step is to perform [[transfer function loop reduction]]:

![[Pasted image 20231029154627.png]]

Finally we apply [[transfer function series manipulation|series transfer function reduction]]:

![[Pasted image 20231029154648.png]]

Our final output is slightly differently formatted to normal:

$$\begin{align*}
C &= (RG_{1}+X) \frac{G_{2}}{1+G_{1}H_{1}}
\end{align*}$$

