---
aliases: [""]
tags: []
---

## Thin cambered airfoil analysis
### Important results

Something that is worth noting is that these equations also work for symetric airfoils, they just simplify a lot because $\frac{dz}{dx}=0$ in the symetric case.

> ### $$\begin{align*}  \text{Fourier results:}& & A_{0} &=  \alpha - \frac{1}{\pi} \int^{\pi}_{0}  \frac{dz}{dx} \: d\theta_{0}\\& & A_{n} &= \frac{2}{\pi} \int^{\pi}_{0}  \frac{dz}{dx} \cos (n\theta_{0}) \: d\theta_{0} \\\\ \text{lift coefficient:}& & C_{l} &= 2\pi \left(A_{0} + \frac{A_{1}}{2}\right) \\ && &= 2\pi(\alpha - \alpha_{L=0}) \\\\ \text{zero lift angle:}&& \alpha_{L=0} &=  \frac{1}{\pi} \int^{\pi}_{0}\frac{dz}{dx}  \left(1 -   \cos \theta_{0}  \right) \: d\theta_{0} \\\\ \text{leading edge moment:}& & C_{m,LE} &=  - \frac{\pi}{2} \left( A_{0}  + A_{1}- \frac{A_{2}}{2}  \right) \\\\ \text{quater chord moment:}& & C_{m,c/4} &=  C_{m,LE} + \frac{C_{l}}{4}\\ &&&=\frac{\pi}{4} (A_{2} - A_{1}) \end{align*}$$
>> where:
>> $\alpha=$ AOA
>> $A_{0},A_{n}=$ variables derived from the applying fourier series to the [[fundemental equation of thin aerofoil theory]]
>> $C_{l}=$ [[2D and 3D lift coefficient|2D lift coefficient]]
>> $\alpha_{L=0}=$ [[no lift angle]]
>> $\theta=$  dummy variable stand in for $\xi$ 
>> $\theta_{0}=$ dummy variable stand in for $x$
>> $x=$ a position along the chord hence $0\leq x \leq c$ 
>> $\xi=$ position along the chord for a constant $x$ (used during integration)
>> $V_{\infty}=$ freestream velocity
>> $\frac{dz}{dx}=$ the gradient of the mean camber (here as a function of $\theta_{0}$)
>> $C_{m,LE}=$ 2D leading edge moment coefficent
>> $C_{m,c/4}=$ 2D quater chord moment coefficient
>> 

### Theory and derivations
#### Starting modelling
The first step is the same as from [[thin symmetric airfoil analysis#Proof]] except we don't have the luxuary of $\frac{dz}{dx}=0$ since it's cambered, so I guess it's not really the same at all... this is going to become painful quickly (fun). So let's grab the [[fundemental equation of thin aerofoil theory]]:
$$\begin{align*}
 V_{\infty} \left(\alpha -\frac{dz}{dx}\right) &= \frac{1}{2\pi}\int^{\pi}_{0} \frac{\gamma(\theta) \sin\theta }{\cos \theta - \cos\theta_{0}} d\theta  
\end{align*}$$

To have a chance at solving for $\gamma$ we are going to need to get the $\alpha - \frac{dz}{dx}$ into a nicer to work with form, first lets define:

$$\begin{align*}
\text{let:}\:\:\left(\alpha - \frac{dz}{dx}\right) &= f(\theta_{0})
\end{align*}$$
 Then we can use [[defining the fourier series|Fourier series]]:
$$\begin{align*}
f(\theta_{0}) &= A_{0} - \sum\limits^{\infty}_{n=1} A_{n} \cos n\theta_{0}
\end{align*}$$
$$\begin{align*}
A_{0} &= \frac{1}{\pi} \int^{\pi}_{0} f(\theta_{0}) \: d\theta_{0} & A_{n} &= \frac{1}{\pi} \int^{\pi}_{0} f(\theta_{0}) \cos( n\theta_{0} )\: d\theta_{0}\\
  &= \frac{1}{\pi} \int^{\pi}_{0} \left(\alpha - \frac{dz}{dx}\right) \: d\theta_{0} &   &= \frac{1}{\pi} \int^{\pi}_{0} \left(\alpha - \frac{dz}{dx}\right) \cos( n\theta_{0}) \: d\theta_{0}\\
  &... & &... \\
  A_{0} &= \alpha - \frac{1}{\pi} \int^{\pi}_{0}  \frac{dz}{dx} \: d\theta_{0} & A_{n}  &= \frac{2}{\pi} \int^{\pi}_{0}  \frac{dz}{dx} \cos (n\theta_{0}) \: d\theta_{0}\\
\end{align*}$$
The equations above are litterally just applying [[defining the fourier series|Fourier series]] to $f(\theta_{0})$ then subbing back and doing a little bit of simplification, depending on the defenition of the camber line for $\frac{dz}{dx}$ the defenitions of $A_{0}$ and $A_{n}$ change.

If we sub in the function $f(\theta_{0})$ in it's fourier form back into the [[fundemental equation of thin aerofoil theory]] we will get:
$$\begin{align*}
 V_{\infty} \left(A_{0} - \sum\limits^{\infty}_{n=1} A_{n} \cos n\theta_{0}\right) &= \frac{1}{2\pi}\int^{\pi}_{0} \frac{\gamma(\theta) \sin\theta }{\cos \theta - \cos\theta_{0}} d\theta  
\end{align*}$$

Now looking at this you may be thinking "but how the fuck are we supposed to solve for $\gamma$ it looks [[it is hard to put into words just how incredibly cursed this equation is|even worse]]", well actually... you are completely correct this cursed piece of shit is waaaaay beyond our [[look sometimes the skill issue is acceptable|skill level]] to solve, so the omipotent slides just give us the solution. We don't need to know the intermetant steps to get it:

$$\begin{align*}
\gamma(\theta) &= 2V_{\infty}\left( A_{0} \frac{1+\cos\theta}{\sin\theta} + \sum\limits^{\infty}_{n=1} A_{n}\sin n\theta \right)
\end{align*}$$

So we can get a defenition of the [[vortex sheet strength|vortex sheet strength distrobution]] if we know $A_{0}$ and $A_{n}$. The equation above can be checked by subbing it back into the [[fundemental equation of thin aerofoil theory]] as well as by checking against the [[kutta condition]], it works for both and so is valid (not showing it here since it's a long proof and not needed).

#### Lift coefficient

Now we can start to find some useful numbers, such as lift. Taking the [[Kutta-Joukowski Theorem]], the equation above and the defenition of [[vortex sheet strength]]:
$$\begin{align*}
L' &= \rho V_{\infty} \Gamma  & \gamma(\theta) &= 2V_{\infty}\left( A_{0} \frac{1+\cos\theta}{\sin\theta} + \sum\limits^{\infty}_{n=1} A_{n}\sin n\theta \right) & \Gamma &= \int^{c}_{0} \gamma(\xi) d\xi
\end{align*}$$
Combining everything and converting from $\xi$ to $\theta$ form gets:

$$\begin{align*}
L' &= \rho V_{\infty} \int^{\pi}_{0} 2V_{\infty} \left( A_{0} \frac{1+\cos\theta}{\sin\theta} + \sum\limits^{\infty}_{n=1} A_{n} \sin n\theta \right) \frac{c}{2} \sin\theta \: d\theta\\
&= \rho V_{\infty}^{2} c \left( \int^{\pi}_{0} A_{0}\: d\theta + \int^{\pi}_{0} A_{0} \cos\theta \: d\theta + \sum\limits^{\infty}_{n=1} A_{n} \int^{\pi}_{0} \sin(n\theta ) \sin\theta \: d\theta  \right)
\end{align*}$$

The first two integrals are easy to deal with, but the last one requires the use of the identity:
$$ \int^{\pi}_{0} \sin (n\theta) \sin(m\theta) \: d\theta = \begin{dcases} &\frac{1}{2}\pi &\text{when: } n=m\\ &0 &\text{when: } n\neq m \end{dcases} $$
$$\begin{align*}
& \sum\limits^{\infty}_{n=1} A_{n} \int^{\pi}_{0} \sin(n\theta ) \sin\theta \: d\theta & \to & & A_{1} \frac{\pi}{2}
\end{align*}$$

Subbing this back into the lift equation and solving the other trivial integrals finally gets:

$$\begin{align*}
L' &= \rho V_{\infty}^{2} c \left( \pi A_{0} + 0 + A_{1} \frac{\pi}{2} \right)\\
&= \pi\rho V_{\infty}^{2} c  \left( A_{0} + \frac{1}{2}A_{1} \right)\\
C_{l} &= \pi\rho V_{\infty}^{2} c  \left( A_{0} + \frac{1}{2}A_{1} \right) \frac{1}{\frac{1}{2}\rho V_{\infty}^{2} c}\\
&= \pi (2A_{0} + A_{1}) \\
&=  2\pi \left( A_{0} + \frac{A_{1}}{2} \right)
\end{align*}$$

Showing us that lift coefficient is only dependent on the $A_{0}$ and $A_{1}$ reults from the fourrier series shite, which is neat. Although $A_{2},A_{3},A_{4},A_{5}...$ may not contribute to the total lift they will clearly contribute to the pressure  distrobution. 

Now lets rearrange this further, what if we sub in the expressions of $A_{0}$ and $A_{1}$:
$$\begin{align*}
  A_{0} &= \alpha - \frac{1}{\pi} \int^{\pi}_{0}  \frac{dz}{dx} \: d\theta_{0} & A_{1}  &= \frac{2}{\pi} \int^{\pi}_{0}  \frac{dz}{dx} \cos (\theta_{0}) \: d\theta_{0}\\
\end{align*}$$

$$\begin{align*}
 C_{l} &=  2\pi \left( A_{0} + \frac{A_{1}}{2} \right) & &\to &  C_{l} &=  2\pi \left( \alpha - \frac{1}{\pi} \int^{\pi}_{0}  \frac{dz}{dx} \: d\theta_{0} + \frac{1}{2} \frac{2}{\pi} \int^{\pi}_{0}  \frac{dz}{dx} \cos (\theta_{0}) \: d\theta_{0} \right)\\
&& && &= 2\pi \left( \alpha - \frac{1}{\pi} \int^{\pi}_{0} \left( \frac{dz}{dx} -  \frac{dz}{dx} \cos \left(\theta_{0}\right) \right) \: d\theta_{0}\right)\\
&& && &= 2\pi \left( \alpha - \frac{1}{\pi} \int^{\pi}_{0}\frac{dz}{dx}  \left(1 -   \cos \theta_{0}  \right) \: d\theta_{0}\right)\\
\end{align*}$$

This can clearly be re written as:
$$\begin{align*}
C_{l} &= 2\pi(\alpha - \alpha_{L=0}) & \alpha_{L=0} &=  \frac{1}{\pi} \int^{\pi}_{0}\frac{dz}{dx}  \left(1 -   \cos \theta_{0}  \right) \: d\theta_{0}
\end{align*}$$

This is a really important result, since it shows that just like with [[thin symmetric airfoil analysis|symetric foils]] the lift slope is $2\pi$ the only difference between these theoretical lift AOA slopes is the zero lift angle which is a direct result of $\frac{dz}{dx}\neq 0$.

![[Pasted image 20221220133529.png]]

#### Moments

The setups to get leading edge moment is the same as for [[thin symmetric airfoil analysis]], only difference is now we are using a different [[vortex sheet strength]] equation:


$$\begin{align*}
M_{LE}' &= - \int^{c}_{0} \xi dL' & &\to &M_{LE}' &= - \int \xi \rho V_{\infty} d\Gamma  & &\to &M_{LE}' &= - \int^{c}_{0} \xi \rho V_{\infty} \gamma(\xi)  \: d\xi 
\end{align*}$$$$

$$
$$\begin{align*}
M_{LE}' &= - \int^{c}_{0} \xi \rho V_{\infty} \gamma(\xi)  \: d\xi  & \xi &= \frac{c}{2}(1-\cos \theta)\\
 &= - \int^{\pi}_{0} \frac{c}{2}(1-\cos \theta) \rho V_{\infty} \gamma(\xi)  \: \frac{d\xi}{d\theta} d\theta & \frac{d\xi}{d\theta} &= \frac{c}{2}\sin\theta\\
&= - \int^{\pi}_{0} \frac{c}{2}(1-\cos \theta) \rho V_{\infty} \gamma(\theta)  \frac{c}{2}\sin\theta \: d\theta  & \gamma(\theta) &= 2V_{\infty}\left( A_{0} \frac{1+\cos\theta}{\sin\theta} + \sum\limits^{\infty}_{n=1} A_{n}\sin n\theta \right)\\
&= - \int^{\pi}_{0} \frac{c}{2}(1-\cos \theta) \rho V_{\infty} 2V_{\infty}\left( A_{0} \frac{1+\cos\theta}{\sin\theta} + \sum\limits^{\infty}_{n=1} A_{n}\sin n\theta \right) \frac{c}{2}\sin\theta \: d\theta\\
&...\\
M_{LE}' &= - \frac{\rho V_{\infty}^{2}c^{2}}{2} \left( \int^{\pi}_{0} A_{0} \: d\theta - \int_{0}^{\pi} A_{0} \cos^{2} \theta \: d\theta + \sum\limits^{\infty}_{n=1} A_{n} \int^{\pi}_{0} \sin n\theta \sin \theta \: d\theta - \sum\limits^{\infty}_{n=1} \frac{A_{n}}{2} \int^{\pi}_{0} \sin n\theta \sin 2\theta \: d\theta \right)
\end{align*}$$

This simplifies quite a bit if we apply the following trig identity to the last two integrals in the equation above:
$$  \int^{\pi}_{0} \sin (n\theta) \sin(m\theta) \: d\theta = \begin{dcases} &\frac{1}{2}\pi &\text{when: } n=m\\ &0 &\text{when: } n\neq m \end{dcases}  $$
$$\begin{align*}
&\sum\limits^{\infty}_{n=1} A_{n} \int^{\pi}_{0} \sin n\theta \sin \theta \: d\theta & &\to & & A_{1} \frac{\pi}{2} \\
&\sum\limits^{\infty}_{n=1} \frac{A_{n}}{2} \int^{\pi}_{0} \sin n\theta \sin 2\theta \: d\theta & &\to & & A_{2} \frac{\pi}{4}
\end{align*}$$

Subbing these into the moment equation and doing the other two integrals normally gets:

$$\begin{align*}
M_{LE}' &= - \frac{\rho V_{\infty}^{2}c^{2}}{2} \left( A_{0} \pi - A_{0} \frac{\pi}{2} + A_{1} \frac{\pi}{2} - A_{2} \frac{\pi}{4} \right)\\
&= - \frac{\pi}{4} \rho V_{\infty}^{2}c^{2} \left( A_{0}  + A_{1}- \frac{A_{2}}{2}  \right)\\\\
C_{m,LE} &= - \frac{\pi}{4} \rho V_{\infty}^{2}c^{2} \left( A_{0}  + A_{1}- \frac{A_{2}}{2}  \right) \frac{1}{\frac{1}{2}\rho V_{\infty}^{2} c^{2}}\\
&=  - \frac{\pi}{2} \left( A_{0}  + A_{1}- \frac{A_{2}}{2}  \right)
\end{align*}$$

Recall from [[thin symmetric airfoil analysis]] that the equation for the quater chord moment coefficient is:
$$\begin{align*}
C_{m,c/4} &= C_{m,LE} + \frac{C_{l}}{4}
\end{align*}$$

We know the defentitions for these so can get the quater chord moment equation defined from $A_{n}$:

$$\begin{align*}
 C_{m,LE} &= - \frac{\pi}{2} \left( A_{0}  + A_{1}- \frac{A_{2}}{2}  \right) & C_{l} &= 2\pi \left( A_{0} + \frac{A_{1}}{2} \right)
\end{align*}$$
$$\begin{align*}
C_{m,c/4} &= C_{m,LE} + \frac{C_{l}}{4} & &\to & C_{m,c/4} &=- \frac{\pi}{2} \left( A_{0}  + A_{1}- \frac{A_{2}}{2}  \right) + \frac{1}{4}2\pi \left( A_{0} + \frac{A_{1}}{2} \right)\\
&& && &...\\
&& && C_{m,c/4} &= \frac{\pi}{4} (A_{2} - A_{1})
\end{align*}$$

Something quite important to note is that this shows the moment about the quater chord is only dependent on $A_{2}$ and $A_{1}$ which by looking at the defenition of $A_{1},A_{2}$ we know is independent of $\alpha$ hence $C_{m,c/4}$ is independent of AoA:
$$\frac{dC_{m,c/4}}{d\alpha} = 0$$

This is the defenition of the [[aerodynamic centre]]! So for a cambered thin foil the [[aerodynamic centre]] is at the quater chord point! (which is also what was found in [[thin symmetric airfoil analysis]])
