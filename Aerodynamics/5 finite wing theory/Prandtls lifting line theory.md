---
aliases: ["induced veloicty for a finite wing","induced AoA for a finite wing","fundamental equation of lifting line theory"]
tags: []
---

## Prandtls lifting line theory

### Model

So we know that a [[single horseshoe vortex]] model is shit, and so need a better one... this is where the multiple horseshoe vortex model comes in. Instead of modelling the wing with a single vortex filiment we model it with many:

![[Pasted image 20221212105011.png]]

Giving us a circulation equation of:
$$ \Gamma( \pm y_{n} ) = \sum\limits^{n}_{k=1} \gamma_{k} \Delta y $$

([[UNFINISHED STUFF]] I really don't understand this part)

This can be re written as:
$$ \gamma_{n} \Delta y = \Gamma( y_{n} ) - \Gamma(y_{n-1}) $$

As the number of filiments approaches infinity it becomes a continous function and so integration comes into play:

![[Pasted image 20221212105720.png]]

$$\begin{align*}
\gamma_{n} \Delta y &=  \Gamma( y_{n} ) - \Gamma(y_{n-1}) & y_{n} &= y_{n-1} + \Delta y\\
&...\\
\gamma(y) &= \frac{\Gamma(y+\Delta y) -\Gamma(y) }{\Delta y}
\end{align*}$$

([[UNFINISHED STUFF]] ^ I don't know what intermediate teps where taken there)

This equation can then be converted into differential form as $\Delta y \to 0$ resulting in:
$$\begin{align*}
\gamma(y) &= \frac{d\Gamma}{dy}
\end{align*}$$

^7ce856

### Induced velocity

#### Useful bit

> ### $$\begin{align*}  w(y_{0})   &= - \frac{1}{4\pi} \int^{\frac{b}{2}}_{- \frac{b}{2}} \frac{ \frac{d\Gamma}{dy}  }{ y_{0} - y} dy \end{align*}$$
>> where:
>> $w=$  induced upwards veloicty along lifting line from [[tip vortecies and downwash|]]
>> $b=$ [[Wing span]]
>> $\frac{d\Gamma}{dy}=$ rate of change of [[circulation]] along lifting line
>> $y_{0}=$ point of intrest on lifting line 
>> $y=$ integration variable for summing circulation along wing

#### Derivation

Now to start to get some useful info (induced downward veloicty) we yeet the equation for [[Helmholtz theorem and Biot-Savart law#^568c65|induced veloicty from a semi-infinite vortex filiment]] and combine it with [[Prandtls lifting line theory#^7ce856|this stuff]]:

$$\begin{align*}
w  & = -\frac{ \Gamma}{4(y_{0} - y)\pi}\\
dw  & = -\frac{ d\Gamma}{4\pi(y_{0} - y)} & \gamma(y) &= \frac{d\Gamma}{dy}\\
   & = -\frac{ \gamma dy }{4\pi(y_{0} - y)}\\
   & = -\frac{ \frac{d\Gamma}{dy}  }{4\pi(y_{0} - y)} dy \\
w(y_{0})   &= - \frac{1}{4\pi} \int^{\frac{b}{2}}_{- \frac{b}{2}} \frac{ \frac{d\Gamma}{dy}  }{ y_{0} - y} dy
\end{align*}$$

![[Pasted image 20221212115407.png]]

 ### Induced AoA

#### Useful bit
> ### $$\begin{align*}  \alpha_{i}  &= - \frac{w}{V_{\infty}} =   \frac{1}{4\pi V_{\infty}} \int^{\frac{b}{2}}_{- \frac{b}{2}} \frac{ \frac{d\Gamma}{dy}  }{ y_{0} - y} dy \end{align*}$$
>> where:
>> $w=$  induced upwards veloicty along lifting line from [[tip vortecies and downwash|]]
>> $\alpha_{i}=$ [[effective AoA on finite wings|induced AoA]]
>> $V_{\infty}=$ free stream veloicty

#### Derivation

![[Pasted image 20221212113701.png]]

If we apply a small angle approximation we can get the induced angle of attack quite easily:
$$\begin{align*}
\alpha_{i} &= - \frac{w}{V_{\infty}}
\end{align*}$$

Then sub in the equation for induced velocity:

$$\begin{align*}
\alpha_{i}  &=   \frac{1}{4\pi V_{\infty}} \int^{\frac{b}{2}}_{- \frac{b}{2}} \frac{ \frac{d\Gamma}{dy}  }{ y_{0} - y} dy
\end{align*}$$

### Fundamental equation of lifting line theory
#### Useful bit

> ### $$\begin{align*} \frac{2\Gamma(y_{0})}{a_{0} V_{\infty} c(y_{0})} + \frac{1}{4\pi V_{\infty}} \int^{\frac{b}{2}}_{- \frac{b}{2}} \frac{ \frac{d\Gamma}{dy}  }{ y_{0} - y} dy &= \alpha(y_{0}) - \alpha_{L=0}(y_{0}) \end{align*}$$
>> where:
>> $w=$  induced upwards veloicty along lifting line from [[tip vortecies and downwash|]]
>> $b=$ [[Wing span]]
>> $\frac{d\Gamma}{dy}=$ rate of change of [[circulation]] along lifting line
>> $y_{0}=$ point of intrest on lifting line 
>> $y=$ integration variable for summing circulation along wing 
>> $\alpha_{i}=$ [[effective AoA on finite wings|induced AoA]]
>> $V_{\infty}=$ free stream veloicty
>> $\Gamma=$ [[circulation]] at some point
>> $\alpha_{L=0}=$ [[no lift angle]]
>> $a_{0}=$ gradient of $C_{l}/\alpha$ graph usually $\approx 2\pi$
>> $c=$ [[chord (aeronautics)|chord]] length


#### Derivation
Combining info from [[effective AoA on finite wings]] and [[Thin airfoil theory Overview|thin airfoils]] we know that:
$$\begin{align*}
\alpha_{eff}&= \alpha - \alpha_{i} & C_{l} &= a_{0}(\alpha_{eff} - \alpha_{L=0})
\end{align*}$$
$$\begin{align*}
C_{l} &= a_{0}(\alpha - \alpha_{i} - \alpha_{L=0})
\end{align*}$$
Subbing in the equation for induced AoA from above along with [[Kutta-Joukowski Theorem]]:

$$\begin{align*}
 C_{l} &= a_{0}(\alpha - \alpha_{i} - \alpha_{L=0})& C_{l} &=  \frac{\Gamma}{\frac{1}{2}V_{\infty} c} & \alpha_{i}  &=   \frac{1}{4\pi V_{\infty}} \int^{\frac{b}{2}}_{- \frac{b}{2}} \frac{ \frac{d\Gamma}{dy}  }{ y_{0} - y} dy\\
\end{align*}$$
$$\begin{align*}
\frac{\Gamma}{\frac{1}{2}V_{\infty} c} &= a_{0}\left(\alpha - \frac{1}{4\pi V_{\infty}} \int^{\frac{b}{2}}_{- \frac{b}{2}} \frac{ \frac{d\Gamma}{dy}  }{ y_{0} - y} dy - \alpha_{L=0}\right)\\
&...\\
 \frac{2\Gamma(y_{0})}{a_{0} V_{\infty} c(y_{0})} + \frac{1}{4\pi V_{\infty}} \int^{\frac{b}{2}}_{- \frac{b}{2}} \frac{ \frac{d\Gamma}{dy}  }{ y_{0} - y} dy &= \alpha(y_{0}) - \alpha_{L=0}(y_{0})
\end{align*}$$

This equation is known as the fundamental equation of lifting line theory, the reason pretty much everything is a function of $y_{0}$ is because well the shape of the foil can change along a wing. ([[woooooo suffering|this is going to give fun maths]])


