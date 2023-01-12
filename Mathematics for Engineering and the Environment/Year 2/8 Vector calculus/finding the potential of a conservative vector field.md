---
aliases: [""]
tags: []
---

## Finding the potential of a conservative vector field

### Equations

For the 2D case:

> ### $$\begin{align*}    \vec{F}(x,y) = F_{x}(x,y) \hat{i} + F_{y}(x,y) \hat{j}   \end{align*}$$
> ### $$\begin{align*}  \phi_{y}(y)  -\int F_{x}(x,y) \:\delta x &= \phi(x,y)  && & \phi_{x}(x)  -\int F_{y}(x,y) \:\delta y &= \phi(x,y)  \\-\int F_{x}(x,y) \:\delta x &= \phi_{x,y}(x,y) + \phi_{x}(x)  && &   -\int F_{y}(x,y) \:\delta y &= \phi_{x,y}(x,y) + \phi_{y}(y) \end{align*}$$
> ### $$ \phi(x,y) = \phi_{x,y}(x,y) + \phi_{x}(x) + \phi_{y}(y) $$
> ### $$\begin{align*}  \phi_{x}(x)  -\int F_{y}(x,y) \:\delta y &= \phi(x,y)      \end{align*}$$
> ### $$ \vec{F}(x,y) = - \nabla \phi(x,y) $$
> ### $$\nabla \times \vec F =  0$$ 
>> where:
>> $\vec{F}=$ [[conservative field|conservative vector field]]
>> $F_{x},F_{y}=$ scalar functions used to describe the components of $\vec F$
>> $\phi=$ scalar field, the potential of $\vec F$
>> $\phi_{x},\phi_{y}=$ the components of the equation of $\phi$ which are only reliant on $x$ and $y$ respectively
>> $\phi_{x,y}=$ the components of $\phi$ which are dependent on both $x$ and $y$
>> $C=$ some constant

That's just me highlighting the important parts but it would be best to show all the working as done below.

### Method background
We've already discussed how to get the [[conservative field|conservative vector field]] from a potential, but how can we work backwards? It's quite [[had a perfect meme but already used it|simple]] really, we just write out all the information we have and work backwards. 

Assume we have some 2D vector function $\vec F$ then it can be written as:
$$ \vec{F}(x,y) = F_{x}(x,y) \hat{i} + F_{y}(x,y) \hat{j} $$
Then if this is a [[conservative field]] we know that $\vec{F} = -\nabla \phi$ which means that:
$$\begin{align*}
\vec{F}(x,y) &= - \nabla \phi\\
F_{x}(x,y) \hat{i} + F_{y}(x,y) \hat{j} &= -\left(\hat{i}\frac{\delta\phi}{\delta x}+\hat{j}\frac{\delta\phi}{\delta y}\right)
\end{align*}$$
$$\begin{align*}
F_{x}(x,y)  &= - \hat{i}\frac{\delta\phi}{\delta x}  & F_{y}(x,y)  &= - \hat{j}\frac{\delta\phi}{\delta y}\\
-\int F_{x} \:\delta x &= \phi(x,y) - \phi_{y}(y) & -\int F_{y} \: \delta y &= \phi(x,y) - \phi_{x}(x)
\end{align*}$$
Since we are [[derivative symbols#Example (and how to integrate these)|integrating a partial derivative]] we can then find the final solution of $\phi$ from the information above.

It is also generally required to use [[conservative field#Additional properties of a conservative field|conservative field curl]] to verify the field is in fact conservative.


