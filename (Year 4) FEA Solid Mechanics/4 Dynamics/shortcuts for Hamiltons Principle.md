---
aliases:
  - mass matrix
tags:
---

## Shortcuts for [[Hamiltons principle|Hamilton's principle]]

![[Pasted image 20241112121917.png|500]]

If we take a two degree of freedom oscillator, working through [[Hamiltons principle]] we eventually reach the following set of equations (proved [[Notes 04 Dynamics(3).pdf|here]]):

$$\begin{align*}
m_{1} \ddot{q}_{1} + (k_{1} + k_{2}) q_{1} - k_{2} q_{2} &= 0 \\
m_{2} \ddot{q}_{2} - k_{2} q_{1} + k_{2} q_{2} &= 0 
\end{align*}$$

The next step is to slap this into a matrix:

$$\begin{align*}
\begin{pmatrix} m_{1} & 0 \\ 0 & m_{2}  \end{pmatrix}\begin{pmatrix} \ddot{q}_{1} \\ \ddot{q}_{2} \end{pmatrix} + \begin{pmatrix} k_{1} + k_{2} & -k_{2} \\ - k_{2}  & k_{2}  \end{pmatrix}\begin{pmatrix} {q}_{1} \\ {q}_{2} \end{pmatrix} &= \begin{pmatrix} 0\\0 \end{pmatrix}
\end{align*}$$

Look familiar? Well part of it should, the second half is identical to [[principle of minimum total potential energy for a spring#Two springs]] [[stiffness matrix]]! 

Simply, the implication of Hamilton’s Principle is that if our Lagrangian is the difference of two quadratics, which correspond with our Kinetic and Elastic Potential energies, without any integration we can state our Governing Equation of Motion using the Stiffness and Mass Matrices:

$$\begin{align*}
[M]_{n\times n} \{\ddot{q}\}_{n\times1} + [K]_{n\times n} \{{q}\}_{n\times1} &= \{{0}\}_{n\times1}
\end{align*}$$

We can use very similar methodology to what was presented in [[shortcuts for PMTPE for springs]] to combine DoF into a complex system! Note that here $[M]$ is the [[shortcuts for Hamiltons Principle|mass matrix]].

Note that we still haven't actually solved the system, that's because it's significantly more difficult than [[principle of minimum total potential energy|PMTPE]].
