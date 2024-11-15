---
aliases: 
tags:
  - NotesPage
---

# Uncertainty in management Overview

#### Intro

##### Component Uncertainty

So far we've been considering quite tangible sources of uncertainty, that can be (relatively) easily expressed as [[probability density function|PDFs]]. We will now look into more abstract sources of uncertainty that exist when you're working with hundreds (or thousands) of individuals on trying to design some complex machine. 

We can start with a relatively "simple" component, a single turbine blade:
![[Pasted image 20241113154214.png|60]]
This single component is already far too complex for a single person to design, we'll need a team of engineers, each covering area's like: geometry, aerodynamics, heat transfer, structural strength, manufacturing. 
So then, with it being too complex for one person, multiple people are required. Now the question is are each of these topics independent? Obviously, they aren't. This is a single component, optimizing for rigidity will effect mass, heat transfer and manufacturing. Same goes for each of the other area's of interest.

![[Pasted image 20241113154558.png|370]]

So if your designing your section of this part concurrently with the others, you need to know what the properties they've got are. For instance the aero guy needs to know how much the blade can flex, of course the structures guy won't know that until the aero guy's got calculations and the heat guy knows the max temp... so beyond communication on parameters introducing uncertainty, the values themselves are very uncertain. 

##### Assembly Uncertainty

Still, for a single blade you could get everyone in a room to talk things out. Now what about the entire jet engine? Or even the entire aircraft? The same basic problem is there, except obviously increased by a few orders of magnitude. Especially if rather than having one company design it, you've got a few hundred distributed across the entire world, which is common for rockets and aircraft.

To make it manageable, we are then forced to break the assembly down into sub-systems and sub-sub-systems ect ect. Then embark on the task of trying to ensure they all integrate nicely...

##### The problem
In summary, any complex system cannot be designed by a single person, but that introduces problems:
- Complex systems are highly coupled
- Communication of coupled information introduces uncertainty in itself
- The optimal designs of subsystems often conflict on a system level

We need to quantify and manage all this uncertainty!

#### Contents

- [[implementing design decomposition]]
- [[MDAO-like frameworks]]
- [[collaborative design methods]]


## Expanded articles

![[implementing design decomposition]]
![[MDAO-like frameworks]]
![[collaborative design methods]]
