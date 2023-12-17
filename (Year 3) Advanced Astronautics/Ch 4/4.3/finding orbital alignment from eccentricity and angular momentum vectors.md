---
aliases: [""]
tags: []
---

## Finding orbital alignment from eccentricity and angular momentum vectors

### Equation

For the general case:

> ### $$\begin{align*} \cos(i) &= \frac{h_{z}}{h} &&& i &= \arccos\left(\frac{h_{x}}{h}\right) \\ \tan(\Omega) &= \frac{h_{x}}{-h_{y}}&&& \Omega &= \text{atan2}(h_{x} ,\: -h_{y})\\ \tan(\omega) &= \frac{e_{z}/\sin i}{e_{y} \sin \Omega + e_{x} \cos \Omega } &&& \omega &= \text{atan2}\left(\frac{e_{z}}{\sin i} ,\: e_{y} \sin \Omega + e_{x} \cos \Omega \right)\end{align*}$$
> ### $$\begin{align*} \vec{e}  &=  \begin{pmatrix} e_{x}\\e_{y}\\e_{z} \end{pmatrix} &&& \vec{h}  &=  \begin{pmatrix} h_{x}\\h_{y}\\h_{z} \end{pmatrix} \end{align*}$$
>> where:
>> $\omega=$ [[orbital elements and alignment|argument of periapsis]]
>> $\Omega=$ [[orbital elements and alignment|longitude of the ascending node]]
>> $i=$ [[orbital elements and alignment|inclination]]
>> 
>> Note that the signs are left in such a way to emphasise the quadrant!

There are special cases, such as when $e=0$, we obviously have a [[orbit categories by eccentricity|circular orbit]]. This means that there is no single value for [[orbital elements and alignment|argument of periapsis]], in this case an arbitrary value such as zero can be taken.

There is also the case where $i=0$ at which point the distinction between $\omega$ and $\Omega$ becomes lost, here we usually represent them as a single value.

### Derivation

This is actually not so difficult once you realise that the [[eccentricity vector]] and [[specific orbital moment of momentum|orbital angular momentum vector]] can be written as a very simple [[perifocal coordinate frame|perifocal frame]] vector:

$$\begin{align*}
 \begin{pmatrix} e \\0 \\0 \end{pmatrix} &= \vec{e}_{perifocal} &&&  \begin{pmatrix} 0 \\0 \\h \end{pmatrix} &= \vec{h}_{perifocal}
\end{align*}$$

Then if we consider the translated forms:

$$\begin{align*}
\vec{e}  &=  \begin{pmatrix} e_{x}\\e_{y}\\e_{z} \end{pmatrix} &&\to& \vec{e} &=  Q_{p\to r}\vec{e}_{perifocal}  &&\to& 
\begin{pmatrix} e_{x}\\e_{y}\\e_{z} \end{pmatrix} &= \begin{pmatrix} \cos(\Omega)\cos(\omega)- \cos(i)\sin(\Omega)\sin(\omega) & -\cos(\Omega)\cos(\omega)- \cos(i)\cos(\omega)\sin(\Omega)& \sin(\Omega)\sin(i)\\\cos(\omega)\sin(\Omega)+ \cos(\Omega)\cos(i)\sin(\omega) & \cos(\Omega)\cos(i)\cos(\omega)- \sin(\Omega)\sin(\omega)& -\cos(\Omega)\sin(i)\\\sin(i)\sin(\omega)& \cos(\omega)\sin(i)& \cos i \end{pmatrix} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}e
 \\\\
\vec{h}  &=  \begin{pmatrix} h_{x}\\h_{y}\\h_{z} \end{pmatrix} &&\to& \vec{h} &=  Q_{p\to r}\vec{h}_{perifocal}  &&\to& 
\begin{pmatrix} h_{x}\\h_{y}\\h_{z} \end{pmatrix} &= \begin{pmatrix} \cos(\Omega)\cos(\omega)- \cos(i)\sin(\Omega)\sin(\omega) & -\cos(\Omega)\cos(\omega)- \cos(i)\cos(\omega)\sin(\Omega)& \sin(\Omega)\sin(i)\\\cos(\omega)\sin(\Omega)+ \cos(\Omega)\cos(i)\sin(\omega) & \cos(\Omega)\cos(i)\cos(\omega)- \sin(\Omega)\sin(\omega)& -\cos(\Omega)\sin(i)\\\sin(i)\sin(\omega)& \cos(\omega)\sin(i)& \cos i \end{pmatrix} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}h
\end{align*}$$

A set of solvable equations can then be found by expanding out the matrices:

$$\begin{align*}  
\frac{e_{x}}{e} &= \cos(\Omega)\cos(\omega)- \cos(i)\sin(\Omega)\sin(\omega)\\
\frac{e_{y}}{e} &= \cos(\omega)\sin(\Omega)+ \cos(\Omega)\cos(i)\sin(\omega)\\
\frac{e_{z}}{e} &= \sin(i)\sin(\omega) \\\\ 
\frac{h_{x}}{h} &= \sin(\Omega)\sin(i)\\
\frac{h_{y}}{h} &= -\cos(\Omega)\sin(i)\\
\frac{h_{z}}{h} &= \cos i \\
\end{align*}$$

These are now in a form that doesn't seem so difficult to solve, and the abundance of equations allows for [[quadrant disambiguation]]. From these we can derive the following:

$$\begin{align*} \cos(i) &= \frac{h_{z}}{h} \\ \tan(\Omega) &= \frac{h_{x}}{-h_{y}}\\ \tan(\omega) &= \frac{e_{z}/\sin i}{e_{y} \sin \Omega + e_{x} \cos \Omega } \end{align*}$$


In the case that we were not given $\vec{e}$ and $\vec{h}$, we may instead of been given the instantaneous $\vec{r}$ and $r$, at which point we would use them to find $\vec{e}$ and $\vec{h}$ first, then sub into the equations above!
