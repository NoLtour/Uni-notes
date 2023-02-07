---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you find the
## Range of a piston engined aircraft
### Getting fuel consumption
Basically the same as the other range equations we have calculated so far, except that the way we measure fuel constumption changed.

![[fuel consumption of a piston engined aircraft]]

### Converting to thrust
Though the form above is pretty useless, so we can convert it to a more useful form by converting power into thrust.

![[propeller combined efficiency]]

We know that to maintain a steady speed drag=thrust and P=Fv so $P=DV$, subbing that into the equations:

$$\begin{align*}
  & & \eta P' &= P & P &= DV\\
\frac{dW(t)}{dt} &= -P's' &  P' &= \frac{P}{\eta}\\
\frac{dW(t)}{dt} &= -\frac{P}{\eta}s'\\
\frac{dW(t)}{dt} &= -\frac{DV}{\eta}s' & 1=\frac{W}{L}\\
\frac{dW(t)}{dt} &= -\frac{DV}{\eta}s'\cdot\frac{W}{L}\\
\frac{dW(t)}{dt} &= -V\frac{s'}{\eta}\cdot\frac{WD}{L}\\
\frac{dW(t)}{dt} &=- \frac{dx}{dt}\frac{s'}{\eta}\cdot\frac{WD}{L}\\
-\int \frac{L}{WD}\frac{\eta}{s'} dW &=\int 1 dx\\
-\frac{\eta}{s'}\cdot\frac{L}{D}\int \frac{1}{W}  dW &=\int 1 dx\\
-\frac{\eta}{s'}\cdot\frac{L}{D} \ln(W) + k  dW &= R\\
R &= \frac{\eta}{s'}\frac{L}{D}\cdot \ln\left( \frac{W_1}{W_2} \right)
\end{align*}$$

### Conclusion
This is known as the [[Breguet range equation (piston engine)]] but for propeller aircraft:
![[Breguet range equation (piston engine)]]