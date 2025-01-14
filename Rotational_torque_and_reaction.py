#Calculates the angular acceleration that occurs in a rotating body
# when an axial torque is applied. A moment of inertia is set
# for the rotating body.
#The time and rotation angle of the rotating body are output.
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# パラメータの設定
radius = 0.035         # Radius of the rotating body [m]
mass = 0.050           # Mass of rotating body [kg]
torque = 5.5E-3        # Rotational Torque [Nm]
time_duration = 0.5    # simulation time [sec]
dt = 0.005             # time step [sec]

# 慣性モーメントの計算
#inertia = 0.5 * mass * radius**2  # I = 1/2 * m * r^2     =>  Inertia of the disk
inertia = 4.0/3.0 * mass * radius**2  # I = 4/3 * M * l^2  =>  Inertia of a rectangular solid

# 角加速度の計算
angular_acceleration = torque / inertia  # α = τ / I

# 時間配列の作成
time = np.arange(0, time_duration, dt)

# 角速度と角度の配列の初期化
angular_velocity = np.zeros(len(time))
angle = np.zeros(len(time))

# 初期条件
angular_velocity[0] = 0  # Initial angular velocity [rad/sec]
angle[0] = 0             # Initial angle [rad]

# 角度と角速度の計算
for i in range(1, len(time)):
    angular_velocity[i] = angular_velocity[i-1] + angular_acceleration * dt
    angle[i] = angle[i-1] + angular_velocity[i-1] * dt + 0.5 * angular_acceleration * dt**2

# グラフのプロット
plt.plot(time, angle, label='Angle (rad)')
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.title('Rotational Motion of a Cylinder with Applied Torque')
plt.legend()
plt.grid(True)

# CSVファイルに書き出すデータを作成
data = {
    't': time,
    'theta': angle
}

# CSVファイルにデータを書き出し
df = pd.DataFrame(data)
df.to_csv('torque_reaction.csv', index=False)

plt.show()
