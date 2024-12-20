---
aliases: [""]
tags: []
---

## Laplace transform of a derivative

### Useful bit

> ## $$ \mathcal{L} \left[ \frac{df}{dx} \right] = s \tilde{f}(s) - f(0) $$
> ## $$ \mathcal{L} \left[ \frac{d^{2}f}{dx^{2}} \right] = s^{2} \tilde{f}(s) - s f(0) - f'(0) $$
> ## $$ \mathcal{L} \left[ \frac{d^{n}f}{dx^{n}} \right] = s^{n} \tilde{f}(s) - \sum\limits^{n-1}_{k=0} s^{n-(k+1)} f^{k}(0) $$ 
>> where:
>> $\mathcal{L}[...]=$ [[Laplace transform]] function
>> $\tilde{f}(s)=$ [[Laplace transform]] of $f(x)$
>> $s=$ frequency, independent variable of [[Laplace transform]]
>> $f(x)=$ some function
>> $f^{k}(x)=$ kth derivative of some function
>> $x=$ independent variable of function being transformed


### Proof

$$\begin{align*}
\mathcal{L} \left[ \frac{df}{dx} \right] &=  \int^{\infty}_{0} \frac{df}{dx} e^{-sx} \cdot dx\\
  &= uv - \int \dot{u} v & \dot{v} &= \frac{df}{dx} & u &= e^{-sx} \\
& & v &= f(x) & \dot{u} &= -se^{-sx}\\
&= [ e^{-sx}f(x) ]^{\infty}_{0} - \int^{\infty}_{0} -se^{-sx} f(x) \cdot dx\\
&= [ e^{-sx}f(x) ]^{\infty}_{0} + s \int^{\infty}_{0} e^{-sx} f(x) \cdot dx\\
& & \lim_{x\to\infty}e^{-sx}f(x) &= 0\\
&= 0 - e^{0}f(0) + s\tilde{f}(x)\\
\therefore \mathcal{L} \left[ \frac{df}{dx} \right]&= s\tilde{f}(x) - f(0)
\end{align*}$$
