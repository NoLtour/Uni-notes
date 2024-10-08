---
aliases:
  - information and covariance matrices
  - Fisher information matrix
  - MLE confidence interval
tags:
---

## Maximum likelihood estimation confidence

When applying [[maximum likelihood estimation]] we know our answer is wrong, this is because we don't have infinite perfect samples. Though in practical terms that imperfect solution is generally good enough, and it becomes better with more samples:
![[Pasted image 20241008111453.png]]

It is however important to be able to quantify how certain we are in our estimation, and that is what's covered here.

#### Information and Covariance Matrices

The information and covariance matrices have the following definitions, please note that although they look disgusting it's not THAT bad for [[continuous distribution functions|distribution functions]] with like 1-2 parameters:

> ### $$\begin{align*} I_{ij}  &=  E \left[-\frac{\partial^{2}l (t;\theta)}{\partial \theta_{i} \partial\theta_{j}}\right] \end{align*}$$
> ### $$\begin{align*} I^{-1} &= \begin{pmatrix} \text{Var}(\theta_{1}) & \text{Cov}(\theta_{1},\theta_{2}) & ...  & \text{Cov}(\theta_{1},\theta_{k} ) \\ \text{Cov}(\theta_{2},\theta_{1}) & \text{Var}(\theta_{2}) & ... &  \text{Cov}(\theta_{2},\theta_{k} ) \\ ... & ... & ... & ... \\ \text{Cov}(\theta_{k},\theta_{1})  & \text{Cov}(\theta_{k},\theta_{2}) & ... & \text{Var}(\theta_{k})  \end{pmatrix}\end{align*}$$
>> where:
>> $l=$ [[maximum likelihood estimation#^6e1413|log likelihood estimation function]]
>> $\text{Var}(\theta_{i})=$ [[standard deviation for probabability functions|varience]] in the parameter $\theta_i$
>> $\text{Cov}(\theta_{i},\theta_{j})=$ the covariance of the parameters $\theta_i$ and $\theta_j$
>> $I=$ the [[maximum likelihood estimation confidence|Fisher information matrix]]
>> $I_{ij}=$ an element of the Fisher information matrix

#### [[maximum likelihood estimation|MLE]] Confidence interval

This is the interval within which we have 95% certainty that the parameters found for our [[continuous distribution functions|distribution function]] is correct. It is defined from the [[standard deviation for probabability functions|varience]]:

> ### $$\begin{align*}  P(\theta_{l} \leq \hat{\theta}  \leq \theta_{u}) &= \gamma &&\overset{(95\%\text{ case})}{=} 0.95 \end{align*}$$
> ### $$\begin{align*} \theta_{l}&=  \hat{\theta} - Z_{\alpha/2} \sqrt{\text{Var}(\hat{\theta})}& &&\theta_{u}&=  \hat{\theta} + Z_{\alpha/2} \sqrt{\text{Var}(\hat{\theta})} \end{align*}$$
> ### $$\begin{align*} \alpha &= 1- \gamma &&& Z_{\alpha/2}=\begin{cases} 1.96&&& 95\%\text{ certainty}\\2.58&&& 99\%\text{ certainty} \end{cases} \end{align*}$$
>> where:
>> ${\theta}=$ some parameter of our target [[continuous distribution functions|distribution function]]
>> $\hat{\theta}=$ the most likely value of the parameter according to [[maximum likelihood estimation]]
>> $\theta_{l},\theta_{u}=$ the upper and lower bounds under the target certainty
>> $\text{Var}(\hat\theta)=$ the variance for the parameter in question ([[maximum likelihood estimation confidence#Information and Covariance Matrices]])
>> $Z_{\alpha/2}=$ the standard normal statistic (taken from lookup tables generally or calculated) (NOTE: values placed here might ONLY work for gaussians? unsure)
>> $\gamma=$ confidence that the true $\theta$ is in that range

#### Example

Once again we will be working with the [[continuous distribution functions|gaussian distribution]], going to reuse some working from [[maximum likelihood estimation#Example 1]]. From there we have the partial derivatives of the [[maximum likelihood estimation|log likelihood estimation function]]:
$$\begin{align*}
\frac{\partial l}{\partial \mu} &= -\frac{1}{2 \sigma^{2}} \sum\limits^{n}_{i=1} 2\mu -2t_{i} \\
\frac{\partial l}{\partial \sigma} &=  - \frac{n}{\sigma} +\frac{1}{ \sigma^{3}} \sum\limits^{n}_{i=1} \left( t_{i}-\mu\right)^{2} 
\end{align*}$$

Looking at the elements of the [[maximum likelihood estimation confidence|Fisher information matrix]], we need to take the additional partial derivatives of each with respect to $\mu$ and $\sigma$:

$$\begin{align*}
\frac{\partial^{2} l}{\partial \mu^{2}} &= \frac{\partial }{\partial \mu} \left[ -\frac{1}{2 \sigma^{2}} \sum\limits^{n}_{i=1} 2\mu -2t_{i} \right] &&\to&    
\frac{\partial^{2} l}{\partial \mu^{2}} &=  -\frac{1}{2 \sigma^{2}} \sum\limits^{n}_{i=1} 2 &&\to&    
\frac{\partial^{2} l}{\partial \mu^{2}} &=  -\frac{n}{ \sigma^{2}} 
\\
\frac{\partial^{2} l}{\partial \mu \partial \sigma} &= \frac{\partial }{\partial \sigma} \left[ -\frac{1}{2 \sigma^{2}} \sum\limits^{n}_{i=1} 2\mu -2t_{i} \right] &&\to&    
\frac{\partial^{2} l}{\partial \mu \partial \sigma} &=    \frac{2}{  \sigma^{3}} \sum\limits^{n}_{i=1}  \mu - t_{i}  
\\
\frac{\partial^{2} l}{\partial \sigma^{2}} &= \frac{\partial }{\partial \sigma} \left[ - \frac{n}{\sigma} +\frac{1}{ \sigma^{3}} \sum\limits^{n}_{i=1} \left( t_{i}-\mu\right)^{2}  \right] &&\to&     
\frac{\partial^{2} l}{\partial \sigma^{2}} &=   \frac{n}{\sigma^{2}} -\frac{3}{ \sigma^{4}} \sum\limits^{n}_{i=1} \left( t_{i}-\mu\right)^{2}   
\\
\end{align*}$$

We can simplify these by recalling the definitions derived from the [[maximum likelihood estimation#Example 1]], the following were found while solving:
$$\begin{align*}
\sigma &=  \sqrt{\frac{1}{n} \sum\limits^{n}_{i=1} \left( t_{i}-\mu\right)^{2} } &&\to& \sigma^{2}n &= \sum\limits^{n}_{i=1} \left( t_{i}-\mu\right)^{2}
\end{align*}$$
$$\begin{align*}
 0 &= \sum\limits^{n}_{i=1} \mu -t_{i}
\end{align*}$$

So then subbing these in:

$$\begin{align*}
 \frac{\partial^{2} l}{\partial \mu^{2}} &=  -\frac{n}{ \sigma^{2}} &&\to&
 \frac{\partial^{2} l}{\partial \mu^{2}} &=  -\frac{n}{ \sigma^{2}}
\\
 \frac{\partial^{2} l}{\partial \mu \partial \sigma} &=    \frac{2}{  \sigma^{3}} \sum\limits^{n}_{i=1}  \mu - t_{i}  &&\to&
 \frac{\partial^{2} l}{\partial \mu \partial \sigma} &=   0
\\
 \frac{\partial^{2} l}{\partial \sigma^{2}} &=   \frac{n}{\sigma^{2}} -\frac{3}{ \sigma^{4}} \sum\limits^{n}_{i=1} \left( t_{i}-\mu\right)^{2}  &&\to&
 \frac{\partial^{2} l}{\partial \sigma^{2}} &=   \frac{n}{\sigma^{2}} -\frac{3n}{ \sigma^{2}}  &&\to&
 \frac{\partial^{2} l}{\partial \sigma^{2}} &=   -\frac{2n}{\sigma^{2}} 
\end{align*}$$

Finally the [[maximum likelihood estimation confidence|Fisher information matrix]] can be constructed:

$$\begin{align*}
 I_{ij}  &=  E \left[-\frac{\partial^{2}l (t;\theta)}{\partial \theta_{i} \partial\theta_{j}}\right] &&\to& 
I&= \begin{pmatrix} -\dfrac{\partial^{2} l}{\partial \mu^{2}} & -\dfrac{\partial^{2} l}{\partial \mu\partial \sigma} \\ - \dfrac{\partial^{2} l}{\partial \mu\partial \sigma} & -\dfrac{\partial^{2} l}{\partial \sigma^{2}} \end{pmatrix} &&\to& 
I&= \begin{pmatrix} \dfrac{n}{\sigma^{2}} & 0\\0 & \dfrac{2n}{\sigma^{2}} \end{pmatrix}
\end{align*}$$

Then finding the inverse we can finally get the variances by [[inverse matrix]]:

$$\begin{align*} 
\det I &= \frac{2n^{2}}{\sigma^{4}} &&& I^{-1} &= \frac{\sigma^{4}}{2n^{2}} \begin{pmatrix} \dfrac{2n}{\sigma^{2}} & 0\\0 & \dfrac{n}{\sigma^{2}} \end{pmatrix}
 &&\to& I^{-1} &=  \begin{pmatrix} \frac{\sigma^{2}}{n} & 0\\0 & \frac{\sigma^{2}}{2n} \end{pmatrix}
\end{align*}$$

Hence finally:

$$\begin{align*}
\text{Var}(\mu) &= \frac{\sigma^{2}}{n} &&& \text{Var}(\sigma) &= \frac{\sigma^{2}}{2n}
\end{align*}$$

We can see that both the standard deviation and mean have increasing certainty (decreasing variance) as then number of samples $n$ increases, and both are increased based on the standard deviation. Which makes sense as the standard deviation will increase the distribution of samples hence making finding the true parameters more difficult.
