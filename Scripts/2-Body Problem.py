import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import time

M = 5.9722*(10**24)
m1 = 2
m2 = 1
G = 1

initial_r1 = [0,0,0]
initial_r2 = [1,1,1]

initial_v1 = [0,0,0]
initial_v2 = [1,1,0]

initial = np.array([initial_r1, initial_r2, initial_v1, initial_v2]).ravel()

def system_odes(t, N, m1, m2):
    r1, r2 = N[0:3], N[3:6]
    dr1_dt, dr2_dt = N[6:9], N[9:12]
    
    f1, f2 = dr1_dt, dr2_dt

    df1_dt = G*m2*(r2 - r1)/np.linalg.norm(r2 - r1)**3
    df2_dt = G*m1*(r1 - r2)/np.linalg.norm(r1 - r2)**3

    return np.array([f1, f2, df1_dt, df2_dt]).ravel()

ti, tf = 0, 10
t_points = np.linspace(ti, tf, 2001)
t1 = time.time()
solution = solve_ivp(
    fun=system_odes,
    t_span=(ti, tf),
    y0=initial,
    t_eval=t_points,
    args=(m1, m2)
)

t_sol = solution.t
p1x_sol = solution.y[0]
p1y_sol = solution.y[1]
p1z_sol = solution.y[2]

p2x_sol = solution.y[3]
p2y_sol = solution.y[4]
p2z_sol = solution.y[5]

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

planet1_plt, = ax.plot(p1x_sol, p1y_sol, p1z_sol, 'green', label='Planet 1', linewidth=1)
planet2_plt, = ax.plot(p2x_sol, p2y_sol, p2z_sol, 'red', label='Planet 2', linewidth=1)
planet1_dot, = ax.plot([p1x_sol[-1]], [p1y_sol[-1]], [p1z_sol[-1]], 'o', color='green', markersize=6)
planet2_dot, = ax.plot([p2x_sol[-1]], [p2y_sol[-1]], [p2z_sol[-1]], 'o', color='red', markersize=6)

ax.set_title("The 2-Body Problem")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.grid()
plt.legend()

from matplotlib.animation import FuncAnimation

# -------  Animating the solutions ------- #

def update(frame):
    lower_lim = max(0, frame - 300)
    print(f"Progress: {(frame+1)/len(t_points):.1%} | 100.0 %", end='\r')

    x_current_1 = p1x_sol[lower_lim:frame+1]
    y_current_1 = p1y_sol[lower_lim:frame+1]
    z_current_1 = p1z_sol[lower_lim:frame+1]

    x_current_2 = p2x_sol[lower_lim:frame+1]
    y_current_2 = p2y_sol[lower_lim:frame+1]
    z_current_2 = p2z_sol[lower_lim:frame+1]

    planet1_plt.set_data(x_current_1, y_current_1)  
    planet1_plt.set_3d_properties(z_current_1)

    planet1_dot.set_data([x_current_1[-1]], [y_current_1[-1]])
    planet1_dot.set_3d_properties([z_current_1[-1]])



    planet2_plt.set_data(x_current_2, y_current_2)  
    planet2_plt.set_3d_properties(z_current_2)

    planet2_dot.set_data([x_current_2[-1]], [y_current_2[-1]])
    planet2_dot.set_3d_properties([z_current_2[-1]])

    return planet1_plt, planet1_dot, planet2_plt, planet2_dot
animation = FuncAnimation(fig, update, frames=range(0, len(t_points), 2), interval=10, blit=True)
plt.show()