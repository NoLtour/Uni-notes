---
aliases: ["truss deformation"]
tags: ["Question","QFormat3"]
---

#### How do you go about
## Calculating truss deformation
The extention of the [[truss]] can be calculated using [[Youngs modulus]] subbing in equations of [[Stress]] and [[Strain]].

![[Pasted image 20211022232807.png]]

> $$ \Delta L = \frac{L_0}{EA}F  $$ 
>> where:
>> $\Delta L=$ extention
>> $L_0=$ origional length
>> $E=$ extention
>> $A=$ cross sectional area
>> $F=$ force
> also note that $\frac{L_0}{EA} \approx constant$


This is for a [[pin jointed trusses|pin jointed truss]], so there are some primary assumptions we work on:
- Bars extend/contract axially
- Bars are free to rotate around pin joints
- Bars always remain attacked to each other at the joints

It's best to use an example, consider:

![[Pasted image 20211022230534.png]]

![[Pasted image 20211022233652.png]]

If we exagerate the movments:
![[Pasted image 20211022233751.png]]

But in reality, since the extentions are so small you can just accuratly approximate the movement with:
![[Pasted image 20211022234028.png]]

