---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you model
## Deformation due to bending in beams
###  Introduction

First if we picture a beam: 
![[Pasted image 20211108090944.png]]
Then apply a bending moment to it:
![[Pasted image 20211108091021.png]]

You can get an intuitive feeling that it would compress towords the top and stretch towords the bottom, but as you can see the plane cross section remains strait.

### Assumptions

^4e4c28

Of course in reality everything has [[random idk|unexpected behaviour]], so for analysis we are going to work under some assumtions:
- The plane cross section remains a plane under loading conditions
- The beam is bent into a circular arc
- The radius of curviture of the circle is large compared to the thickness of the beam
- Tensile and compressive stresses act longitudionaly
- The beam is expressing linear elastic behaviour and has the same [[youngs modulus]] for both tension and compression

#### Explenation of what that means
This is what we mean by "modelling it as a circular arc", this is exagerated though. In reality we would model it as a much more gentle curve.
![[Pasted image 20211108091957.png]]

This is the origional beam segment that gets defomed in the image above.
![[Pasted image 20211108092144.png]]

As you can see the top gets compressed and the bottoms in tension, of course depending on the way the moments and [[shear stress]] is applied will change where it is under compression and tension.

### Strain
![[longitudinal strain in a beam]]

![[strains effects on cross section of a beam]]