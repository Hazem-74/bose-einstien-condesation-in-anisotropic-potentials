# Bose-Einstein Condensation in Anisotropic Potentials

This project explores the thermodynamic and geometric aspects of **Bose–Einstein condensation (BEC)** in anisotropic harmonic potentials. It provides a set of Jupyter notebooks that visualize the structure of quantum states, the fraction of condensed particles as a function of temperature, and the behavior of key thermodynamic quantities such as the reduced chemical potential and specific heat.

---

## Project Overview

In anisotropic traps (where the trapping frequencies along x, y, and z axes differ), the geometry of accessible quantum states deviates from simple spherical symmetry. This notebook provides computational and visual tools to illustrate how anisotropy affects the state distribution and macroscopic thermodynamics of the Bose gas.

The analyses include:

* Visualization of **quantum state space** as a tetrahedron bounded by energy constraints.
* Calculation and plotting of **condensate fraction** as temperature varies below and above the critical temperature.
* Estimation of **temperature-dependent chemical potential**.
* Evaluation of **specific heat per particle** incorporating the reduced chemical potential.

---

## File Summary

### `Graphs.ipynb`

This notebook contains four primary sections:

1. **Quantum State Geometry Visualization**

   * Constructs a **3D tetrahedron** representing the quantized energy states up to a fixed energy ε in an anisotropic potential characterized by frequencies (ωₓ, ωᵧ, ω_z).
   * Uses `matplotlib`’s `Poly3DCollection` to visualize both the **full tetrahedral energy surface** and its **base triangle**, illustrating the energy space boundaries:
     [
     \frac{n_x}{\varepsilon / \hbar \omega_x} + \frac{n_y}{\varepsilon / \hbar \omega_y} + \frac{n_z}{\varepsilon / \hbar \omega_z} = 1
     ]
   * Demonstrates how anisotropy affects the state density and degeneracy distribution.

2. **Condensate Fraction (N₀/N) vs Temperature**

   * Models the **fraction of condensed particles** below the critical temperature (T_c) using the standard approximation:
     [
     \frac{N_0}{N} = 1 - \left(\frac{T}{T_c}\right)^3
     ]
   * Plots (N_0/N) against temperature to highlight the sharp onset of condensation.

3. **Reduced Chemical Potential μ*(T)**

   * Implements a **linear temperature dependence model**:
     [
     \mu^*(T) = A (T_c - T)
     ]
   * Demonstrates how μ*(T) varies with temperature approaching (T_c), representing the reduction in effective potential depth with increasing thermal energy.

4. **Specific Heat (C_v/Nk_B)**

   * Defines (C_v/Nk_B) in terms of ζ(3) and ζ(4) functions:
     [
     C_v/Nk_B =
     \begin{cases}
     C_1 \left(\frac{T}{T_c}\right)^3, & T \leq T_c \
     f(T, \mu^*(T)), & T > T_c
     \end{cases}
     ]
   * Plots specific heat as a function of temperature, showing the expected discontinuity at (T = T_c), characteristic of second-order phase transitions.

---

## Requirements

**Python Version:** 3.8+
**Dependencies:**

* numpy
* matplotlib
* scipy

Install dependencies using:

```bash
pip install numpy matplotlib scipy
```

---

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Hazem-74/bose-einstien-condesation-in-anisotropic-potentials.git
   cd "Bose-Einstein Condensation in Anisotropic Potentials"
   ```

2. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

3. Open `Graphs.ipynb` and run all cells sequentially.

---

## Notes

* All physical constants are normalized (e.g., ℏ = 1) for computational simplicity.
* The anisotropic potential parameters (ωₓ, ωᵧ, ω_z) and temperature scaling can be adjusted for different configurations.
* The visualizations are qualitative but reflect correct physical dependencies.

---

## License

This project is for academic and illustrative purposes. For reuse or modification, credit **{USER_HANDLE}** and link back to the original repository.
