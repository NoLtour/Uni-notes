---
aliases: [ "elliptic lift distrobution characteristics"]
tags: []
---

## Elliptic lift distrobution analysis

### Results

For an elliptic lift distrobution you get very nice results, since induced velocity is constant along the wing everything else comes out quite clean:

> ### $$\begin{align*} \text{Induced velocity:}& & w(y_{0})  &= - \frac{\Gamma_{0}}{2b} \\\\ \text{Induced AoA:}& & \alpha_{i} &= \frac{C_{L}}{\pi A }=  \frac{\Gamma_{0}}{2 b V_{\infty}}\\\\  \text{Lift coefficient:}& & C_{L}&= \frac{\pi b\Gamma_{0}}{2V_{\infty}S} \\\\ \text{Induced drag coefficient:}& & C_{Di}&= \frac{C_{L}^{2}}{\pi A } \\  \end{align*}$$
>> where:
>> $w(y_{0})=$ [[Prandtls lifting line theory|induced veloicty for a finite wing]] as a function of position along span (constant for elliptic)
>> $\Gamma_{0}=$ a constant describing max [[circulation]] along span
>> $b=$ [[Wing span]]
>> $\alpha_{i}=$ [[Prandtls lifting line theory|induced AoA for a finite wing]]
>> $C_{L}=$ lift coefficient
>> $C_{Di}=$ [[induced drag coefficient]]
>> $S=$ [[Wing plan area]]
>> $A=$ [[wing aspect ratio]]
>> $b=$ [[Wing span]]

^cbb7e1



### Derivation

#### Induced velocity along the span

We are going to do some analysis to get the characteristics of an elliptic wing so consider a wing where the circulation is:
$$\begin{align*}
\Gamma &= \Gamma_{0} \sqrt{ 1- \left(\frac{2y}{b}\right)^{2} }
\end{align*}$$

![[Pasted image 20221213140338.png]]

So we can use this in the equations we've derived previously we'll need the derivative form:

$$\begin{align*}
\Gamma &= \Gamma_{0} \sqrt{ 1- \left(\frac{2y}{b}\right)^{2} } & \to& & \frac{d\Gamma}{dy} &= - \frac{2\Gamma_{0}}{b} \frac{\frac{2y}{b}}{\sqrt{1- \left(\frac{2y}{b}\right)^{2}}} 
\end{align*}$$



Then we'll use the [[Prandtls lifting line theory|induced veloicty for a finite wing equation]]:

$$\begin{align*}
w(y_{0})   &= - \frac{1}{4\pi} \int^{\frac{b}{2}}_{- \frac{b}{2}} \frac{ \frac{d\Gamma}{dy}  }{ y_{0} - y} dy\\
  &= - \frac{1}{4\pi} \int^{\frac{b}{2}}_{- \frac{b}{2}} \frac{  - \frac{2\Gamma_{0}}{b} \frac{\frac{2y}{b}}{\sqrt{1- \left(\frac{2y}{b}\right)^{2}}}   }{ y_{0} - y} dy\\
&...\\
w(y_{0}) &= \frac{\Gamma_{0}}{2\pi b} \int^{\frac{b}{2}}_{-\frac{b}{2}} \frac{\frac{2y}{b}}{(y_{0}-y)\sqrt{1-\left(\frac{2y}{b}\right)^{2}}} dy
\end{align*}$$

This is a pain in the ass to integrate normally, so we do the same as in thin foils stuff and convert this into the angular domain:

$$\begin{align*}
y &= - \frac{b}{2} \cos\theta & &\to & dy &= \frac{b}{2} \sin\theta \: d\theta\\
\frac{2y}{b} &= -\cos\theta  \\
\left(\frac{2y}{b}\right)^{2} &= \cos^{2}\theta\\
\sqrt{ 1- \left(\frac{2y}{b}\right)^{2} } &= \sin\theta\\
\end{align*}$$

These identities will be useful for later, we also need to get the new limits:

$$\begin{align*}
y_{1} &= \frac{b}{2} & &\to & \theta_{1} &= \pi \\
y_{2} &= - \frac{b}{2} & &\to & \theta_{2} &= 0 
\end{align*}$$

Also we need to convert the $y_{0}$ into angular form:

$$\begin{align*}
y_{0} &= - \frac{b}{2} \cos\theta_{0}
\end{align*}$$

Now subbing all this into the equation for induced velocity:

$$\begin{align*}
w(y_{0}) &= \frac{\Gamma_{0}}{2\pi b} \int^{\frac{b}{2}}_{-\frac{b}{2}} \frac{\frac{2y}{b}}{(y_{0}-y)\sqrt{1-\left(\frac{2y}{b}\right)^{2}}} dy & &\to & 
w(\theta_{0}) &= \frac{\Gamma_{0}}{2\pi b} \int^{\pi}_{0} \frac{-\cos\theta }{\left(- \frac{b}{2} \cos\theta_{0}-- \frac{b}{2} \cos\theta\right)\sin\theta} \frac{b}{2} \sin\theta \: d\theta \\
&& && &...\\
&& && w(\theta_{0}) &= - \frac{\Gamma_{0}}{2\pi b} \int^{\pi}_{0} \frac{\cos\theta}{\cos\theta - \cos\theta_{0}} d\theta
\end{align*}$$

Applying Glauert integral formula:

$$\begin{align*}
\int^{\pi}_{0} \frac{\cos n\theta}{\cos\theta - \cos\theta_{0}} d\theta &=  \pi \frac{\sin n\theta_{0}}{\sin \theta_{0}}
\end{align*}$$

$$\begin{align*}
w(\theta_{0}) &= - \frac{\Gamma_{0}}{2\pi b} \int^{\pi}_{0} \frac{\cos\theta}{\cos\theta - \cos\theta_{0}} d\theta & &\to & w &= - \frac{\Gamma_{0}}{2\pi b} \pi \frac{\sin\theta_{0}}{\sin\theta_{0}}\\
&& &&    &= - \frac{\Gamma_{0}}{2b}
\end{align*}$$

Hence for an eliptic lift distorbution the induced velocity is constant over the span! ([[these take so looooooooooooooong to write|pog]])

#### Induced AoA and lift coefficient

Now we can find [[Prandtls lifting line theory|induced AoA for a finite wing]], which is quite simple since $w$ is cosntant:

$$\begin{align*}
\alpha_{i}  &= - \frac{w}{V_{\infty}} & & \to & \alpha_{i}  &=  \frac{\Gamma_{0}}{2 b V_{\infty}}
\end{align*}$$

Then finding lift coefficient is also not that hard use [[lift and induced drag coefficients for a finite wing]]:

$$\begin{align*}
C_{L} &= \frac{2}{ V_{\infty}  S} \int^{\frac{b}{2}}_{- \frac{b}{2}} \Gamma \: dy_{0} & \Gamma &= \Gamma_{0} \sqrt{ 1- \left(\frac{2y}{b}\right)^{2} }\\
 &= \frac{2 \Gamma_{0}}{ V_{\infty}  S} \int^{\frac{b}{2}}_{- \frac{b}{2}}  \sqrt{ 1- \left(\frac{2y_{0}}{b}\right)^{2} } \: dy_{0}\\
&...\\
C_{L}&= \frac{\pi b\Gamma_{0}}{2V_{\infty}S}
\end{align*}$$

It is useful to express $\alpha_{i}$ interms of $C_L$ so let's do that quickly:

$$\begin{align*}
\alpha_{i}  &=  \frac{\Gamma_{0}}{2 b V_{\infty}} & &\to & \alpha_{i} &=  \frac{SC_{L}}{\pi b^{2}}\\
&& && &= \frac{C_{L}}{\pi A }
\end{align*}$$

(Here $A$ is [[Wing plan area|Aspect ratio from this relation]])

#### Induced drag

Taking the equation from [[lift and induced drag coefficients for a finite wing]]:

$$\begin{align*}
C_{Di} &= \frac{2}{V_{\infty} S} \int^{\frac{b}{2}}_{- \frac{b}{2}} \Gamma(y_{0}) \alpha_i(y_{0}) \: dy_{0}\\
  &= \frac{2 \Gamma_{0}}{V_{\infty} S}\frac{C_{L}}{\pi A } \int^{\frac{b}{2}}_{- \frac{b}{2}} \sqrt{ 1- \left(\frac{2y_{0}}{b}\right)^{2} }  \: dy_{0}\\
  &... \\
C_{Di} &= \frac{2 \Gamma_{0}}{V_{\infty} S}\frac{C_{L}}{\pi A } \frac{b\pi}{4} & C_{L}&= \frac{\pi b\Gamma_{0}}{2V_{\infty}S}\\
&= \frac{C_{L}}{\pi A } \frac{b\pi\Gamma_{0}}{2V_{\infty} S}\\
&= \frac{C_{L}^{2}}{\pi A }
\end{align*}$$

This is an important result, since it shows that increasing the lift coefficient will have a squared effect on the induced drag so to minimise the effect of drag it's best to either decrease $C_{L}$ or increase the aspect ratio of the wing.


