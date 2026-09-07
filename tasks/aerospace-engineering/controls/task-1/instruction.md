Consider a dynamic soaring scenario where a UAV is in a powerless downwind descent. The wind is linear, with wind shear $\beta$ along the positive x-axis. The coordinate system is left-handed.

Determine the eigenvalues governing the stability of the states $V$, $\gamma$, and $\psi$ using the following standard 3 DOF equations of motion (Swaminathan, 2023) in a wind-relative reference frame:

$$
\begin{align}
m\dot{V} &= T-D-mg\sin(\gamma)-m\dot{V}_w\cos(\gamma)\sin(\psi) \
mV\cos(\gamma)\dot{\psi} &= L\sin(\mu)-m\dot{V}_w\cos(\psi) \
mV\dot{\gamma} &= L\cos(\mu)-mg\cos(\gamma)+m\dot{V}_w\sin(\gamma)\sin(\psi) \
\dot{x} &= V\cos(\gamma)\sin(\psi)+V_w \
\dot{y} &= V\cos(\gamma)\cos(\psi) \
\dot{h} &= V\sin(\gamma)\
\end{align}
$$

Also determine the three feedback coefficients that shift the real part of the most stable pole to $-1$ using only the lift coefficient. Changes in imaginary parts are not of interest. The control inputs are $C_L$, $\mu$, and Thrust.

Use fractional order $\alpha=0.95$ and Riemann-Liouville fractional derivatives (Podlubny, 1999) for the linearization. Environment properties are in the first sheet of `workspace/data/Parameters.xlsx`; UAV properties are in the second sheet. Report results to 6 decimal places.

Create `/logs/agent/results.xlsx` with a table containing "Mode Number", "Real Part of Eigenvalue", and "Imaginary Part of Eigenvalue" in A1:C4. Below it, provide the three feedback coefficients under the heading "Feedback Matrix:" in A6:C7.
