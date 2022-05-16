---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Maclaurin series
### Meth
This is a special form of the [[Taylor series]] where $a=0$, here are what that resaults in:

$$\begin{align*}
f(x+a) &= f(a) + \frac{f^{'}(a) }{1!}x + \frac{f^{''}(a) }{2!}x^{2}+ \frac{f^{'''}(a) }{3!}x^{3}+ \frac{f^{''''}(a) }{4!}x^{4} + ...\\
& & &let\:a=0\\\\
f(x+0) &= f(0) + \frac{f^{'}(0) }{1!}x + \frac{f^{''}(0) }{2!}x^{2}+ \frac{f^{'''}(0) }{3!}x^{3}+ \frac{f^{''''}(0) }{4!}x^{4} + ...\\
f(x) &= f(0) + \frac{f^{'}(0) }{1!}x + \frac{f^{''}(0) }{2!}x^{2}+ \frac{f^{'''}(0) }{3!}x^{3}+ \frac{f^{''''}(0) }{4!}x^{4} + ...
\end{align*}$$

Hence any function can be calculated by:

> ### $$ f(x)= f(0) + \frac{f^{'}(0) }{1!}x + \frac{f^{''}(0) }{2!}x^{2}+ \frac{f^{'''}(0) }{3!}x^{3}+ \frac{f^{''''}(0) }{4!}x^{4} + ... $$ 
>> where:
>> $|x| < 1$ it is quite accurate

Link to [[standard Maclaurin series expansions]]. 

### Example

> Find an approximate value for $e^{0.4}$ using the [[Maclaurin series]]:

$$\begin{align*}
f(x) &= e^{x} & &f(0) = 1\\
f^{'}(x) &= e^{x}& &f^{''}(0) = 1\\
f^{''}(x) &= e^{x}& &f^{'}(0) = 1
\end{align*}$$

$$\begin{align*}
f(x)&= f(0) + \frac{f^{'}(0) }{1!}x + \frac{f^{''}(0) }{2!}x^{2}+ \frac{f^{'''}(0) }{3!}x^{3}+ \frac{f^{''''}(0) }{4!}x^{4} + ...\\
f(x)&\approx 1 + \frac{1}{1}x + \frac{1}{2}x^{2}+ \frac{1}{6}x^{3}+ \frac{1}{24}x^{4} + ... &&let\:x=0.4\\
f(0.4)&\approx 1.491733333
\end{align*}$$

$$\begin{align*}
   e^{0.4} &\approx 1.491733333\\
   e^{0.4} &= 1.4918246
\end{align*}$$

So quite accurate.