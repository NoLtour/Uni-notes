---
aliases: [""]
tags: []
---

## Complex fourier series
[[It took me 20 mins to find this in my meme folder|Fourier complex? I find it quite simple.]]

### Theory

Pretty much take the complex trig identities and apply them to the [[Fourier Series Overview|Fourier series]] stuff:

$$\begin{align*}
f(x) &= \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ a_{n} \cos \left( \frac{n\pi}{L} x \right) + b_{n} \sin \left(\frac{n\pi}{L} x\right) \right] & \sin(A) &= \frac{1}{2j} ( e^{jA} - e^{-jA} ) & \cos(A) &= \frac{1}{2} ( e^{jA} + e^{-jA} )\\
&= \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ a_{n} \frac{1}{2} \left( e^{j\frac{n\pi}{L} x  } + e^{-j\frac{n\pi}{L} x} \right)+ b_{n} \frac{1}{2j} \left( e^{j\frac{n\pi}{L} x  } - e^{-j\frac{n\pi}{L} x} \right)  \right]\\
&= \frac{1}{2}a_{0} + \sum\limits^{\infty}_{n=1} \left[\frac{1}{2} ( a_{n} - jb_{n} )  e^{j\frac{n\pi x}{L} }\right] + \sum\limits^{\infty}_{n=1} \left[\frac{1}{2} ( a_{n} + jb_{n} )  e^{-j\frac{n\pi x}{L} }\right]\\
&... \: (\text{some algerbraic magic})\\
f(x) &= \sum\limits^{\infty}_{n=-\infty} c_{n} e^{\frac{jn\pi x}{L}} & c_{n} &= \begin{dcases} \frac{1}{2}(a_{n} - jb_{n}) & n>0\\
\frac{1}{2}a_{0} & n=0\\
\frac{1}{2}(a_{-n} + jb_{-n}) & n<0 \end{dcases}
\end{align*}$$
 
> ## $$ \begin{align*} f(x)  & = \sum\limits^{\infty}_{n=-\infty} c_{n} e^{\frac{jn\pi x}{L}} & c_{n} &= \begin{dcases} \frac{1}{2}(a_{n} - jb_{n}) & n>0\\\frac{1}{2}a_{0} & n=0\\\frac{1}{2}(a_{-n} + jb_{-n}) & n<0 \end{dcases} \\ & = \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1} c_{n} e^{\frac{jn\pi x}{L}} + \sum\limits^{\infty}_{n=1} c_{(-n)} e^{\frac{-jn\pi x}{L}} \\ & = \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1} \left[c_{n} e^{\frac{jn\pi x}{L}} + c_{(-n)} e^{\frac{-jn\pi x}{L}}\right]  \end{align*} $$  
> ### $$ c_{n} = \frac{1}{2L} \int^{L}_{-L} f(x) e^{-j \frac{n\pi x}{L} } \cdot dx $$
> ### $$ a_{0} = \frac{1}{L} \int^{L}_{-L} f(x)  \cdot dx $$
>> where:
>> $f(x)=$ some function
>> $j=\sqrt{-1}$ 
>> $c_{n} =$ the $n$th constant

When dealing with this type of problem, the following identity is very frequently used:

> ## $$ \sin(A) = \frac{1}{2} $$

### Example
![[Pasted image 20221019231102.png]]

