---
aliases: ["Mach disk","under-expanded","under-expanded nozzle","over-expanded","over-expanded nozzle"]
tags: []
---

## Over and under expanded nozzles
### Intro to over expanded nozzles
![[Pasted image 20231027191029.png]]

![[types of nozzle expansion state#6 Over expanded exhaust]]

### Shocks

![[Pasted image 20231027200948.png]]

We really did go from [[quite literal when dealing with supersonic shite|0 to 100 in like a millisecond]]. Anyway, this isn't so bad, it just needs to approached one stage at a time.

#### Stages
##### 1 Compression

In the first section, the exit pressure is sub atmospheric by definition of an [[over and under  expanded nozzles]]. Hence for pressure equalisation a compressive shock must occur, this takes the form of:
- [[oblique shocks|Oblique shocks]] - This shock forms such that the resulting pressure is equal to the atmospheric pressure across the [[Mach reflection|slip line]], it should be noted that the flow will still be supersonic across this shock. This then proceeds into another [[oblique shocks|oblique shock]] further increasing the pressure.
- [[normal shock properties equations|A normal shock]] - The streamlines through the "Mach disk" suggest that the angle allows for [[oblique shocks|oblique shock]] formation (it's in the bounds of the [[oblique shock chart]]), which means the normal shock formation is caused due to pressure. To reach a pressure as high as the double oblique shocks in the surrounding streamlines a normal shock is required. This also means the flow directly after the [[over and under  expanded nozzles|Mach disk]] is subsonic.

##### 2 Acceleration

What occurs next is really fucky, look at the streamlines. They actually form a [[converging diverging nozzles|converging diverging nozzle]], this causes the flow in the centre to potential reach the supersonic domain again. So once the flow starts expanding again it's supersonic but now higher than ambient pressure. 

##### 3 Expansion

Now the flow continues to expand, so expansion mechanisms take place, specifically [[Prandtl–Meyer expansion fan|expansion fans]]. The fans form such that the [[Mach reflection|slip line]] (free jet boundary) matches atmospheric pressure. This essentially creates a diverging nozzle, accelerating the flow.

Then [[compression fans]] coalesce into a [[oblique shocks|oblique shock]] due to the pressure dropping too much. This causes #1 to repeat.

##### 4 The shock revolution and it's consequences

Every shock increases entropy, so the flow will have less useful energy through each shock diamond. This couples with other chaotic mechanisms (flow mixing and various reflected boundaries) till they fizzle out into the environment:

![[Pasted image 20231027210107.png]]

#### Over-expanded without the Mach disk

The problem greatly simplifies in the event that no [[over and under  expanded nozzles|Mach disk]] forms:

![[Pasted image 20231027211721.png]]

Pretty similar since most of the underlying mechanisms are the same. Considering that what causes the Mach disk to form is:
- The high pressure converging flow creates a region of really high pressure
- The pressure is too high to be met by a oblique shock, so a normal shock forms

We can deduce that in the event where a Mach disk doesn't form, it's due to the pressure in the Mach diamond being low enough that it's unnecessary. 

![[Pasted image 20231028160219.png]]

ASK LECTURER

### Under expanded nozzle

![[underexpansion.jpg]]

Something you realise quite quickly, all the mechanisms at play are identical to a [[over and under  expanded nozzles|over-expanded nozzle]], but the difference is the start point. For under expanded nozzles it's starting from an over-pressure state.

##### 1 Expansion

Now the flow continues to expand, so expansion mechanisms take place, specifically [[Prandtl–Meyer expansion fan|expansion fans]]. The fans form such that the [[Mach reflection|slip line]] (free jet boundary) matches atmospheric pressure. This essentially creates a diverging nozzle, accelerating the flow.

Then [[compression fans]] coalesce into a [[oblique shocks|oblique shock]] due to the pressure dropping too much. 

##### 2 Compression

The exit pressure is sub atmospheric. Hence for pressure equalisation a compressive shock must occur, this takes the form of:
- [[oblique shocks|Oblique shocks]] - This shock forms such that the resulting pressure is equal to the atmospheric pressure across the [[Mach reflection|slip line]], it should be noted that the flow will still be supersonic across this shock. This then proceeds into another [[oblique shocks|oblique shock]] further increasing the pressure.
- [[normal shock properties equations|A normal shock]] - The streamlines through the "Mach disk" suggest that the angle allows for [[oblique shocks|oblique shock]] formation (it's in the bounds of the [[oblique shock chart]]), which means the normal shock formation is caused due to pressure. To reach a pressure as high as the double oblique shocks in the surrounding streamlines a normal shock is required. This also means the flow directly after the [[over and under  expanded nozzles|Mach disk]] is subsonic.


##### 3 Acceleration

What occurs next is really fucky, look at the streamlines. They actually form a [[converging diverging nozzles|converging diverging nozzle]], this causes the flow in the centre to potential reach the supersonic domain again. So once the flow starts expanding again it's supersonic but now higher than ambient pressure. 

This causes #1 to repeat.