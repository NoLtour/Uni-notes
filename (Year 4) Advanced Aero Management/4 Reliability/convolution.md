---
aliases:
  - filter function
  - kernel
  - kernel function
tags:
---

## Convolution

convolution is an operation that combines two functions to produce a third function, expressing how the shape of one function is modified by another. It’s defined as the integral of the product of the two functions after one is flipped and shifted:

> ### $$\begin{align*} (f * g) (t) &=  \int^{\infty}_{\infty} f(\tau) \: g(t-\tau) d\tau \end{align*}$$
>> where:
>> $f*g=$ is the convolution of f in terms of g (order matters!)
>> $f(t)=$ input function being convolved (or signal function)
>> $g(t)=$ function of the kernel (or filter function)

For the convolution to yield a useful result, you'll have the kernel $g(t)$ have a [[absolutely integrable|finite area]]. Convolution can be done (approximately) numerically or analytically, it's INSANELY useful just a bit confusing at first.

There exists extension of convolution into 2D and 3D sets, but it's easiest to see for a 1D function:

![[01_convolution-operation-example-1494286218.png|700]]

The simplest use is for averaging, which can be done very effectively with a square wave or Gaussian. That said, it's useful in doing far far more complex operations such as edge finding.