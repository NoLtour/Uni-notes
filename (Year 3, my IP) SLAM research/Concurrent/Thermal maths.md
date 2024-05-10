
Lunar radiation
$$\begin{align*}
q_{l} &= \frac{R_{l}^{2}}{R_{m}^{2}} ( q_{s} A + T_{l}^{4}  \varepsilon_{l} \sigma) \:\:\: (1)
\end{align*}$$


Initial modelling

$$\begin{align*}
Q_{in} &= q_{l} \alpha_{v} A_{lf} + q_{s} \alpha_{v} A_{sf} + Q_{dis} \:\:\: (2)
\end{align*}$$

WRONG, E_IR AND E_SOLAR ARE DIFFERENT, APPROXIMATION INVALID!!!!!!!!!

$$\begin{align*}
Q_{out} &= T^{4}_{v} \sigma \varepsilon_{v} A_{total} \:\:\: (3)
\end{align*}$$

$$\begin{align*}
Q_{heaters} &= Q_{out,cold} - Q_{in,cold} \:\:\:(4)
\end{align*}$$

---

Margins

$$\begin{align*}
T_{t,hot} &= T_{max} - 15 \degree K \:\:\:(5)
\end{align*}$$

$$\begin{align*}
T_{t,cold} &= T_{min} + 15 \degree K \:\:\:(6)
\end{align*}$$

Heat flux through MLI surfaces

$$\begin{align*}
q_{MLI}(T_{e}, \:T_{i}) &= h'(T_{e} - T_{i}) + \varepsilon' \sigma (T_{e}^{4} - T_{i}^{4} ) \:\:\:(7)
\end{align*}$$


$$\begin{align*}
A T_{e}^{4} \sigma \varepsilon_{is} &= A\alpha_{is} q_{s}  &&\to& T_{e}(q_{s}) &= \sqrt[4]{ \frac{\alpha_{is} q_{s}}{\sigma \varepsilon_{is}} } \:\:\:(8)
\end{align*}$$

$$\begin{align*}
Q_{ins} &= A_{li} \:q_{MLI}( T_{l}, \:T_{i} ) + A_{si} \:q_{MLI}( T_{s}, \:T_{i} ) + A_{oi} \:q_{MLI}( T_{v}, \:T_{i} ) \:\:\: (9)
\end{align*}$$

Heat flux through Lunar surfaces and solar surfaces

$$\begin{align*}
Q_{nat} &= Q_{dis}+ Q_{ins} + \sum\limits_{n} q_{n} \alpha_{n} A_{n} - \sum\limits_{n} T_{t}^{4} \sigma \varepsilon_{n} A_{n} \:\:\:(10)
\end{align*}$$

Radiator sizing

$$\begin{align*}
A_{rad} &= \frac{Q_{nat,hot}}{T_{t,hot}^{4} \sigma \varepsilon_{rad}  } \:\:\:(11)
\end{align*}$$

$$\begin{align*}
Q_{max\:heater} &= A_{rad} T^{4}_{t,cold} \sigma \varepsilon_{rad} - Q_{nat,cold} \:\:\:(12)
\end{align*}$$



Thermal mass

$$\begin{align*}
 dT &= \frac{dt}{mc_{p}} \left[ \left(\sum\limits_{n} Q_{in,n} \right)- T_{t}^{4}  \sigma \left(\sum\limits_{n} \varepsilon_{n} A_{n} \right) \right] \:\:\: (13)
\end{align*}$$

Panel sizing:

$$\begin{align*}
q_{s,mean}A_{c} (\alpha_{c} - \eta_{EOL}) &= T_{c}^{4}A_{c}\varepsilon_{c} \sigma + T_{c}^{4}A_{b}\varepsilon_{b} \sigma \:\:\:(?)
\end{align*}$$

$$\begin{align*}
\frac{q_{s,mean}A_{c} (\alpha_{c} - \eta_{EOL}) - T_{c}^{4}A_{c}\varepsilon_{c} \sigma}{T_{c}^{4} \varepsilon_{b} \sigma} &=   A_{b} \:\:\:(14)
\end{align*}$$
