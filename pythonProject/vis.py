import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Constants
hbar = 1  # Set to 1 for simplicity in plotting
omega_x = 1.0
omega_y = 1.5
omega_z = 2.0
varepsilon = 2.0  # Energy value

# Tetrahedron vertices
vertices = np.array([
    [0, 0, 0],
    [varepsilon / hbar / omega_x, 0, 0],
    [0, varepsilon / hbar / omega_y, 0],
    [0, 0, varepsilon / hbar / omega_z]
])

# Define the faces of the tetrahedron by the indices of the vertices
faces = [
    [vertices[0], vertices[1], vertices[2]],
    [vertices[0], vertices[1], vertices[3]],
    [vertices[0], vertices[2], vertices[3]],
    [vertices[1], vertices[2], vertices[3]]
]

# Base area triangle vertices (highlighted separately)
base_vertices = np.array([
    [varepsilon / hbar / omega_x, 0, 0],
    [0, varepsilon / hbar / omega_y, 0],
    [0, 0, 0]
])

# Create a figure for plotting
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(121, projection='3d')

# Plot the tetrahedron
ax.add_collection3d(Poly3DCollection(faces, facecolors='Green', linewidths=1, edgecolors='b', alpha=.25))

# Plot the vertices
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='red', s=50)

# Set labels for the axes
ax.set_xlabel('n_x')
ax.set_ylabel('n_y')
ax.set_zlabel('n_z')

# Set the limits of the axes for better visualization
ax.set_xlim([0, varepsilon / hbar / omega_x])
ax.set_ylim([0, varepsilon / hbar / omega_y])
ax.set_zlim([0, varepsilon / hbar / omega_z])

# Add LaTeX formatted vertex labels
vertex_labels = [
    r'$(0, 0, 0)$',  # (0, 0, 0)
    r'$\left( \frac{\varepsilon}{\hbar \omega_x}, 0, 0 \right)$',  # (E/ℏωx, 0, 0)
    r'$\left( 0, \frac{\varepsilon}{\hbar \omega_y}, 0 \right)$',  # (0, E/ℏωy, 0)
    r'$\left( 0, 0, \frac{\varepsilon}{\hbar \omega_z} \right)$'   # (0, 0, E/ℏωz)
]


for i, vertex in enumerate(vertices):
    ax.text(vertex[0], vertex[1], vertex[2], vertex_labels[i], fontsize=12, color='black')

# Comment out or remove this line to remove the title
ax.set_title('Tetrahedron Representing Quantum States Up to Energy E')

# Display the plot
plt.tight_layout()
#plt.show()

# Plotting the Base Area (separate plot)
fig = plt.figure(figsize=(12, 6))

# Plot the base area triangle
ax2 = fig.add_subplot(122, projection='3d')

# Plot the base area triangle
ax2.add_collection3d(Poly3DCollection([base_vertices], facecolors='cyan', linewidths=1, edgecolors='b', alpha=.5))

# Plot the base vertices
ax2.scatter(base_vertices[:, 0], base_vertices[:, 1], base_vertices[:, 2], color='blue', s=50)

# Add LaTeX formatted labels to the vertices
base_vertex_labels = [
    r'$\left( \frac{\varepsilon}{\hbar \omega_x}, 0, 0 \right)$',  # (E/ℏωx, 0, 0)
    r'$\left( 0, \frac{\varepsilon}{\hbar \omega_y}, 0 \right)$',  # (0, E/ℏωy, 0)
    r'$(0, 0, 0)$' # (0, 0, 0)

]

for i, txt in enumerate(base_vertex_labels):
    ax2.text(base_vertices[i][0], base_vertices[i][1], base_vertices[i][2], txt, color='black')

# Set labels for the axes
ax2.set_xlabel('n_x')
ax2.set_ylabel('n_y')
ax2.set_zlabel('n_z')

# Set the limits of the axes for better visualization
ax2.set_xlim([0, varepsilon / hbar / omega_x])
ax2.set_ylim([0, varepsilon / hbar / omega_y])
ax2.set_zlim([0, varepsilon / hbar / omega_z])

# Title for the base area plot
ax2.set_title('Base Area of Tetrahedron (Triangle)')

# Display the plots
plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Constants
zeta4 = np.pi**4 / 90  # Approximation of Zeta[4]
zeta3 = 1.20206  # Approximation of Zeta[3]
C1 = 12 * zeta4 / zeta3

# Define mu*(T)
def mu_star(T, A, Tc):
    return A * (Tc - T)

# Define Cv/NkB function
def cv_over_nkb(T, A, Tc):
    if T <= Tc:
        return C1 * (T / Tc)**3
    else:
        mu_star_val = mu_star(T, A, Tc)
        return (3 * zeta4 / zeta3) * (4 * T**3 + mu_star_val * T**2) * np.exp(mu_star_val * T)

# Parameters
A = 20
Tc = 1.0

# Temperature range
T = np.linspace(0, 3, 500)
Cv_NkB = [cv_over_nkb(t, A, Tc) for t in T]

# Plot
fig, ax = plt.subplots()

# Main plot
ax.plot(T, Cv_NkB, color="blue")
ax.axvline(Tc, color="gray", linestyle="--")
ax.text(Tc + 0.05, 0.5, r"T = $T_c$", color="black")
ax.set_xlim(0.7, 1.1)
ax.set_ylim(0, 15)
ax.set_xlabel("Temperature (T)")
ax.set_ylabel(r"$\frac{C_v}{N k_B}$")
ax.set_title(r"Plot of $\frac{C_v}{N k_B}$ with Temperature-Dependent $\mu^*(T)$")

#plt.show()


