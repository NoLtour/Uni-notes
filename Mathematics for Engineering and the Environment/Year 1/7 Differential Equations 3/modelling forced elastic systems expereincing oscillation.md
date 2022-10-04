---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Modelling forced elastic systems expereincing oscillation
[[insert funny message here|tldr]], you get the [[modelling oscillations of damped elastic systems using constant-coefficient differential equations|equation for modelling oscillating systems]] and add some thing onto it then use methods from [[general solution of linear nonhomogeneous constant coefficient equations]].

### Intro
Basically this is where you have some oscillating system that has some extra driving force acting on it. There are some definitions you should probably be aware of:
- [[free vibrations]]
- [[forced vibrations]]

### Example
So if we model a lamp post vibrating in the wind:
![[Pasted image 20220109122644.png]]
Using a bunch of assumptions are rearrangements as described [[Pasted image 20220109122742.png|here]] we get the equation:

$$ \frac{d^{2}x}{dt^{2}} + 2\zeta \omega \frac{dx}{dt} + \omega^{2}x = F\cos\Omega t $$

Now it's just following the method in [[general solution of linear nonhomogeneous constant coefficient equations]]:

$$\begin{align*}
&&x &= aF\cos\Omega t + bF\sin\Omega t \\
&&\frac{dx}{dt} &= -aF\Omega\sin\Omega t + bF\Omega\cos\Omega t \\
&&\frac{d^{2}x}{dt^{2}} &= -aF\Omega^{2}\cos\Omega t - bF\Omega^{2}\sin\Omega t \\
\frac{d^{2}x}{dt^{2}} + 2\zeta \omega \frac{dx}{dt} + \omega^{2}x &= F\cos\Omega t\\
\left(-aF\Omega^{2}\cos\Omega t - bF\Omega^{2}\sin\Omega t\right) + 2 \left(-aF\Omega\sin\Omega t + bF\Omega\cos\Omega t\right) + \omega^{2}\left(aF\cos\Omega t + bF\sin\Omega t\right) &= F\cos\Omega t\\

\left(-a\Omega^{2}\cos\Omega t - b\Omega^{2}\sin\Omega t\right) + 2 \left(-a\Omega\sin\Omega t + b\Omega\cos\Omega t\right) + \omega^{2}\left(a\cos\Omega t + b\sin\Omega t\right) &= \cos\Omega t\\

\end{align*}$$

$$\begin{align*}
-a\Omega^{2}\cos\Omega t + 2b\Omega\cos\Omega t + a\omega^{2}\cos\Omega t &= \cos\Omega t & - b\Omega^{2}\sin\Omega t -2a\Omega\sin\Omega t + \omega^{2}b\sin\Omega t &= 0\\
-a\Omega^{2}+ 2b\Omega +a \omega^{2} &= 1 & - b\Omega^{2} -2a\Omega+ \omega^{2}b &= 0\\
&&  \frac{\omega^{2}b - b\Omega^{2}}{2\Omega} &= a\\
-\frac{\omega^{2}b - b\Omega^{2}}{2\Omega}\Omega^{2}+ 2b\Omega +\frac{\omega^{2}b - b\Omega^{2}}{2\Omega} \omega^{2} &= 1
\end{align*}$$
Now rearrange for $b$ and sub that into the equation from earlyer ([[that would take way too long so I'm just skipping to the final particular integral]]):

$$\begin{align*}
\frac{(\omega^{2}-\Omega^{2})F \cos \Omega t + 2 \zeta \omega \Omega F \sin \Omega t }{ \sqrt{ (\omega^{2} - \Omega^{2})^{2} + 4\zeta^{2}\omega^{2}\Omega^{2} } }
\end{align*}$$

Then you need to find the [[complementary function]] which you can also get using [[general solutions for modelling oscillations of damped elastic systems using constant-coefficient differential equations]] and slap them together...

(life is pain, now imagine they give you some values and force you to differentiate this fucking abomination, acc that said it wouldn't be that bad... but still this hurts my head looking at it)