---
aliases: ["bit rate","sampling frequency","digital modulation techniques","shannons law"]
tags: []
---

## Communications signal encoding
### Intro
As discussed in [[communications through the atmosphere#Frequency bands|this link]] there is very limited frequency bands that are available for use, so we've got to cram as much information as possible into as little as possible.

### Analog to digital encoding
#### Sampling frequency
If you have a analogue signal then it will also have a frequency at which sufficient useful information is gathered. For example if trying to record a human voice the maximum frequency a human voice can produce ([[sigma mode|for typical settings]]) is about 3400Hz, so this is the frequency we want to reproduce $f_{max}=3400Hz$. 

Since we want to properly capture enough information to reproduce $f_{max}$ we actually need to sample at atleast double $f_{max}$. Hence sampling rate $f_{s}$ is:
$$ f_{s} \geq 2f_{max}  $$
In the human voice example we probably want about $7000Hz$ sample rate.

#### Bit rate ($R_{b}$)
Bit rate is simply sample size multiplied by sampling rate:

> ### $$ R_{b} = f_{s} S $$ 
>> where:
>> $R_{b}=$ bit rate (bits/second)
>> $f_{s}=$ sample frequency
>> $S=$ sample size (bits)

### Digital modulation techniques
#### Common types
![[Pasted image 20221123164927.png]]

- Amplitude shift keying (ASK). This is a form of amplitude modulation that represents digital data as variations in amplitude of a carrier wave.
- Frequency shift keying (FSK). This is a form of frequency modulation that represents digital data as discrete variations in frequency of a carrier wave.
- Phase shift keying (PSK). This is a form of digital modulation that represents digital data as variations in phase of a constant frequency carrier wave.

#### The important one
For our applications and for most applications PSK is used, since it can encode lots of data (you can use more that 2 phase states btw) and it only contaminates 1 frequency band.

With PSK it is clear that each oscillation can be used to encode 1 phase state, so in the case where 2 phases are used for 1 bit representation it is clear that the maximum number of bits you can cram into a transmission is directly related to frequency, this can be found using shannons law:
> ### $$ R_{max} = B \log_{2}\left(1+ \frac{S}{N}\right) $$ 
>> where:
>> $R_{max}=$ channel capacity in bits per second
>> $B=$  bandwidth of the channel in hertz
>> $S/N=$ [[signal to noise ratio]]

