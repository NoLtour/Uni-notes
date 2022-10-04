---
aliases: ["solving linear second order ordinary differential equations","solving linear second order ODEs"]
tags: ["Question","QFormat3"]
---

#### What is the method for
## Solving linear homogeneous constant-coefficient equations
### Theory (first part covers general case)

When solving, essentially what you are doing is attempting to find 2 [[linearly dependent and independent functions|linearly independent]] solutions of the [[homogeneous and nonhomogeneous differential equations|homogeneous equation]]: 
> ### $$ \frac{d^{2}y}{dx^{2}} + p(x) \frac{dy}{dx} + q(x)y = 0 $$

(here I'm talking with reference to the equation above)
In practice what this means is that you get 2 functions of $y(x)$ which can be subbed back into the [[homogeneous and nonhomogeneous differential equations|homogeneous equation]] and are [[linearly dependent and independent functions|linearly independent functions]] hence satisfying: $A \times y_{1} (x) \neq B \times y_{2} (x)$ ($A,B$ are constants)

Once you have those two equations you can sub them into: $y(x) = c_{1} y_{1}(x) + c_{2} y_{2}(x)$ to get your solution for a general function of $y$. 

#### Proofing [[solving linear homogeneous constant-coefficient equations#Method|the method]]

So we start with some random linear homogeneous constant-coefficient equation: 
$$ a \frac{d^{2}y}{dx^{2}} + b \frac{dy}{dx} + c y = 0$$
This can then be rearranged:
$$\begin{align*}
\frac{d^{2}y}{dx^{2}} + \frac{b}{a} \frac{dy}{dx} + \frac{c}{a} y &= 0\\
\frac{d^{2}y}{dx^{2}} + f \frac{dy}{dx} + g y &= 0
\end{align*}$$

^9d621e

From here we need to make an educated guess on a valid function of $y$, here lets use $y=e^{\alpha x}$:
$$\begin{align*}
 \frac{d^{2}y}{dx^{2}} + f \frac{dy}{dx} + g y &= 0 & y&=e^{\alpha x}\\
 & & \frac{dy}{dx} &= \alpha e^{\alpha x}\\
 & & \frac{dy^{2}}{dx^{2}} &= \alpha^{2} e^{\alpha x}\\
\alpha^{2} e^{\alpha x} + f \alpha e^{\alpha x} + g e^{\alpha x} &= 0\\
\alpha^{2} + f \alpha + g &= 0
\end{align*}$$

Since everything cancels nicely we can see that $y=e^{\alpha x}$ is valid, this also leaves the equation in a solvable form that you are familiar with from when you first learn this method. Now by calculating the values of $\alpha$ we can hopefully get 2 [[linearly dependent and independent functions|linearly independent functions]] of $y(x)$.

$$ \alpha = \frac{-f \pm \sqrt{ f^{2} - 4g } }{2} $$

In an ideal world your solutions $\alpha_{1},\alpha_{2}$ are unique ($\alpha_{1}\neq \alpha_{2}$), if that's the case they can be substituted into your equation $y=e^{\alpha x}$ to give 2 [[linearly dependent and independent functions|linearly independent functions]] (clearly the two equations $y_1,y_2$ are linearly independent since they have different exponents):

$$\begin{align*}
y &= A \times y_{1} (x) + B \times y_{2} (x) \\
& & y_{1} &= e^{\alpha_{1} x} & y_{1} &= e^{\alpha_{1} x}\\
y &= A  e^{\alpha_{1} x} + B e^{\alpha_{2} x}
\end{align*}$$

In the event that $\alpha_{1},\alpha_{2}$ are complex the above stuff still works but you'll have to simplify using [[representing complex numbers using angle and magnitude|euler's formula]]:
$$\begin{align*}
y &= A  e^{\alpha_{1} x} + B e^{\alpha_{2} x} & \alpha_{1,2} &= a \pm jb & e^{\theta } &= \cos (\theta ) + j\sin (\theta ) \\
y &= A  e^{(a + jb) x} + B e^{(a - jb) x} & & & e^{-\theta } &= \cos (\theta ) - j\sin (\theta ) \\
y &= e^{ax}(A  e^{jbx} + B e^{-jbx} ) \\
y &= e^{ax}(A  (\cos (bx ) + j\sin (bx)) + B (\cos (bx ) - j\sin (bx))  ) \\
y &= e^{ax}( (A+B)\cos (bx )  + (A-B) (j\sin (bx)  ) \\
y &= e^{ax}( A\cos (bx )  +  jB\sin (bx)  )
\end{align*}$$
If your wondering what happened on the last two lines, since $A,B$ are arbitrary constants I just changed em while keeping the same symbol [[opaiwjfafw|for convenience]]. 

Now the fun proof, what the fuq to do when $\alpha_{1} = \alpha_{2}  = \alpha$, well it's actually quite simple really basically we just need to find another valid function of $y$ for [[solving linear homogeneous constant-coefficient equations#^{9d621e]] which is [[linearly dependent and independent functions|linearly independent]] of $y=e^{\apha x}$, lets guess $y=e^{-\gamma x}$: 

$$\begin{align*}
 \frac{d^{2}y}{dx^{2}} + f \frac{dy}{dx} + g y &= 0 & y&=e^{-\gamma x}\\
 & & \frac{dy}{dx} &= -\gamma e^{-\gamma x}\\
 & & \frac{dy^{2}}{dx^{2}} &= \gamma^{2} e^{-\gamma x}\\
\gamma^{2} e^{-\gamma x} - f \gamma e^{-\gamma x} + g e^{-\gamma x} &= 0\\
\gamma^{2} - f \gamma + g &= 0
\end{align*}$$
And then the method is the same as normal:

$$ \gamma = \frac{--f \pm \sqrt{ f^{2} - 4g } }{2} $$

It should be noted that the term $\sqrt{ f^{2} - 4g }$ being zero is what causes $\alpha$ to only have a single root, which also applies to $\gamma$ but this also means that:
$$\begin{align*}
 \gamma &= \frac{f \pm \sqrt{ f^{2} - 4g } }{2} & \alpha &= \frac{-f \pm \sqrt{ f^{2} - 4g } }{2} & f^{2} - 4g &= 0 \\
\gamma &= \frac{f  }{2} & \alpha &= -\frac{f   }{2}\\
 \gamma &= -\alpha
\end{align*}$$

So now we have two [[linearly dependent and independent functions|linearly independent functions]] for $y$: $y_{1} = e^{\alpha x}, y_{2} = e^{-\alpha x}$
which subbed back gets:
$$\begin{align*}
y &= A \times y_{1} (x) + B \times y_{2} (x)\\
y &= e^{\alpha x} + B e^{-\alpha x}
\end{align*}$$

### Method (for constant coefficients)

^dfa318

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