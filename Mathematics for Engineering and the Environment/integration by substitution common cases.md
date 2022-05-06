---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### 
## Integration by substitution common cases

This is just [[integration using the general composite rule|integration by substitution]] but some cases that are specifically mentioned in the book ([[idk I want to put a meme here|excuse]], [[here its math themed|also this]]).

### Form $\frac{dx}{dt} = f\left(\frac{x}{t}\right)$
#### Equation
The substitution is $y=\frac{x}{t}$ which is rearranged into $x=yt$ then from [[What's the product rule|product rule]] gives $\frac{dx}{dt} = t \frac{dy}{dt} + y$.

> ### $$ \frac{dx}{dt} = f\left(\frac{x}{t}\right) $$
> ### $$ \frac{dx}{dt} = t \frac{dy}{dt} + y $$ 
> ### $$ x = yt $$
>> where:
>> $y=$ the substitution variable

#### Example
> Solve:
> $$ t^{2} \frac{dx}{dt} = x^{2} + xt $$

$$\begin{align*}
\frac{dx}{dt} &= \frac{x^{2}}{t^{2}} + \frac{x}{t}\\
& & y &= \frac{x}{t} & \frac{dx}{dt} &= t \frac{dy}{dt} + y\\
t \frac{dy}{dt} + y &= y^{2} + y\\
 t \frac{dy}{dt} &= y^{2} \\
 \frac{1}{y^{2}} \cdot dy &= \frac{1}{t} \cdot dt \\
\int \frac{1}{y^{2}} \cdot dy &= \int \frac{1}{t} \cdot dt \\
\frac{-1}{y} &= \ln t + C\\
 ...&\:sub\:back\:...\\
x &= \frac{-t}{\ln t + C}
\end{align*}$$