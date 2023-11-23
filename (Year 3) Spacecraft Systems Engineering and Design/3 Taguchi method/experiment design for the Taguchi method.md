---
aliases: ["degrees of freedom"]
tags: []
---

## Experiment design for the [[Taguchi Method Overview|Taguchi Method]]

### Potential test cases

To optimise we'll need to choose what [[design parameters and noise factors|design parameters]] and [[design parameters and noise factors|noise factors]] we test, to do so we need to quantify the possibilities.

> ### $$\begin{align*} \text{Total unique combos}  &= s^{m}  \end{align*}$$
>> where:
>> $s=$ [[design parameters and noise factors|parameter level]] count
>> $m=$ [[design parameters and noise factors|design parameter]] count

The total number of unique combo's can become [[in a manor quite similar to the size of the mother who is morbidly obese|huge]], so we generally don't actually test for all of them (Cost and schedule constraints often prevent the analysis of all possible test cases). However it's best to at least test at 3 levels ($n\geq 3$), since this allows for the representation of non-linear relationships.

### Degrees of Freedom

The aim is to choose what information to gather so that the relationship between inputs and outputs can be determined with the least amount of effort.

To choose the minimum number of experiments we should consider we can use this equation for degrees of freedom:

> ### $$\begin{align*} \text{DOF}  &= 1 + m(s-1)  \end{align*}$$
>> where:
>> $\text{DOF}=$ minimum number of experiments to relate [[design parameters and noise factors|design parameters]] to performance characteristics
>> $s=$ [[design parameters and noise factors|parameter level]] count
>> $m=$ [[design parameters and noise factors|design parameter]] count

So the number of experiment's we should check for is:

$$\begin{align*}
1 + m(s-1) \leq \text{unique experiment count} \leq s^{m}
\end{align*}$$


### Orthogonal matrices

The Taguchi method uses orthogonal matrices from Design of Experiments theory to explore the parameter space with a significantly small number of experiments.

Each row of the matrix correspond to an individual test, with each column containing the chosen design parameter [[design parameters and noise factors|level]]. This results in a matrix with:
- $m$ columns ([[design parameters and noise factors|parameter]] count)
- $n$ rows (test number)

#### Rules for level selection
The way this matrix is populated must be done to optimally explore the parameter space, this is achieved by following rules.

For selection where all [[design parameters and noise factors|design parameters]] have the same number of potential [[design parameters and noise factors|levels]], the rules are:
- Each level must appear the same number of times in it's column
- The pattern in the column must remain the same

#### Examples

![[Pasted image 20231122201349.png]]

![[Pasted image 20231122201327.png]]

 
