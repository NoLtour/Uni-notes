---
aliases: [""]
tags: []
---

## Solving linear oscillatory FEA systems in the absence of external force

### 1 DoF

If we recall the 1-DoF system from [[Hamiltons principle on a single DoF oscillator]], we can solve it using the [[ansatz]] $q=e^{st}$:

$$\begin{align*}
 &&q&= e^{st} \\
m\ddot{q} + k q &= 0 &&\to& m s^{2} e^{st} + ke^{st} &= 0 &&\to&  (m s^{2}+ k) e^{st} &= 0 &&\to&  s &= \pm i\sqrt{\frac{k}{m}}
\end{align*}$$

So our solutions become:

$$\begin{align*}
q(t) &= e^{t i\sqrt{\frac{k}{m}}} &&& q(t) &= e^{-t i\sqrt{\frac{k}{m}}}
\end{align*}$$

Which forms the [[general and particular solution|general solution]]:

$$\begin{align*}
&&&& \omega &= \sqrt{\frac{k}{m}} \\
q(t) &= A e^{t i\sqrt{\frac{k}{m}}} + B e^{-t i\sqrt{\frac{k}{m}}} &&\to& &... &&\to&  q(t) &= C \cos(\omega t) + D \sin (\omega t)
\end{align*}$$

Which we've seen countless times before in other modules, with $\omega$ obviously being the [[undamped free vibration (dynamics)|natural frequency]].

### Multiple DoF

We're dealing with systems with many DoF, taking the form:

$$\begin{align*}
[M]\{\ddot{q}\} + [K]\{q\} &= \{0\}
\end{align*}$$

We're going to skip over the proof, but these systems will show [[synchronous motion]], where all coordinates move such that their extremities and equilibria are reached at the same time (all nodes share frequency and phase). Hence, we could express the node states as:

$$\begin{align*}
\{q(t)\} &=  \{u\}\sin(\omega t)
\end{align*}$$

Here $\{u\}$ is the amplitude vector, which then results in:

$$\begin{align*}
\{q(t)\} &=  \{u\}\sin(\omega t) &&\to& \{\dot{q}(t)\} &=  w\{u\}\cos(\omega t) &&\to& \{\ddot{q}(t)\} &=  -w^{2}\{u\}\sin(\omega t)
\end{align*}$$

Subbing back:

$$\begin{align*}
[M]\{\ddot{q}\} + [K]\{q\} &= \{0\} &&\to&   -[M] w^{2}\{u\}\sin(\omega t)  + [K] \{u\}\sin(\omega t)  &= \{0\} &&\to&   

(-w^{2}[M]\{u\}  + [K] \{u\})\sin(\omega t) &= \{0\}
\end{align*}$$

If we ignore the trivial solution of $\sin(\omega t)=0$ we can get:

$$\begin{align*}
&& \lambda &= \omega^{2} \\
(-w^{2}[M]\{u\}  + [K] \{u\})\sin(\omega t) &= \{0\} &&\to& [K] \{u\} &= \lambda[M]\{u\} &&\to& [M]^{-1}[K] \{u\} &= \lambda\{u\}
\end{align*}$$

Which is just a standard [[eigenvalues and eigenvectors|eigenvalue]] problem, like what we solved in [[Aero Systems Control Overview|control systems]]. 

In frequency response terms, this means that an $n$ degree of freedom system will end up with $n$ natural frequencies ($\omega_{i}$). There may also be a "rigid body mode" where the structure moves without oscillation if $\omega_{i}=0$, this occurs on structures which aren't anchored.

> ### $$\begin{align*}  [M]\{\ddot{q}\} + [K]\{q\} &= \{0\} \end{align*}$$
> ### $$\begin{align*} \{q \} &=  \{u\}\sin(\omega t) \end{align*}$$
> ### $$\begin{align*}  ([M]^{-1}[K] - I\lambda) \{u\} &= 0 &&& \det{([M]^{-1}[K] - I\lambda)}=0 \end{align*}$$
>> where:
>> $[M]=$ [[shortcuts for Hamiltons Principle|mass matrix]]
>> $[K]=$ [[stiffness matrix]]
>> $\{q\}=$ column vector for nodes state
>> $\{u\}=$ amplitudes of oscillation
>> $\lambda=\omega_{i}^{2}=$ the $i_{th}$ natural frequency squared
>> $I=$ [[unit matrix]]
>> 
>> By solving the determinant, we can find the value's of $\lambda$ and then the value's of $u$

#### Example

![[Pasted image 20241114105939.png]]
Take this system, it's equation would end up being:

$$\begin{align*}
\begin{pmatrix} m & 0 \\ 0 & m \end{pmatrix} \{\ddot{q}\} + \begin{pmatrix} k & -k \\ -k  & k \end{pmatrix}\{q\} &= 0
\end{align*}$$

If we sub that into our determinant equation we'd get:

$$\begin{align*}
\det{([M]^{-1}[K] - I\lambda)}&= 0 &&\to&  \det{\left(\begin{pmatrix} m & 0 \\ 0 & m \end{pmatrix}^{-1}\begin{pmatrix} k & -k \\ -k  & k \end{pmatrix}-I \lambda\right)}&= 0
\end{align*}$$

$$\begin{align*}
&\begin{pmatrix} m & 0 \\ 0 & m \end{pmatrix}^{-1}\begin{pmatrix} k & -k \\ -k  & k \end{pmatrix} - I\lambda&&\to& \frac{1}{m} 
&\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} k & -k \\ -k  & k \end{pmatrix} - I\lambda &&\to&
& \frac{1}{m}\begin{pmatrix} k & -k \\ -k & k \end{pmatrix} - I\lambda  &&\to&
& \begin{pmatrix} \frac{k}{m}- \lambda  & - \frac{k}{m}  \\ - \frac{k}{m} & \frac{k}{m}- \lambda  \end{pmatrix}  
\end{align*}$$

Back to the determinant:

$$\begin{align*}
\det  \begin{pmatrix} \frac{k}{m}- \lambda  & - \frac{k}{m}  \\ - \frac{k}{m} & \frac{k}{m}- \lambda  \end{pmatrix}      &= 0 &&\to& 
\left( \frac{k}{m}- \lambda\right)^{2}  -  \left(- \frac{k}{m} \right)^{2} &= 0 &&\to&  -2 \frac{k}{m}\lambda + \lambda^{2}  &= 0  &&\to&  \lambda\left(2 \frac{k}{m} - \lambda\right)  &= 0
\end{align*}$$

Hence:

$$\begin{align*}
\lambda_{1} &= 0 &&& \lambda_{2}  &= \frac{2k}{m}\\
\omega_{1} &= 0 &&& \omega_{2} &= \sqrt{\frac{2k}{m}}
\end{align*}$$

Then we can find the relative amplitudes:

$$\begin{align*}
 ([M]^{-1}[K] - I\lambda) \{u\} &= 0 &&\to& 
 \begin{pmatrix} \frac{k}{m}- \lambda  & - \frac{k}{m}  \\ - \frac{k}{m} & \frac{k}{m}- \lambda  \end{pmatrix}   \begin{pmatrix} u_{1}\\u_{2} \end{pmatrix}  &= 0 &&\to& 
  \begin{pmatrix} u_{1}\left(\frac{k}{m}- \lambda\right) - u_{2} \frac{k}{m}    \\  - u_{1} \frac{k}{m} + u_{2}\left( \frac{k}{m}- \lambda\right) \end{pmatrix}  &= 0 &&\to& 
  \begin{pmatrix} u_{1} (k- m\lambda ) - u_{2} k   \\  - u_{1} k + u_{2} ( k-m \lambda ) \end{pmatrix}  &= 0
\end{align*}$$

We can just take the first row:

$$\begin{align*}
u_{1} (k- m\lambda ) - u_{2} k  &= 0 &&\to&  \frac{u_{1}}{u_{2}} &= \frac{k}{k - m\lambda }
\end{align*}$$

Now subbing in our lambda's, we can get our corresponding amplitude ratio's:

$$\begin{align*}
&& \lambda &= 0 \\
\frac{u_{1}}{u_{2}} &= \frac{k}{k - m\lambda } &&\to& \frac{u_{1}}{u_{2}} &= \frac{k}{k -0}   &&\to& \frac{u_{1}}{u_{2}} &= 1
\end{align*}$$

$$\begin{align*}
&& \lambda &= \frac{2k}{m} \\
\frac{u_{1}}{u_{2}} &= \frac{k}{k - m\lambda } &&\to& \frac{u_{1}}{u_{2}} &= \frac{k}{k -m\frac{2k}{m}}   &&\to& \frac{u_{1}}{u_{2}} &= -1
\end{align*}$$

Note that we can also check for non natural frequencies!
