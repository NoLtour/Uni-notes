---
aliases: ["GLD"]
tags: []
---

## General lift distrobution for a finite wing
### Results
#### Elliptic lift distrobution in fourier form

The elliptic lift distrobution when converted to fourier series form becomes:
$$\begin{align*}
B_{1} &= \frac{\Gamma_{0}}{2bV_{\infty}}, & B_{n}  &= 0 \: \{n>1\}
\end{align*}$$
So all infinite sums of $B_{n}\times(...)$ only require the consideration of $B_{1}$.

#### Equations

> ### $$\begin{align*} \text{Circulation distrobution equation:}&& \Gamma(\theta) &= 2b V_{\infty} \sum\limits^{\infty}_{n=1} B_{n} \sin (n\theta)\\\\ \text{Fundemental equation:}& & \alpha(\theta_{0})  - \alpha_{L=0} (\theta_{0}) &= \sum\limits^{\infty}_{n=1} B_{n}\sin(n\theta_{0}) \left[ \frac{4b}{a_{0} c(\theta_{0})} + \frac{n}{\sin\theta_{0}} \right]\\ && \alpha(y_{0})  - \alpha_{L=0} (y_{0}) &= \frac{2\Gamma(y_{0})}{a_{0} V_{\infty} c(y_{0})} +\frac{1}{4\pi V_{\infty}} \int^{\frac{b}{2}}_{- \frac{b}{2}} \frac{\frac{d\Gamma}{dy}}{y_{0}-y} dy \\\\ \text{Lift coefficient:}& &C_{L}&= \pi A B_{1}\\\\ \text{Induced drag coefficient:}&& C_{Di} &=  \frac{C_{L}^{2}}{\pi A}(1+\delta)\\ && &= \frac{C_{L}^{2}}{\pi eA} \\\\ \text{Induced drag factor:}& & \delta &= \sum\limits^{\infty}_{n=2}n \left( \frac{B_{n}}{B_{1}} \right)^{2}, & \delta\geq 0 \\\\ \text{Angular position:}& & \theta &= - \frac{b}{2} \cos\theta \end{align*}$$
>> where:
>> $B_{n}=$  Coefficient of the [[defining the fourier series|Fourier series]] for the lift distrobution of some equation within finite wing theory
>> $\Gamma=$ Circulation at some point along the wing
>> $b=$ [[Wing span]]
>> $\alpha_{i}=$ [[Prandtls lifting line theory|induced AoA for a finite wing]] at that point on the wing
>> $\alpha_{L=0}=$ [[no lift angle]] at that point on the wing
>> $a_0=$ lift curve slope of foil at that point on wing (typically around $2\pi$)
>> $\theta_{0}=$ a variable that represents position along the span in angular form such that $0\leq \theta_{0}\leq \pi$
>> $c=$ chord length at some point along the wing
>> $C_{L}=$ lift coefficient
>> $C_{Di}=$ [[induced drag coefficient]]
>> $S=$ [[Wing plan area]]
>> $A=$ [[wing aspect ratio]]
>> $b=$ [[Wing span]]
>> $e= \frac{1}{1+\delta}=$ [[Oswald efficiency factor]]
>> $\delta=$ [[induced drag factor]]


#### Finding $B_{n}$
Well all this analysis is great and all but how the fuck does it help us if we don't know what $B$ is? You can just do normal [[defining the fourier series|Fourier series]] calculation if your given a function of $\Gamma$ but in the event that isn't the case it can be found numerically.
For $B_{n}$ to be valid it must satisfy the [[Prandtls lifting line theory]], so it must satisfy:
$$\begin{align*}
\sum\limits^{\infty}_{n=1} B_{n}\sin(n\theta_{0}) \left[ \frac{4b}{a_{0} c(\theta_{0})} + \frac{n}{\sin\theta_{0}} \right] &= \alpha(\theta_{0})  - \alpha_{L=0} (\theta_{0})
\end{align*}$$

For a defined wing geometry everything in the equation above should be known except $B_{n}$, so it can be re written so that:
$$\begin{align*}
e_{j,n} &= B_{n}\sin(n\theta_{0}) \left[ \frac{4b}{a_{0} c(\theta_{0})} + \frac{n}{\sin\theta_{0}} \right]  & f_{j} &= \alpha(\theta_{0})  - \alpha_{L=0} (\theta_{0})
\end{align*}$$

$$\begin{align*}
\sum\limits^{\infty}_{n=1} B_{n}\sin(n\theta_{0}) \left[ \frac{4b}{a_{0} c(\theta_{0})} + \frac{n}{\sin\theta_{0}} \right] &= \alpha(\theta_{0})  - \alpha_{L=0} (\theta_{0}) & &\to & \sum\limits^{\infty}_{n=1} B_{n} e_{j,n} &= f_{j}
\end{align*}$$

Keep in mind that this equation is something that descibes the relationship between it's variables at any point along the wings span (here using $\theta_0$ as position along the span). So to solve the equation we must solve for $B_{n}$ while sampling at all points along the wing (since the geometry is discrete it's an infinite amount):

$$\begin{align*}
\sum\limits^{\infty}_{n=1} B_{n} e_{j,n} &= f_{j}
\end{align*}$$
Find $B_{1},B_{2},B_{3}...B_{\infty}$ from:
$$\begin{align*}
B_{1} e_{1,1} + B_{2} e_{1,2} + ... + B_{\infty} e_{1,\infty} &= f_{1}\\
B_{1} e_{2,1} + B_{2} e_{2,2} + ... + B_{\infty} e_{2,\infty} &= f_{2}\\
&...\\
B_{1} e_{\infty,1} + B_{2} e_{\infty,2} + ... + B_{\infty} e_{\infty,\infty} &= f_{\infty}\\
\end{align*}$$
Since in reality this is just a set of linear equations we can actually solve it using matrices (from [[solving linear equations with matricies]]):
$$\begin{align*}
\begin{pmatrix} e_{1,1} & e_{1,2} & ... & e_{1,\infty} \\ e_{2,1} & e_{2,2} & ... & e_{2,\infty} \\ ... & ... & ... & ... \\ e_{\infty,1} & e_{\infty,2} & ... &e_{\infty,\infty} \end{pmatrix} \begin{pmatrix} B_{1}\\ B_{2}\\... \\B_\infty \end{pmatrix} &= \begin{pmatrix} f_{1}\\ f_{2}\\... \\f_\infty \end{pmatrix}\\
 \begin{pmatrix} B_{1}\\ B_{2}\\... \\B_\infty \end{pmatrix} &= \begin{pmatrix} e_{1,1} & e_{1,2} & ... & e_{1,\infty} \\ e_{2,1} & e_{2,2} & ... & e_{2,\infty} \\ ... & ... & ... & ... \\ e_{\infty,1} & e_{\infty,2} & ... &e_{\infty,\infty} \end{pmatrix}^{-1} \begin{pmatrix} f_{1}\\ f_{2}\\... \\f_\infty \end{pmatrix}
\end{align*}$$

So nice and simple, just got to invert an infinite matrix to get an infinite set of $B$'s and a lovely exact defenition of our lift distrobution... easy! Now some people would call doing that "litterally impossible", so we may have to make some approximations. Instead of using an infinite sample along the wing span we can switch that $\infty$ out for $N$ samples:
![[Pasted image 20221221203003.png]]
This way our infinite equation becomes a hell of a lot more manageable:
$$\begin{align*}
\sum\limits^{\infty}_{n=1} B_{n} e_{j,n} &= f_{j} & &\to & \sum\limits^{N}_{n=1} B_{n} e_{j,n} &= f_{j}
\end{align*}$$

This then makes our infinite matrix finite and actually solveable:
$$\begin{align*}
\begin{pmatrix} B_{1}\\ B_{2}\\... \\B_ N \end{pmatrix} &= \begin{pmatrix} e_{1,1} & e_{1,2} & ... & e_{1, N} \\ e_{2,1} & e_{2,2} & ... & e_{2, N} \\ ... & ... & ... & ... \\ e_{ N,1} & e_{ N,2} & ... &e_{ N, N} \end{pmatrix}^{-1} \begin{pmatrix} f_{1}\\ f_{2}\\... \\f_ N \end{pmatrix}
\end{align*}$$

(The reason why the sample count corresponds to the number of $B$'s found is because for the equations to be solveable we'll need a square matrix)
Of course the large $N$ is the closer the values of $B$ found are to the real values and the more accurate our approximation, if you want useful data this is where computers come in because even small numbers of $N$ are waaay to hard to do manually ([[gets 4x4 matrix inverting PTSD|not hard but looooooong]])

### Derivation
#### Lift distrobution
So in the previous case, [[elliptic lift distrobution analysis|elliptic lift distrobution]] was "easy" because we had a defined equation for $\Gamma$ along the wing span. What about the situation where the function $\Gamma$ is not so conveniently defined? Here we will make a framework for getting the characteristics of any arbitrary function of $\Gamma$. Thing is we know that to derive useful information there is going to be a bunch of integration and differentitation so if only there was some way to express any function in a way that would be easy to apply calculus too...... Introducing [[defining the fourier series|Fourier series]] which can be used to express any function (with limitations that don't really apply to this use case) while being easy to integrate/differentiate even with no defined function!!!! ([[I am conflicted on the one hand ewwwwww on the other hand hella based|it's actually really cool]])

So pretty much, take the arbitry function $\Gamma$ and express it as a [[defining the fourier series|Fourier series]], since everything's unknown we can just jump strait to angular form since there's no reason to start as a function of $y$ like we did for [[elliptic lift distrobution analysis]]:

$$\begin{align*}
\Gamma(\theta) &= \:???? & &\to & \Gamma(\theta) &= 2b V_{\infty} \sum\limits^{\infty}_{n=1} B_{n} \sin (n\theta)
\end{align*}$$

Here since we know according to the boundary conditions $\Gamma=0$ at the limits of the wing tips it's clear there will be no $\cos$ component to the equation which allows us to simplify to what's above:
![[Pasted image 20221221115230.png]]

#### Substitution into [[Prandtls lifting line theory#Fundamental equation of lifting line theory|fundamental equation of lifting line theory]]

So starting with the [[Prandtls lifting line theory|fundamental equation of lifting line theory]]:

$$\begin{align*}
\frac{2\Gamma(y_{0})}{a_{0} V_{\infty} c(y_{0})} + \frac{1}{4\pi V_{\infty}} \int^{\frac{b}{2}}_{- \frac{b}{2}} \frac{ \frac{d\Gamma}{dy}  }{ y_{0} - y} dy &= \alpha(y_{0}) - \alpha_{L=0}(y_{0})\\
\frac{C_{l}}{a_{0}} + \alpha_{i} &= \alpha  - \alpha_{L=0} 
\end{align*}$$

Looking back on how we actually derived this, it's clear you can also express it in this alternative form... since $\alpha$ and $\alpha_{L=0}$ are just some general function of span we can just describe them as general functions of $\theta_{0}$ so they function in the angular domain:
$$\begin{align*}
&\alpha(y_{0}) & &\to & &\alpha(\theta_{0})\\
& \alpha_{L=0}(y_{0})& &\to & &\alpha_{L=0}(\theta_{0})
\end{align*}$$

Now we just need to convert the LHS of the equation into the angular domain (for easyer manipulation later). Starting with the $\alpha_{i}$ bit, which is a pain in the ass, firstly we can take our nice [[defining the fourier series|Fourier series]] form of $\Gamma(\theta)$ and differentiate it:

$$\begin{align*}
\Gamma(\theta) &= 2b V_{\infty} \sum\limits^{\infty}_{n=1} B_{n} \sin (n\theta) & &\to & \frac{d\Gamma}{d\theta} &= 2bV_{\infty} \sum\limits^{\infty}_{n=1} nB_{n} \cos (n\theta)
\end{align*}$$

Then we just do some manipulation on the equation of $\alpha_{i}$ so that it is in angular form and sub in that ^, we'll need the defenitions from angular domain just like we used in [[elliptic lift distrobution analysis]]:
$$\begin{align*}
y &= - \frac{b}{2}\cos\theta  & y_{0} &= - \frac{b}{2}\cos\theta_{0}
\end{align*}$$


$$\begin{align*}
\alpha_{i}(y) &= \frac{1}{4\pi V_{\infty}} \int^{\frac{b}{2}}_{- \frac{b}{2}} \frac{ \frac{d\Gamma}{dy}  }{ y_{0} - y} dy & &\to & \alpha_{i}(\theta) &= \frac{1}{4\pi V_{\infty}} \int^{\pi}_{0} \frac{ \frac{d\Gamma}{d\theta}  }{ - \frac{b}{2}\cos\theta_{0} - - \frac{b}{2}\cos\theta } d\theta\\
&& && &= \frac{1}{4\pi V_{\infty}} \int^{\pi}_{0} \frac{ 2bV_{\infty} \sum\limits^{\infty}_{n=1} nB_{n} \cos (n\theta) }{ - \frac{b}{2}\cos\theta_{0} - - \frac{b}{2}\cos\theta}  d\theta\\
&& && &...\\
&& && \alpha_{i} (\theta) &= \frac{1}{\pi} \sum\limits^{\infty}_{n=1} nB_{n} \int^{\pi}_{0} \frac{\cos(n\theta)}{\cos\theta - \cos\theta_{0}} \: d\theta\\
&& && &= \sum\limits^{\infty}_{n=1} nB_{n} \frac{\sin(n\theta_{0})}{\sin\theta_{0}}
\end{align*}$$

Still not done, got to convert the $\frac{C_{l}}{a_{0}}$ bit into the angular domain and use the equation of $\Gamma$ too:
$$\begin{align*}
 \frac{C_{l}}{a_{0}}  &= \frac{2\Gamma(y_{0})}{a_{0} V_{\infty} c(y_{0})} & &\to & \frac{C_{l}}{a_{0}}  &= \frac{2}{a_{0} V_{\infty} c(\theta_{0})}\Gamma(\theta_{0})\\
 && && &= \frac{2}{a_{0} V_{\infty} c(\theta_{0})}2b V_{\infty} \sum\limits^{\infty}_{n=1} B_{n} \sin (n\theta_{0})\\ 
 && && &= \frac{4 b  }{a_{0}  c(\theta_{0})} \sum\limits^{\infty}_{n=1} B_{n} \sin (n\theta_{0})\\
\end{align*}$$

Now we can sub all these to get our new [[Prandtls lifting line theory|fundamental equation of lifting line theory]] in angular form:
$$\begin{align*}
\frac{C_{l}}{a_{0}} + \alpha_{i} &= \alpha  - \alpha_{L=0}  & &\to & \frac{4 b  }{a_{0}  c(\theta_{0})} \sum\limits^{\infty}_{n=1} B_{n} \sin (n\theta_{0}) + \sum\limits^{\infty}_{n=1} nB_{n} \frac{\sin(n\theta_{0})}{\sin\theta_{0}} &= \alpha(\theta_{0})  - \alpha_{L=0} (\theta_{0})\\
&& && &...\\
&& && \sum\limits^{\infty}_{n=1} B_{n}\sin(n\theta_{0}) \left[ \frac{4b}{a_{0} c(\theta_{0})} + \frac{n}{\sin\theta_{0}} \right] &= \alpha(\theta_{0})  - \alpha_{L=0} (\theta_{0})
\end{align*}$$

This final form of the equation is known as the Fourier series form of the [[Prandtls lifting line theory]] equation for general lift distrobution.

#### Lift coefficient

Same procedure as usual, subbing into [[Kutta-Joukowski Theorem]] and then integrating over the wing span and converting the integral to angular domain:

$$\begin{align*}
C_{L} &= \frac{1}{\frac{1}{2}\rho V_{\infty}^{2} S} L & L&= \int^{\frac{b}{2}}_{- \frac{b}{2}}  L'\:dy & L' &= \rho V_{\infty}\Gamma & \Gamma(\theta) &= 2b V_{\infty} \sum\limits^{\infty}_{n=1} B_{n} \sin (n\theta)\\
\end{align*}$$
$$\begin{align*}
C_{L} &= \frac{1}{\frac{1}{2}\rho V_{\infty}^{2} S} \int^{\frac{b}{2}}_{- \frac{b}{2}} \rho V_{\infty}\left(2b V_{\infty} \sum\limits^{\infty}_{n=1} B_{n} \sin (n\theta)\right) \:dy\\
&...\\
C_{L} &= \frac{2 b^{2}}{S} \sum\limits^{\infty}_{n=1} B_{n} \int^{\pi}_{0} \sin (n\theta) \sin \theta \: d\theta\\
& & \int^{\pi}_{0} \sin (n\theta) \sin(m\theta) \: d\theta &=  \begin{dcases} &\frac{1}{2}\pi &\text{when: } n=m\\ &0 &\text{when: } n\neq m \end{dcases}\\
&= \frac{2 b^{2}}{S} B_{1} \frac{1}{2}\pi\\
&= \pi A B_{1}
\end{align*}$$
([[wing aspect ratio]] is $A$)
This is an especially intresting result since thinking back to what $B_{1}$ actually means for the fourier representation of the equation it means that only the part of the [[circulation]] function that contributes to the magnitude of the $\sin(\theta)$ bit of the function contributes to lift... aka this bit:
![[Pasted image 20221221190744.png]]

#### Induced drag

Just like for elliptic lift distrobution analysis for general lift distrobution we start by taking  [[lift and induced drag coefficients for a finite wing]] then sub in:
$$\begin{align*}
C_{Di} &= \frac{2}{V_{\infty} S} \int^{\frac{b}{2}}_{- \frac{b}{2}} \Gamma(y_{0}) \alpha_i(y_{0}) \: dy_{0}\\
&= \frac{2}{V_{\infty}S} \int^{\pi}_{0} \left( 2bV_{\infty} \sum\limits ^{\infty}_{n=1} B_{n}\sin (n\theta) \right) \left( \sum\limits^{\infty}_{m=1} mB_{m} \frac{\sin(m\theta)}{\sin \theta} \right) \frac{dy}{d\theta} d\theta
\end{align*}$$

This equation simplifies greatly by subbing in the definition derived for $C_{L}$ to clean it up and using the following trig identity, which can be applied after expanding out the infinite sum (think about it):
$$\begin{align*}
C_{L} &= \pi A B_{1} &&&& & \int^{\pi}_{0} \sin (n\theta) \sin(m\theta) \: d\theta &=  \begin{dcases} &\frac{1}{2}\pi &\text{when: } n=m\\ &0 &\text{when: } n\neq m \end{dcases}
\end{align*}$$

$$\begin{align*}
C_{Di} &= \frac{2}{V_{\infty}S} \int^{\pi}_{0} \left( 2bV_{\infty} \sum\limits ^{\infty}_{n=1} B_{n}\sin (n\theta) \right) \left( \sum\limits^{\infty}_{m=1} mB_{m} \frac{\sin(m\theta)}{\sin \theta} \right) \frac{dy}{d\theta} d\theta & &\to & C_{Di} &= \pi A \sum\limits^{\infty}_{n=1}nB_{n}^{2}\\
&&&& &=  \pi A \left( B_{1}^{2} + \sum\limits^{\infty}_{n=2}nB_{n}^{2}\right)\\
&&&& &= \pi AB_{1}^{2} \left[ 1 + \sum\limits^{\infty}_{n=2}n \left( \frac{B_{n}}{B_{1}} \right)^{2} \right]\\
&&&& &= \frac{C_{L}^{2}}{\pi A} \left[ 1 + \sum\limits^{\infty}_{n=2}n \left( \frac{B_{n}}{B_{1}} \right)^{2} \right]
\end{align*}$$

The reason we've converted it into this form is that if we allocate the variable $\delta$ to represent the distrobution of the lift such that:
$$\begin{align*}
\delta &= \sum\limits^{\infty}_{n=2}n \left( \frac{B_{n}}{B_{1}} \right)^{2}, & \delta\geq 0
\end{align*}$$
Then it's clear that:
$$\begin{align*}
C_{Di} &=  \frac{C_{L}^{2}}{\pi A}(1+\delta)
\end{align*}$$

If you look at what is discussed in [[general lift distrobution for a finite wing#Elliptic lift distrobution in fourier form]] then it becomes clear that you can actually just use $\delta$ as a measure of deviation from an elliptic lift distrobution, which means that elliptic lift distrobution is the most efficieint lift distrobution possible since an elliptic lift distrobution is the only case in which $\delta=0$.

An alternative form uses the substitution $e= \frac{1}{1+\delta}$ resulting in:
$$\begin{align*}
C_{Di} &= \frac{C_{L}^{2}}{\pi eA}
\end{align*}$$
([[WHAT IS UP WITH PEOPLE USING e FOR THINGS OTHER THAN FUCKING e JUST USE A DIFFERENT VARIABLE YOU CUNTS|I fucking hate this form to a completely justified incredibly high degree]])


