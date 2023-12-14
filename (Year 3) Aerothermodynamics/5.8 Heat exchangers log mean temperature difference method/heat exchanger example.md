---
aliases: [""]
tags: []
---

## Heat exchanger example

This is a counter flow heat exchanger.

![[Pasted image 20231214140334.png]]

The simplest method is first finding the heat transfer:

$$\begin{align*}
\dot{Q} &= C_{h} (T_{h,o} - T_{h,i} ) =120000\:W
\end{align*}$$

Then the simply do the other side of the balance:

$$\begin{align*}
\dot{Q} &= C_{c} (T_{c,i} - T_{c,o} ) &&\to&
T_{c,i}-\frac{\dot{Q}}{C_{c}} &=   T_{c,o} =95\degree C

\end{align*}$$

Find $h'$ (from [[general heat exchanger]]) in preparation for later:

$$\begin{align*}
\frac{1}{h'} &= \frac{1}{h_{h}} + \frac{1}{h_{c}} &&\to& h' &= \frac{1}{\frac{1}{h_{h}} + \frac{1}{h_{c}}}=162.96\:Wm^{-2}K^{-1}
\end{align*}$$

Then from [[counter-flow heat exchanger]]:

$$\begin{align*}
\Delta T_{1} &= T_{h,i} - T_{c,o} = 55K\\
  \Delta T_{2} &= T_{h,o} - T_{c,i}=95K
\end{align*}$$

Subbing in:

$$\begin{align*}
&& \frac{  \Delta T_{1} - \Delta T_{2}   }{\ln\frac{\Delta T_{1}}{\Delta T_{2}}} &= \Delta T_{lm} \\
\dot{Q}  &=  \ln (\Delta T_{lm}) h' A &&\to& \frac{\dot{Q}}{\ln \frac{  \Delta T_{1} - \Delta T_{2}   }{\ln\frac{\Delta T_{1}}{\Delta T_{2}}} h'}  &=   A=10.06\:m^{2}
\end{align*}$$
