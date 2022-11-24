---
aliases: ["decibel","dB","decibels","dBW"]
tags: []
---

## The decibel ($dB$)
### Generic decibel
A decibel is just a way of expressing a ratio between the power of two thing's logarithmically:

> ### $$ R = P_{a}/P_{b} $$ 
> ### $$ R_{dB} = 10\log_{10}(R) $$
> ### $$ ( P_{a}/P_{b} )_{dB} = 10\log_{10}( P_{a}/P_{b} ) $$
>> where:
>> $R=$ the ratio of $P_{a}$ to $P_{b}$
>> $R_{dB}=$ [[the decibel|decibel]]
>> $P_{a},P_{b}=$ power of a something

When working with communications, it is common to describe things using [[the decibel|decibels]] since ratio's are often orders of magnitude in scale.

### 1 Watt dB ($dBW$)
It is common to express power levels relative to 1 Watt, hence:

> ### $$ (P_{T})_{dBW} = 10\log_{10}(P_{T}/1) = 10\log_{10}(P_{T})$$ 
>> where:
>> $P_{T}=$ some power

eg: 
$$\begin{align*}
P_{T} &= 42.3 dBW & \to& &P_{T} = 10^{42.3/10} &= 16982 kW
\end{align*}$$
