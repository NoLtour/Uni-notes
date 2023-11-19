
![[Pasted image 20231118140415.png]]

#### Given in robot local axis

$$\begin{align*}
R &= 
\end{align*}$$


$$\begin{align*}
R=\begin{pmatrix} 
x_{t} \\ y_{t} \\ \alpha_{t}
 \end{pmatrix}
\end{align*}$$


$$\begin{align*}
E&= R-C =\begin{pmatrix} x_{e} \\ y_{e} \\ \alpha_{e} \end{pmatrix}
\end{align*}$$

$$\begin{align*}
G_{c} E &= U\\
\begin{pmatrix} \frac{2}{d} & 0 &\frac{2s}{d} \\ \frac{2}{d} & 0 & -\frac{2s}{d} \end{pmatrix} \begin{pmatrix} x_{e} \\ y_{e} \\ \alpha_{e} \end{pmatrix} &= \begin{pmatrix} 
\theta_{dl} \\ \theta_{dr}
 \end{pmatrix}
\end{align*}$$

$$\begin{align*}
C=\begin{pmatrix} 
x \\ y \\ \alpha
 \end{pmatrix}
\end{align*}$$

### Attempt 2

##### Local axis

$$\begin{align*}
\alpha(\theta_{R}, \theta_{L})  &= \frac{d}{4s}\left(\theta_{L}-\theta_{R}\right) & R(\theta_{R}, \theta_{L})  &= s\left(\frac{2 \theta_{L}}{\theta_{l}-\theta_{r}}-1\right) & 
\end{align*}$$

 $$\begin{align*}
X^{*}_{kL} &= F( u_{k} )\\
\begin{pmatrix} 
x \\ y \\ \alpha
 \end{pmatrix} &= \begin{pmatrix} 
 R \sin(\alpha) \\R\:(1-\cos\alpha) \\  \alpha
 \end{pmatrix} = \begin{pmatrix} 
 s\left(\frac{2 \theta_{L}}{\theta_{l}-\theta_{r}}-1\right) \sin\left(\frac{d}{4s}\left(\theta_{L}-\theta_{R}\right)\right) \\ s\left(\frac{2 \theta_{L}}{\theta_{l}-\theta_{r}}-1\right)\:\left(1-\cos\frac{d}{4s}\left(\theta_{L}-\theta_{R}\right)\right) \\ \frac{d}{4s}\left(\theta_{L}-\theta_{R}\right)
 \end{pmatrix} \\
\end{align*}$$

##### Global axis

 $$\begin{align*}
X^{*}_{kI} &= R_{B\to I} \:F( u_{k} )\\ 
\end{align*}$$

