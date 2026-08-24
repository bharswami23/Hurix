Consider a dynamic soaring scenario where a UAV is in a powerless downwind descent. The wind is linear, with wind shear $\beta$ along the positive x-axis. The coordinate system is left-handed.

Determine the eigenvalues governing the stability of the states $V$, $\gamma$, and $\psi$ using the following standard 3 DOF equations of motion in a wind-relative reference frame:

$$
\begin{aligned}
m\dot{V} &= T-D-mg\sin(\gamma)-m\dot{V}_w\cos(\gamma)\sin(\psi) \tag{1}\
mV\cos(\gamma)\dot{\psi} &= L\sin(\mu)-m\dot{V}_w\cos(\psi) \tag{2}\
mV\dot{\gamma} &= L\cos(\mu)-mg\cos(\gamma)+m\dot{V}_w\sin(\gamma)\sin(\psi) \tag{3}\
\dot{x} &= V\cos(\gamma)\sin(\psi)+V_w \tag{4}\
\dot{y} &= V\cos(\gamma)\cos(\psi) \tag{5}\
\dot{h} &= V\sin(\gamma). \tag{6}
\end{aligned}
$$

Also determine the three feedback coefficients that shift the real part of the most stable pole to $-1$ using only the lift coefficient. Changes in imaginary parts are not of interest. The control inputs are $C_L$, $\mu$, and Thrust.

Use fractional order $\alpha=0.95$ and Riemann-Liouville fractional derivatives for the linearization. Environment properties are in the first sheet of `workspace/data/Parameters.xlsx`; UAV properties are in the second sheet. Report results to 6 decimal places.

Create `/logs/agent/results.xlsx` with a table containing "Mode Number", "Real Part of Eigenvalue", and "Imaginary Part of Eigenvalue" in A1:C4. Below it, provide the three feedback coefficients under the heading "Feedback Matrix:" in A6:C7.
