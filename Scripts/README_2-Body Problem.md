**Two-Body Problem Simulator Documentation**
=====================================================

**Overview**
------------

This code simulates the two-body problem in celestial mechanics using Python. The simulation plots the positions of two planets over time and animates their motion.

**Imported Libraries**
----------------------

*   `numpy` (as `np`) for numerical computations
*   `matplotlib.pyplot` (as `plt`) for plotting
*   `scipy.integrate.solve_ivp` for solving ordinary differential equations (ODEs)
*   `time` for timing the simulation

**Constants and Initial Conditions**
------------------------------------

The code defines several constants:

*   `M`: mass of the central body (Earth) in kg
*   `m1` and `m2`: masses of the two planets in kg
*   `G`: gravitational constant in m^3 kg^-1 s^-2

Initial conditions for the simulation are defined as follows:

*   `initial_r1` and `initial_r2`: initial positions of the two planets in 3D space (in meters)
*   `initial_v1` and `initial_v2`: initial velocities of the two planets in 3D space (in m/s)

**Simulation Function**
----------------------

The `system_odes` function defines the system of ODEs that governs the motion of the two planets:

*   `f1`, `f2`, `df1_dt`, and `df2_dt`: equations for the position and velocity of each planet

```python
def system_odes(t, N, m1, m2):
    r1, r2 = N[0:3], N[3:6]
    dr1_dt, dr2_dt = N[6:9], N[9:12]

    f1, f2 = dr1_dt, dr2_dt

    df1_dt = G*m2*(r2 - r1)/np.linalg.norm(r2 - r1)**3
    df2_dt = G*m1*(r1 - r2)/np.linalg.norm(r1 - r2)**3

    return np.array([f1, f2, df1_dt, df2_dt]).ravel()
```

**Simulation Setup**
--------------------

The code sets up the simulation as follows:

*   `ti` and `tf`: time interval for the simulation (in seconds)
*   `t_points`: array of time points at which to evaluate the solution
*   `solution`: solve_ivp object that solves the system of ODEs

```python
ti, tf = 0, 10
t_points = np.linspace(ti, tf, 2001)

initial = np.array([initial_r1, initial_r2, initial_v1, initial_v2]).ravel()

solution = solve_ivp(
    fun=system_odes,
    t_span=(ti, tf),
    y0=initial,
    t_eval=t_points,
    args=(m1, m2)
)
```

**Plotting the Simulation**
---------------------------

The code plots the simulation using matplotlib:

*   `fig` and `ax`: figure and axes objects
*   `planet1_plt`, `planet2_plt`, `planet1_dot`, and `planet2_dot`: plot objects for each planet

```python
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

planet1_plt, = ax.plot(p1x_sol, p1y_sol, p1z_sol, 'green', label='Planet 1', linewidth=1)
planet2_plt, = ax.plot(p2x_sol, p2y_sol, p2z_sol, 'red', label='Planet 2', linewidth=1)
```

**Animation**
-------------

The code animates the simulation using matplotlib's animation module:

*   `update` function: update function for each frame of the animation
*   `FuncAnimation` object: animation object that updates the plot at regular intervals

```python
def update(frame):
    lower_lim = max(0, frame - 300)
    print(f"Progress: {(frame+1)/len(t_points):.1%} | 100.0 %", end='\r')

    # ...

animation = FuncAnimation(fig, update, frames=range(0, len(t_points), 2), interval=10, blit=True)
plt.show()
```

**Notes**
---------

*   The animation is created by updating the plot at regular intervals using the `update` function.
*   The simulation can be sped up or slowed down by adjusting the value of `interval`.
*   The animation can be saved to a file using matplotlib's animation module.