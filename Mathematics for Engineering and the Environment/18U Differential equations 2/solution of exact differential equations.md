---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### 
## Solution of exact differential equations
### Determining variable relationship
Lil bit of intro information, (assuming I actually understand this) so if you have multiple variables then it is common for one to determine the other, eg $t$ determines the value of $x$ (For example if $x=\sin t$ then $x$ is determined by $t$ because the solution is ambiguous with $t=\arcsin x$), but it would be nice if there was some way to prove that such a relationship exists for the purposes of calculus and to figure out which variables determine the other.

Such a test does exist it is:
> ### $$ \frac{dh}{dt} = \frac{\delta h}{\delta x} \frac{dx}{dt} + \frac{\delta h}{\delta t} $$ 
>> where:
>> $h=h(t,x)=$ a function of $t,x$
>> $d=$ [[derivative symbols#d x total derivative|this maths thing]]
>> $\delta=$ [[derivative symbols#delta x partial derivative|this other max thing]]
>> $x=$ [[dependent variables|dependent variable]]
>> $t=$ [[independent variables|independent variable]]

### Use in integration

If a first order differential equation exists of the form:
$$ p(t,x) \frac{dx}{dt} + q(t,x) = 0 $$
And a function ($h(T,x)$) can be found such that:
$$ \frac{\delta h}{\delta x} = p(t,x) \:\:\:\:\: and \:\:\:\:\: \frac{\delta h}{\delta t} = q(t,x) $$
Then subbing back:
$$\begin{align*}
p(t,x) \frac{dx}{dt} + q(t,x) &= 0 & \frac{\delta h}{\delta x} &= p(t,x) & \frac{\delta h}{\delta t} &= q(t,x) \\
\frac{\delta h}{\delta x} \frac{dx}{dt} + \frac{\delta h}{\delta t} &= 0\\
\frac{dh}{dt} &= 0
\end{align*}$$

Since $\frac{dh}{dt}=0$ we can find a constant for any value of $x,t$ hence the solution to the original differential equation will be:
$$ h(t,x) = C $$

### Example
> Solve the differential equation of the form:
> $$ 2xt \frac{dx}{dt} + x^{2} - 2t = 0 $$

$p(t,x) = 2xt$

$$\begin{align*}
p(t,x) &= 2xt & q(t,x) &= x^{2} - 2t\\
\frac{\delta h}{\delta x} &= & \frac{\delta h}{\delta t}&= \\
h &= 2xt & \frac{\delta h}{\delta t}&= \\
&
\end{align*}$$