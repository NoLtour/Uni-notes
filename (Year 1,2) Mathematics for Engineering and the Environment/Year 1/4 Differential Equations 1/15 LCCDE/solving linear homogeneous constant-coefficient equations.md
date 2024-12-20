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

#### Proofing [[solving linear homogeneous constant-coefficient equations#Method (for constant coefficients)|the method]]

##### Normal case

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

##### Complex case

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

##### Single root case
So lets say your formula $\ddot{y}+b\dot{y}+cy=0$ results in $\alpha_{1} = \alpha_{2}$, so mathematically written this means that:

$$\begin{align*}
\ddot{y}+b\dot{y}+cy=0 \:\: \to \:\: \alpha^{2} + b \alpha + c &= 0\\
\alpha &= \frac{-b \pm \sqrt{b^{2} - 4c} }{ 2 } & \sqrt{b^{2} - 4c} &= 0\\
&& c &= \frac{b^{2}}{4}\\
\alpha &= - \frac{b}{2}
\end{align*}$$

Since $\alpha$ is a duplicate root the [[complementary function]] is incomplete since functions $y_{1},y_{2}$ would be identical and hence obviously [[linearly dependent and independent functions|linearly dependent]]. So to get around this we use a method introduced slightly later [[Inhomogeneous linear second order ODEs#When your guess overlaps with a part of the complementary function|(this linked method)]], so we take the original [[ansatz]] (guess) of $y=e^{\alpha x}$ and slap an x onto it hence getting $y=xe^{\lambda x}$ from which we just do the steps that we did originally for the [[solving linear homogeneous constant-coefficient equations#Normal case|first situation]] but with this new equation to get $y_{2}$:

$$\begin{align*}
\ddot{y}+b\dot{y}+\frac{b^{2}}{4}y&=0 & y &= xe^{\lambda x}\\
&& \dot{y} &= x\lambda e^{\lambda x} + e^{ \lambda x }\\
&& \ddot{y} &= \lambda^{2} x e^{ \lambda x } + 2 \lambda e^{\lambda x}\\
\lambda^{2} x e^{ \lambda x } + 2 \lambda e^{\lambda x} + b( x\lambda e^{\lambda x} + e^{ \lambda x } ) + \frac{b^{2}}{4} xe^{\lambda x} &= 0\\
\lambda^{2} x   + 2 \lambda  + b( x\lambda  + 1 ) + \frac{b^{2}}{4} x &=
\end{align*}$$

This can then be split according to like terms:
$$\begin{align*}
 \lambda^{2} x + bx\lambda  + \frac{b^{2}}{4} x &= 0 & 2\lambda + b &= 0\\
\lambda^{2} + b\lambda  + \frac{b^{2}}{4} &= 0 & \lambda  &= - \frac{b}{2} \\
\lambda  &= - \frac{b}{2} \: \: \therefore consistant\\
\lambda &= \alpha
\end{align*}$$

Now we just collect all our terms to make the [[complementary function]]:

$$\begin{align*}
y &= c_{1} y_{1} + c_{2} y_{2} & y_{1} &= e^{\alpha x} &  y_{2} &= xe^{\lambda x} & \lambda &= \alpha\\
y &= c_{1} e^{\alpha x} + c_{2} x e^{\alpha x}\\
y &= e^{\alpha x} (c_{1}  + c_{2} x)
\end{align*}$$

So that's how the thing exists ([[yay the proofs are done kinda excessive lol|pog]])


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