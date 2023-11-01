---
aliases: ["absorptance","total radiation absorption","reflectance","transmittance","absorptivity"]
tags: []
---

## Total radiation absorption transmittance and reflectance

### Variation with wavelength

We've already characterised this using the [[radiation incidence behaviour|spectral absorptance]], but as stated there this varies with wavelength (similar charts exist for [[radiation incidence behaviour|spectral transmittance]] and [[radiation incidence behaviour|spectral reflectance]]):

![[Pasted image 20221230144015.png]]

Often when doing maths we will approximate objects as [[black and grey bodies|black bodies]] or [[black and grey bodies|grey bodies]], but in truth the absorption changes with wavelength and absorption characteristics vary greatly between different materials (this is the reason why we can see different [[bazinga|coloured objects]]). 

### Totals

#### Total equations

If only there was a way to get the total of something, when given equations for multiple inputs... [[flashbacks to integration|that would be amazing]]! (integration obviously)

So multiply [[radiation incidence behaviour|spectral transmittance]] by [[radiation incidence behaviour|incident thermal radiation at some wavelength]] and integrate over all wavelengths:

> ### $$\begin{align*} \overline{Q}_{a}  &= \int^{\infty}_{0} q_{i}(\lambda) \: \alpha_{\lambda}(\lambda) \: d\lambda & \overline{Q}_{r}  &= \int^{\infty}_{0} q_{i}(\lambda) \: \rho_{\lambda}(\lambda) \: d\lambda & \overline{Q}_{t}  &= \int^{\infty}_{0} q_{i}(\lambda) \: \tau_{\lambda}(\lambda) \: d\lambda  \\\\ \alpha = \frac{\overline{Q}_{a}}{\overline{Q}_{i}}  &= \dfrac{\int^{\infty}_{0} q_{i}(\lambda) \: \alpha_{\lambda}(\lambda) \: d\lambda}{\int^{\infty}_{0} q_{i}(\lambda) \: d\lambda} & \rho = \frac{\overline{Q}_{r}}{\overline{Q}_{i}}  &= \dfrac{\int^{\infty}_{0} q_{i}(\lambda) \: \rho_{\lambda}(\lambda) \: d\lambda}{\int^{\infty}_{0} q_{i}(\lambda) \: d\lambda}& \tau = \frac{\overline{Q}_{t}}{\overline{Q}_{i}}  &= \dfrac{\int^{\infty}_{0} q_{i}(\lambda) \: \tau_{\lambda}(\lambda) \: d\lambda}{\int^{\infty}_{0} q_{i}(\lambda) \: d\lambda} \end{align*}$$ 
>> where:
>> $\overline{Q}_{a}=$ total radiation absorption for a material ($W/m^{2}$)
>> $\overline{Q}_{r}=$ total radiation reflection for a material ($W/m^{2}$)
>> $\overline{Q}_{t}=$ total radiation transmitted for a material ($W/m^{2}$)
>> $\overline{Q}_{i}=$ total radiation incident
>> $\alpha=$ absorptance
>> $\rho=$ reflectance
>> $\tau=$ transmittance
>> $q_{i}=$ intensity of some wavelength of radiation
>> $\lambda=$ wavelength of incident radiation
>> $\alpha_{\lambda}=$ [[radiation incidence behaviour|spectral absorptance]]
>> $\rho_{\lambda}=$ [[radiation incidence behaviour|spectral reflectance]]
>> $\tau_{\lambda}=$ [[radiation incidence behaviour|spectral transmittance]]
>> 
>> Note that since [[total radiation absorption transmittance and reflectance|absorptance]] is clearly dependent on both the input radiation and the materials absorption of that radiation the [[total radiation absorption transmittance and reflectance|absorptance]] changes depending on radiation source as well as material choice! (this of course applies to transmittance and reflectance too)

#### Solar case

Generally we are using the solar spectrum, in this case [[radiation incidence behaviour|incident thermal radiation]] is given using the symbol $q_{S}$, so for [[total radiation absorption transmittance and reflectance|solar absorptance]]:

> ### $$\begin{align*}  \alpha_{S}  &= \dfrac{\int^{\infty}_{0} q_{S}(\lambda) \: \alpha_{\lambda}(\lambda) \: d\lambda}{\int^{\infty}_{0} q_{S}(\lambda) \: d\lambda} \approx \dfrac{\int^{3}_{0.2} q_{S}(\lambda) \: \alpha_{\lambda}(\lambda) \: d\lambda}{\int^{3}_{0.2} q_{S}(\lambda) \: d\lambda} \end{align*}$$
>> where:
>> $\alpha_{S}=$ solar absorptance
>> $q_{S}(\lambda)=$ [[radiation incidence behaviour|incident thermal radiation]] from the sun
>> $\alpha_{\lambda}=$ [[radiation incidence behaviour|spectral absorptance]]

Obviously solar transmittance and reflectance also exist, with the equations for them being quite obvious.

The equation above approximates the solar absorptance using the wavelength range $0.2\to3$ because about ~$97\%$ of the energy from solar radiation falls within this range:
![[Pasted image 20221230151949.png]]
