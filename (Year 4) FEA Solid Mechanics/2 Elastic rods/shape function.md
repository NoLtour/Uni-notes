---
aliases:
  - interpolation function
tags:
---

## Shape function

### Description

Displacement (or interpolation) functions are key to the displacement-based finite element method (FEM), as they define how displacements vary within each element. This variation also determines the strains and stresses. FEM divides a complex structure into simpler elements, each with a straightforward displacement assumption, so that the combined element responses approximate the entire structure's behavior.

Shape functions, typically polynomials (linear or quadratic), describe these displacements. These assumptions allow FEM to solve equilibrium equations at discrete points, transforming a continuous system into a manageable numerical model.

### Utility

The neat thing about shape functions is they provide continuity between nodes in out FEA analysis, if we chained loads of nodes together it'd end up looking something like:

![[Pasted image 20241028093416.png]]

Rather than without the shape function, where we'd only have discrete samples!
