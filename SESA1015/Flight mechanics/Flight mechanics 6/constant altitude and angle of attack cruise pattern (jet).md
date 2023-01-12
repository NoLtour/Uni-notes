---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Constant altitude and angle of attack [[cruise pattern]] (jet)
Unlike the [[cruise climb with constant speed|the other technique]] we encountered this one involves varying the speed and maintaining the same altitude.

# CHECK WORKING NOT SURE IF RIGHT

### Assumptions
The angle of attack is constant and the altitude is constant:
- $L/D=$ constant (angle of attack is constant)
- $\rho=$ constant (altitude is constant)

Hence since:
$$\begin{align*}
  W = L &= \frac{1}{2}\rho V^{2}S C_L
\end{align*}$$
We must be varying the speed to control lift as weight changes, so $V=\sqrt\frac{2W}{\rho S C_L}$

### Maths time
We know from [[specific fuel consumption (aircraft)|specific fuel consumption]]:
$$\begin{align*}
   \frac{dW}{dt} = -sT &= -sD\\
\therefore \frac{dW}{dx} \frac{dx}{dt} = \frac{dW}{dx}V &=
\end{align*}$$
$$\begin{align*}
   \frac{dW}{dx}V &= -sD & V=&\sqrt\frac{2W}{\rho S C_L} & D &= \frac{1}{2}V^{2}\rho SC_D \\
\frac{dW}{dx} &= -s\frac{1}{2}V^{2}SC_D \rho\\
&= -s\frac{1}{2}VSC_D \rho\\
&= -\frac{s \cdot SC_D \rho}{2} \sqrt\frac{2W}{\rho S C_L}\\
\int 1 \cdot dx &= -\int \frac{2}{s \cdot SC_D \rho} \sqrt\frac{\rho S C_L}{2W} \cdot dW\\
x &= -\frac{2}{s \cdot SC_D \rho} \cdot \sqrt{ \frac{\rho S C_L}{2} } \int  \sqrt\frac{1}{W} \cdot dW\\
&= -\frac{1}{s C_D \rho} \cdot \sqrt{ \frac{2\rho C_L}{S} } \int  \frac{1}{\sqrt W} \cdot dW\\
&= -\frac{1}{s C_D \rho} \cdot \sqrt{ \frac{2\rho C_L}{S} } \cdot 2\ln(\sqrt W) + c \\\\
&= \frac{2}{s C_D \rho} \cdot \sqrt{ \frac{2\rho C_L}{S} } \cdot \ln\left(\sqrt {\frac{W_s+W_f}{W}}\right)\\
&= \frac{2}{s C_D \rho} \cdot \sqrt{ \frac{2\rho C_L}{S} } \cdot \ln\left( {\frac{W_s+W_f}{W}}\right)\\
\end{align*}$$

$$\begin{align*}
\therefore R &= \frac{2}{s C_D \rho} \cdot \sqrt{ \frac{2\rho C_L}{S} } \cdot \ln\left(1+ {\frac{W_f}{W_s}}\right)\\
&= \frac{2}{s} \cdot \sqrt{ \frac{2 }{S\rho} } \cdot \frac{\sqrt{C_L}}{C_D} \cdot \ln\left(1+ {\frac{W_f}{W_s}}\right)
\end{align*}$$

So to maxamise $R$ we must find when $\frac{\sqrt{C_L}}{C_D}$ is at a maximum.
Hence we will need equations for the [[Drag coefficient]] 

$$\begin{align*}
   &   &  C_D &= C_{Do} + \dfrac{K(C_L)^{2}}{\pi A}\\
 \frac{d}{dC_L} \cdot\frac{\sqrt{C_L}}{C_D}&=  \frac{d}{dC_L} \cdot\frac{\sqrt{ C_L }}{C_{Do} + \dfrac{K(C_L)^{2}}{\pi A}} & \\
&= \frac{\left(C_{Do}+\frac{K}{\pi A}C_L^{2}\right) \frac{1}{2} C_L^{\frac{-1}{2}} - C_L^{\frac{1}{2}} \frac{2K}{\pi A} C_L}{ \left(C_{Do} + \frac{K}{\pi A} C_L^{2}\right)^2 }\\
0 &= \left(C_{Do}+\frac{K}{\pi A}C_L^{2}\right) \frac{1}{2} C_L^{\frac{-1}{2}} - C_L^{\frac{1}{2}} \frac{2K}{\pi A} C_L\\
C_L^{\frac{1}{2}} \frac{2K}{\pi A} C_L &= \left(C_{Do}+\frac{K}{\pi A}C_L^{2}\right) \frac{1}{2} C_L^{\frac{-1}{2}}\\

4C_L^{2} \frac{K}{\pi A}  &= C_{Do}+\frac{K}{\pi A}C_L^{2}\\

3\dfrac{K(C_L)^{2}}{\pi A}  &= C_{Do} & C_{Di}&=\dfrac{K(C_L)^{2}}{\pi A} \\
\therefore C_{Do} &= 3C_{Di} \:\:\:\: at\:max\:R\\
\end{align*}$$

^fbd1e2

Note $C_{Do} = 3C_{Di}$.

Now if we use the resault above and the [[lift coefficient at min drag]]:

$$\begin{align*}
\dfrac{3K(C_L)^{2}}{\pi A}  &= C_{Do} \\
C_{Lmax} &= \sqrt{\frac{C_{Do}}{\frac{3K}{\pi A}}}\\
&= \frac{1}{\sqrt3} \sqrt{\frac{C_{Do}\pi A}{K}} & C_{LminD} &= \sqrt\frac{C_{Do}\pi A}{K}\\
&= \frac{1}{\sqrt3} C_{LminD} \\
& & V \propto \frac{1}{\sqrt C_L}\\
\therefore V_{cruise} &= \sqrt[4]{3} V_{minDrag}\\
&\approx 1.316 V_{minDrag}
\end{align*}$$

Now subbing back into our $R$ equation:

$$\begin{align*}
    R &= \frac{2}{s} \cdot \sqrt{ \frac{2 }{S\rho} } \cdot \frac{\sqrt{C_L}}{C_D} \cdot \ln\left(1+ {\frac{W_f}{W_s}}\right) & C_{Lmax} &= \sqrt{\frac{C_{Do}}{\frac{3K}{\pi A}}} & C_D &= C_{Do} + C_{Di} & C_{Do} &= 3C_{Di}\\
& & C_{Lmax} &= \sqrt{\frac{C_{Do}\pi A}{3K}} & C_D &= \frac{4}{3} C_{Do} \\
&= \frac{2}{s} \cdot \sqrt{ \frac{2 }{S\rho} } \cdot \frac{\sqrt{\sqrt{\frac{C_{Do}\pi A}{3K}}}}{\frac{4}{3} C_{Do}} \cdot \ln\left(1+ {\frac{W_f}{W_s}}\right)\\
&= \frac{3}{2s} \cdot \sqrt{ \frac{2 }{S\rho} } \cdot \sqrt[4]{\frac{C_{Do}\pi A}{3K(C_{Do})^{4}}}  \cdot \ln\left(1+ {\frac{W_f}{W_s}}\right)\\
&= \frac{3}{2s} \cdot \sqrt{ \frac{2 }{S\rho} } \cdot \sqrt[4]{\frac{\pi A}{3K(C_{Do})^{3}}}  \cdot \ln\left(1+ {\frac{W_f}{W_s}}\right)
\end{align*}$$

#### Implications
The optimum speed for maximising range without changing altitude occurs at 1.316 times the [[min drag speed in steady level flight|min drag speed]].

> ### $$ R_{max} = \frac{3}{2s} \cdot \sqrt{ \frac{2 }{S\rho} } \cdot \sqrt[4]{\frac{\pi A}{3K(C_{Do})^{3}}}  \cdot \ln\left(1+ {\frac{W_f}{W_s}}\right) = \frac{2}{s} \cdot \sqrt{ \frac{2 }{S\rho} } \cdot \frac{\sqrt{C_{LRmax}}}{C_D} \cdot \ln\left(1+ {\frac{W_f}{W_s}}\right)$$ 
> #### $$ C_{LRmax} = \sqrt{\frac{C_{Do}\pi A}{3K}} $$
> #### $$ V_{cruise} = \sqrt[4]{3}\cdot V_{minDrag} $$
>> where:
>> $R_{max}=$  The max range for constant altitude flight
>> $C_{Lmax} =$ The coefficient of lift at max range
>> $S=$ [[Wing plan area|Gross wing area]]
>> $s=$ [[specific fuel consumption (aircraft)|s.f.c]]
>> $\rho=$ air density
>> $A=$ [[wing aspect ratio]]
>> $C_{Do}=$ [[form drag coefficient]] 

This tells us to get the best range we need to:
- fly at a high altitude.
- minamise wing area
- maxamise aspect ratio
- minamise dry weight
- minamise [[specific fuel consumption (aircraft)|s.f.c]]

![[inaccuracys when modeling cruise patterns]]
