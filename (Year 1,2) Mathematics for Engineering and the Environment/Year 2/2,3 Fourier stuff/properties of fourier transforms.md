---
aliases: ["Fourier transform shift properties","Fourier transform linerarity","Fourier transform of the differential","Fourier transform of differential"]
tags: []
---

## Properties of [[fourier transforms]]

### Fourier transform of the differential


> ### $$ \mathcal{F}\left[ \frac{df}{dt} \right] = j\omega \mathcal{F}[f(t)] $$ 
> ### $$ \mathcal{F}\left[ \frac{d^{n}f}{dt^{n}} \right] = (j\omega)^{n} \mathcal{F}[f(t)] $$ 
>> where:
>> $f(x)=$ some input function of $x$ 
>> $j=\sqrt{-1}$
>> $\omega=$ frequency
>> $\mathcal{F}[...]=$ fourier transform of some function 

### Fourier transform linerarity

Essentially, if you apply a fourier transform to some function which is constructed out of multiple added functions, you can fourier transform each component and add em back together:

> ### $$ \mathcal{F}[ Af(x) + Bg(x) ] =  A\mathcal{F}[ f(x) ] + B\mathcal{F}[g(x)] $$ 
>> where:
>> $f(x),g(x)=$ some input function of $x$ 
>> $A,B=$ variables independent of $x$
>> $j=\sqrt{-1}$
>> $\omega=$ frequency
>> $\mathcal{F}[...]=$ fourier transform of some function 

### Fourier transform shift properties

> ### $$ \mathcal{F}[  f(x + A ) ] = e^{-j\omega A} \mathcal{F}[f(x)]  = e^{-j\omega A} F(\omega) $$ 
>> where:
>> $f(x) =$ some input function of $x$ 
>> $A =$ variables independent of $x$
>> $j=\sqrt{-1}$
>> $F(\omega)=$ the fourier transform of $f(t)$
>> $\omega=$ frequency
>> $\mathcal{F}[...]=$ fourier transform of some function 

> ### $$   F(\omega-A) = \mathcal{F}[ e^{jAt} f(x ) ] $$ 
>> where:
>> $f(x) =$ some input function of $x$ 
>> $A =$ variables independent of $\omega$
>> $j=\sqrt{-1}$
>> $F(\omega)=$ the fourier transform of $f(t)$
>> $\omega=$ frequency
>> $\mathcal{F}[...]=$ fourier transform of some function 
