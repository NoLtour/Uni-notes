---
aliases:
  - uniform distribution function
  - triangular distribution function
  - gaussian distribution
  - normal distribution
  - mean time to failure
  - exponential distrobution
  - Weibull distribution
  - distribution functions
  - continuous distribution function
tags:
---

## Distribution functions

There are lots of different [[probability density function|probability density functions]], they each have slightly different shapes and so when modelling a real phenomena we must select the one which is most reasonably suited. Here we point out the ones covered in the course, which are frequently used in real application but obviously the true number of distribution functions far exceeds what's covered here. As engineers it's our job to let the nerds figure out the truth and [[absolutes are for suckers we make shit work|stick to thing's that are good enough]].

### Uniform distribution function

Can't get much simpler than this, over some interval there is equal likelihood of it occurring:

> ### $$\begin{align*} f(t)  &= \begin{cases}    \frac{1}{b-a},& a \leq t \leq b \\    0, &\text{else}\end{cases}  \end{align*}$$
> ### $$\begin{align*} F(t)  &= \begin{cases}  0, &t<a\\  \frac{t-a}{b-a},& a \leq t \leq b \\    1, &t>b\end{cases}  \end{align*}$$
>> where:
>> $f(t)=$ the [[probability density function]] in terms of $t$, for a uniform distribution function
>> $F(t)=$ it's corresponding [[cumulative distribution function]] in terms of $t$
>> $a,b=$ the limits for where it has non zero chance of occurring
>> $t=$ some parameter, often time 

| PDF                                  | CDF                                  |
| ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20241007105348.png]] | ![[Pasted image 20241007105401.png]] |

### Triangular distribution function

Slightly more complex, here there is a linear ramp that leads up and then down from the midpoint of limits a, c:

> ### $$\begin{align*} f(t)  &= \begin{cases} \frac{2(t-a)}{(c-a)(b-a)} & a \leq t \leq b\\ \frac{2(c-t)}{(c-a)(b-a)},& b \leq t \leq c \\    0, &\text{else}\end{cases}  \end{align*}$$
>> where:
>> $f(t)=$ the [[probability density function]] in terms of $t$, for a triangular distribution function
>> $a,c=$ the limits for where it has non zero chance of occurring
>> $b= \frac{a+c}{2}=$ the midpoint
>> $t=$ some parameter, often time 

| PDF                                                                                                                       | CDF                                  |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| ![[Pasted image 20241007105824.png]]<br>(note the missing t, [[not my mistake or problem\|it's like that on the slides]]) | ![[Pasted image 20241007105841.png]] |

### Gaussian distribution

The one we've all been waiting for.... lets go!

> ### $$\begin{align*} f(t)  &= \frac{1}{\sigma \sqrt{2\pi}} \exp\left[-\frac{1}{2} \left(\frac{t-\mu}{\sigma}\right)^{2} \right] \end{align*}$$
>> where:
>> $f(t)=$ the [[probability density function]] in terms of $t$, for a [[continuous distribution functions|gaussian distribution]] in terms of $t$ 
>> $t=$ some parameter, often time 
>> $\mu=$ location parameter, "[[mean value by integration|mean]]"
>> $\sigma=$ scaling parameter, "[[standard deviation for probabability functions|standard deviation]]"


| PDF                                  | CDF                                  |
| ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20241007110643.png]] | ![[Pasted image 20241007110657.png]] |

There are also the other neat properties that go with this distribution, like the stable chances of falling within $n$ standard deviations of the mean:
![[Pasted image 20241007110755.png]]
Calculated you get statements like "95.44% within 2 standard deviations" or "99.74% within 3 standard deviations". Convenient calls like this help make this such a nice function to work with.


### Exponential Distribution

The exponential distribution has the unique feature that it's [[hazard function|hazard rate]] is constant. Additionally, it's got the convenient feature that it's zero before $t=0$, making it useful in cases where negative $t$ is invalid which is frequently true when dealing with time.

> ### $$\begin{align*} f(t)  &=  \begin{cases} \lambda e^{-\lambda t} & , t\geq 0 \\ 0 & , t<0 \end{cases} \end{align*}$$
> ### $$\begin{align*} h(t) &= \text{constant} =\lambda \end{align*}$$
>> where:
>> $f(t)=$ the [[probability density function]] in terms of $t$, for a exponential distribution function
>> $h(t)=$ the [[hazard function|hazard rate]]
>> $t=$ some parameter, often time 
>> $\lambda=$ the constant [[hazard function|hazard rate]], also referred to as the scaling parameter
>> $1/\lambda=$ the mean time to failure


| PDF                                  | CDF (has closed form analytical form) |
| ------------------------------------ | ------------------------------------- |
| ![[Pasted image 20241007152554.png]] | ![[Pasted image 20241007152609.png]]  |

### Weibull distribution

#### Two parameter version

Ok with how much the lecturer loves this function, it is going to be all over the exam. He likes it for good reason though, this function is really flexible and has a closed form [[cumulative distribution function|CDF]]!

> ### $$\begin{align*} f(t)  &=\frac{\beta}{\eta^{\beta}} t^{\beta-1} \exp\left[-\left(\dfrac{t}{n}\right)^{\beta}\right]  \end{align*}$$
> ### $$\begin{align*} F(t)  &= 1 - \exp\left[\left(\dfrac{t}{\eta}\right)^{\beta}\right] \end{align*}$$
> ### $$\begin{align*} h(t)  &= \frac{\beta}{\eta^{\beta}} t^{\beta-1} \end{align*}$$
>> where:
>> $f(t)=$ the [[probability density function]] in terms of $t$, for a Weibull distribution function
>> $F(t)=$ the [[cumulative distribution function]]
>> $h(t)=$ the [[hazard function]]
>> $t=$ some parameter, often time
>> $\beta=$ shape parameter
>> $\eta=$ scaling parameter 

Note that $\eta$ is sometimes referred to as the characteristic life, this is the point where 63.2% of the population would have failed in a failure analysis case.

And yes, looking at this abomination I also have no idea how they integrated that. They might have instead started from the CDF and differentiated it into the PDF, then again it looks clean enough to be some standard integral identity? Anyway that's getting side tracked.

By modifying $\beta$ we can change the shape of the plot:
> ### $$\begin{align*} \\\beta  &= 1 & &\text{The hazard rate becomes constant, hence it's equivilent to the exponential dist func} \\ \beta&> 1 & &\text{We see a increasing hazard rate} \\ \beta&< 1 & &\text{We see a decreasing hazard rate} \\ \beta&= 3.5 & &\text{The PDF becomes a resonable approximation of the normal distrobution}\\\: \end{align*}$$
#### Three parameter version

By adding an additional parameter $\gamma$, often called the "location parameter" we can shift the [[continuous distribution functions|Weibull distribution]] away from the origin:

> ### $$\begin{align*} f(t)  &=\begin{cases} \frac{\beta}{\eta^{\beta}} (t-\gamma)^{\beta-1} \exp\left[-\left(\dfrac{t-\gamma}{n}\right)^{\beta}\right]&&, t\geq\gamma \\ 0&&,t<\gamma \end{cases} \end{align*}$$
> ### $$\begin{align*} F(t)  &= 1 - \exp\left[\left(\dfrac{t-\gamma}{\eta}\right)^{\beta}\right] \end{align*}$$
> ### $$\begin{align*} h(t)  &= \frac{\beta}{\eta^{\beta}} (t-\gamma)^{\beta-1} \end{align*}$$
>> where:
>> $f(t)=$ the [[probability density function]] in terms of $t$, for a Weibull distribution function
>> $F(t)=$ the [[cumulative distribution function]]
>> $h(t)=$ the [[hazard function]]
>> $t=$ some parameter, often time
>> $\beta=$ shape parameter
>> $\eta=$ scaling parameter 

| PDF                                  | CDF (has closed form analytical form) |
| ------------------------------------ | ------------------------------------- |
| ![[Pasted image 20241007154922.png]] | ![[Pasted image 20241007154937.png]]  |
