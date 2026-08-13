\## Task Background



Working directory: `/workspace`



Only access:



\* `/workspace`

\* `/logs`



Consider a dynamic soaring scenario where a UAV is in a powerless downwind descent. There is linear wind, with wind shear $\\beta$, along the positive direction of the x-axis. The coordinate system used is a left-handed coordinate system.



It is desired to know the eigenvalues of this system to determine the nature of stability. Use the standard 3 DOF equations of motion for a point-mass object in a wind-relative reference frame given below:
$$

m\\dot{V}\&=T - D - mg\\sin{(\\gamma)} - 

m\\dot{V\_w}\\cos{(\\gamma)}\\sin{(\\psi)}\\tag{1}\\\\mV\\cos{(\\gamma)}\\dot{\\psi}\&=L\\sin{(\\mu)}-m\\dot{V\_w}\\cos{(\\psi)}\\tag{2}\\\\mV\\dot{\\gamma} 

\&= L\\cos{(\\mu)} - mg\\cos{(\\gamma)} + 

m\\dot{V\_w}\\sin{(\\gamma)}\\sin{(\\psi)}\\tag{3}\\\\\\dot{x} \&= 

V\\cos{(\\gamma)}\\sin{(\\psi)} + V\_w\\tag{4}\\\\\\dot{y} \&= 

V\\cos{(\\gamma)}\\cos{(\\psi)}\\tag{5}\\\\\\dot{h} \&= V\\sin{(\\gamma)}\\tag{6}

$$
Also find the 1x3 feedback matrix that will shift the real part of the most stable pole to $-1$ using only the lift coefficient. The change in the imaginary parts are not of interest. The eigenvalues of interest only correspond to the states $V,\\gamma,\\psi$. The control inputs are $C\_L, \\mu, Thrust$.



The linearization of the equations for determining the eigenvalues is done w.r.t. the fractional order $\\alpha=0.95$. The Riemann-Liouville fractional derivatives are taken for linearization. The environment properties are given in the first sheet of the excel file workspace/data/Parameters.xlsx while the UAV properties are given in the second sheet of the same excel file. Report your answers correct to $6$ decimal places.



You must create the output xlsx file, `/logs/agent/results.xlsx`, with a table listing the "Mode Number" and the "Eigenvalues" of the closed loop system corresponding to that mode spanning cells A1 to C4. Below the table, give the $1x3$ feedback matrix with the heading "Feedback Matrix:" spanning cells A6 to C7.

