---
aliases:
  - MLE
tags:
---

## Maximum likelihood estimation

Basically, we take the distribution function, then determine the likelihood that some set of parameters is the correct set of parameters based on how likely our samples are to be produced from that set of parameters. The parameter set which has the highest likelihood of producing our samples is the best available set, hence we use that.

Put mathematically it's below, note that we don't need to take the log but doing so generally makes it possible to actually solve on paper and helps with [[numerical instability]].

> ### $$\begin{align*} f(t; \theta_{1},\theta_{2},\theta_{3} ... \theta_{n})  &=  f(t;\theta) \end{align*}$$
> ### $$\begin{align*} l(\theta) = \log L(\theta) &=  \log \left[ \prod^{n}_{i=1} f(t_{i} ; \theta) \right]\\ &=\sum\limits^{n}_{i=1} \log f(t_{i} ; \theta) \end{align*}$$
> ### $$\begin{align*} \theta \text{ is when } l(\theta) \text{ is maximised},&&& \therefore \frac{\partial l}{\partial \theta_{j}}=0 \:\:(j=1,2,3 ... n) \end{align*}$$
>> where:
>> $f(t;\theta)=$ some [[continuous distribution functions|continuous distribution function]] where the form is known but its parameters $\theta$ aren't known
>> $t_{i}=$ a sample value
>> $l(\theta)=$ is the log of $L(\theta)$
>> $L(\theta)=$ is the overall probability density that some combination of $\theta$ parameters is correct
>> $\theta=$ the parameters associated with $f(t)$
>> $j=$ the index of the parameter ($\theta_{j}$) being found


#### Example

It makes more sense if it's been demonstrated, the following is demonstration using the [[continuous distribution functions|gaussian distribution]]:

$$\begin{align*}
f(t)  &= \frac{1}{\sigma \sqrt{2\pi}} \exp\left[-\frac{1}{2} \left(\frac{t-\mu}{\sigma}\right)^{2} \right]
\end{align*}$$

Here our parameter set is $\mu$ and $\sigma$, so:

$$\begin{align*}
 \log f(t;\mu,\sigma) &= \log \left[ \frac{1}{\sigma \sqrt{2\pi}} \exp\left[-\frac{1}{2} \left(\frac{t-\mu}{\sigma}\right)^{2} \right] \right] &&\to& 
 l(\mu, \sigma) &=  -\frac{1}{2} \left(\frac{t-\mu}{\sigma}\right)^{2} - \log \sigma \sqrt{2\pi} 
\end{align*}$$

This can then be subbed into the $l$ function:

$$\begin{align*}
l(\theta) &= \sum\limits^{n}_{i=1} \log f(t_{i} ; \theta)   &&\to&  l(\mu,\sigma) &= \sum\limits^{n}_{i=1} \left[ -\frac{1}{2} \left(\frac{t_{i}-\mu}{\sigma}\right)^{2} - \log \sigma \sqrt{2\pi}  \right]  &&\to&  

l(\mu,\sigma) &=  - n\log \sigma \sqrt{2\pi} -\frac{1}{2 \sigma^{2}} \sum\limits^{n}_{i=1} \left( t_{i}-\mu\right)^{2}
\end{align*}$$

Then we find the derivative:

$$\begin{align*}

\frac{\partial l}{\partial \mu} &= \frac{\partial }{\partial \mu} \left[ - n\log \sigma \sqrt{2\pi} -\frac{1}{2 \sigma^{2}} \sum\limits^{n}_{i=1} \left( t_{i}-\mu\right)^{2}\right] &&\to&
\frac{\partial l}{\partial \mu} &= -\frac{1}{2 \sigma^{2}} \sum\limits^{n}_{i=1} 2\mu -2t_{i} 
\end{align*}$$

$$\begin{align*}
\frac{\partial l}{\partial \sigma} &= \frac{\partial }{\partial \sigma} \left[ - n\log \sigma \sqrt{2\pi} -\frac{1}{2 \sigma^{2}} \sum\limits^{n}_{i=1} \left( t_{i}-\mu\right)^{2}\right] &&\to&
\frac{\partial l}{\partial \sigma} &= \frac{\partial }{\partial \sigma} \left[ - n\log \sigma - \frac{n}{2}\log 2\pi  -\frac{1}{2 \sigma^{2}} \sum\limits^{n}_{i=1} \left( t_{i}-\mu\right)^{2}\right]&&\to&
\frac{\partial l}{\partial \sigma} &=  - \frac{n}{\sigma} +\frac{1}{ \sigma^{3}} \sum\limits^{n}_{i=1} \left( t_{i}-\mu\right)^{2} 
\end{align*}$$

Finally we can find the turning point (maximum):
$$\begin{align*}
\frac{\partial l}{\partial \mu}=0 &= -\frac{1}{2 \sigma^{2}} \sum\limits^{n}_{i=1} 2\mu -2t_{i}  &&\to& 0 &= \sum\limits^{n}_{i=1} \mu -t_{i}   &&\to& 0 &= \left(\sum\limits^{n}_{i=1} t_{i}\right) - n\mu &&\to& \mu &= \frac{1}{n} \sum\limits^{n}_{i=1} t_{i}
\end{align*}$$

$$\begin{align*}
\frac{\partial l}{\partial \sigma}=0 &=  - \frac{n}{\sigma} +\frac{1}{ \sigma^{3}} \sum\limits^{n}_{i=1} \left( t_{i}-\mu\right)^{2}  &&\to&
 n &=  \frac{1}{ \sigma^{2}} \sum\limits^{n}_{i=1} \left( t_{i}-\mu\right)^{2}  &&\to&
\sigma &=  \sqrt{\frac{1}{n} \sum\limits^{n}_{i=1} \left( t_{i}-\mu\right)^{2} }
\end{align*}$$

If this looks familiar, that's because it is. Congrats on deriving the [[mean value by integration|mean]] and [[standard deviation for probabability functions|standard deviation]].


