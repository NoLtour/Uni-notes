---
aliases:
  - number of transfer units
tags:
---

## Number of transfer units method

### Equation

Not going to do the proof since it doesn't seem necessary:


> ### $$\begin{align*} \text{Parallel flow:}&& \varepsilon &= \frac{1- \exp({-\text{NTU}[1+C_{r}]})}{1+C_{r}} \\\\ \text{Counter flow:}&& \varepsilon &= \left\{ \begin{aligned} &\frac{1- \exp(-\text{NTU}[1-C_{r}])}{1- C_{r}\exp(-\text{NTU}[1-C_{r}])},&C_{r}&\neq C_{h} \\&\frac{\text{NTU}}{1+\text{NTU}},&C_{r}&= C_{h} \end{aligned} \right. \end{align*}$$

> ### $$\begin{align*} \frac{\dot{Q}}{\dot{Q}_{max}}  &= \varepsilon &&& \dot{Q}_{max} &= C_{min}(T_{h,i} - T_{c,i})  \end{align*}$$
> ### $$\begin{align*} C_{min} &= \min(C_{h} , C_{c}) &&& C_{max} &= \max(C_{h} , C_{c}) &&&  C_{r} &= \frac{C_{min}}{C_{max}} &&& \text{NTU} &= \frac{h' A}{C_{min}} \end{align*}$$
>> where:
>> $\text{NTU}=$number of transfer units 
>> $C_{h},C_{c}=$ the $c_{p} \dot{m}$ for the hot and cold flows
>> $\dot{Q}_{max}=$ the highest possible heat transfer ($A=\infty$)
>> $\dot{Q}=$ heat transfer 
>> $h'=$ [[general heat exchanger|total convection coefficient]]
>> $A=$ fluid contact area
>> $T=$ temp
>> $C=\dot{m}c_{p}=$ flowing [[constant pressure specific heat|constant pressure heat capacity]]
>> $\varepsilon=$ effectiveness of heat exchanger

This is a set of equations that can be used to determine the output temperatures given the input temperatures and exchange area

### Example

From the following determine the exit temperatures, given $A=10.06\:m^{2}$:

![[Pasted image 20231214202930.png]]

Firstly we identify the min, max and find all the constants

$$\begin{align*}
C_{min} &= C_{c} &&& C_{max} &= C_{h} &&& C_{r} &= \frac{C_{min}}{C_{max}} =0.5 &&& \text{NTU} &= \frac{h' A}{C_{min}}=1.09294  &&& h' &= \frac{1}{\frac{1}{h_{h}} + \frac{1}{h_{c}}} =162.963
\end{align*}$$

Then effectiveness can be evaluated:

$$\begin{align*}
\varepsilon &= \frac{1- \exp(-\text{NTU}[1-C_{r}])}{1- C_{r}\exp(-\text{NTU}[1-C_{r}])} =0.59255
\end{align*}$$

From this it's easy to evaluate the heat transfer:

$$\begin{align*}
\dot{Q} &= \varepsilon \dot{Q}_{max} =\varepsilon C_{min}( T_{h,in} - T_{c,in} )=120000
\end{align*}$$

Then it's trivial to determine temperatures from the [[general heat exchanger]] equations!
