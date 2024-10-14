---
aliases:
  - multivariate MLE
tags:
---

## Multivariate [[maximum likelihood estimation]]

Well the methods basically the same as was seen in [[maximum likelihood estimation]], the difference here is that now the problems (even [[I would say suffer but it means not on exam|more]]) generally too complex to do analytically.

### [[multivariate normal distribution|Multivariate gaussian distribution]] example

Taking the starting formula, we convert it into a form suited for our [[multivariate normal distribution|multivariate gaussian distribution]]:

$$\begin{align*}
l(\theta) = \ln L(\theta) &=  \ln \left[ \prod^{n}_{i=1} f(t_{i} ; \theta) \right]\\ &=\sum\limits^{n}_{i=1} \ln f(t_{i} ; \theta) &&\to& l( \boldsymbol{\mu},\boldsymbol{\Sigma}) &= \sum\limits^{n}_{i=1} \ln f(\boldsymbol{x}_{i},\boldsymbol{\mu},\boldsymbol{\Sigma})
\end{align*}$$

Taking our expression for the [[probability density function|PDF]]:

$$\begin{align*}
f(\boldsymbol{x},\boldsymbol{\mu},\boldsymbol{\Sigma})  &= \frac{1}{\sqrt{(2\pi)^{p}\det\boldsymbol{\Sigma}}} \exp \left[-\frac{1}{2} (\boldsymbol{x} - \boldsymbol{\mu})^{T} \boldsymbol{\Sigma}^{-1} (\boldsymbol{x}-\boldsymbol{\mu}) \right] \\ &\downarrow\\

\ln f(\boldsymbol{x},\boldsymbol{\mu},\boldsymbol{\Sigma})  &=  - \frac{1}{2}( \ln[(2\pi)^{p}] + \ln[\det\boldsymbol{\Sigma}]) -\frac{1}{2} (\boldsymbol{x} - \boldsymbol{\mu})^{T} \boldsymbol{\Sigma}^{-1} (\boldsymbol{x}-\boldsymbol{\mu}) \\ &\downarrow\\

\ln f(\boldsymbol{x},\boldsymbol{\mu},\boldsymbol{\Sigma})  &=  -\frac{p}{2} \ln(2\pi) - \frac{1}{2} \ln(\det\boldsymbol{\Sigma}) -\frac{1}{2} (\boldsymbol{x} - \boldsymbol{\mu})^{T} \boldsymbol{\Sigma}^{-1} (\boldsymbol{x}-\boldsymbol{\mu})
\end{align*}$$

Which subbing into the likelihood function:

$$\begin{align*}
l( \boldsymbol{\mu},\boldsymbol{\Sigma}) &= \sum\limits^{n}_{i=1} \ln f(\boldsymbol{x}_{i},\boldsymbol{\mu},\boldsymbol{\Sigma}) &&\to&
-2l( \boldsymbol{\mu},\boldsymbol{\Sigma}) &=  np \ln(2\pi) +n \ln(\det\boldsymbol{\Sigma}) + \sum\limits^{n}_{i=1}(\boldsymbol{x}_{i} - \boldsymbol{\mu})^{T} \boldsymbol{\Sigma}^{-1} (\boldsymbol{x}_{i}-\boldsymbol{\mu})

\end{align*}$$

Now we simply have to maximise this for those nasty ass matrices which are now our parameters. In this particular case there is actually a closed form solution for finding the turning point, going to skip the details (outside module scope and [[I am so glad we don't have to derive it|loooooong]]), but eventually you get:

$$\begin{align*}
\mu_{i} &= \frac{1}{n} \sum\limits^{n}_{a=1} x_{a} &&& \Sigma_{ij}= \text{cov}(x_{i}, x_{j})
\end{align*}$$

Where $\text{cov}(...)$ is from [[maximum likelihood estimation confidence#Information and Covariance Matrices]].

