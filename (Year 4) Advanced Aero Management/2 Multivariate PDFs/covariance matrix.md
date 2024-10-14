---
aliases:
  - covariance matricies
tags:
---

## Covariance matrix

A covariance matrix is a square matrix that describes the relationships between multiple variables in a dataset. Each entry in the matrix represents the covariance between two variables:

- The diagonal entries (e.g., $\Sigma_{11}, \Sigma_{22}$) are the variances of the individual variables. Variance measures how much each variable varies from its mean.
- The off-diagonal entries (e.g., $\Sigma_{12}, \Sigma_{21}$) are the covariances between pairs of variables. Covariance indicates the direction of the linear relationship between two variables:
- A positive value means the variables tend to increase together.
- A negative value means one variable tends to increase when the other decreases.
- A zero covariance suggests no linear relationship.

The covariance matrix is symmetric, meaning $\Sigma_{ij} = \Sigma_{ji}$, and it plays a critical role in [[multivariate models|multivariate]] statistics, such as in the multivariate normal distribution, where it captures the structure of relationships between variables.
