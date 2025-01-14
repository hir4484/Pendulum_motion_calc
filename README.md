This is the physics calculation source code for the pendulum animation posted
 in the YouTube video "Center of gravity and motion of a wheel-type inverted pendulum."
 
 https://www.youtube.com/watch?v=5-RCN_Ldh-A&t=328s
 
The physics calculation is done in Python, and the animation is done using Processing.

*********************************************************
Pendulum_motion.py

Using numerical analysis, the time and angle are calculated from the equation
 of motion of the pendulum. The fourth-order Runge-Kutta method is applied
 to the differential equation.


Rotational_torque_and_reaction.py

Calculates the angular acceleration that occurs in a rotating body when an axial
 torque is applied. A moment of inertia is set for the rotating body.
The time and rotation angle of the rotating body are output.


Pendulum_and_translational_motion_with-a.py

This calculates the position of a falling inverted pendulum when translational
 acceleration is applied to it. The translational acceleration is applied to the
 support point of the inverted pendulum.
It can also handle cases where a wheel is attached to the support point
 and the reaction force of the axle is taken into account.
The time and the coordinates of the pendulum's center of gravity are output.


*********************************************************
Due to the nature of the pendulum, which is assumed to be an inverted pendulum,
 the initial angle is large, which can cause some problems with the accuracy of the
 numerical integration.
Change the rtol and atol parameters of solve_ivp to values ​​about one order of
 magnitude smaller than the default values. The calculation should be correct.
