---
aliases: [""]
tags: []
---

## Thin camvered airfoil analysis

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

So we can get a defenition of [[vortex sheet strength]] if we know $A_{0}$ and $A_{n}$.
