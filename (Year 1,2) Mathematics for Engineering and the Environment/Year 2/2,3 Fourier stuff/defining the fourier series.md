---
aliases: ["Fourier series","french propaganda (vomit)"]
tags: []
---

## Defining the Fourier series
(ngl this sounds [[French|Fr*nch]]. (I looked it up, it is Fr\*nch [[ahhhhhhhhhhhhhhhhh FRENCH|:anguish:]], [[ewwwwwwwwwwwwwww Frnch|terrible]] ))

### Definition

> ### $$ f(x) = \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ a_{n} \cos \left( \frac{n\pi}{L} x \right) + b_{n} \sin \left(\frac{n\pi}{L} x\right) \right] $$ 
>> where:
>> $f(x)=f(x+2L)=$ a periodic function (it repeats perfectly every $2L$)
>> $a_{0}=$ a offset constant (offsets the function from an average of 0)
>> $a_{n},b_{n}=$ the $n$th constant related to $\cos$ and $\sin$ respectively
>> $L=$ half the period of the function

^3f0fc8

The constants $a_{n},b_{n}$ usually end up being defined as a function of $n$ which when solved allows you to calculate the constants $a_{1},a_{2},a_{3}...$ where the more constants calculated the closer the approximation of the original periodic function $f(x)$.

(CBA to do the proof, just look it up)

#### Finding the constants

> ### $$ a_{m} = \frac{1}{L} \int^{R_{1}}_{R_{2}} f(x) \cos\left(\frac{n\pi}{L} x\right) \cdot dx $$ 
> ### $$ b_{m} = \frac{1}{L} \int^{R_{1}}_{R_{2}} f(x) \sin\left(\frac{n\pi}{L} x\right) \cdot dx $$ 
> ### $$ a_{0} = \frac{1}{L} \int^{R_{1}}_{R_{2}} f(x) \cdot dx $$
>> where:
>> $a_{m}=$ often expands to a function defining the $n$th $a$ constant in terms of $m$.
>> $b_{m}=$ often expands to a function defining the $n$th $b$ constant in terms of $m$.
>> $f(x)=f(x+2L)=$ a periodic function (it repeats perfectly every $2L$)
>> $L=$ half the period of the function
>> $R_{1},R_{2}=$ a region the functions defined over, often this is just $R_{1}=L$ and $R_{2}=-L$

^918760

### Example (Sawtooth function)
> Find the [[Fourier Series Overview|Fourier series]] for:
> ![[Pasted image 20221011090614.png]]

From the graph we can clearly see that the function is $f(x)=x$ in the range $-\pi\leq x \leq \pi$ repeating every $2\pi$. 

So now we just sub the function into [[defining the fourier series#^918760|these equations]] and solve to get definitions for the constants.

$$\begin{align*}
a_{m} &= \frac{1}{\pi} \int^{\pi}_{-\pi} f(x) \cos(mx) \cdot dx & f(x) = x\\
&= \frac{1}{\pi} \int^{\pi}_{-\pi} x \cos(mx) \cdot dx
\end{align*}$$

Here we have to use [[Integration by parts]] which gives:
$$\begin{align*}
a_{m} &= \frac{1}{\pi}\left(  \left[ \frac{1}{m} x \sin (mx) \right]^{\pi}_{-\pi} - \int^{\pi}_{-\pi} \frac{1}{m} \sin(mx) \cdot dx \right)\\
a_{m} &= \frac{1}{\pi}\left(  \left[ \frac{1}{m} x \sin (mx) \right]^{\pi}_{-\pi} - \left[ \frac{-\cos(mx)}{m^{2}}    
\right]^{\pi}_{-\pi} \right)\\
&= \frac{1}{\pi} \left( \frac{\pi 0 - \pi 0}{m} + \frac{\cos(m\pi) - \cos(m\pi)}{m^{2}} \right)\\
a_{m} &= 0
\end{align*}$$

NOTE: For the last part I used the identity $\cos(k\pi)=(-1)^{k}$ where $k$ is any integer. And $\sin(k\pi)=0$ where $k$ is any integer. ^7a2fe6

Then we find $b_{m}$ subbing once again into [[defining the fourier series#^918760|these equations]]:
$$\begin{align*}
b_{m} &= \frac{1}{\pi} \int^{\pi}_{-\pi} f(x) \sin(mx) \cdot dx & f(x) = x\\
&= \frac{1}{\pi} \int^{\pi}_{-\pi} x \sin(mx) \cdot dx
\end{align*}$$

Here we also have to use [[Integration by parts]] which gives:
$$\begin{align*}
b_{m} &= \frac{1}{\pi}\left(  \left[- \frac{1}{m}\cos(mx)\right]^{\pi}_{-\pi} - \int^{\pi}_{-\pi} - \frac{1}{m} \cos(mx) \cdot dx \right)\\
 &= \frac{1}{\pi}\left(  \left[- \frac{1}{m}\cos(mx) 
+ \frac{\sin(mx)}{m^{2}} \right]^{\pi}_{-\pi} \right)\\
 &= \frac{1}{\pi}\left( \frac{-2\pi\cos(m\pi)}{m} + \frac{2\sin(m\pi)}{m^{2}} \right)\\
&= \frac{-2(-1)^{m}}{m} + 0\\
b_{m} &= \frac{2(-1)^{m+1}}{m}
\end{align*}$$

NOTE: I did [[defining the fourier series#^7a2fe6|this]] again for the last steps.

It's clearer to see with $b$ since it's non zero, but the goal here was to get some expression that can define for us $b_{1},b_{2},b_{3}....b_{\infty}$ now all that's left is $a_{0}$.

$$\begin{align*}
a_{0} &= \frac{1}{\pi} \int^{\pi}_{-\pi} f(x) \cdot dx & f(x) &=  x\\
 &= \frac{1}{\pi} \int^{\pi}_{-\pi} x \cdot dx\\
&= \frac{1}{\pi} \left[ \frac{x^{2}}{2} \right]^{\pi}_{-\pi}\\
a_{0} &=0
\end{align*}$$

Now we have all the terms defined we can sub back into the main equation.
$$\begin{align*}
f(x) &= \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}[ a_{n} \cos ( n x ) + b_{n} \sin (n x) ] & a_{0}&=0 & a_{n}&=0 & b_{n} &= \frac{2(-1)^{n+1}}{n}\\
&= \sum\limits^{\infty}_{n=1} \frac{2(-1)^{n+1}}{n} \sin (n x) \\
&= 2 \sin(x) - \sin(2x) + \frac{2}{3}\sin(3x) - \frac{1}{2}\sin(4x) + \frac{2}{5}\sin(5x) - \: .... \: + \frac{2(-1)^{n+1}}{n} \sin (n x)
\end{align*}$$

In a similar way to most series, as you increase the term count it becomes a closer approximation to the actual function:

Something that is worth noting is that in reality $a_{0}$ and $a_{m}$ are obviously going to be zero, in the case of $a_{m}$ this is because the function is clearly a [[odd function]] hence it wont contain any [[even function]]s ($\cos$). The fact that there is no upwards or downwards shift also makes it clear that $a_{0}$ would end up as zero. This will be elaborated in [[shortcuts for the fourier series|this doc]].

Also something worth observing is that the goal of setting up the functions this way is to ensure that when we setup equations that make use of $\sin(?)$ and $\cos(?)$ such that we get functions that simplify to zero or some alternating integer (aka: v$(-1)^{n}$).

![[Pasted image 20221011143249.png]]



### Example: Tent function

> Find the [[Fourier Series Overview|Fourier series]] for:
> ![[Pasted image 20221011163613.png]]

From the graph we can clearly see that the function is $f(x)=|x|$ in the range $-\pi\leq x \leq \pi$ repeating every $2\pi$. 

So now we just sub the function into [[defining the fourier series#^918760|these equations]] and solve to get definitions for the constants.

$$\begin{align*}
a_{0} &= \frac{1}{\pi} \int^{\pi}_{-\pi} f(x) \cdot dx & f(x) &=  |x|\\
 &= \frac{1}{\pi} \int^{\pi}_{-\pi} |x| \cdot dx  \\
&= \frac{1}{\pi} \left( \left[ - \frac{x^{2}}{2} \right]^{0}_{-\pi} + \left[ \frac{x^{2}}{2} \right]^{\pi}_{0} \right)\\
a_{0} &=\pi
\end{align*}$$

Then we calculate $a_{m}$ using integration by parts on $\frac{1}{\pi} \int^{\pi}_{-\pi} |x| \cos(mx) \cdot dx$ (we split it into two parts like this to show the effect of the abs function):

$$\begin{align*}
a_{m} &= \frac{1}{\pi} \left( -\left[ \frac{x\sin(mx)}{m} + \frac{\cos(mx)}{m^{2}} \right]^{0}_{-\pi} + \left[ \frac{x\sin(mx)}{m} + \frac{\cos(mx)}{m^{2}} \right]^{\pi}_{0} \right) \\
 &= \frac{1}{\pi} \left( - \left[ 0 - 0 + \frac{1}{m^{2}} - \frac{(-1)^{m}}{m^{2}} \right] + \left[ 0-0+ \frac{(-1)^{m}}{m^{2}} - \frac{1}{m^{2}} \right] \right) \\
 &= 2 \frac{(-1)^{m} - 1}{\pi m^{2}}
\end{align*}$$

(cba to write up the solution for $b_{m}$ but it's the same sort of thing as above but now it ends up going to zero $b_{m}=0$). In the end you get the equation:

$$\begin{align*}
f(x) &= \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}[ a_{n} \cos ( n x ) + b_{n} \sin (n x) ] & a_{0}&=0 & a_{n}&=2 \frac{(-1)^{n} - 1}{\pi n^{2}} & b_{n} &= 0\\
&=   \sum\limits^{\infty}_{n=1}\left[ 2 \frac{(-1)^{n} - 1}{\pi n^{2}} \cos ( n x )  \right]   
\end{align*}$$

Which when expanded approximates the function, and you can see it quickly gets quite accurate by the following:

![[Pasted image 20221013115321.png]]


