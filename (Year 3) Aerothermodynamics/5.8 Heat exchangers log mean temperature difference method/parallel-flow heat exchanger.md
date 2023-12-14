---
aliases:
  - logarithmically weighted temp difference (parallel-flow)
tags:
---

## Parallel-flow heat exchanger

### Equation

> ### $$\begin{align*} \dot{Q}  &=  \ln (\Delta T_{lm}) h' A &&&  \ln\frac{\Delta T_{2}}{\Delta T_{1}}  &= - \left(\frac{1}{C_{h}}+ \frac{1}{C_{c}}\right)h' A \end{align*}$$
> ### $$\begin{align*} \frac{  \Delta T_{1} - \Delta T_{2}   }{\ln\frac{\Delta T_{1}}{\Delta T_{2}}} &= \Delta T_{lm}   \end{align*}$$
> ### $$\begin{align*} \Delta T &= T_{h} - T_{c}  &&& \Delta T_{1} &= T_{h,i} - T_{c,i}  &&&  \Delta T_{2} &= T_{h,o} - T_{c,o}  \end{align*}$$
>> where:
>> $\dot{Q}=$ heat transfer
>> $T_{lm}=$ [[parallel-flow heat exchanger|logarithmically weighted temp difference]]
>> $h'=$ [[general heat exchanger|total convection coefficient]]
>> $A=$ fluid contact area
>> $T=$ temp
>> $C=\dot{m}c_{p}=$ flowing [[constant pressure specific heat|constant pressure heat capacity]]

Note that this also assumes perfect flow mixing, such that the entire fluid cross section is a single temperature.

### Derivation

If we have a heat exchanger where we have two flows, passing in the same direction. It could be seen that the hotter fluid and colder fluid will approach each others temperatures the longer the two are in contact, this is visualised below:

![[Pasted image 20231214124243.png]]

Here we are [[neglect is an engineers best freind|neglecting]] the wall separating the two fluids, this can be done by assuming a wall of negligible thickness and high conductivity.

To account for the effect of temp change of fluid with progression, we can construct a model of each wall element:

![[Pasted image 20231214124920.png]]

These are derived from the [[general heat exchanger]] equations (but easy enough to just figure out on the fly):

$$\begin{align*}
d\dot{Q} &= - \dot{m}_{h} c_{p,h} dT_{h} =-C_{h} dT_{h}\\
d\dot{Q} &= - \dot{m}_{c} c_{p,c} dT_{h} =C_{c} dT_{c} \\
d\dot{Q} &= h' dA \: \Delta T
\end{align*}$$

Since $c_{p}$ and $\dot{m}$ are constants, it's convenient to combine them into a single term $C$.

The function for $\Delta T$ is obviously just the different between the hot and cold sides:

$$\begin{align*}
&& d\dot{Q} &=-C_{h} dT_{h} &&\to& - \frac{d\dot{Q}}{C_{h}} &= dT_{h} \\
&&d\dot{Q} &=C_{c} dT_{c} &&\to & \frac{d\dot{Q}}{C_{c}} &= dT_{c} \\
\Delta T &= T_{h} - T_{c} &&\to& d\Delta T &= dT_{h} - dT_{c}  &&\to&d\Delta T &= - \frac{d\dot{Q}}{C_{h}} - \frac{d\dot{Q}}{C_{c}}
\end{align*}$$

Then making use of the other substitution:

$$\begin{align*}
&& d\dot{Q} &= h' dA \: \Delta T\\
d\Delta T &= - \frac{d\dot{Q}}{C_{h}} - \frac{d\dot{Q}}{C_{c}} &&\to&  d\Delta T &= - \left(\frac{1}{C_{h}} + \frac{1}{C_{c}}\right)h' dA \: \Delta T 
 &&\to& \int^{\Delta T_{2}}_{\Delta T_{1}} \frac{1}{ \Delta T} d\Delta T &= - \left(\frac{1}{C_{h}} + \frac{1}{C_{c}}\right)h' \int^{A}_{0} dA 
  &&\to& \ln\frac{\Delta T_{2}}{\Delta T_{1}}  =\ln\frac{T_{h,o}-T_{c,o}}{T_{h,i}-T_{c,i}} &= - \left(\frac{1}{C_{h}}+ \frac{1}{C_{c}}\right)h' A
\end{align*}$$

Here we assumed that $dA$ is constant, so the contact area between the fluids is constant.

This can be changed into a somewhat more convenient form:

$$\begin{align*}
&& \dot{Q} &= C(T_{h,o} - T_{h,i}) \\
&& \dot{Q} &= C(T_{c,i} - T_{c,o}) \\
\ln\frac{\Delta T_{2}}{\Delta T_{1}}  &= - \left(\frac{1}{C_{h}}+ \frac{1}{C_{c}}\right)h' A &&\to&  
\ln\frac{\Delta T_{2}}{\Delta T_{1}}  &= - \left(\frac{T_{h,o} - T_{h,i}}{\dot{Q}}+ \frac{ T_{c,i} - T_{c,o}}{\dot{Q}}\right)h' A  &&\to&  
\dot{Q}\ln\frac{\Delta T_{2}}{\Delta T_{1}}  &= - \left(  \Delta T_{1} - \Delta T_{2}  \right)h' A   &&\to&  
\dot{Q}  &=   \frac{  \Delta T_{1} - \Delta T_{2}   }{\ln\frac{\Delta T_{1}}{\Delta T_{2}}}h' A  
\end{align*}$$

Finally a new identity known as [[parallel-flow heat exchanger|logarithmically weighted temp difference]] is introduced to "simplify" the equation.

$$\begin{align*}
&&  \frac{  \Delta T_{1} - \Delta T_{2}   }{\ln\frac{\Delta T_{1}}{\Delta T_{2}}} &= \Delta T_{lm}\\
\dot{Q}  &=   \frac{  \Delta T_{1} - \Delta T_{2}   }{\ln\frac{\Delta T_{1}}{\Delta T_{2}}}h' A   &&\to& \dot{Q}  &=  \ln (\Delta T_{lm}) h' A
\end{align*}$$

