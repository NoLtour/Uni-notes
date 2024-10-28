---
aliases: [""]
tags: []
---

## Shortcuts for PMTPE for springs

### Unit spring

We already discussed [[principle of minimum total potential energy for a spring]], but that method is slow and wont scale nicely. Something convenient is due to math magic (proven outside the scope of this module) there's LOTS of shortcuts which allow us to formulate these problems with faaar less effort.

Let's start with a unit spring again, but this time it's just free standing with two points:

![[Pasted image 20241016145450.png]]

It's strain energy can be laid out in a new way:

$$\begin{align*}
U &= \frac{1}{2} k (q_{2} - q_{1}) &&\to&  U &= \frac{1}{2} \begin{pmatrix} q_{1} & q_{2} \end{pmatrix} \begin{pmatrix} k & -k\\-k & k \end{pmatrix}\begin{pmatrix}q_{1}\\q_{2}\end{pmatrix} &&\to&  U &= \frac{1}{2} \begin{pmatrix} q_{1}\\ q_{2} \end{pmatrix}^{T} \begin{pmatrix} k & -k\\-k & k \end{pmatrix}\begin{pmatrix}q_{1}\\q_{2}\end{pmatrix}
\end{align*}$$

This format looks strange but is useful because it becomes a unit block for chaining many springs together. To tidy things up we often instead use the shorthand:

$$\begin{align*}
 U &= \frac{1}{2} \begin{pmatrix} q_{1}\\ q_{2} \end{pmatrix}^{T} \begin{pmatrix} k & -k\\-k & k \end{pmatrix}\begin{pmatrix}q_{1}\\q_{2}\end{pmatrix} &&\to& U&= \frac{1}{2} \{q\}^{T}[K] \{q\} 
\end{align*}$$

^ef3930

Note that we call $[K]$ a [[stiffness matrix]].

Then the potential energy is trivial:
$$\begin{align*}
V &= -(F_{1} q_{1} + F_{2} q_{2}) &&\to& V &= -\begin{pmatrix} F_{1} & F_{2} \end{pmatrix} \begin{pmatrix}q_{1}\\q_{2}\end{pmatrix} &&\to& V &= -\begin{pmatrix} F_{1} \\ F_{2} \end{pmatrix}^{T} \begin{pmatrix}q_{1}\\q_{2}\end{pmatrix} &&\to& V&= \{F\}^{T}\{q\} 
\end{align*}$$

^1ce236

### Combining springs

Ok, so lets take what was solved in [[principle of minimum total potential energy for a spring#Two springs]], but add a reaction this time:

![[Pasted image 20241016150214.png]]

Taking the strain energy, we can bang out it's matrix form:

$$\begin{align*}
U_{1} &= \frac{1}{2} k_{1} (q_{2} - q_{1}) &&\to&  U_{1} &= \frac{1}{2} \begin{pmatrix} q_{1}\\ q_{2} \end{pmatrix}^{T} \begin{pmatrix} k_{1} & -k_{1}\\-k_{1} & k_{1} \end{pmatrix}\begin{pmatrix}q_{1}\\q_{2}\end{pmatrix} \\
U_{2} &= \frac{1}{2} k_{2} (q_{3} - q_{2}) &&\to&  U_{2} &= \frac{1}{2} \begin{pmatrix} q_{2}\\ q_{3} \end{pmatrix}^{T} \begin{pmatrix} k_{2} & -k_{2}\\-k_{2} & k_{2} \end{pmatrix}\begin{pmatrix}q_{2}\\q_{3}\end{pmatrix} \\
\end{align*}$$

This is where the short cuts come in, we *could* combine these by just adding them onto eachother after expanding it... but that would be pointless. We want to use our short cut, so let's zero pad em:

$$\begin{align*}
  U_{1} &= \frac{1}{2} \begin{pmatrix} q_{1}\\ q_{2} \end{pmatrix}^{T} \begin{pmatrix} k_{1} & -k_{1}\\-k_{1} & k_{1} \end{pmatrix}\begin{pmatrix}q_{1}\\q_{2}\end{pmatrix} &&\to&
  U_{1} &= \frac{1}{2} \begin{pmatrix} q_{1}\\ q_{2}\\q_{3} \end{pmatrix}^{T} \begin{pmatrix} k_{1} & -k_{1} & 0\\-k_{1} & k_{1} & 0\\0 & 0 & 0 \end{pmatrix}\begin{pmatrix}q_{1}\\q_{2}\\q_{3}\end{pmatrix} \\
U_{2} &= \frac{1}{2} \begin{pmatrix} q_{2}\\ q_{3} \end{pmatrix}^{T} \begin{pmatrix} k_{2} & -k_{2}\\-k_{2} & k_{2} \end{pmatrix}\begin{pmatrix}q_{2}\\q_{3}\end{pmatrix} &&\to&  U_{2} &= \frac{1}{2} \begin{pmatrix} q_{1}\\q_{2}\\ q_{3} \end{pmatrix}^{T} \begin{pmatrix}0 & 0 & 0 \\0 & k_{2} & -k_{2}\\0 & -k_{2} & k_{2} \end{pmatrix}\begin{pmatrix}q_{1}\\q_{2}\\q_{3}\end{pmatrix} \\
\end{align*}$$

As you can see, if we expanded these out then nothings changed. Obviously this is done for formatting reasons, those reasons being that now we can add em together:

$$\begin{align*}
U &= U_{1} + U_{2} &&\to& U &= \frac{1}{2} \begin{pmatrix} q_{1}\\q_{2}\\ q_{3} \end{pmatrix}^{T} \begin{pmatrix}k_{1} & -k_{2} & 0 \\-k_{1} & k_{1}+k_{2} & -k_{2}\\0 & -k_{2} & k_{2} \end{pmatrix}\begin{pmatrix}q_{1}\\q_{2}\\q_{3}\end{pmatrix} \\ & &&& &= \frac{1}{2} \{q\}^{T}[K] \{q\} 
\end{align*}$$

The potential energy equation is simple enough that I'm just going to state it:

$$\begin{align*}
V &= -\begin{pmatrix}R\\F_{1}\\F_{2}\end{pmatrix}^{T}\begin{pmatrix}q_{1}\\q_{2}\\q_{3}\end{pmatrix} &&\to& V &= - \{F\}^{T} \{q\}
\end{align*}$$

Now we have our potential and strain energies, we'd do the whole differentiation thing.... but instead something that kinda just works (not showing the proof) is going:

$$\begin{align*}
[K]\{q\} &= \{F\} &&\to& \begin{pmatrix}k_{1} & -k_{2} & 0 \\-k_{1} & k_{1}+k_{2} & -k_{2}\\0 & -k_{2} & k_{2} \end{pmatrix}\begin{pmatrix}q_{1}\\q_{2}\\q_{3}\end{pmatrix}  &= \begin{pmatrix}R\\F_{1}\\F_{2}\end{pmatrix}
\end{align*}$$

A problem you hit however is that $[K]$ is [[singular matrix|singular]], which makes sense if you consider the problem. We have no boundary conditions to hold the thing in place, of course it's singular. So how do we apply boundary conditions?

Well if the wall is fixed, then $q_{1}=0$ which means:

$$\begin{align*}
\begin{pmatrix}k_{1} & -k_{2} & 0 \\-k_{1} & k_{1}+k_{2} & -k_{2}\\0 & -k_{2} & k_{2} \end{pmatrix}\begin{pmatrix}q_{1}=0\\q_{2}\\q_{3}\end{pmatrix}  &= \begin{pmatrix}R\\F_{1}\\F_{2}\end{pmatrix} &&\to& \begin{pmatrix} k_{1}+k_{2} & -k_{2}\\ -k_{2} & k_{2} \end{pmatrix}\begin{pmatrix}q_{2}\\q_{3}\end{pmatrix}  &= \begin{pmatrix}F_{1}\\F_{2}\end{pmatrix}
 &&\to& \begin{pmatrix}q_{2}\\q_{3}\end{pmatrix}  &=  \begin{pmatrix} k_{1}+k_{2} & -k_{2}\\ -k_{2} & k_{2} \end{pmatrix}^{-1}\begin{pmatrix}F_{1}\\F_{2}\end{pmatrix}
\end{align*}$$

Then if we want to recover reaction force, we still can:

$$\begin{align*}
\begin{pmatrix}k_{1} & -k_{2} & 0 \\-k_{1} & k_{1}+k_{2} & -k_{2}\\0 & -k_{2} & k_{2} \end{pmatrix}\begin{pmatrix}q_{1}\\q_{2}\\q_{3}\end{pmatrix}  &= \begin{pmatrix}R\\F_{1}\\F_{2}\end{pmatrix} &&\to&
\begin{pmatrix}k_{1} & -k_{2} & 0 \end{pmatrix}\begin{pmatrix}q_{1}\\q_{2}\\q_{3}\end{pmatrix}  &= R
\end{align*}$$

Simple as.

Looking back over it, it's quite simple to imagine how many of these steps (which were written out for clarity) could be skipped, even further streamlining the process.
