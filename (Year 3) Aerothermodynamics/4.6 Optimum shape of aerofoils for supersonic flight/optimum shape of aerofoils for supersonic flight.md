---
aliases: [""]
tags: []
---

## Optimum shape of aerofoils for supersonic flight

### Equation

> ### $$\begin{align*} C_{D} &= \frac{4}{c\sqrt{ M^{2}_{\infty} - 1}}   \int^{c}_{0}      \left[   \alpha^{2} +   \left(\frac{dh}{dx}  \right)^{2} +   \left( \frac{dy_{c}}{dx} \right)^{2} \right] \:dx \end{align*}$$
> ### $$\begin{align*} &&y_{c}&= 0\\C_{L} &=    \frac{4}{c\sqrt{ M^{2}_{\infty} - 1}}\int^{c}_{0}     \left(  \alpha -  \frac{dy_{c}}{dx}\right) \:dx & &\to & C_{L} &=      \frac{4\alpha}{\sqrt{ M^{2}_{\infty} - 1}} \end{align*}$$
>> where:
>> $C_{D}=$ [[drag coefficient]]
>> $C_{L}=$ [[lift coefficient]]
>> $h=$ thickness
>> $y_{c}=$ camber
>> $c=$ chord
>> $x=$ position along foil length ($0\to c$)

### Generic airfoil definition

A generic definition of an airfoil is as follows:

![[Pasted image 20231123233635.png]]

With angle sign convention:

![[Pasted image 20231123233708.png]]

Making use of the 3 factors used to define an airfoil $h,y_{c},\theta$ we can relate them with 2 equations. For both upper and lower surface:

$$\begin{align*}
\theta_{u} &= \frac{dh}{dx} + \frac{dy_{c}}{dx} - \alpha & \theta_{l} &= \frac{dh}{dx} - \frac{dy_{c}}{dx} + \alpha 
\end{align*}$$

Note that small angle approximations have been used.

### Derivations

#### Lift coefficient

Lift coefficient is simply the integral of sum of pressure coefficient along the foils length:

$$\begin{align*}
&&  C_{p} &=   \frac{2\theta}{\sqrt{ M^{2}_{\infty} - 1}} &&& \theta_{u} &= \frac{dh}{dx} + \frac{dy_{c}}{dx} - \alpha &&& \left.\frac{dy_{c}}{dx}\right|_{x=c} &= 0 \\
&&&&&& \theta_{l} &= \frac{dh}{dx} - \frac{dy_{c}}{dx} + \alpha &&& \left.\frac{dy_{c}}{dx}\right|_{x=0} &= 0 \\
C_{L} &= \frac{1}{c} \int^{c}_{0} (C_{pl} - C_{pu}) \:dx & &\to & C_{L} &= \frac{1}{c} \int^{c}_{0}      \frac{2 }{\sqrt{ M^{2}_{\infty} - 1}}(\theta_{l} - \theta_{u}) \:dx
& &\to & C_{L} &= \frac{1}{c} \int^{c}_{0}      \frac{4}{\sqrt{ M^{2}_{\infty} - 1}}\left(  \alpha -  \frac{dy_{c}}{dx}\right) \:dx
& &\to & C_{L} &=      \frac{4\alpha}{\sqrt{ M^{2}_{\infty} - 1}} 
\end{align*}$$

Interestingly this suggests that camber has no impact on lift generation for supersonic flows.

#### Drag coefficient


Drag coefficient is simply the integral of sum of tangential pressure coefficient along the foils length:


$$\begin{align*}
&&  C_{p} &=   \frac{2\theta}{\sqrt{ M^{2}_{\infty} - 1}} &&& \theta_{u} &= \frac{dh}{dx} + \frac{dy_{c}}{dx} - \alpha \\&&&&&& \theta_{l} &= \frac{dh}{dx} - \frac{dy_{c}}{dx} + \alpha  \\ 
C_{D} &= \frac{1}{c} \int^{c}_{0} (C_{pl}\theta_{l} - C_{pu}\theta_{u}) \:dx & &\to & C_{D} &= \frac{1}{c} \int^{c}_{0}      \frac{2 }{\sqrt{ M^{2}_{\infty} - 1}}(\theta^{2}_{l} - \theta^{2}_{u}) \:dx
& &\to & C_{D} &= \frac{2}{\sqrt{ M^{2}_{\infty} - 1}} \frac{1}{c} \int^{c}_{0}      \left[ 2 \alpha^{2} +   \left(\frac{dh}{dx} -\frac{dy_{c}}{dx} \right)^{2} +   \left(\frac{dh}{dx} +\frac{dy_{c}}{dx} \right)^{2} \right] \:dx
\end{align*}$$

Then simplifying further:

$$\begin{align*} 
C_{D} &= \frac{2}{\sqrt{ M^{2}_{\infty} - 1}} \frac{1}{c} \int^{c}_{0}      \left[ 2 \alpha^{2} +   \left(\frac{dh}{dx} -\frac{dy_{c}}{dx} \right)^{2} +   \left(\frac{dh}{dx} +\frac{dy_{c}}{dx} \right)^{2} \right] \:dx \:dx & &\to & 
C_{D} &= \frac{4}{c\sqrt{ M^{2}_{\infty} - 1}}   \int^{c}_{0}      \left[   \alpha^{2} +   \left(\frac{dh}{dx}  \right)^{2} +   \left( \frac{dy_{c}}{dx} \right)^{2} \right] \:dx
\end{align*}$$

This result tells us that camber and thickness both increase drag for any non zero value:
- Camber can be set to zero in designing an airfoil
- A airfoil cannot have zero thickness for structural reasons

#### Optimising a airfoil

![[Pasted image 20231124000215.png]]

Let's design an arbitrary airfoil, here we define it using:
$$\begin{align*}
h(x) &= \frac{tx}{2k} + f(x) &&\to& \frac{dh}{dx} &= \frac{t}{2k} + \frac{df}{dx}   & &\text{when: } x\leq k\\\\\\
h(x) &= \frac{t(c-x)}{2(c-k)} + g(x) &&\to& \frac{dh}{dx} &= -\frac{t}{2(c-k)} + \frac{dg}{dx}  & &\text{when: } x>k 
\end{align*}$$

What these equations simply describe is that the thickness is the sum of a straight line to the thickest point plus some arbitrary function $f$ and $g$.

Based on what was previously discussed, minimum drag requires us to minimise:

$$\begin{align*}
C_{D} &= \frac{4}{c\sqrt{ M^{2}_{\infty} - 1}}   \int^{c}_{0}      \left[   \alpha^{2} +   \left(\frac{dh}{dx}  \right)^{2} +   \left( \frac{dy_{c}}{dx} \right)^{2} \right] \:dx & &\to &  
\text{minimum }  \int^{c}_{0}      \left(\frac{dh}{dx}\right)^{2}  \:\:dx
\end{align*}$$

So subbing to find minimum:

$$\begin{align*}
&\int^{c}_{0} \left(\frac{dh}{dx}\right)^{2}  \:dx & &\to 
&\int^{c}_{k} \left( \frac{t}{2k} + \frac{df}{dx}  \right)^{2}  \:dx  + \int^{k}_{c} \left( -\frac{t}{2(c-k)} + \frac{dg}{dx} \right)^{2}  \:dx  & &\to & 
&\int^{c}_{k} \left[ \frac{t^{2}}{4k^{2}} + \left(\frac{df}{dx}\right)^{2}  + 2 \frac{df}{dx} \frac{t}{2k}  \right]  \:dx  + \int^{k}_{c} \left[  \frac{t^{2}}{4(c-k)^{2}} + \left(\frac{dg}{dx}\right)^{2} -2\frac{dg}{dx}\frac{t}{2(c-k)} \right]   \:dx 
\end{align*}$$

It's obvious that to minimise this integrals result we want
$$\begin{align*}
 && \left.\frac{dh}{dx}\right|_{x=0,k} &= 0 \\
 && \left.\frac{dg}{dx}\right|_{x=k,c} &= 0 \\
&\int^{c}_{k} \left[ \frac{t^{2}}{4k^{2}} + \left(\frac{df}{dx}\right)^{2}  + 2 \frac{df}{dx} \frac{t}{2k}  \right]  \:dx  + \int^{k}_{c} \left[  \frac{t^{2}}{4(c-k)^{2}} + \left(\frac{dg}{dx}\right)^{2} -2\frac{dg}{dx}\frac{t}{2(c-k)} \right]   \:dx  & &\to &
&\int^{c}_{k} \left[ \frac{t^{2}}{4k^{2}} + \left(\frac{df}{dx}\right)^{2}   \right]  \:dx  + \int^{k}_{c} \left[  \frac{t^{2}}{4(c-k)^{2}} + \left(\frac{dg}{dx}\right)^{2}   \right]   \:dx 
\end{align*}$$

Looking at this equation it becomes apparent that any non zero value of $h(x)$ and $g(x)$ just increases drag. So we should just set them both to zero. Reflecting upon what this means in out context, the "optimum" airfoil will be some sort of diamond shape.

$$\begin{align*}
&\int^{c}_{k} \left[ \frac{t^{2}}{4k^{2}} + \left(\frac{df}{dx}\right)^{2}   \right]  \:dx  + \int^{k}_{c} \left[  \frac{t^{2}}{4(c-k)^{2}} + \left(\frac{dg}{dx}\right)^{2}   \right]   \:dx  & &\to & &\int^{c}_{k}   \frac{t^{2}}{4k^{2}}    \:dx  + \int^{k}_{c}  \frac{t^{2}}{4(c-k)^{2}}     \:dx &&\to& \frac{t^{2}}{4} \left(\frac{1}{k} + \frac{1}{c-k}\right)
\end{align*}$$

Now we can find the minimum drag point for $k$ by finding the turning point:

$$\begin{align*}
\frac{d}{dk} \frac{t^{2}}{4} \left(\frac{1}{k} + \frac{1}{c-k}\right) &= 0 & &\to& 0 &= - \frac{1}{k^{2}} + \frac{1}{(c-k)^{2}} & &\to& k^{2} &= c^{2} - 2kc + k^{2} & &\to & k &= \frac{c}{2}
\end{align*}$$

So minimum drag airfoil is nothing more than a diamond with max thickness at the centre!

![[Pasted image 20231124004448.png]]

Some thing's to note:
- Lowest drag when as thin as possible (within structural constraints)
- Ignores effects of viscosity and off-design issues (take-off, landing and low-speed performance)