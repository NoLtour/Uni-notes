---
aliases: ["Hopitals rule"]
tags: ["Question","QFormat3"]
---

#### What is
## Hospitals rule
(Yes I did just name it that, [[barbarian letters|cope]] I don't have an international keyboard and I don't )

Sometimes you need to find limits in the form:
$$\begin{align*}
\lim_{x\to a} \frac{f(x)}{g(x)} 
\end{align*}$$
Where $f(a)=g(a)=0$ but $\lim_{x\to a} \frac{f(x)}{g(x)}$ does have a definite value, since $0/0$ is invalid so substitution of $x=a$ wont work, what can be done instead is using:

> ### $$ \lim_{x\to a} \frac{f(x)}{g(x)} = \lim_{x\to a} \frac{f^{'}(x)}{g^{'}(x)}  $$ 
>> where:
>> $g^{'}(a)\neq 0$

Alternatively if $g^{'}(a)= 0$ you can literally just keep differentiating:

> ### $$ \lim_{x\to a} \frac{f(x)}{g(x)} = \lim_{x\to a} \frac{f^{'}(x)}{g^{'}(x)}= \lim_{x\to a} \frac{f^{''}(x)}{g^{''}(x)} = \lim_{x\to a} \frac{f^{'''}(x)}{g^{'''}(x)} = ...  $$ 
>> where:
>> $g^{i'}(a)\neq 0$
