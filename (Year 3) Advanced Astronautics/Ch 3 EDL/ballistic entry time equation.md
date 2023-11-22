---
aliases: [""]
tags: []
---

## Ballistic entry time equation

You can do a bunch of fancy manipulation which eventually brings in [[Taylor series]], allowing integration to get time for re-entry interms of density.

> ### $$\begin{align*} t  &= - \frac{1}{\alpha V_{0} \sin\gamma_{0}}\left[  \ln\frac{\rho}{\rho_{0}} + \sum\limits_{n=1}^{\infty} \frac{1}{ n! \:n } \left( \frac{\rho-\rho_{0}}{\beta} \right)^{n}  \right] \\ &\approx - \frac{1}{\alpha V_{0} \sin\gamma_{0}}\left[  \ln\frac{\rho}{\rho_{0}} +  \left( \frac{\rho-\rho_{0}}{\beta} \right) +  \frac{1}{ 4 } \left( \frac{\rho-\rho_{0}}{\beta} \right)^{2} + \:...  \right]  \end{align*}$$
>> where: 
>> $V_{0}=$ initial [[non-thrusting entry terms|inertal velocity magnitude]]
>> $\beta=2B \alpha \sin\gamma_{0}$
>> $B=$ [[ballistic coefficient]]
>> $\rho=$ final density from [[atmospheric model for re-entry]]
>> $\rho_{0}=$ initial density
>> $\gamma_{0}=\gamma=$ [[non-thrusting entry terms|flight-path angle]] (constant)
>> $\alpha^{-1}=$ [[atmospheric model for re-entry|scale height constant]]
>> $t=$ re-entry time to reach $\rho$
>
>> assumptions:
>> - The magnitude of weight in the direction of travel is significantly smaller than drag, $W<<D\sin\gamma$ such that it can be neglected
>> - There is zero thrust and lift
>> - The entry angle is constant $\gamma=\gamma_{0}$
>> - The atmosphere can be modelled using this [[atmospheric model for re-entry]]
>> - Vehicle mass is constant

Note that unlike [[ballistic entry velocity equation]] we can't assume that initial re-entry density is zero, initial density is being used to determine starting altitude so approximating it to be zero implies starting at an altitude of infinity!

