---
aliases: ["range in the statosphere"]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Calculating range in the statosphere
#### Intro
Although we know from [[min drag in steady level flight|you basically get free fuel by flying higher]], but sadly this relationship dosn't last forever. As you start to approach the [[speed of sound]] air will begin to move at supersonic speeds around various parts of the plane, this causes lots of issues with aerodynamics limiting aircraft to only flying at speeds a certain amount below the [[speed of sound]]. ([[based engineering|note that as engineers it is our job to say "fuck you" to what science says we can do]])

We can also assume that speed of sound is constant according to [[International Standard Atmosphere|ISA]], atleast within the stratsophere (since temperature is constant {that's what is says in the notes but the internet dosn't agree?}).

#### Applying this to range equation
We basically just combine:
![[Breguet range equation (jets)#^20c05c]]

![[Mach number#^7ad944]]

$$\begin{align*}
  R &= \frac{1}{s} \frac{VL}{D} \ln\left(1+\frac{W_f}{W_s}\right) & V&=Ma\\
\therefore R &= \frac{}{s} \frac{(aM)L}{D} \ln\left(1+\frac{W_f}{W_s}\right)
\end{align*}$$

For current generation jets the maximum mach number we can reach is about 0.82 before shock waves start screwing with our aerodynamics. So yeah, physics don't like us having nice things like free speed.