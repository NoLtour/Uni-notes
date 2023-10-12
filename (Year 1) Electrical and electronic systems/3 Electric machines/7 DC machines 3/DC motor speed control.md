---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can we achieve
## DC motor speed control
The simplest solution is slapping a DC motor in series with a [[rheostat]], but this kinda sucks because now you loose power as heat for no good reason, hence it is a trash approach and anyone who suggests it should/will/is getting executed by firing squad.

Now the galaxy brain approach (which I 100% didn't just learn about, and knew all along (since birth actually) because I would never consider the previous approach) is to slap a transistor in there, then use a really fast [[alternating current]] with the following waveform and circuit configuration:
![[Pasted image 20220224142943.png]]
By also slapping an [[inductor]] in series with the motor you can ensure a more stable current, and given a really high frequency the current will basically approximate as constant. (the diode in the circuit basically allows for the current to keep flowing correctly during the periods where there is no current from the soruce)

The mean current can be found using:
> ### $$ I_{mean} = \frac{P_{on}}{P_{on}+P_{off}} I_{amp}= \frac{P_{on}}{P} I_{amp} $$ 
>> where:
>> $I_{mean}=$ the mean current reaching the motor
>> $I_{amp}=$ the amplitude of the AC wave 
>> $P_{on}=$ The period where the wave current is at $I_{amp}$
>> $P_{off}=$ The period where the wave current is zero
>> $P=$ The period of the AC wave

Of course the above equation just works for square waves, but you get the idea... vary the period on/off to vary the average current and average motor speed, in this case due to the high frequency the average is basically equal to the real value anyway so yeah... stuff.