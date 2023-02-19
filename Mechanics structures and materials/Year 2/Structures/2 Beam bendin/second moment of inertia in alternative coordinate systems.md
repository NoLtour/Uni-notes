---
aliases: ["determining max rigidity and min rigidity of a asymmetric beam cross section"]
tags: []
---

## Second moment of inertia in alternative coordinate systems

![[Pasted image 20230219163143.png]]

Using trig and a bunch of substitution you can show that:

> ### $$\begin{align*} I_{zz'}  &= \frac{I_{zz}+I_{yy}}{2} + \frac{I_{zz}-I_{yy}}{2} \cos(2\theta) + I_{yz} \sin( 2 \theta )  \end{align*}$$
> ### $$\begin{align*} I_{yy'}  &= \frac{I_{zz}+I_{yy}}{2} + \frac{I_{zz}-I_{yy}}{2} \cos(2\theta) + I_{yz} \sin( 2 \theta ) \text{This is in the nots but I am sure it's wrong} \end{align*}$$
> ### $$\begin{align*} I_{y'z'}  &=  \frac{I_{zz}-I_{yy}}{2} \sin(2\theta) + I_{yz} \cos( 2\theta ) \end{align*}$$
>> where:
>> $=$ 
>> $=$
>> $=$

### Determining max rigidity and min rigidity of a asymmetric beam cross section

This is really ez using the equations above, doing some rearranging:

> ### $$\begin{align*} \tan(2 \theta_{m}) &= \frac{2I_{yz}}{I_{zz}-I_{yy}} \end{align*}$$
> ### $$\begin{align*}  I_{max} &= \frac{I_{z}+I_{y}}{2} + \sqrt{ \left(\frac{I_{zz}-I_{yy}}{2}\right)^{2} + I_{yz}^{2} }  \end{align*}$$
> ### $$\begin{align*}  I_{min} &= \frac{I_{z}+I_{y}}{2} - \sqrt{ \left(\frac{I_{zz}-I_{yy}}{2}\right)^{2} + I_{yz}^{2} }  \end{align*}$$
>> where:
>> $\theta_{m}=$ angle of max and min stiffness
>> $=$
>> $=$

If you are currently thinking "this reminds me of [[mohrs circle]]" well yeah they basically follow the same maths.