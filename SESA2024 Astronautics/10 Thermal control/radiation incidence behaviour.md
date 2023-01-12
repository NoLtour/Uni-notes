---
aliases: ["incident thermal radiation","thermal radiation absorbed","thermal radiation reflected","thermal radiation transmitted","spectral absorptance","spectral reflectance","spectral transmittance"]
tags: []
---


## Radiation incidence behaviour

### Incident behaviour

So when radiation hits a surface a combination of 3 things will happen:
- It will be reflected off the surface
- It will be absorbed by the surface
- It will be transmitted through the surface

The incident radiation will be equal to the total of these things:

> ### $$\begin{align*} q_{i}(\lambda) &= q_{a}(\lambda) + q_{r}(\lambda) + q_{t}(\lambda)  \end{align*}$$
>> where:
>> ![[Pasted image 20221230142025.png]]
>> $q_{i}(\lambda)=$ incident radiation impacting the surface
>> $q_{a}(\lambda)=$ radiation absorbed by the surface
>> $q_{r}(\lambda)=$ radiation reflected off the surface
>> $q_{t}(\lambda)=$ radiation transmitted through the surface
>> 
>> All given as some function of wavelength ($\lambda$), since depending on wavelength all these values can change.

^644450

### Measures of material characteristics

The equation from [[radiation incidence behaviour#^644450|here]] can be described by:
- [[radiation incidence behaviour|spectral absorptance]]
- [[radiation incidence behaviour|spectral reflectance]]
- [[radiation incidence behaviour|spectral transmittance]]

For any material. Since they are ratio's of their fraction of the outcome for the incident radiation it's clear they will sum to 1.

> ### $$\begin{align*} 1 &=  \alpha_{\lambda} + \rho_{\lambda} +  \tau_{\lambda} \end{align*}$$
>> where:
>> $\alpha_{\lambda}=$ [[radiation incidence behaviour|spectral absorptance]] 
>> $\rho_{\lambda}=$ [[radiation incidence behaviour|spectral reflectance]]  
>> $\tau_{\lambda}=$ [[radiation incidence behaviour|spectral transmittance]] 

For spacecraft [[radiation incidence behaviour|spectral transmittance]] is typically really low since we choose opaque materials, so the above can often approximate to:
$$\begin{align*}
1 &\approx \alpha_{\lambda} + \rho_{\lambda}
\end{align*}$$



#### Spectral absorptance

Ratio of radiation absorbed compared to incident radiation.

> ### $$\begin{align*} \alpha_{\lambda}  &\equiv \frac{q_{a}(\lambda)}{q_{i}(\lambda)}  \end{align*}$$
>> where:
>> $\alpha_{\lambda}=$ [[radiation incidence behaviour|spectral absorptance]] (absorption ratio at a specific wavelength)
>> $q_{i}(\lambda)=$ incident radiation impacting the surface
>> $q_{a}(\lambda)=$ radiation absorbed by the surface


#### Spectral reflectance

Ratio of radiation reflected compared to incident radiation.

> ### $$\begin{align*} \rho_{\lambda}  &\equiv \frac{q_{r}(\lambda)}{q_{i}(\lambda)}  \end{align*}$$
>> where:
>> $\rho_{\lambda}=$ [[radiation incidence behaviour|spectral reflectance]] (reflectance ratio at a specific wavelength)
>> $q_{i}(\lambda)=$ incident radiation impacting the surface
>> $q_{r}(\lambda)=$ radiation reflected off the surface


#### Spectral transmittance

Ratio of radiation absorbed compared to incident radiation.

> ### $$\begin{align*} \tau_{\lambda}  &\equiv \frac{q_{t}(\lambda)}{q_{i}(\lambda)}  \end{align*}$$
>> where:
>> $\tau_{\lambda}=$ [[radiation incidence behaviour|spectral transmittance]] (transmittance ratio at a specific wavelength)
>> $q_{i}(\lambda)=$ incident radiation impacting the surface
>> $q_{t}(\lambda)=$ radiation transmitted through the surface


