# PROB WRONG

Now the fun proof, what the fuq to do when $\alpha_{1} = \alpha_{2}  = \alpha$, well it's actually quite simple really basically we just need to find another valid function of $y$ for [[solving linear homogeneous constant-coefficient equations#^{9d621e]] which is [[linearly dependent and independent functions|linearly independent]] of $y=e^{\apha x}$, lets guess $y=e^{-\gamma x}$: 

$$\begin{align*}
 \frac{d^{2}y}{dx^{2}} + f \frac{dy}{dx} + g y &= 0 & y&=e^{-\gamma x}\\
 & & \frac{dy}{dx} &= -\gamma e^{-\gamma x}\\
 & & \frac{dy^{2}}{dx^{2}} &= \gamma^{2} e^{-\gamma x}\\
\gamma^{2} e^{-\gamma x} - f \gamma e^{-\gamma x} + g e^{-\gamma x} &= 0\\
\gamma^{2} - f \gamma + g &= 0
\end{align*}$$
And then the method is the same as normal:

$$ \gamma = \frac{--f \pm \sqrt{ f^{2} - 4g } }{2} $$

It should be noted that the term $\sqrt{ f^{2} - 4g }$ being zero is what causes $\alpha$ to only have a single root, which also applies to $\gamma$ but this also means that:
$$\begin{align*}
 \gamma &= \frac{f \pm \sqrt{ f^{2} - 4g } }{2} & \alpha &= \frac{-f \pm \sqrt{ f^{2} - 4g } }{2} & f^{2} - 4g &= 0 \\
\gamma &= \frac{f  }{2} & \alpha &= -\frac{f   }{2}\\
 \gamma &= -\alpha
\end{align*}$$

So now we have two [[linearly dependent and independent functions|linearly independent functions]] for $y$: $y_{1} = e^{\alpha x}, y_{2} = e^{-\alpha x}$
which subbed back gets:
$$\begin{align*}
y &= A \times y_{1} (x) + B \times y_{2} (x)\\
y &= A e^{\alpha x} + B e^{-\alpha x}\\
y &= e^{\alpha x} + B e^{-\alpha x}
\end{align*}$$