---
aliases: ["the 2 entropy equations"]
tags: ["Question","QFormat3"]
---

#### What are and how do you get
## The two [[entropy]] equations
### Final equation
#### [[isobaric expansion or compression|Isobaric]] heating (volume and temp vary)
(extensive form)
> ### $$ S_{12} = mC_v \ln\left(\frac{T_2}{T_1}\right) + mR \ln\left(\frac{V_2}{V_1}\right) $$ 
>> where:
>> $S_{12}=$ [[entropy]] change from $1 \to 2$ 
>> $C_v=$ [[constant volume specific heat]]
>> $R=$ [[individual gas constant|specific gas constant]]
>> $m=$ Mass
>> $T=$ Temperature
>> $V=$ Volume

^40621f


#### [[isochoric heat transfer|isochoric]] heating (temp and pressure vary)

> ### $$ S_{12} = mC_v \ln\left(\frac{T_2}{T_1}\right) - mR \ln\left(\frac{P_2}{P_1}\right) $$ 
>> where:
>> $S_{12}=$ [[entropy]] change from $1 \to 2$ 
>> $C_v=$ [[constant volume specific heat]]
>> $R=$ [[individual gas constant|specific gas constant]]
>> $m=$ Mass
>> $T=$ Temperature
>> $P=$ Pressure

^a33899

### Derivation
#### [[isobaric expansion or compression|Isobaric]] heating

So we know that we transfer a small amount of energy ($dQ$) and allow the volume to change ($dV$) which maintains a constant pressure:
(equations used: [[isobaric expansion or compression#heat Heat transfer|1]], [[ideal gas law#Useful Based forms of the equation|2]],[[entropy#Equation|3]])
$$\begin{align*}
dQ = mC_P \cdot dT &= mC_v \cdot dT + P \cdot dV & PV &= mRT \\
\frac{dQ}{T} &= \frac{mC_v}{T} \cdot dT + \frac{P}{T} \cdot dV & \frac{P}{T} &= \frac{mR}{V}& \frac{dQ}{T} &= dS\\
dS &= mC_V \cdot \frac{dT}{T} + mR \cdot \frac{dV}{V} && \\
\int^{S_2}_{S_1} 1 \cdot dS &= mC_v \left( \int^{T_2}_{T_1} \frac{1}{T} \cdot dT \right) + mR \left( \int^{V_2}_{V_1} \frac{1}{V} \cdot dV\right) \\
\therefore S_{12} &= mC_v \ln\left(\frac{T_2}{T_1}\right) + mR \ln\left(\frac{V_2}{V_1}\right)
\end{align*}$$

As you can see we now have the [[entropy]] defined interms of two [[state variables]].

#### [[isochoric heat transfer|isochoric]] heating
Here we start with the first equation and make use of the [[enthalpy]] relation $E_h = E_u + PV$:
$$\begin{align*}
S_{12} &= mC_v \ln\left(\frac{T_2}{T_1}\right) + mR \ln\left(\frac{V_2}{V_1}\right) & E_h &= E_u + PV\\
&& dE_h &= dE_u + V dP + P dV \\
&& dE_h - V dP &= dE_u + P dV & dE_u &= m C_v dT & dE_h &= m C_p dT\\
&& m C_p dT - V dP &= m C_v dT + P dV
\end{align*}$$

You know what I don't get it, I don't think we need to know the proof. It's [[isochoric heat transfer|isochoric]] or "constant volume" so why the fuck do we have $dV$, $dV=0$ there is no fucking change in volume?! That should just cancel, but we carry it through?!! what! I just don't get this proof.
