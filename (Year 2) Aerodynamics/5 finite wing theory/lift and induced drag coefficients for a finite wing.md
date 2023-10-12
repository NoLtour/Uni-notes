---
aliases: [""]
tags: []
---

## Lift and induced drag coefficients for a finite wing

### Lift

> ### $$\begin{align*}   C_{L} &= \frac{2}{ V_{\infty}  S} \int^{\frac{b}{2}}_{- \frac{b}{2}} \Gamma \: dy_{0}\end{align*}$$
>> where:
>> $C_{L}=$ lift coefficient
>> $V_{\infty}=$ freestream velocity
>> $b=$ wing span
>> $\Gamma=$ [[circulation]] 
>> $y_{0}=$ position along wing for integration
>> $S=$ [[Wing plan area]]

#### Derivation
Quite simple just take the lift of a cross section from [[Kutta-Joukowski Theorem]] and integrate over the span:
$$\begin{align*}
L &= \int^{\frac{b}{2}}_{- \frac{b}{2}} L'(y_{0}) \: dy_{0} & L' &=  \rho V_{\infty} \Gamma\\
&= \int^{\frac{b}{2}}_{- \frac{b}{2}} \rho V_{\infty} \Gamma \: dy_{0}\\
C_{L} &= \frac{1}{\frac{1}{2}\rho V_{\infty}^{2} S} \int^{\frac{b}{2}}_{- \frac{b}{2}} \rho V_{\infty} \Gamma \: dy_{0}\\
 &= \frac{2}{ V_{\infty}  S} \int^{\frac{b}{2}}_{- \frac{b}{2}} \Gamma \: dy_{0}
\end{align*}$$

### Induced drag

> ### $$\begin{align*}   C_{Di} &= \frac{2}{V_{\infty} S} \int^{\frac{b}{2}}_{- \frac{b}{2}} \Gamma(y_{0}) \alpha_i(y_{0}) \: dy_{0}  \end{align*}$$
>> where:
>> $C_{Di}=$  [[induced drag coefficient]]
>> $V_{\infty}=$ freestream velocity
>> $b=$ wing span
>> $\Gamma=$ [[circulation]]
>> $\alpha_{i}=$ [[Prandtls lifting line theory|induced AoA for a finite wing]]
>> $y_{0}=$ position along wing for integration
>> $S=$ [[Wing plan area]]


#### Derivation
The derivation for [[effective AoA on finite wings|induced drag]] coefficient is identical to the lift one:

$$\begin{align*}
D_{i} &= \int^{\frac{b}{2}}_{- \frac{b}{2}} D_{i}'(y_{0}) \: dy_{0} & D_{i}' &=  L \alpha_{i}\\
D_{i} &= \int^{\frac{b}{2}}_{- \frac{b}{2}} L \alpha_i \: dy_{0}\\
&...\\
C_{Di} &= \frac{2}{V_{\infty} S} \int^{\frac{b}{2}}_{- \frac{b}{2}} \Gamma(y_{0}) \alpha_i(y_{0}) \: dy_{0}

\end{align*}$$
