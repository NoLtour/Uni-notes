---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can we relate
## Pressure, volume and temperatures relationship in an idea gas
### Pv and Temperature
Using [[calculating the pressure of a gas molecule|this proof]] along with [[relationship between temperature and kinetic energy of particles|this equation]]

![[calculating the pressure of a gas molecule#^3c65ed]]

![[relationship between temperature and kinetic energy of particles#^2669d3]]

I wonder how these equations combine :thinking: :
$$\begin{align*}
   KE_{particle}& = \frac{3}{2} k_B T\\
pV=\frac{2N}{3}KE_{particle}&\\
pV=\frac{2N}{3}\frac{3}{2} k_B T&\\
\therefore pV = Nk_B T
\end{align*}$$

This is a form of the [[ideal gas law]].

### Relating to mol
Finally we can relate the [[Boltzmann constant]] to the [[universal gas constant]] with $R_u=N_A k_B$ and $n=\frac{N}{N_A}$ producing a more useful form of the [[ideal gas law]]:

$$\begin{align*}
   pV &= nR_uT
\end{align*}$$

### Relating to mass
All of these are kinda useless for engineers, because we don't count the number of particles we work with. We use kg, because [[engineers are simply based]].

$$\begin{align*}
  pV &= nR_uT &  m_u &= \frac{m}{n} &  R&= \frac{R_u}{m_u} \\
pV m_u  &= \frac{m}{n} nR_uT & Rm_u&=R_u\\
pV   &= \frac{m}{m_u} Rm_uT\\
pV   &= mRT
\end{align*}$$

By the way R is the [[individual gas constant]].