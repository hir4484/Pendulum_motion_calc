#This calculates the position of a falling inverted pendulum when translational
# acceleration is applied to it. The translational acceleration is applied to the
# support point of the inverted pendulum.
#It can also handle cases where a wheel is attached to the support point
# and the reaction force of the axle is taken into account.
#
#The time and the coordinates of the pendulum's center of gravity are output.
#
#Due to the nature of the pendulum, which is assumed to be
# an inverted pendulum, the initial angle is large, which can
# cause some problems with the accuracy of the numerical
# integration.
# Change the rtol and atol parameters of solve_ivp to values
# ​​about one order of magnitude smaller than the default values. 
#The calculation should be correct.
#
#


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import pandas as pd

# Parameters
L = 0.2     # Length of the pendulum (m) 20cm, 5cm
m = 0.4     # Mass of the pendulum (kg)
mw = 0.03   # mass of the wheel (kg)
g = 9.81    # Gravitational acceleration (m/s^2)
a = 0.17    # Horizontal acceleration of the support point (m/s^2)
#a = -9.81*np.tan(3.1240)   # Acceleration to prevent falling
#a = -9.81*np.sin(3.1240) / ( np.cos(3.1240) - 3*mw / (8*m))   #  When reaction is included


# Initial conditions
theta0 = 3.1240  # Initial angle [rad]
omega0 = 0.0     # Initial angular velocity [rad/sec]
x0_0 = 0.0       # Initial position of the support point
v0_0 = 0.0       # Initial velocity of the support point (m/s)

# Time span
t_span = (0, 1.5)  # Simulate for 10 seconds / 2000 points = 5ms間隔
t_eval = np.linspace(t_span[0], t_span[1], 1500)  # Time points to evaluate

# Equations of motion
def equations_of_motion(t, y):
    theta, omega, x0, v0 = y
    dtheta_dt = omega
    domega_dt = (-g / L) * np.sin(theta) - (a / L) * np.cos(theta)
    #domega_dt = (-g / L) * np.sin(theta)  - (a / L) * np.cos(theta) + 3*mw*a/(8*m*L)
    dx0_dt = v0
    dv0_dt = a  # Constant acceleration for the support point
    return [dtheta_dt, domega_dt, dx0_dt, dv0_dt]

# Initial state vector
y0 = [theta0, omega0, x0_0, v0_0]

# Solve the differential equations
sol = solve_ivp(equations_of_motion, t_span, y0, t_eval=t_eval)

# Extract solutions
theta_sol = sol.y[0]
x0_sol = sol.y[2]

# Calculate the position of the pendulum's center of mass
x_G = x0_sol + L * np.sin(theta_sol)
y_G = -L * np.cos(theta_sol)

# Plot the results
plt.figure(figsize=(10, 5))
#plt.plot(sol.t, x_G, label='x_G (Horizontal Position)')
#plt.plot(sol.t, y_G, label='y_G (Vertical Position)')
plt.plot(x_G, y_G, label='xy_G (H, V Position)')
#plt.xlabel('Time (s)')
plt.xlabel('X_Position (m)')
plt.ylabel('Y_Position (m)')
plt.title('Pendulum Motion with Accelerating Support Point')
plt.legend()
plt.grid()

# CSVファイルに書き出すデータを作成
data = {
    'time': sol.t,
    'x_G': x_G,
    'y_G': y_G
}

# CSVファイルにデータを書き出し
df = pd.DataFrame(data)
df.to_csv('pendulum_motion_accel.csv', index=False)

plt.text(0.03, 0.2, a, fontsize=12, color='red')

plt.show()