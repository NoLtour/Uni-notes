---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What's the method for
## Buckingham $\pi$ dimensional analysis
### Getting p,n and k
#### Method
This is a method for dimensional analysis, the theorum states that if there is a physically meaningful equation involving $n$ number of physical variables, then the origional equation can be rewritten in terms of a set of $p=n-k$ dimensionless parameters ($\pi_1,\pi_2,...\pi_p$) constructed from the origional variables:

> $$ p = n-k $$ 
>> where:
>> $p=$ number of dimensionless parameters ($\pi_1,\pi_2,...\pi_p$)
>> $n=$ number of physical variables (ignore dimensionless variables)
>> $k=$ the number of physical dimensions involved 

#### Example

>> What is k,n and p for analysing the relationship between the variables $g$, $l$, $m$ and $\tau$ (period)
>> ![[Pasted image 20211026201954.png]]
> First lets break them down into dimensions:
> - $g=LT^{-2}$
> - $l=L$
> - $m=M$
> - $\tau=T$
> So we have 3 dimensions (length,time,mass), hence $k=3$
> We have 4 variables, hence $n=4$
> So $p = n-k$ giving us $p = 4-3 = 1$

### Finding the dimensionless parameters
#### Method
The goal of the theoruem is to provide a method for finding sets of dimensionless parameters by using the given variables, even if the equation relating those variables is unknown (like trying to do [[using dimentional homogeneity to find units|this thing]] without knowing the equation for it).


#### Example
>> In turbulent flow the head loss when a liquid flows through a smooth pipe is dependant upone the quantities below. Determine the fundamental scaling relationships that might be important.
>> ![[Pasted image 20211026203121.png]]
> - Head loss turns out to be dimensionless so we ignore it
> - Mean velocity (V) = $LT^{-1}$
> - Diameter (D) = $L$
> - Liquid density ($\rho$) = $ML^{-3}$
> - Dynamic viscosity ($\mu$) = $ML^{-1}T^{-1}$
> - Acc due to grav ($g$) = $LT^{-2}$
> 
>  We have 3 dimensions (length, time, mass) so $k=3$
>  We have 5 variables so $n=5$
>  So $p=2$ meaning we have 2 dimensionless parameters: $\pi_1,\pi_2$
> --- 
> Before we can continue we choose the parameters to be our dimensionless parameters, (this can be litterally anything, but you generally choose variables that are of intrest in the problem {ones you can't measure(excessive brackes {see [[top 10 reasons for excessive bracket use]] } ) } ).
>  So we will use Dynamic viscosity ($\mu$) and gravity ($g$) for our dimensionless parameters.
> When doing the maths later we have one value of $\pi_n$ per dimensionless parameter, and in the maths for that we construct our equation for $\pi_n$ using:
>> $\pi_n$ = (all parameters that arn't dimensionless parameters to their powers)\*(dimensionless parameter we are focused on)
>
> Now to calculate $\pi_1$: 
> $$ \begin{align*}
\pi_1 &= V^{a}D^{b}\rho^{c}\mu\\
&= (LT^{-1})^{a}  (L)^{b}  (ML^{-3})^{c}  (ML^{-1}T^{-1})\\
&   &   0&=aL+bL-3cL-L   &   0&=-aT-T   &   0&=cM+M\\
&   &   1&=a+b-3c   &   a&=-1   &   c&=-1\\
&   &   1&=-1-1-3c\\
&   &   c&=-1\\
\pi_1 &= V^{-1}D^{-1}\rho^{-1}\mu\\
&= \frac{\mu}{VD\rho}\\
\end{align*} $$
>
> And then $\pi_2$:
> $$ \begin{align*}
\pi_2 &= V^{a}D^{b}\rho^{c}g\\
&= (LT^{-1})^{a}  (L)^{b}  (ML^{-3})^{c}  (LT^{-2})\\
&   &   0&=aL+bL-3cL+L   &   0&=-aT-2T   &   0&=cM\\
&   &   0&=a+b-3c+1   &   a&=-2   &   c&=0\\
&   &   0&=-2+b+1 \\
&   &   b&= 1 \\
\pi_1 &= V^{-2}D^{1} g\\
&=\frac{Dg}{V^{2}}
\end{align*} $$
> 
> Note that $\pi_1 = \frac{\mu}{VD\rho}$ can be written as $(\frac{\mu}{VD\rho})^x$ with any value for x, meaning you can use $x=-1$ to flip it and get: $\frac{VD\rho}{\mu}$
>>  Also note that what $\pi_1$ and $\pi_2$ translate to interms of a dimensional relationship is:
>> $$ \pi_1 \cdot \mu = VD\rho $$
> $$and$$
>> $$ \pi_2 \cdot g = \frac{V^{2}}{D} $$
>Since $\pi_n$ acctually represents a dimensionless ratio between these quanitys