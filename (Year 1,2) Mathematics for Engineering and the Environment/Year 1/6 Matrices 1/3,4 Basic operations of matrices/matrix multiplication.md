---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How do you preform
## Matrix multiplication
This is where matrices really start, prepare for stuff.

### Conditions

![[conditions for matrix multiplication#Rule]]


### Method

To solve $A\times B$ use the following method:
- Take each element in the first row of $A$ and multiply it by the element in the first column of $B$ that has the same increment from the start
- Repleat this for the same row in $A$ using the next column of $B$
- Each of these resaults should be put into a new matrix with the row position of the $A$ elements and the column position of the $B$ elements
- Do this for each row in $A$

### Important notes

In matrix multiplication $(A\times B) \neq (B\times A)$ atleast most of the time, for specific values of A,B it is possible for the two forms to be equivilent.
![[Pasted image 20211205174839.png]]
### Example
It's simplest to explain with an example:

$$ \begin{pmatrix} 1 & 2 & 3 & 4 \\ 5 & 6 & 7 & 8 \end{pmatrix} \begin{pmatrix} 9  \\ 10 \\ 11 \\ 12 \end{pmatrix} = \begin{pmatrix} (1*9) + (2*10) + (3*11) + (4 * 12) \\ (5*9) + (6*10) + (7*11) + (8 * 12)  \end{pmatrix} =\begin{pmatrix} 110 \\ 278  \end{pmatrix} $$

#### Textbook examples

![[Pasted image 20211205174319.png]]