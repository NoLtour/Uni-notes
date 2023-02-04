---
aliases: ["double integration method"]
tags: ["Question","QFormat3"]
---

#### What is
## Solving statically indeterminate beams with double integration method
### Intro
Ok so this basically just contines from [[solving statically indeterminate beams]].

### Method

1) Find the equalibrium equations
2) Use the method for [[calculating the deflection of a beam]]
3) Use the deflection equation to create more equations relating the unknowns
4) Solve for the unkowns (once you have as many equations as unknowns)

### Example
![[Pasted image 20211129120620.png]]

First we get it into a more useful format:

> ![[Pasted image 20211129120721.png]]

Then a format where we can see the cross section:

> ![[Pasted image 20211129120702.png]]

Now we find it's equalibrium equations:
> Verticle:
> $$\begin{align*}
R_1 +R_2 &= wL 
\end{align*}$$

> Rotational:
> $$\begin{align*}
M_1 + \frac{L}{2} wL &= LR_1
\end{align*}$$

Now we can find the equation for Q and M:
> $$\begin{align*}
M(x) + M_1 + \frac{x}{2} &= xR_1 xw\\
M(x)  &= R_1x - \frac{wx^{2}}{2} - M_1 &   Q(x)&=\frac{d}{dx} M(x) \\
& & &= R_1 - wx
\end{align*}$$

Now we can use the method for [[calculating the deflection of a beam]]:

> $$\begin{align*}
v(x) &= - \frac{1}{IE} \int \int M(x) \cdot dx \cdot dx \\
&= - \frac{1}{IE} \int \int R_1x - \frac{wx^{2}}{2} - M_1 \cdot dx \cdot dx\\
&= - \frac{1}{IE} \int \frac{R_1x^{2}}{2} - \frac{wx^{3}}{6} - M_1x + k_1 \cdot dx & \frac{dv}{dx}(0)&=0\\
& & - \frac{1}{IE}\left(\frac{R_10^{2}}{2} - \frac{w0^{3}}{6} - M_10 + k_1\right)&=0\\
& & k_1&=0\\
&= - \frac{1}{IE} \left(\frac{R_1x^{3}}{6} - \frac{wx^{4}}{24} - \frac{M_1x^{2}}{2} + k_2\right) & v(0) &= 0 \\
& & - \frac{1}{IE} \left(\frac{R_10^{3}}{6} - \frac{w0^{4}}{24} - \frac{M_10^{2}}{2} + k_2\right) &= 0\\
& & k_2&=0\\
\therefore v(x)&= - \frac{1}{IE} \left(\frac{R_1x^{3}}{6} - \frac{wx^{4}}{24} - \frac{M_1x^{2}}{2}\right)
\end{align*}$$

We have an equation for v(x) and we know that $v(L)=0$ this will give us a new equation, which will leave us with 3 equations for our 3 unknowns. Hence we will be able to solve for the values of the unkowns!

> $$\begin{align*}
0 &= - \frac{1}{IE} \left(\frac{R_1L^{3}}{6} - \frac{wL^{4}}{24} - \frac{M_1L^{2}}{2}\right)\\
&= \frac{R_1L^{3}}{6} - \frac{wL^{4}}{24} - \frac{M_1L^{2}}{2}\\
&= \frac{R_1L}{3} - \frac{wL^{2}}{12} - M_1 & M_1 + \frac{L}{2} wL &= LR_1 & R_1 +R_2 &= wL \\
\end{align*}$$

(I don't need to do more math, you get the point. It is possible to solve from here. You then ofc relate to $R_2$.)