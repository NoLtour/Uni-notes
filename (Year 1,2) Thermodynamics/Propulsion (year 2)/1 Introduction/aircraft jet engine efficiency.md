---
aliases: ["propulsive efficiency","thermal efficiency"]
tags: []
---

## Aircraft jet engine efficiency

### Intro

Ok so we can define overall efficiency as the propulsive efficiency (a measure of how well an engine can convert the kinetic energy into displacement work) of the engine multiplied by the thermal efficiency (how well an engine can convert heat into kinetic energy) of the engine:

$$\begin{align*}
\eta_{O} &= \eta_{P} \times \eta_{th}
\end{align*}$$

This doesn't really tell us much though, so lets get some equations for propulsive and thermal efficiency!

### Propulsive efficiency

So this is how efficient we use our KE, so it's just the power of the engine divided by the total KE imparted into the environment by the engine:

$$\begin{align*}
\eta_{P} &= \frac{\dot{W}_{aircraft}}{\dot{W}_{jet}}
\end{align*}$$

The equation for engine power is easy enough, just simple thrust multiplied by velocity of the vehicle. We know the velocity of the vehicle is just $V_{\infty}$ and thrust is [[momentum conservation applied to a jet engine|thrust of a jet engine]] so combining this: 
$$\begin{align*}
\dot{W}_{aircraft} &= V_{\infty} \times F & F  &= \dot{m}_{a}[(1+f) V_{jet} - V_{\infty}] + A_{j}(P_{j}-P_{a})\\
&= V_{\infty} \dot{m}_{a}[(1+f) V_{jet} - V_{\infty}] + V_{\infty} A_{j} (P_{j}-P_{a}) 
\end{align*}$$ 
^e77207

Now the KE used in the air through the engine is simple enough to find, just KE of air out minus KE of air in:

$$\begin{align*}
KE_{in} &= \frac{1}{2} V_{\infty}^{2} \dot{m}_{a} & KE_{exit} &= \frac{1}{2} V_{jet}^{2} \dot{m}_{a}(1+f)
\end{align*}$$
$$\begin{align*}
\dot{W}_{jet} &= KE_{exit} - KE_{in}\\
&=  \frac{1}{2} V_{jet}^{2} \dot{m}_{a}(1+f) - \frac{1}{2} V_{\infty}^{2} \dot{m}_{a}\\
&= \frac{1}{2} \dot{m}_{a} [ (1+f) V_{jet}^{2} - V_{\infty}^{2} ]
\end{align*}$$



Now we can sub back to get propulsive efficiency:

$$\begin{align*}
\eta_{P} &= \frac{\dot{W}_{aircraft}}{\dot{W}_{jet}} & \to& & \eta_{P} &= \frac{V_{\infty} \dot{m}_{a}[(1+f) V_{jet} - V_{\infty}] + V_{\infty} A_{j} (P_{j}-P_{a}) }{\frac{1}{2} \dot{m}_{a} [ (1+f) V_{jet}^{2} - V_{\infty}^{2} ]} 
\end{align*}$$

Now that looks disgusting, and it is ([[math vomit is great|yay]])! So we take the ever present engineering approach of "what can I cut out to make my life easyer?" and the answer is 2 things: ^30f127
- We know that for a not shit jet engine the amount of fuel relative to the amount of air is tiny, so $f<<1$ and hence $f+1\approx1$
- Secondly for a non shit engine (which is the most common when dealing with civil jets) the exhaust is basically fully expanded so $P_{j}\approx P_{a}$ hence $P_{j}-P_{a}\approx0$

Subbing this into our math vomit produces:
$$\begin{align*}
\eta_{P} &= \frac{V_{\infty} \dot{m}_{a}[ 1 V_{jet} - V_{\infty}] + V_{\infty} A_{j} (0) }{\frac{1}{2} \dot{m}_{a} [1 V_{jet}^{2} - V_{\infty}^{2} ]}\\
&=  \frac{V_{\infty} [ V_{jet} - V_{\infty}]  }{\frac{1}{2} [ V_{jet}^{2} - V_{\infty}^{2} ]}\\
&... \text{rearanging magic}\\
\eta_{P} &= \frac{2}{\frac{V_{j}}{V_{\infty}} + 1}
\end{align*}$$



> ### $$\begin{align*}  \eta_{P} &= \frac{2}{\frac{V_{j}}{V_{\infty}} + 1}\end{align*}$$
>> where:
>> $\eta_{P}=$  [[aircraft jet engine efficiency|propulsive efficiency]]
>> $V_{\infty}=$ vehicle velocity
>> $V_{jet}=$ exhaust velocity 


That is so much cleaner... we can also use the principles above to clean up our jet thrust equation:

$$\begin{align*}
F  &= \dot{m}_{a}[(1+f) V_{jet} - V_{\infty}] + A_{j}(P_{j}-P_{a}) & \to && F  &= \dot{m}_{a}[ V_{jet} - V_{\infty}]  
\end{align*}$$
From which it becomes obvious that for positive thrust to exist $V_{jet}>V_{\infty}$, which makes intuitive sense. This means that the equation for propulsive efficiency is essentially stating that the closer $V_{j}$ is to $V_\infty$ the more (propulsively) efficient our engine:
![[Pasted image 20230207160904.png]]

Of course if we think about it the closer $V_j$ is to $V_{\infty}$ the lower our thrust ($F  = \dot{m}_{a}[ V_{jet} - V_{\infty}]$)   and here is a real shocker we need thrust to fly. So there is a limit to dropping this. If only there was some way to increase thrust without reducing propulsive efficiency ($\dot{m}_{a}$)... air flow rate exists, ever wonder why jet engines keep getting bigger and increasing air bypass ratio? Well this is why.

Course there are limitations in increasing engine size, mainly mass and it needs to fit under the wing in landing!

### Overall efficiency

K this one's pretty [[yes I am using stupid internet slang in my notes fuck you|ez]], it's just power of the engine divided by total heat in. We already know the aircrafts engine power from [[aircraft jet engine efficiency#^e77207]] then heat in is just burning fuel:

$$\begin{align*}
\eta_{O} &= \frac{\dot{W}_{aircraft}}{\dot{Q}_{in}}
\end{align*}$$

The fuel part needs some variable defining fuel consumption... let's just use LCV (lower calorific value, the heat released per mass of some fuel) multiplied by fuel mass flow rate $\dot{m}_{f}$ so $\dot{Q}_{in} = \text{LCV} \dot{m}_{f}$ subbing this in and the equation for [[aircraft jet engine efficiency#^e77207|engine power]] :

$$\begin{align*}
\eta_{O} &= \frac{\dot{W}_{aircraft}}{\dot{Q}_{in}} & \to& & \eta_{O} &= \frac{V_{\infty} \dot{m}_{a}[(1+f) V_{jet} - V_{\infty}] + V_{\infty} A_{j} (P_{j}-P_{a}) }{\text{LCV} \dot{m}_{f}}
\end{align*}$$

Recall [[aircraft jet engine efficiency#^30f127|those convenient assumptions]] we used to clean up the  equation before... well lets use em again so:

$$\begin{align*}
\eta_{O} &= \frac{V_{\infty} \dot{m}_{a}[(1+f) V_{jet} - V_{\infty}] + V_{\infty} A_{j} (P_{j}-P_{a}) }{\text{LCV} \dot{m}_{f}} & \to& & \eta_{O} &= \frac{V_{\infty} \dot{m}_{a}[ V_{jet} - V_{\infty}]  }{\text{LCV} \dot{m}_{f}}\\
&&&&&= \frac{V_{\infty}  [ V_{jet} - V_{\infty}]  }{\text{LCV} f}
\end{align*}$$

Alternatively using specific thrust fuel consumption:

$$\begin{align*}
\eta_{O} &= \frac{F}{\dot{m}_{f}} \frac{V_{\infty}}{\text{LCV}} = \frac{1}{\text{TSFC}} \frac{V}{\text{LCV}}
\end{align*}$$

> ### $$\begin{align*}  \eta_{O} &=  \frac{V_{\infty}  [ V_{jet} - V_{\infty}]  }{\text{LCV} f} \end{align*}$$
> ### $$\begin{align*}  \eta_{O} &=  \frac{1}{\text{TSFC}} \frac{V_{\infty}}{\text{LCV}} \end{align*}$$
>> where:
>> $\eta_{O}=$  overall jet efficiency
>> $V_{\infty}=$ vehicle velocity
>> $V_{jet}=$ exhaust velocity
>> $f=$ [[momentum conservation applied to a jet engine|fuel to air ratio]]
>> $\text{TSFC}=$ [[thrust specific fuel consumption]]
>> $\text{LCV}=$ fuel lower calorific value

### Thermal efficiency

Well we could sub into:
$$\begin{align*}
\eta_{O} &= \eta_{P} \times \eta_{th}
\end{align*}$$
Then rearrange to get it, but it can also be deriveed quite easily using the fact that thermal efficiency is just the kinetic energy imparted on air by the jet divided by heat in:

$$\begin{align*}
\eta_{th} &= \frac{\dot{W}_{jet}}{\dot{Q}_{in}}
\end{align*}$$
We know from all the shite above the equations for $\dot{W}_{jet}$ and $\dot{Q}_{in}$ already so just subbing that in and rearranging:

$$\begin{align*}
\eta_{th} &= \frac{\dot{W}_{jet}}{\dot{Q}_{in}} & \to& & (math+effort) & &\to && \eta_{th}&= \frac{1}{2} \frac{V_{j}^{2} - V^{2}}{f \times \text{LCV}}
\end{align*}$$

This result can be verified using $\eta_{O} = \eta_{P} \times \eta_{th}$ but [[the notes also cba on this so get fucked lol|I cba]]. 

> ### $$\begin{align*}     \eta_{th}&= \frac{1}{2} \frac{V_{j}^{2} - V^{2}}{f \times \text{LCV}} \end{align*}$$
>> where:
>> $\eta_{th}=$  jet thermal efficiency
>> $V_{\infty}=$ vehicle velocity
>> $V_{jet}=$ exhaust velocity
>> $f=$ [[momentum conservation applied to a jet engine|fuel to air ratio]] 
>> $\text{LCV}=$ fuel lower calorific value

The reason for splitting up the overall efficiency in the thermal and propulsive part is so that we can more easily see how to optimize each component. We already observed that the propulsive efficiency can be improved by reducing the difference between the jet speed and aircraft speed, and consequently the need for large air mass flow rates. For the thermal efficiency, we can use our knowledge of [[Brayton cycle]]s from part 1 thermofluids. We will go into more detail later in the module, but for an ideal Brayton cycle the thermal efficiency will increase with the overall pressure ratio, which is directly related to the temperature ratio.

Increasing pressure ratio and engine temp is a trend that can be clearly seen in industry:
![[Pasted image 20230207164122.png]]

As you'd expect!
