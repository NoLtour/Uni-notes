---
aliases: ["Hopitals rule"]
tags: ["Question","QFormat3"]
---

#### What is
## Hospitals rule
(Yes I did just name it that, [[barbarian letters|cope]] I don't have an international keyboard and naming equations after people is [[it really do be cringe though|annoying and cringy]])

Sometimes you need to find limits in the form:
$$\begin{align*}
\lim_{x\to a} \frac{f(x)}{g(x)} 
\end{align*}$$
Where $f(a)=g(a)=0$ but $\lim_{x\to a} \frac{f(x)}{g(x)}$ does have a definite value, since $0/0$ is invalid so substitution of $x=a$ wont work, what can be done instead is using:

> ### $$ \lim_{x\to a} \frac{f(x)}{g(x)} = \lim_{x\to a} \frac{f^{'}(x)}{g^{'}(x)}  $$ 
>> where:
>> $g^{'}(a)\neq 0$

You might intuitively see that if the expression above is true it should work for second order derivatives and so on, which is true: Alternatively if $g^{'}(a)= 0$ you can literally just keep differentiating:

> ### $$ \lim_{x\to a} \frac{f(x)}{g(x)} = \lim_{x\to a} \frac{f^{'}(x)}{g^{'}(x)}= \lim_{x\to a} \frac{f^{''}(x)}{g^{''}(x)} = \lim_{x\to a} \frac{f^{'''}(x)}{g^{'''}(x)} = ...  $$ 
>> where:
>> $g^{i'}(a)\neq 0$
