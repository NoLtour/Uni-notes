---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How would you go about
## Calculating aircraft range
### Maths
#### Setting it up
We know:

![[specific fuel consumption (aircraft)#^1d3da2]]

$$\begin{align*}
   \frac{dW}{dt} &= -sT\\
& & W=&T & L=&W\\
\frac{dW}{dt} &= -sD &   &  &  1=&\frac{W}{L}\\
\therefore \frac{dW}{dt} &= -s \frac{WD}{L}\\
\end{align*}$$

Also:

$$\begin{align*}
  \frac{dW}{dt}  &= \\
&= \frac{dW}{dx} \frac{dx}{dt}\\
\therefore \frac{dW}{dt} &= \frac{dW}{dx} V
\end{align*}$$

Equating these two resaults:

$$\begin{align*}
   \frac{dW}{dx} V &= -s \frac{WD}{L}\\
\frac{dW}{dx} &= - \frac{s}{V} \frac{D}{L}W
\end{align*}$$

We now have an equation relating the rate of change of weight over distance, assuming that $\frac{s}{V}$ and $\frac{D}{L}$ are constant that is.

#### Integration time
So lets start to integrate:

$$\begin{align*}
  \frac{dW}{dx} &= - \frac{s}{V} \frac{D}{L}W\\
\int \frac{1}{W}dW &= \int - \frac{s}{V} \frac{D}{L}dx\\
\int \frac{1}{W}dW &= -\frac{s}{V} \frac{D}{L} \int 1 dx\\
\ln(W) &= -\frac{s}{V} \frac{D}{L}x + k\\
& & at\:x=0,\:\:W=W_f+W_s &\\
& & \ln(W_f+W_s) &= -\frac{s}{V} \frac{D}{L}0 + k\\
& & \ln(W_f+W_s) &= k\\
\ln(W) &= -\frac{s}{V} \frac{D}{L}x + \ln(W_f+W_s)\\
\ln\left(\frac{W}{W_f+W_s}\right) &= -\frac{s}{V} \frac{D}{L}x\\
- \frac{V}{s} \frac{L}{D} \ln\left(\frac{W}{W_f+W_s}\right) &= x\\
\therefore \frac{V}{s} \frac{L}{D} \ln\left(1+\frac{W_f}{W_s}\right) &= x\\
\end{align*}$$

#### Final equation
![[Breguet range equation (jets)]]