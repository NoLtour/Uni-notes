---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the mathamatical method for
## Modeling vibration
### Main bit
In the tutorial they start with free oscillation then move onto damped oscillation, that's [[it really is though|kinda cringe]] so I'm going to do it in the opposite order and then describing free oscillation as a special case so I don't have to prove it twice ([[I prefer to say efficient lol|I'm lazy]]). If your going over this for the first time skip to [[modeling vibration (not driven)#Proof]] then come back to this and continue reading from here.

> ### $$ 0=m \frac{d^{2}x}{dt^{2}} + c \frac{dx}{dt} + kx$$ 
>> where:
>> $m=$ mass of particle
>> $x=$ displacement from equilibrium
>> $t=$ time
>> $c=$ a constant relating speed and drag (damping coefficient)
>> $k=$ [[spring constant]]

^9328aa

Then use [[solving linear homogeneous constant-coefficient equations]].

### Proof
First lets get a diagram representing some mass on a spring of negligible mass:
![[Pasted image 20220302112318.png]]

Each of the forces are:
- $T(x,\dot{x},\ddot{x}, ...)=$ Some tension force function
- $D(x,\dot{x},\ddot{x}, ...)=$ Some drag force function
- $mg=$ Weight

Now this isn't very helpfull, so we can use simple models for drag and tension:
- $T=k(x+Q)$
- $D=c\dot{x}$ where $c$ is some constant

The displacement $Q$ is the value needed for tension and weight to be equal when $\dot{x}=0,x=0$:
$$\begin{align*}
T + D &= mg\\
k(x+Q) + c\dot{x} &= mg & let:&\:x=0,\:\dot{x}=0\\
k(Q) &= mg\\
Q &= \frac{mg}{k}
\end{align*}$$

Now lets get an equation defining net acceleration of the mass interms of everything acting on it:
$$\begin{align*}
-m\ddot{x} &= T + D - mg & D &= c\dot{x} & T &= k(x+Q) & Q&= \frac{mg}{k}\\
&=  k(x+\frac{mg}{k}) + c\dot{x} - mg\\
&=  k(x) + mg + c\dot{x} - mg\\
0 &= m\ddot{x} + k(x) + c\dot{x}\\
0 &= m \frac{d^{2}x}{dt^{2}} + c \frac{dx}{dt} + kx
\end{align*}$$

We can see that by measuring x from the equilibrium point ($Q+l_{0}$) we get a situation where g cancels out:

![[Pasted image 20220302113825.png]]

Also you have probably noticed that the equation $0=m \frac{d^{2}x}{dt^{2}} + c \frac{dx}{dt} + kx$ seems like a [[linear homogeneous constant-coefficient equation]], and that's because it is! So the next step would be to solve it according to the method from [[solving linear homogeneous constant-coefficient equations]].