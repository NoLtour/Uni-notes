---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### 
## Solution of exact differential equations
Lil bit of intro information, (assuming I actually understand this) so if you have multiple variables then it is common for one to determine the other, eg $t$ determines the value of $x$ (For example if $x=\sin t$ then $x$ is determined by $t$ because the solution is ambiguous with $t=\arcsin x$), but it would be nice if there was some way to prove that such a relationship exists for the purposes of calculus and to figure out which variables determine the other.

Such a test does exist it is:
> ### $$ \frac{dh}{dt} = \frac{\delta h}{\delta x} \frac{dx}{dt} + \frac{\delta h}{\delta t} $$ 
>> where:
>> $h=h(t,x)=$ a function of $t,x$
>> $d=$ [[derivative symbols#d x total derivative|this maths thing]]
>> $\delta=$ [[derivative symbols#delta x partial derivative|this other max thing]]
>> $x=$ [[dependent variables|dependent variable]]
>> $t=$ [[independent variables|independent variable]]

If a first order differential equation exists of the form:
$$ p(t,x) \frac{dx}{dt} + q(t,x) = 0 $$
And a function ($h(T,x)$) can be found such that:
$$ \frac{\delta h}{\delta x} = q(t,x) \:\:\:\:\: and \:\:\:\:\: \frac{\delta h}{\delta t} = q(t,x) $$
Then subbing back:
$$\begin{align*}
p(t,x) \frac{dx}{dt} + q(t,x) &= 0\\
&
\end{align*}$$