---
aliases: [""]
tags: []
---

## Numerical method for determining circulation distribution
### Intro
Ok so lets say you've got some known wing geometry and want to work out the lift/circulation distribution, a numerical method for this exists.

Essentially it involves:
1) Calculate the induced AOA along the wing caused by the current circulation distribution.
2) Calculate the 2D lift coefficient along the entire wing using the calculated induced AOA.
3) Calculate what circulation is needed at every point along the wing to achieve that lift distribution.
4) Sub the new circulation distribution back into (1) and keep repeating till the circulation converges.

This method has a clear issue though, we need some initial circulation distribution to start the convergence process... here we can just initially use an elliptical circulation distribution.

### More detailed steps

#### 0 Generate initial data

Look at [[elliptic lift distrobution analysis]], take the equation used there:
$$\begin{align*}
\Gamma &= \Gamma_{0} \sqrt{ 1- \left(\frac{2y}{b}\right)^{2} }
\end{align*}$$
[[I hope your ears are bleeding|Boom]] here is your initial data, easy as.


#### 1 Calculate induced AOA
Since we need to integrate numerically we'll need to break the wing into discrete sections so that we can integrate between them:
![[Pasted image 20221222231107.png]]

More sections means higher accuracy at the cost of computing time, integration can be done by just treating sections as squares, treating sections as trapeziums or applying Simpsons rule (any valid method for numerical integration is applicable). Of course more accurate numerical integration methods produce better results at lower section resolution. With that out the way back to induced AOA.

We've got an equation for induced angle of  attack from [[Prandtls lifting line theory#Induced AoA|induced AoA for a finite wing]]:
$$\begin{align*}
 \alpha_{i}(y_{0}) &=    \frac{1}{4\pi V_{\infty}} \int^{\frac{b}{2}}_{- \frac{b}{2}} \frac{ \frac{d\Gamma}{dy}  }{ y_{0} - y} dy
\end{align*}$$
Here we will be integrating for each section so will have to solve the equation above for each position along the wing $y_{1}\to y_{k+1}$ and the integration itself will use rectangles (due to lazyness). So the resulting equation to be applied at each section along the span is:
$$\begin{align*}
\alpha_{i}(y_{n}) &=  \frac{1}{4\pi V_{\infty}} \sum\limits^{k}_{j=2} \frac{ \left(\frac{d\Gamma}{dy}\right)_{j}  }{ y_{n} - y_{j}} \times (\Delta y)
\end{align*}$$

Since we're slacking and using rectangles (a very inaccurate integration method) we'll need to use a very high value of $k$ to compensate. Either way after applying this for each section along the span we've got a complete set of induced AOA.
Note that the equation listed above doesn't produce induced AOA values for $\alpha_{i}(y_{1})$ and $\alpha_{i}(y_{k+1})$ so some approximation will need to be used at the boundary, here because we're already assuming a high sample count we can just use $\alpha_{i}(y_{1})=\alpha_{i}(y_{2})$ and $\alpha_{i}(y_{k+1})=\alpha_{i}(y_{k})$. This will obviously lead to errors on the boundary but with the sample count this high it really should be insignificant.

#### 2 Calculate induced AOA
Once again using an equation from earlier to get the $C_{l}$ along the wing:
$$\begin{align*}
C_{l}(y_{n}) &= a_{0}(y_{n})[\: \alpha(y_{n}) - \alpha_{i}(y_{n}) - \alpha_{L=0}(y_{n}) \:]
\end{align*}$$

Since we know the wing geometry and now have a complete set of $\alpha_{i}$'s we can just sub into this equation to get the $C_{l}$ at any point along the wing... so do that.

#### 3 Calculate the circulation

Ok now comes the back calculation, we can use [[Kutta-Joukowski Theorem]] to figure out what circulation distribution would be required to get the $C_{l}$ distribution:
$$\begin{align*}
L' &= \rho_{\infty} V_{\infty} \Gamma\\
C_{l} \frac{1}{2} \rho_{\infty} V_{\infty}^{2} c &= \\
\frac{1}{2} C_{l} V_{\infty}c &= \Gamma
\end{align*}$$

Keep in mind that chord length may vary with span depending on chosen wing geometry, thus:
$$\begin{align*}
\Gamma(y_{n}) &= \frac{1}{2}V_\infty\: C_{l}(y_{n})\:c(y_{n})
\end{align*}$$

Subbing into that equation then gets us a new circulation distribution!

#### 4 Sub backwards
It's just as was said, now sub the new circulation distribution back into step 1 and keep repeating till the result converges. You may be thinking "but how does this achieve anything?" well since we are using the defined geometry values for the foil along the entire span then solving the equations the outputs reflect the geometry by subbing back it converges and eventually is a realistic distribution (at least good enough to get some approximate numbers).
Generally you'll end up with this sort of thing:
![[Pasted image 20221222234541.png]]
