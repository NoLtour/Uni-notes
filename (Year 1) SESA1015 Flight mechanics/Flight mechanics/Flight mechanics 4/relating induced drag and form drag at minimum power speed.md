---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Whats the methods for
## Relating induced drag and form drag at minimum power speed
We know [[minimum power speed]] occurs when $V_{MP} = V_{MD} \cdot \sqrt[4] \frac{1}{3}$ and [[min drag speed in steady level flight]] $V_{MD}=\sqrt{ \frac{W}{\rho S} } \cdot \sqrt[4]{  \frac{ 4k }{ C_{Do} }   }$

$$\begin{align*}
&& V_{MP} &= V_{MD} \cdot \sqrt[4] \frac{1}{3} & W &= \frac{1}{2} \rho S C_L V^{2} & V_{MD}&=\sqrt{ \frac{W}{\rho S} } \cdot \sqrt[4]{  \frac{ 4k }{ C_{Do} }   }\\
&&  V_{MP} &= \sqrt{ \frac{W}{\rho S} } \cdot \sqrt[4]{  \frac{ 4k }{ C_{Do} }   } \cdot \sqrt[4] \frac{1}{3} &\frac{2W}{\rho S V^{2}} &= C_L\\
&&V_{MP}^{2} &= \frac{W}{\rho S} \cdot \sqrt{  \frac{ 4k }{ 3 C_{Do} }   } \\
&&& &  \frac{2W}{\rho S \frac{W}{\rho S} \cdot \sqrt{  \frac{ 4k }{ 3 C_{Do} }   }} &= C_L\\
&&& &  \frac{2 \sqrt{ 3 C_{Do} }}{ \sqrt{ 4k }   } &= C_L\\
C_D &= C_{Do} + k C_L^2 && &  \frac{ \sqrt{ 3 C_{Do} }}{ \sqrt{ k }   } &= C_L\\
C_D &= C_{Do} + k \left(\frac{ \sqrt{ 3 C_{Do} }}{ \sqrt{ k }   }\right)^{2}\\
C_D &= C_{Do} + 3 C_{Do}\\
\therefore C_{Di} &= 3C_{Do}
\end{align*}$$

^dfc8e1

