---
aliases: ["derivative symbol","this maths thing","partial derivative","total derivative"]
tags: ["Question","QFormat3"]
---

#### What are the two
## Derivative symbols
### $d x$ (total derivative)
Total derivatives are where it is possible for more than 1 variable to be varied.

### $\delta x$ (partial derivative)
In mathematics, a partial derivative of a function of several variables is its derivative with respect to one of those variables, with the others held constant.

#### Notation for holding a constant

$$ \left. \frac{\delta F}{\delta x}\right\vert_y $$

Means taking the partial derivative of $F$ with respect to $x$ while taking $y$ as a constant.

### Example (and how to integrate these)
Find the partial derivative of $h=4tx+x\ln t + 9t^{2} + t + 69x + k$ for $\frac{\delta h}{\delta x}$ and $\frac{\delta h}{\delta t}$
$$\begin{align*}
&& h&=4tx+x\ln t + 9t^{2} + t + 69x + k\\
\frac{\delta h}{\delta x} &= 4t+\ln t + 69 & & & \frac{\delta h}{\delta t} &= 4x+x \frac{1}{t} + 18t + 1 
\end{align*}$$
Note how both functions are missing data, so if you tried to integrate them back you would be missing information! Still by integrating both you can figure out what info was lost:
$$\begin{align*}
\frac{\delta h}{\delta x} &= 4t+\ln t + 69 & \frac{\delta h}{\delta t} &= 4x+x \frac{1}{t} + 18t + 1 \\
\int \delta h &= \int  4t+\ln t + 69 \cdot \delta x & \int \delta h &= \int 4x+x \frac{1}{t} + 18t + 1 \cdot \delta t\\
h &= 4tx+x\ln t + 69x + f_{1}(t) & h &= 4xt+x \ln t + 9t^{2} + t + f_{2}(x) 
\end{align*}$$
Combining both of the h's back into a single function:
$$\begin{align*}
h &= 4tx + x\ln t + 69x + 9t^{2} + t + C
\end{align*}$$
Which is equivalent to what we started with ([[poggga|pog]])