---
aliases: ["solving linear second order ordinary differential equations","solving linear second order ODEs"]
tags: ["Question","QFormat3"]
---

#### What is the method for
## Solving linear homogeneous constant-coefficient equations
### Theory

When solving, essentially what you are doing is attempting to find 2 [[linearly dependent and independent functions|linearly independent]] solutions of the [[homogeneous and nonhomogeneous differential equations|homogeneous equation]]: 
> ### $$ \frac{d^{2}y}{dx^{2}} + p(x) \frac{dy}{dx} + q(x) = 0 $$

(here I'm talking with reference to the equation above)
In practice what this means is that you get 2 functions of $y(x)$ which can be subbed back into the [[homogeneous and nonhomogeneous differential equations|homogeneous equation]] and are [[linearly dependent and independent functions|linearly independent functions]] hence satisfying: $A \times y_{1} (x) \neq B \times y_{2} (x)$ ($A,B$ are constants)

Once you have those two equations you can sub them into: $y(x) = c_{1} y_{1}(x) + c_{2} y_{2}(x)$ to get your solution for


### Method
![[linear homogeneous constant-coefficient equation#^9a6d21]] ^7adaea

1) 
> Treat it like a quadratic and find it's roots:
> $$ \begin{align*}
a \frac{d^{2}x}{dt^{2}}+ b \frac{dx}{dt} + cx &= 0 &\to&& am^{2}+bm+c&=0\\
&& roots:\:&m_1,m_2
\end{align*} $$
2) 
> Depending on what roots are found one of the following formats is used:
>> ### $$ x(t) = Ae^{m_1 t} + Be^{m_2 t} $$ 
>>> when:
>>> $m_1,m_2=$ real numbers
>>> $m_1 \neq m_2$
>>
>>> where:
>>> $A,B$ = constants
>
>> ### $$ x(t) = (At+B)e^{m_1 t} $$ 
>>> when:
>>> $m_1,m_2=$ real numbers
>>> $m_1=m_2$
>>
>>> where:
>>> $A,B$ = constants 
>
>> ### $$ x(t) = e^{at} ( A\cos(bt) + B\sin(bt) ) $$ 
>>> when:
>>> $m_1,m_2=$ [[complex numbers]]
>>
>>> where:
>>> $A,B$ = constants
>>> $root=a\pm bi$
3) 
> Use [[boundary conditions]] and [[initial conditions]] to find the [[general and particular solution|particular solution]] (if possible)

### Example

#### Finding a [[general and particular solution|general solution]]
> Find the [[general and particular solution|general solution]] for:
> $$ \frac{d^{2}x}{dt^{2}} - 9 \frac{dx}{dt} + 6x = 0 $$

$$\begin{align*}
m^{2} - 9m + 6 &= 0\\
&& m_1 &= \frac{9+ \sqrt{57}}{2}  & m_2 &= \frac{9- \sqrt{57}}{2} 
\end{align*}$$

Hence general solution is:
$$\begin{align*}
x(t) = Ae^{\frac{9+ \sqrt{57}}{2} t} + Be^{\frac{9- \sqrt{57}}{2}  t}
\end{align*}$$

#### Finding a [[general and particular solution|particular solution]]
> Continueing from the previous example find the [[general and particular solution|particular solution]] given that:
> $$\begin{align*}
x(0) &= 1 & \frac{dx}{dt}(0) = 2 
\end{align*}$$

$$\begin{align*}
x(t) &= Ae^{\frac{9+ \sqrt{57}}{2} t} + Be^{\frac{9- \sqrt{57}}{2}  t}\\
&&\frac{dx}{dt} &= \frac{9+ \sqrt{57}}{2} Ae^{\frac{9+ \sqrt{57}}{2} t} + \frac{9-\sqrt{57}}{2} Be^{\frac{9- \sqrt{57}}{2}  t}\\
&&&& let:\:x(0) &= 1 & \frac{dx}{dt}(0) = 2 \\
1 &= Ae^{0} + Be^{0} & 2 &= \frac{9+ \sqrt{57}}{2} Ae^{0} + \frac{9-\sqrt{57}}{2} Be^{0}\\
1 - B &= A & 2 &= \frac{9+ \sqrt{57}}{2} A + \frac{9-\sqrt{57}}{2} B\\
&& 2 &= \frac{9+ \sqrt{57}}{2} (1 - B) + \frac{9-\sqrt{57}}{2} B\\
&& 2 &= \frac{9+ \sqrt{57}}{2} - \frac{9+ \sqrt{57}}{2}B  + \frac{9-\sqrt{57}}{2} B\\
&& 2 -\frac{9+ \sqrt{57}}{2} &=  - \sqrt{57} B \\
&&B&=0.8311\\
A&=0.1989\\
\therefore x(t) &= 0.1989e^{\frac{9+ \sqrt{57}}{2} t} + 0.8311e^{\frac{9- \sqrt{57}}{2}  t}
\end{align*}$$