#Using numerical analysis, the time and angle are calculated
# from the equation of motion of the pendulum. The fourth-order
# Runge-Kutta method is applied to the differential equation.
#
#Due to the nature of the pendulum, which is assumed to be
# an inverted pendulum, the initial angle is large, which can
# cause some problems with the accuracy of the numerical
# integration.
#
# Change the rtol and atol parameters of solve_ivp to values
# ​​about one order of magnitude smaller than the default values. 
#The calculation should be correct.
#
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(t, theta):
    g = 9.81
    L = 0.20   # Pendulum length [m]
    return -g / L * np.sin(theta)

def runge_kutta(theta0, omega0, t0, tf, h):
    t = np.arange(t0, tf, h)
    theta = np.zeros_like(t)
    omega = np.zeros_like(t)
    theta[0], omega[0] = theta0, omega0

# 4次ルンゲ・クッタ法の適用
    for i in range(1, len(t)):
        k1_theta = h * omega[i-1]
        k1_omega = h * f(t[i-1], theta[i-1])
        k2_theta = h * (omega[i-1] + k1_omega / 2)
        k2_omega = h * f(t[i-1] + h / 2, theta[i-1] + k1_theta / 2)
        k3_theta = h * (omega[i-1] + k2_omega / 2)
        k3_omega = h * f(t[i-1] + h / 2, theta[i-1] + k2_theta / 2)
        k4_theta = h * (omega[i-1] + k3_omega)
        k4_omega = h * f(t[i-1] + h, theta[i-1] + k3_theta)

        theta[i] = theta[i-1] + (k1_theta + 2 * k2_theta + 2 * k3_theta + k4_theta) / 6
        omega[i] = omega[i-1] + (k1_omega + 2 * k2_omega + 2 * k3_omega + k4_omega) / 6

    return t, theta, omega

theta0 = 3.1240  # initial angle [rad]
omega0 = 0.0     # Initial Angular Velocity [rad/sec]
t0 = 0.0         # start time
tf = 4.0         # end time
h = 0.005        # time step [sec]

t, theta, omega = runge_kutta(theta0, omega0, t0, tf, h)

plt.plot(t, theta)
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.title('Pendulum Angle Over Time')


# CSVファイルに書き出すデータを作成
data = {
    'time': t,
    'theta': theta,
    'omega': omega
}

# CSVファイルにデータを書き出し
df = pd.DataFrame(data)
df.to_csv('time_theta_omega.csv', index=False)

plt.show()