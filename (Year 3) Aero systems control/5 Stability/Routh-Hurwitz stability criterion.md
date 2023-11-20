---
aliases: [""]
tags: []
---

## Routh-Hurwitz stability criterion

#### Intro

We already know that the sign of poles determines system stability ([[summery of relationship between system poles and system response|topic 4]]), but actually finding the poles may not be trivial.

$$\begin{align*}
\frac{C}{R} &= \frac{a_{n} s^{n} + ... + a_{2} s^{2} + a_{1} s + a_{0}  }{b_{n} s^{n} + ... + b_{2} s^{2} + b_{1} s + b_{0}}\\\\
& \downarrow \text{ Step input}\\\\
C &= \frac{a_{n} s^{n} + ... + a_{2} s^{2} + a_{1} s + a_{0}  }{b_{n} s^{n} + ... + b_{2} s^{2} + b_{1} s + b_{0}} \frac{1}{s}\\\\
& \downarrow \text{ Solving for poles}\\\\
C &= \frac{1}{s} \frac{(s - z_{n})...(s - z_{2})(s - z_{1})(s - z_{0})}{(s - p_{n})...(s - p_{2})(s - p_{1})(s - p_{0})} \\\\
& \downarrow \text{ Partial fractions}\\\\
C &= \frac{A_{0}}{s} + \frac{A_{1}}{s-p_{0}}  + \frac{A_{2}}{s-p_{1}} + \frac{A_{2}}{s-p_{2}} + ... +  \frac{A_{n+1}}{s-p_{n}}\\\\
& \downarrow \text{ Inverse Laplace}\\\\
c(t) &= A_{0} + A_{1}e^{p_{0}t}  + A_{2}e^{p_{0}t} + ... + A_{n+1}e^{p_{n}t}
\end{align*}$$

As we found previously, it's clear that if any pole ($p_{i}$) has a positive real component then it's $e$ will increase with $t$, aka unstable.  Determining stability from an equation of any length using some standard procedure would be good. The only information needed about the poles would be the signs.

Course the "solving for the poles" step is trivial for a quadratic. But it becomes basically impossible pretty quickly, so to solve for poles and only get their signs we can use the [[Routh-Hurwitz stability criterion]], [[what did you expect from me lol|roll credits]].

#### Method

The Routh-Hurwitz stability criterion is a method of determining how many poles have positive real components (hence if it's unstable).

This shows the general case method, note that you can only get instability in a system which has feedback loops. Which makes sense.

> #### System
> ![[Pasted image 20231107184646.png]]
> ### $$\begin{align*} &\text{Closed loop transfer function}&&&&\text{Characteristic equation}  \\ &\frac{C}{R}  = \frac{G}{1+GH} & &\to  &&0=1 + GH  \end{align*}$$ 
> ### $$\begin{align*} 0=1+GH= a_{n}s^{n} + a_{n-1}s^{n-1} + a_{n-2}s^{n-2} + a_{n-3}s^{n-3} + ... + a_{1}s + a_{0}  \end{align*}$$ 
> #### The resulting table
> ### $$\begin{align*} &\left.\begin{array}{ccc} s^{n} &|& a_{n} & a_{n-2} & a_{n-4} & ... & 0 \\ s^{n-1} &|& a_{n-1} & a_{n-3} & a_{n-5} & ... & 0 \\ s^{n-2} &|& b_{1,1} & b_{2,1} & b_{3,1} & ... & 0 \\ s^{n-3} &|& b_{1,2} & b_{2,2} & b_{3,2} & ... & 0 \\ s^{n-3} &|& b_{1,3} & b_{2,3} & b_{3,3} & ... & 0 \\ ... &|& ... & ... & ... & ... & ... &    &\\ s^{1} &|& b_{1,m-1} & 0 & 0 & ... &0\\ s^{0}&|& b_{1,m} & 0 & 0 & ... &0\\ \end{array}\right. &&\equiv& & & \left.\begin{array}{ccc} s^{n} &|& x_{1,1} & x_{2,1} & x_{3,1} & ... & 0 \\ s^{n-1} &|& x_{1,2} & x_{2,2} & x_{3,2} & ... & 0 \\ s^{n-2} &|& x_{1,3} & x_{2,3} & x_{3,3} & ... & 0 \\ s^{n-3} &|& x_{1,4} & x_{2,4} & x_{3,4} & ... & 0 \\ s^{n-3} &|& x_{1,5} & x_{2,5} & x_{3,5} & ... & 0 \\ ... &|& ... & ... & ... & ... & ... &    &\\ s^{1} &|& x_{1,m+1} & 0 & 0 & ... &0\\ s^{0}&|& x_{1,m+2} & 0 & 0 & ... &0\\ \end{array}\right. \end{align*}$$
> #### Finding $b$'s
> ### $$\begin{align*} b_{\alpha,\:\beta} &= - \frac{1}{x_{\alpha-1,\:1}} \det \begin{pmatrix} x_{\alpha-2,\:1} & x_{\alpha-2,\:\beta+1} \\ x_{\alpha-1,\:1} & x_{\alpha-1,\:\beta+1} \\ \end{pmatrix} & &\to & b_{1,\:1} &= - \frac{1}{a_{n-1}} \det \begin{pmatrix} a_{n} & a_{n-2} \\ a_{n-1} & a_{n-3} \\ \end{pmatrix}\\&& && b_{2,\:1} &= - \frac{1}{a_{n-1}} \det \begin{pmatrix} a_{n} & a_{n-4} \\ a_{n-1} & a_{n-5} \\ \end{pmatrix} \\ && && &... \\ && && b_{1,\:3} &= - \frac{1}{b_{2,1}} \det \begin{pmatrix} b_{1,1} & b_{2,1} \\ b_{2,1} & b_{2,2} \\ \end{pmatrix}\\ && && b_{2,\:3} &= - \frac{1}{b_{2,1}} \det \begin{pmatrix} b_{1,1} & b_{3,1} \\ b_{2,1} & b_{3,2} \\ \end{pmatrix} \\ && && &... \end{align*}$$ 
> #### The resulting table
>> where:
>> $a=$ characteristic equation constants
>> $b=$ values which need to be found 
>> $\alpha,\:\beta=$ variables for navigating the table
>
>> Stable if:
>> $$\begin{align*} a_{n}, \:a_{n-1}, \:b_{1,1}, \:b_{1,2}, \:b_{1,3},\: ..., \:b_{1,m-1}, \:b_{1,m} \:\: \text{are all the same sign} \end{align*}$$

The Routh-Hurwitz criterion states:
1. A necessary and sufficient condition for stability is that there are no sign changes in the first column of the Routh array.
2. The number of sign changes in the first column is equal to the number of poles in the right half s-plane.
3. If the first element in a row is zero, then it is replaced by a small positive number e and the sign changes when e->0 are counted after completing the array.
4. If all elements in a row are zero, the system has poles in the right half s-plane or on the imaginary axis.

### Example

Not going to type it out, look at slide:

![[Pasted image 20231107202101.png]]
