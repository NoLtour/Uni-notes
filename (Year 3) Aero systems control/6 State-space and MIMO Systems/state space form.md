---
aliases: ["state vector","control vector","output vector","state matrix","control matrix","output matrix","feedforward matrix"]
tags: []
---

## State space form

### General form

This is a general form that any $n$ input to $1$ output [[block diagram parts|system]] can be represented as:

> ![[Pasted image 20231109205016.png]]
> ### $$\begin{align*} \dot{\bf{x}}  &= \bf{A}\bf{x} + \bf{B}\bf{u}  \end{align*}$$
> ### $$\begin{align*} {\bf{y}}  &= \bf{C}\bf{x} + \bf{D}\bf{u}  \end{align*}$$
>> where:
>> $\bf{x}=$ state vector, the values in $\bf{x}$ represent the current state of the system and are used to predict the future behaviour of the system.
>> $\bf{u}=$ control vector, which represents the control input applied to the system. It is an external input that affects the behaviour of the system.
>> $\bf{y}=$ output vector, contains the output variables of the system. The values in $\bf{y}$ represent the observable outputs of the system, which are influenced by the state and control inputs.
>> $\bf{A}=$ state matrix, it defines how the state variables of the system change over time in response to the current state.
>> $\bf{B}=$ control matrix, it defines how the state variables ($\bf{x}$) of the system change in response to the control input ($\bf{u}$).
>> $\bf{C}=$ output matrix, It defines how the output variables are related to the state variables of the system
>> $\bf{D}=$ feedforward matrix,  It defines how the output variables ($\bf{y}$) are related to the control input ($\bf{u}$).

The bit more important than that block diagram is the equations, these are constructed out of matrices and vectors to fully describe a complex system.

### Examples

#### Simple lag

Take the case where the entire system [[transfer function]] can be written as:
$$\begin{align*}
G=\frac{W}{R} &= \frac{1}{s-T_{1}}
\end{align*}$$

Then it's transfer diagram following the generic layout described above would be:
![[Pasted image 20231109205256.png]]

We can algebraically get that into the forms $\dot{\bf{x}}  = \bf{A}\bf{x} + \bf{B}\bf{u}$ and ${\bf{y}}  = \bf{C}\bf{x} + \bf{D}\bf{u}$

$$\begin{align*}
&& &&&&&&&&&&&& u&= r\\
&& &&&&&&&&\text{inv}&\text{ Laplace}&&& x&= w\\
 \frac{W}{R} &= \frac{1}{s-T_{1}}  & &\to &  W(s-T_{1})  &= R  & &\to &  Ws-WT_{1}  &= R& &\to &  \dot{w}-T_{1}w  &= r& &\to &  \dot{x}  &= T_{1}x+u\\
&& &&&&&&&&&&&&&& y&= 1x\\\\
&& &&&&&&&&&&&&&&\therefore A&= T_{1}\\
&& &&&&&&&&&&&&&& B&= 1\\
&& &&&&&&&&&&&&&& C&= 1\\
&& &&&&&&&&&&&&&& D&= 0\\
\end{align*}$$

#### 3rd order system

$$\begin{align*}
G= \frac{W}{R} &= \frac{5}{s^{3} + 6s^{2} + 9s + 3}
\end{align*}$$

Once again:

$$\begin{align*}
\frac{W}{R} &= \frac{5}{s^{3} + 6s^{2} + 9s + 3} & &\to & 5R &= Ws^{3} + W6s^{2} + W9s + W3 & &\to & 5r &= \dddot{w} + 6\ddot{w} + 9\dot{w} + 3w
\end{align*}$$

In this case the state space model isn't unique. The simplest choice is $x_{1}=w$, so $\dot{x}_{1}=\dot{w}$. Though for convenience we'll use the definition:
$$\begin{align*}
x_{1} &=  w\\
x_{2} &= \dot{x}_{1}=\dot{w}\\
x_{3} &=\dot{x}_{2}= \ddot{x}_{1}=\ddot{w}\\
x_{4} &= \dot{x}_{3}= \ddot{x}_{2}=\dddot{x}_{1}=\dddot{w}\\
\end{align*}$$

The reason for writing it this way will become apparent later, for now let's transform our previous function:

$$\begin{align*}
5r &= \dddot{w} + 6\ddot{w} + 9\dot{w} + 3w & \to& & 5r &= \dot{x}_{3} + 6x_{3} + 9x_{2} + 3x_{1} & \to& & - 6x_{3} - 9x_{2} - 3x_{1} +5r &= \dot{x}_{3} 
\end{align*}$$

The reason for writing it that way is it means that:
$$\begin{align*} 
\begin{aligned} 
\dot{x}_{1}&= x_{2}\\
\dot{x}_{2}&= x_{3}\\
\dot{x}_{3} &= - 6x_{3} - 9x_{2} - 3x_{1} +5r\\
\end{aligned}
&&\to && 
\begin{aligned} 
\dot{x}_{1}&=0x_{1}+ 1x_{2} +0x_{3}+0r\\
\dot{x}_{2}&= 0x_{1}+ 0x_{2} +1x_{3}+0r\\
\dot{x}_{3} &= - 3x_{1}  - 9x_{2}- 6x_{3} +5r\\
\end{aligned}
&&\to &&   \begin{bmatrix} \dot{x}_{1} \\ \dot{x}_{2} \\ \dot{x}_{3} \end{bmatrix} &= \begin{bmatrix} 0 & 1 & 0 \\0 & 0 & 1 \\-6 & -9 & -3  \end{bmatrix} \begin{bmatrix} {x}_{1} \\ {x}_{2} \\ {x}_{3} \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \\ 5 \end{bmatrix}r\\\\
&&&&&&&&\dot{\bf{x}} &= \begin{bmatrix} 0 & 1 & 0 \\0 & 0 & 1 \\-6 & -9 & -3  \end{bmatrix} \bf{x} + \begin{bmatrix} 0 \\ 0 \\ 5 \end{bmatrix} r\\
\end{align*}$$

Here:
$$\begin{align*}
\begin{bmatrix} 1 & 0 & 0 \end{bmatrix} \bf{x} &= w
\end{align*}$$

Drawn as a block diagram it would be:

![[Pasted image 20231109213842.png]]
 



#### Transfer function with [[system transfer function feature definitions|zeros]]

The following transfer function has [[system transfer function feature definitions|zeros]]:
$$\begin{align*}
G= \frac{Y}{U} &= \frac{K(s+a)}{s+b} 
\end{align*}$$

So to get it into state space form we start with cross multiplication as usual:

$$\begin{align*}
 \frac{Y}{U} &= \frac{K(s+a)}{s+b} & &\to & Ys + Yb  &= UKs+UKa  & &\to & \dot{y} + by  &= K\dot{u} + Kau 
\end{align*}$$

We hit a wall since the $\dot{y}$ means we can't get into [[state space form]]. The solution to this is splitting the numerator and denominator into separate transfer functions:

![[Pasted image 20231109223012.png]]

By doing this we can split the formula normally and then sub back:

$$\begin{align*}
\frac{X}{U} &= \frac{K}{s+b} & &\to&  X(s+b) &= KU  & &\to&  \dot{x} + bx &= Ku & &\to&  \dot{x}   &=- bx + Ku  \\
\frac{Y}{X} &= s+a  & &\to& Y  &= X(s+a)  & &\to& y &= \dot{x} + ax&& & &\to& y &= - bx + Ku + ax\\
&& && && && &&  &&  &&  y &= x(a- b) + Ku 
\end{align*}$$

#### 3rd order transfer function with [[system transfer function feature definitions|zeros]]
(This is [[I own a bakery in french|pain]])

$$\begin{align*}
\frac{W}{R} &= \frac{5s^{2} + 2s + 2}{s^{3} + 6s^{2} + 9s + 3}
\end{align*}$$

To anyone reading this, you should be really glad you don't have to type the latex for this. (let $W=Y$)

$$\begin{align*}
\frac{X}{R} &= \frac{1}{s^{3} + 6s^{2} + 9s + 3} & &\to &   1R &= Xs^{3} + X6s^{2} + X9s +X3 & &\to & r &= \dddot{x} + 6\ddot{x} + 9\dot{x} + 3x & &\to &- 6x_{3} - 9x_{2} - 3x_{1}+r &= \dot{x}_{3}\\
\frac{Y}{X} &= 5s^{2} + 2s + 2  & &\to & Y&=   5Xs^{2} + 2Xs + 2X & &\to & y &= 5\ddot{x} + 2\dot{x} + 2x& &\to & y &= 5x_{3} + 2x_{2} + 2x_{1} \\
\end{align*}$$

Subbing into the 
$$\begin{align*} 
\begin{aligned} 
\dot{x}_{1}&= x_{2}\\
\dot{x}_{2}&= x_{3}\\
\dot{x}_{3} &= - 6x_{3} - 9x_{2} - 3x_{1} +1r\\
\end{aligned}
&&\to && 
\begin{aligned} 
\dot{x}_{1}&=0x_{1}+ 1x_{2} +0x_{3}+0r\\
\dot{x}_{2}&= 0x_{1}+ 0x_{2} +1x_{3}+0r\\
\dot{x}_{3} &= - 3x_{1}  - 9x_{2}- 6x_{3} +1r\\
\end{aligned}
&&\to &&   \begin{bmatrix} \dot{x}_{1} \\ \dot{x}_{2} \\ \dot{x}_{3} \end{bmatrix} &= \begin{bmatrix} 0 & 1 & 0 \\0 & 0 & 1 \\-6 & -9 & -3  \end{bmatrix} \begin{bmatrix} {x}_{1} \\ {x}_{2} \\ {x}_{3} \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}r\\\\
&&&&&&&&\dot{\bf{x}} &= \begin{bmatrix} 0 & 1 & 0 \\0 & 0 & 1 \\-6 & -9 & -3  \end{bmatrix} \bf{x} + \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} r\\
\end{align*}$$

Now:

$$\begin{align*}
 y &= 5x_{3} + 2x_{2} + 2x_{1} & &\to & y &=  \begin{bmatrix} 2  &  2  &  5 \end{bmatrix}\bf{x}
\end{align*}$$

Recall [[state space form#General form]], we clearly have it in the form:
$$\begin{align*}
\dot{\bf{x}}  &= \bf{A}\bf{x} + \bf{B}\bf{u} & {\bf{y}}  &= \bf{C}\bf{x} + \bf{D}\bf{u}
\end{align*}$$
$$\begin{align*}
\bf{A} &= \begin{bmatrix} 0 & 1 & 0 \\0 & 0 & 1 \\-6 & -9 & -3  \end{bmatrix} &
\bf{B} &= \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} &
\bf{C} &= \begin{bmatrix} 2  &  2  &  5 \end{bmatrix}&
\bf{D} &= 0 
\end{align*}$$

The take away being [[system transfer function feature definitions|zeros]] contribute to the output matrix. If your wondering what the block diagram would look like:

![[Pasted image 20231109225908.png]]
