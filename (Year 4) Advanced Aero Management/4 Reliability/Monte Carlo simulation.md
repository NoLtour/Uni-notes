---
aliases: ["Monte Carlo method"]
tags: []
---

## Monte Carlo simulation

### Explanation

This is essentially a way where we solve problems which are too complex to do analytically, by trying to determine the properties of a system with sufficient samples.

Monte Carlo methods vary, but tend to follow a particular pattern:

1) Define a domain of possible inputs
2) Generate inputs randomly from a probability distribution over the domain
3) Perform a deterministic computation of the outputs
4) Aggregate the results

### Convergence

The error with Monte Carlo will be roughly:

$$\begin{align*}
E_{rr}(\mu) &= \frac{k}{\sqrt{N}}
\end{align*}$$
So to decrease error by 10x, we need 100x more samples! Which for some applications may be computationally impractical.

### Example, area of a shape

Let's say we have a complex 2D shape, and we want to find it's area:

![[Pasted image 20241023162404.png]]

We can then do a few steps:
1) (Define domain) Draw a box around the shape
2) (Sample the domain randomly) We then sample points in the box
3) (Deterministic computation) We then determine if the points are in the shape
4) (Aggregation) We then find the percentage of points in the shape

![[Pasted image 20241023162845.png]]

In step 4, we can use the area of the box ($A$) along with the number of points in the shape $(N')$ and the number of samples ($N$) to get an approximation of the total area of the shape ($A_{s}$):

$$\begin{align*}
A_{s} &\approx A \frac{N'}{N}
\end{align*}$$

Obviously, increasing the number of samples increases the accuracy:

![[Pasted image 20241023162916.png]]
