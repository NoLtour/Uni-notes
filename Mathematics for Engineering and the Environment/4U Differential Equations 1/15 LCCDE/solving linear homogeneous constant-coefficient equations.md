---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the method for
## Solving linear homogeneous constant-coefficient equations
### Method
![[linear homogeneous constant-coefficient equation#^9a6d21]]

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
>>> $m_1=m_2$
>>
>>> where:
>>> $A,B$ = constants
>
>> ### $$ x(t) = (At+B)e^{m_1 t} $$ 
>>> when:
>>> $m_1,m_2=$ real numbers
>>> $m_1 \neq m_2$
>>
>>> where:
>>> $A,B$ = constants 
>
>> ### $$ x(t) = e^{at} ( A\cos(bt) + B\sin(bt) ) $$ 
>>> when:
>>> $m_1,m_2=$ complex numbers
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
B&=0.8311
A&=1
\end{align*}$$