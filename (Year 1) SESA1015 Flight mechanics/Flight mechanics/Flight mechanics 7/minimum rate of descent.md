---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you find
## Minimum rate of descent
### Equation

> ### $$ - \frac{dh}{dt}  =  -\dot{h} = V_{MP} \cdot \theta_{\dot{h} \:min} = 4 \sqrt{  \frac{2Wk }{3\rho S} } \cdot \sqrt[4]{  \frac{ k C_{Do}}{ 3 }   } $$ 
>> where:
>> $\frac{dh}{dt}  =  \dot{h}=$ [[minimum rate of descent]] 
>> $V_{DP}=$ [[minimum power speed]]
>> $\theta_{\dot{h} \:min}=$ minimum rate of descent angle

### Proof
We know $- \frac{dh}{dt} = V \frac{D}{W}$ from [[gliding without thrust]], so to minamise the rate of descent we need to find where VD is at a minimum (W can be approximated as constant since not only is this a small duration but thrust is zero).

Luckily we already know that to get VD at a minimum we can use the [[minimum power speed]].

Now we can also get the [[minimum power speed#Lift to drag ratio]] and sub that in.

$$\begin{align*}
   \theta_{\dot{h} \:min} &= \frac{1}{\left(\frac{L}{D}_{minP}\right)} & \frac{L}{D}_{minP} &= \frac{1}{4} \sqrt\frac{3}{k C_{Do}  } \\
 &=  4 \sqrt\frac{k C_{Do}}{ 3 }
\end{align*}$$

The speed at this angle of descent for a shallow glide angle ($L\approx W$) is [[minimum power speed]]:
$$\begin{align*}
 - \frac{dh}{dt} &= V \frac{D}{W} &   V_{MP} &= \sqrt{ \frac{W}{\rho S} } \cdot \sqrt[4]{  \frac{ 4k }{ C_{Do} }   } \cdot \sqrt[4] \frac{1}{3}\\
&= \sqrt{ \frac{W}{\rho S} } \cdot \sqrt[4]{  \frac{ 4k }{ C_{Do} }   } \cdot \sqrt[4] \frac{1}{3} \cdot 4 \sqrt\frac{k C_{Do}}{ 3 }\\
&= 4 \sqrt{ \frac{Wk C_{Do}}{3\rho S} } \cdot \sqrt[4]{  \frac{ 4k }{ 3C_{Do} }   }\\
&= 4 \sqrt{  \frac{2Wk }{3\rho S} } \cdot \sqrt[4]{  \frac{ k C_{Do}}{ 3 }   }
\end{align*}$$

