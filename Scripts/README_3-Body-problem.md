**Documentation: 3-Body Problem Simulation**

**Introduction**

The 3-Body Problem is a fundamental problem in astrodynamics that describes the motion of three celestial bodies interacting with each other. This code simulates the 3-Body Problem using numerical integration and visualizes the trajectories of the three planets.

**Dependencies**

* NumPy (numpy)
* Matplotlib (matplotlib.pyplot)
* SciPy (scipy.integrate.solve_ivp)

**Variables**

| Variable | Description | Units |
| --- | --- | --- |
| `m1`, `m2`, `m3` | Masses of the three planets | kg |
| `initial_position_1`, `initial_position_2`, `initial_position_3` | Initial positions of the three planets | m |
| `initial_velocity_1`, `initial_velocity_2`, `initial_velocity_3` | Initial velocities of the three planets | m/s |
| `t_s`, `t_e` | Time span for the simulation | s |
| `t_points` | Time points for the numerical integration | s |
| `solution` | Solution of the 3-Body Problem | - |

**Functions**

### `system_odes`

* Description: Defines the system of ordinary differential equations (ODEs) describing the motion of the three planets.
* Parameters:
	+ `t`: Current time
	+ `S`: State vector containing positions and velocities of the three planets
	+ `m1`, `m2`, `m3`: Masses of the three planets

### `update`

* Description: Updates the plot at each frame of the animation.
* Parameters:
	+ `frame`: Current frame number
* Returns:
	+ Updated plot elements (planet positions and velocities)

**Code Structure**

The code consists of four main sections:

1. **Initialization**: Initializes the variables and parameters for the simulation.
2. **Numerical Integration**: Solves the 3-Body Problem using numerical integration.
3. **Visualization**: Visualizes the trajectories of the three planets in a 3D plot.
4. **Animation**: Animates the visualization by updating the plot at each frame.

**Example Use Cases**

* Run the simulation with different initial conditions to see how the motion of the three bodies changes.
* Modify the `interval` parameter in the `FuncAnimation` function to change the speed of the animation.

**Notes**

* The `solve_ivp` function from SciPy is used for numerical integration, which provides a robust and efficient method for solving systems of ODEs.
* The `FuncAnimation` function from Matplotlib is used to create an animated plot by updating the visualization at each frame.