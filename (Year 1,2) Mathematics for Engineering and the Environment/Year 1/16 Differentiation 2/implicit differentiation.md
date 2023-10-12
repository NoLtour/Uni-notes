---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Implicit differentiation
### Theory
Something that is really important to keep in mind when working with differentiation is what you are actually doing, take this for example:
$$\begin{align*}
y &= x^{2} + 2x +5\\
\frac{dy}{dx} & = 2x + 2 
\end{align*}$$
Now what did you actually do there? Because in reality the method commonly used for differentiating skips an intermediate step which is:
$$\begin{align*}
y &= x^{2} + 2x +5\\
dy &= 2x dx + 2dx\\
\frac{dy}{dx} &= 2x + 2
\end{align*}$$
All differentiation is just mathematically describing how variables change relative to other variables over small distances, so there is nothing stopping differentiating something like $y^{3} + y = 2x+\ln x$:
$$\begin{align*}
y^{3} + y &= 2x+\ln x\\
3y^{2} dy + dy &= 2dx + dx \frac{1}{x}\\
dy (3y^{2} + 1) &= dx \left(2 + \frac{1}{x}\right)\\
\frac{dy}{dx} &= \frac{2 + \frac{1}{x}}{3y^{2} + 1}
\end{align*}$$
This is really useful for functions where isolating y on the left of the equation isn't possible or for functions that cannot be easily differentiated in such a state:
$$\begin{align*}
y &= (\sin x)^x\\
\ln y &= x \ln \sin x\\
\frac{1}{y} dy &= dx \ln \sin x + x \frac{1}{\tan x} dx\\
\frac{dy}{dx} &= y \left( \ln \sin x + x \frac{1}{\tan x} \right)\\
&= (\sin x)^x \left( \ln \sin x + \frac{x}{\tan x} \right)\\
\end{align*}$$