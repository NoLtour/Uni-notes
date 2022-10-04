---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you find the
## General solution of linear nonhomogeneous constant coefficient equations

Well if we look back at [[general solution of a linear nonhomogeneous equation]] everything we need to do this is there:
![[general solution of a linear nonhomogeneous equation#^50b2a4]]


When trying to find the [[complementary function]] the page [[solving linear homogeneous constant-coefficient equations]] is often useful.

Also I like this:
![[Pasted image 20211219194450.png]]
"Guess till you get it right, [[textbook be doing a little trolling|good luck bitch]]"

### Example

#### Example 1

> Find the general solution of $\frac{d^{2}x}{dt^{2}} + 5\frac{dx}{dt} - 9x = t^{2}$

First we need a [[particular integral]], so we try something suitable, lets try $x(t)=Pt^{2} + Qt + R$

$$\begin{align*}
&&x &= Pt^{2} + Qt + R\\
&&\frac{dx}{dt} &= 2Pt + Q\\
t^{2} &= \frac{d^{2}x}{dt^{2}} + 5\frac{dx}{dt} - 9x & \frac{d^{2}x}{dt^{2}} &= 2P\\
 &= (2P )+ 5(2Pt + Q) - 9(Pt^{2} + Qt + R)\\
 &= 2P + 10Pt + 5Q - 9Pt^{2} - 9Qt - 9R\\
 0 &= t^{2} ( -1 - 9P ) + t( 10P - 9Q ) + ( 2P + 5Q - 9R )\\
& & 1 &= 9P & 0 &= 10P - 9Q & 0 &= 2P +5Q - 9R\\
&& -\frac{1}{9} &= P & \frac{10P}{9} &= Q & \frac{2P +5Q}{9} &= R\\
&& &&  -\frac{10}{81}&=Q\\
&& && &&  - \frac{68}{729} &=R \\
\therefore x(t)&=-\frac{1}{9}t^{2} -\frac{10}{81} t - \frac{68}{729} \\& is \:the\:particular\:integral
\end{align*}$$

We now need to find the [[complementary function]], we can do this using [[solving linear homogeneous constant-coefficient equations]] since the complementary function is when $L[x]=0$ we solve $\frac{d^{2}x}{dt^{2}} + 5\frac{dx}{dt} - 9x=0$:

$$\begin{align*}
0 &= m^{2} + 5m - 9\\
m &= \frac{-5\pm \sqrt{61}}{2} \\
&\\
x(t) &= Ae^{t\frac{-5 + \sqrt{61}}{2}}+ Be^{t\frac{-5 - \sqrt{61}}{2}}
\end{align*}$$

We can now combine them to find the general solution of $\frac{d^{2}x}{dt^{2}} + 5\frac{dx}{dt} - 9x = t^{2}$:

$$\begin{align*}
x(t) &= Ae^{t\frac{-5 + \sqrt{61}}{2}}+ Be^{t\frac{-5 - \sqrt{61}}{2}} -\frac{1}{9}t^{2} -\frac{10}{81} t - \frac{68}{729}
\end{align*}$$

#### Example 2
> Find the general solution of $\frac{d^{2}x}{dt^{2}} + 5 \frac{dx}{dt} - 9x = \cos 2t$

First we need to find the [[particular integral]]:

$$\begin{align*}
x(t) &= A\cos 2t + B\sin 2t \\
\frac{dx}{dt} &= -2A\sin 2t + 2B\cos 2t \\
\frac{d^{2}x}{dt^{2}} &=  -4A\cos 2t - 4B\sin 2t \\
&&\frac{d^{2}x}{dt^{2}} + 5 \frac{dx}{dt} - 9x &= \cos 2t\\\\
&&(-4A\cos 2t - 4B\sin 2t) + 5 (-2A\sin 2t + 2B\cos 2t) - 9(A\cos 2t + B\sin 2t) &= \cos 2t\\
&& A(-13\cos 2t-10\sin 2t) + B( 10\cos 2t -13\sin 2t ) &= \\
&& -13 A + 10B &= 1 & -10A -13B &= 0\\
&& A&= - \frac{13}{269} & B&= \frac{10}{269}\\
x(t) &= - \frac{13}{269} \cos 2t + \frac{10}{269}\sin 2t
\end{align*}$$

Now we find the [[general and particular solution|general solution]], but its the same as example 1 so Ima skip strait to the final answer:

$$\begin{align*}
x(t) &= Ae^{t\frac{-5 + \sqrt{61}}{2}}+ Be^{t\frac{-5 - \sqrt{61}}{2}} - \frac{13}{269} \cos 2t + \frac{10}{269}\sin 2t
\end{align*}$$
