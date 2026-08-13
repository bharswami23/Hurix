The problem is solved by first starting with the 3-DOF equations of motion of the point mass model of the UAV. The state vector is $\\textbf{x} = \[V\\ \\gamma\\ \\psi]$ and the control inputs are $\[C\_L\\ \\mu\\ Thrust]$. Since the flight is steady, $\\dot{\\textbf{x}} = 0$, that is the rates $\\dot{V},\\dot{gamma},\\dot{psi}$ are zero. Since the azimuth is $\\frac{\\pi}{2}$ and $\\dot{\\psi}=0$, we get the bank angle as $0$. This is because $\\cos{\\psi} = 0$ leading naturally to bank angle $\\mu = 0$. We now solve $\\dot{V}=0, \\dot{\\gamma}=0$ for $V, \\gamma$ numerically, either using tools like Mathematica or using the Newton-Raphson scheme. For obtaining the bank and the flight path angle, we impose the restriction in the solver that they lie between $\\frac{-\\pi}{2}$ and $\\frac{\\pi}{2}$. We also ensure that $V > 0$ while solving for the airspeed.

We now linearize the governing equations w.r.t. $V, \\gamma, \\psi$. Some of the fractional derivative rules followed during linearization are $$d^{\\alpha}\\cos{\\psi}/d{\\psi}^{\\alpha} = \\cos\\left({\\psi+\\alpha\\frac{\\pi}{2}}\\right)$$. Also $$d^{\\alpha}V/dV^{\\alpha} = \\frac{V^{1-\\alpha}}{\\Gamma(2-\\alpha)}$$. The linearize equation has the form $$\\delta \\dot{\\textbf{x}} = A\\delta \\textbf{x} + B\\delta \\textbf{u}$$. The state-matrix for this system at the specified fractional order is:
$$
\\left(
\\begin{array}{ccc}
\\frac{\\rho  S V^{2.} \\left(-0.978302 \\text{cd0}-0.978302 \\text{cd1} \\text{CL}-0.978302 \\text{cd2} \\text{CL}^2\\right)+\\sin (\\gamma ) \\left(-0.0513608 g m-1.02722 \\beta  m V^{1.} \\cos (\\gamma ) \\sin (\\psi )\\right)+0.0513608 T}{m V^{0.95}} \& \\frac{-1.71208 \\gamma ^{1.} g m , \_1\\tilde{F}\_2\\left(1;0.525,1.025;-\\frac{\\gamma ^2}{4}\\right)+1.25173 \\beta  \\gamma ^{3.} m V \\sin (\\psi ) , \_1F\_2\\left(2;2.525,2.025;-\\gamma ^2\\right)-1.02722 \\beta  \\gamma ^{1.} m V \\sin (\\psi ) , \_1F\_2\\left(1;1.525,1.025;-\\gamma ^2\\right)-0.0256804 \\text{cd0} \\rho  S V^2-0.0256804 \\text{cd1} \\text{CL} \\rho  S V^2-0.0256804 \\text{cd2} \\text{CL}^2 \\rho  S V^2+0.0513608 T}{\\gamma ^{0.95} m} \& \\frac{-1.71208 \\beta  m V \\psi ^{1.} \\sin (\\gamma ) \\cos (\\gamma ) , \_1\\tilde{F}\_2\\left(1;0.525,1.025;-\\frac{\\psi ^2}{4}\\right)-0.0256804 \\text{cd0} \\rho  S V^2-0.0256804 \\text{cd1} \\text{CL} \\rho  S V^2-0.0256804 \\text{cd2} \\text{CL}^2 \\rho  S V^2-0.0513608 g m \\sin (\\gamma )+0.0513608 T}{m \\psi ^{0.95}} \\
\\frac{0.513608 \\text{CL} \\rho  S V^{0.05} \\cos (\\mu )}{m}+\\frac{0.0487928 g \\cos (\\gamma ) (\\log (V)+18.868)}{V^{1.95}}+\\frac{0.0513608 \\beta  \\sin ^2(\\gamma ) \\sin (\\psi )}{V^{0.95}} \& -\\frac{3.42416 g , \_1\\tilde{F}\_2\\left(1;0.025,0.525;-\\frac{\\gamma ^2}{4}\\right)}{\\gamma ^{0.95} V}+\\beta  \\sin (\\psi ) \\left(1.9566 \\gamma ^{1.05} , \_1F\_2\\left(1;2.025,1.525;-\\gamma ^2\\right)-0.618136 \\gamma ^{3.05} , \_1F\_2\\left(2;3.025,2.525;-\\gamma ^2\\right)\\right)+\\frac{0.0256804 \\text{CL} \\rho  S V \\cos (\\mu )}{\\gamma ^{0.95} m} \& 1.71208 \\beta  \\psi ^{0.05} \\sin ^2(\\gamma ) , \_1\\tilde{F}\_2\\left(1;0.525,1.025;-\\frac{\\psi ^2}{4}\\right)+\\frac{\\frac{0.0256804 \\text{CL} \\rho  S V^2 \\cos (\\mu )}{m}-0.0513608 g \\cos (\\gamma )}{V \\psi ^{0.95}} \\
\\frac{0.513608 \\text{CL} \\rho  S V \\sec (\\gamma ) \\sin (\\mu )-0.0513608 \\beta  m \\tan (\\gamma ) \\cos (\\psi )}{m V^{0.95}} \& \\text{FractionalD}\\left\[\\frac{\\sec (\\gamma ) \\left(\\frac{1}{2} \\text{CL} \\rho  S V^2 \\sin (\\mu )-\\beta  m V \\sin (\\gamma ) \\cos (\\psi )\\right)}{m V},{\\gamma ,0.95}\\right] \& \\frac{0.0256804 \\text{CL} \\rho  S V \\sec (\\gamma ) \\sin (\\mu )-3.42416 \\beta  m \\tan (\\gamma ) , \_1\\tilde{F}\_2\\left(1;0.025,0.525;-\\frac{\\psi ^2}{4}\\right)}{m \\psi ^{0.95}} \\
\\end{array}
\\right)
$$
This gives the state matrix of the system after substituting the obtained values for $V, \\gamma, \\mu$ and other known states, control inputs, environmental and UAV property parameters at the steady conditions. The properties of interest are $Mass (m)=4.5\\ kg, Surface Area (S)=0.5\\ m^2,\\ C\_D = 0.0173-0.0337C\_L + 0.0517C\_L^2$ with $Thrust = 0, C\_L=0.3, azimuth (\\psi) = \\frac{\\pi}{2}$. The environmental conditions are density of air $(\\rho) = 1.2256\\ kg/m^3$, acceleration due to gravity $(g)=9.81\\ m/s^2$, wind-shear $(\\beta) = 0.1\\ s^{-1}$.

$$
\\left(
\\begin{array}{ccc}
-0.035602209121751007825 \& -9.7342872423965225437-1.5417596368452479716 i \& 0.0024582910073010035869 \\
0.050024086172989631893 \& -0.016552863436823606058-0.002621716011209765385 i \& 3.6208132674169198612196\\times 10^{-6} \\
0 \& 0 \& -0.0031902377249472041107 \\
\\end{array}
\\right)
$$

The eigenvalues of this 3x3 matrix can be obtained pretty easily since the third row has only one non-zero entry. Thus, one eigenvalue is obtained directly while the other two can be obtained as the roots of the quadratic equation. These 3 eigenvalues can be used to determine the stability of the flight in the mentioned scenario.

The control inputs are $C\_L, \\mu, Thrust$ and the feedback matrix is taken as $\[0\\ k1\\ 0]$. The control input matrix is:
$$
\\left(
\\begin{array}{ccc}
\\frac{\\rho  S V^2 \\left(-0.0256804 \\text{cd0}-0.513608 \\text{cd1} \\text{CL}^{1.}-0.978302 \\text{cd2} \\text{CL}^{2.}\\right)+\\sin (\\gamma ) (-0.0513608 g m-0.0513608 \\beta  m V \\cos (\\gamma ) \\sin (\\psi ))+0.0513608 T}{\\text{CL}^{0.95} m} \& 0 \& \\frac{\\rho  S V^2 \\left(-0.0256804 \\text{cd0}-0.0256804 \\text{cd1} \\text{CL}-0.0256804 \\text{cd2} \\text{CL}^2\\right)+\\sin (\\gamma ) (-0.0513608 g m-0.0513608 \\beta  m V \\cos (\\gamma ) \\sin (\\psi ))+1.02722 T}{m T^{0.95}} \\
\\frac{V \\left(0.513608 \\text{CL} \\rho  S V \\cos (\\mu )+0.0513608 \\beta  m \\sin ^2(\\gamma ) \\sin (\\psi )\\right)-0.0513608 g m \\cos (\\gamma )}{\\text{CL}^{0.95} m V} \& \\frac{1.71208 \\text{CL} \\rho  S V^2 , \_1\\tilde{F}\_2\\left(1;0.025,0.525;-\\frac{\\mu ^2}{4}\\right)-0.0513608 g m \\cos (\\gamma )+0.0513608 \\beta  m V \\sin ^2(\\gamma ) \\sin (\\psi )}{\\mu ^{0.95} m V} \& 0 \\
\\frac{0.513608 \\text{CL} \\rho  S V \\sec (\\gamma ) \\sin (\\mu )-0.0513608 \\beta  m \\tan (\\gamma ) \\cos (\\psi )}{\\text{CL}^{0.95} m} \& \\frac{0.856039 \\text{CL} \\mu ^{0.05} \\rho  S V \\sec (\\gamma ) , \_1\\tilde{F}\_2\\left(1;0.525,1.025;-\\frac{\\mu ^2}{4}\\right)}{m}-\\frac{0.0513608 \\beta  \\tan (\\gamma ) \\cos (\\psi )}{\\mu ^{0.95}} \& 0 \\
\\end{array}
\\right)
$$

Substituting the flight parameters, environmental conditions, states and control inputs, we get the control-input matrix corresponding to the lift coefficient as:
$$
\\left(
\\begin{array}{c}0.10263780161384122858\\1.3705357535787954237\\0\\end{array}\\right)
$$

Now we need to find the feedback matrix $\\textbf{K} = \[0\\ k\_1\\ 0]$. The closed loop matrix is $A\_{cl} = A-BK$.
Using numerical solver in a tool like Mathematica, the value $k\_1$ that shifts the real part of the most stable mode to $-1$ can be determined. The imaginary parts of the eigenvalues aren't considered while determining $k\_1$. It can be verified that $eig(A-BK)$ has the desired eigenvalues. We can perform the shift with only the $C\_L$ control input since other terms in the control input matrix are either zero or have complex-infinity values. The resulting eigenvalues and the feedback matrix are printed and presented in a xlsx file.

