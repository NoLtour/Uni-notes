---
aliases: ["Orthogonal grid","Curvilinear grid"]
tags: []
---

## O-grid and C-grid

O-grid (Orthogonal grid) and C-grid (Curvilinear grid) are two types of structured grids used in Computational Fluid Dynamics (CFD).

#### O grid
![[Pasted image 20231123182846.png]]

O-Grid (Orthogonal Grid):
- Consists of three sets of orthogonal grid lines.
- Grid lines meet at right angles.
- Suitable for simple geometries with straight boundaries.
- Easy to generate and computationally efficient.
- May have difficulties handling complex or curved geometries.


#### C grid

C-Grid (Curvilinear Grid):
- Grid lines follow the geometry's contours.
- Well-suited for complex and curved geometries.
- Offers more flexibility in capturing intricate shapes.
- More challenging to generate and computationally expensive.
- Can provide higher accuracy in regions with complex geometry.

![[Pasted image 20231123183021.png]]

##### Comparison

- O-Grid: Simple, efficient, but struggles with complex geometries.
- C-Grid: Complex, accurate for intricate shapes, but computationally demanding.
- Choice depends on the geometry: O-Grid for simpler shapes, C-Grid for complex and curved geometries.
- C-Grid tends to be more accurate at capturing wake