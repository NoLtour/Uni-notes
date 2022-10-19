---
aliases: [""]
tags: []
---

## Complex fourier series
[[It took me 20 mins to find this in my meme folder|Fourier complex? I find it quite simple.]]


Pretty much take the complex trig identities and apply them to the [[Fourier Series Overview|Fourier series]] stuff:

$$\begin{align*}
f(x) &= \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ a_{n} \cos \left( \frac{n\pi}{L} x \right) + b_{n} \sin \left(\frac{n\pi}{L} x\right) \right] & \sin(A) &= \frac{1}{2j} ( e^{jA} - e^{-jA} ) & \cos(A) &= \frac{1}{2} ( e^{jA} + e^{-jA} )\\
&= \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ a_{n} \frac{1}{2} \left( e^{j\frac{n\pi}{L} x  } + e^{-j\frac{n\pi}{L} x} \right)+ b_{n} \frac{1}{2j} \left( e^{j\frac{n\pi}{L} x  } - e^{-j\frac{n\pi}{L} x} \right)  \right]\\
&= \frac{1}{2}a_{0} + \sum\limits^{\infty}_{n=1} \left[\frac{1}{2} ( a_{n} - jb_{n} )  e^{j\frac{n\pi x}{L} }\right] + \sum\limits^{\infty}_{n=1} \left[\frac{1}{2} ( a_{n} + jb_{n} )  e^{-j\frac{n\pi x}{L} }\right]\\
&... \: (\text{some algerbraic magic})\\
&= \sum\limits^{\infty}_{n=-\infty} c_{n} e^{\frac{jn\pi x}{L}} & c_{n} &= \begin{dcases} \frac{1}{2}(a_{n} - jb_{n}) & n>0\\
\frac{1}{2}a_{0} & n=0\\
\frac{1}{2}(a_{-n} + jb_{-n}) & n<0 \end{dcases}
\end{align*}$$
 
> ## $$ \begin{align*} f(x)  & = \sum\limits^{\infty}_{n=-\infty} c_{n} e^{\frac{jn\pi x}{L}} & & & c_{n} &= \begin{dcases} \frac{1}{2}(a_{n} - jb_{n}) & n>0\\\frac{1}{2}a_{0} & n=0\\\frac{1}{2}(a_{-n} + jb_{-n}) & n<0 \end{dcases} \end{align*} $$  
>> where:
>> $f(x)=$ some function
>> $j=\sqrt{-1}$
>> $a_{0}=$ a constant to be found
>> $a_{n},b_{n}=$ the $n$th constant to be calculated
>> $c_{n} = \begin{dcases} \frac{1}{2}(a_{n} - jb_{n}) & n>0\\\frac{1}{2}a_{0} & n=0\\\frac{1}{2}(a_{-n} + jb_{-n}) & n<0 \end{dcases}$ 

