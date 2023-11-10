---
aliases: [""]
tags: []
---

## Multivariable systems in [[state space form]]

In [[state space form#Examples]] we only showed cases where we had one input, well as suggested it does work with many inputs... though thing's become quite painful quickly. Let's consider:

![[Pasted image 20231109233236.png]]

Now solve. [[I am moments away from commiting multiple mass genocides my rage is not containable|:)]]

Something that should be kept in mind is in this case $x_{1}\neq\dot{x}$, the convention's changed. 

The $y$ functions (${\bf{y}}   = \bf{C}\bf{x} + \bf{D}\bf{u}$) can be trivially derived by simply looking at the chart:
$$\begin{align*}
y_{1} &= x_{1} + x_{2} &&& y_{2} &= x_{3} + x_{4}\\
\end{align*}$$
Becomes:
$$\begin{align*}
&&\begin{bmatrix} y_{1} \\ y_{2} \end{bmatrix} &= \begin{bmatrix} 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_4 \end{bmatrix}
\end{align*}$$



Going to get functions for $u$:
$$\begin{align*}
&&&&&&y_{1} &= x_{1} + x_{2}\\
U_{1} &= K_{1}(R_{1} - Y_{1}) & &\to & u_{1} &= K_{1}(r_{1} - y_{1})  & &\to & u_{1} &= K_{1}(r_{1} - x_{1} - x_{2}) \\\\\\
&&&&&&y_{2} &= x_{3} + x_{4}\\
U_{2} &= K_{2}(R_{1} - Y_{2}) & &\to & u_{2} &= K_{2}(r_{2} - y_{2})  & &\to & u_{2} &= K_{2}(r_{2} - x_{3} - x_{4}) 
\end{align*}$$
These will be useful later.

Then each section can be approached individually:

$$\begin{align*}
&&&&&&&&&&u_{1} &= K_{1}(r_{1} - x_{1} - x_{2})  \\
&&&&&&&&&&u_{2} &= K_{2}(r_{2} - x_{3} - x_{4}) \\
\frac{X_{1}}{U_{1}} &= \frac{1}{s+1} & &\to & u_{1} &= \dot{x}_{1} + x_{1} & &\to &  \dot{x}_{1} &= u_{1} - x_{1}  & &\to &  \dot{x}_{1} &=  K_{1}(r_{1} - x_{1} - x_{2}) - x_{1} \\ 
\frac{X_{2}}{U_{2}} &= \frac{5}{s+5} & &\to & 5u_{2} &= \dot{x}_{2} + 5x_{2}& &\to &  \dot{x}_{2} &= 5u_{2} - 5x_{2}& &\to &  \dot{x}_{2} &= 5K_{2}(r_{2} - x_{3} - x_{4}) - 5x_{2} \\ 
\frac{X_{3}}{U_{1}} &= \frac{0.4}{s+0.5} & &\to & 0.4u_{1} &= \dot{x}_{3} + 0.5x_{3}& &\to &  \dot{x}_{3} &= 0.4 u_{1} -0.5 x_{3}& &\to &  \dot{x}_{3} &= 0.4 K_{1}(r_{1} - x_{1} - x_{2}) -0.5 x_{3} \\ 
\frac{X_{4}}{U_{2}} &= \frac{4}{s+2} & &\to & 4u_{2} &= \dot{x}_{4} + 2x_{4}& &\to &  \dot{x}_{4} &=4 u_{2} - 2x_{4}& &\to &  \dot{x}_{4} &=4 K_{2}(r_{2} - x_{3} - x_{4}) - 2x_{4} \\ 

\end{align*}$$


These give you the final matrix form with a bit of subing:

$$\begin{align*} 
\begin{aligned} 
 \dot{x}_{1} &=  K_{1}(r_{1} - x_{1} - x_{2}) - x_{1} \\ 
 \dot{x}_{2} &= 5K_{2}(r_{2} - x_{3} - x_{4}) - 5x_{2} \\ 
  \dot{x}_{3} &= 0.4 K_{1}(r_{1} - x_{1} - x_{2}) -0.5 x_{3} \\ 
  \dot{x}_{4} &=4 K_{2}(r_{2} - x_{3} - x_{4}) - 2x_{4} \\ 
\end{aligned}
&&\to && 
\begin{aligned} 
 \dot{x}_{1} &= (-1- K_{1})x_{1} - K_{1}x_{2} + K_{1}r_{1}  \\ 
 \dot{x}_{2} &=   - 5x_{2}- 5K_{2}x_{3} - 5K_{2}x_{4}  + 5K_{2} r_{2}\\ 
  \dot{x}_{3} &=  - 0.4 K_{1}x_{1} - 0.4 K_{1}x_{2} -0.5 x_{3} +0.4 K_{1} r_{1}\\ 
  \dot{x}_{4} &= - K_{2}x_{3} + ( - K_{2}   - 2)x_{4} +4 K_{2} r_{2}\\ 
\end{aligned}
&&\to &&   \begin{bmatrix} \dot{x}_{1} \\ \dot{x}_{2} \\ \dot{x}_{3} \\ \dot{x}_{4} \end{bmatrix} &= \begin{bmatrix} -1-K_{1}  & -K_{1} & 0 & 0\\0 & -5 & -5K_{2} & -5 K_{2}\\ -0.4K_{1} & -0.4K_{1} & -0.5 & 0 \\ 0 & 0 & -K_{2}  & -K_{2}-2  \end{bmatrix} \begin{bmatrix} {x}_{1} \\ {x}_{2} \\ {x}_{3} \\ {x}_{4} \end{bmatrix} + \begin{bmatrix} K_{1} & 0\\0 & 5K_{2}\\ 0.4K_{1} & 0\\ 0 & 4K_{2} \end{bmatrix} \begin{bmatrix} r_{1}\\r_{2} \end{bmatrix}\\\\
&&&&&&&& \dot{\bf{x}}  &= \bf{A}\bf{x} + \bf{B}\bf{r}\\
\end{align*}$$

BOOM, finished. Now wasn't that fun.
 
