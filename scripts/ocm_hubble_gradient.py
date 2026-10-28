"""
OCM Hubble Tension Resolution Gradient Model
Author: Ashil S.
Description: Numerically simulates the radial expansion rate H(r) transitioning 
             from the early-universe Laminar Core (67.4 km/s/Mpc) to the late-universe 
             Turbulent Boundary (73.0 km/s/Mpc) using the n=3 OCM power-law gradient.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_hubble_gradient():
    # Define normalized radial distance array (r / Rd) from 0 to 1.2
    r_normalized = np.linspace(0.0, 1.2, 500)
    
    # Baseline laminar rate and late-universe target
    H_min = 67.4  # CMB early-universe baseline (km/s/Mpc)
    H_late = 73.0 # Local late-universe measurement (km/s/Mpc)
    
    # OCM Power-Law Gradient (n=3 volumetric node maturation)
    # H(r) = H_min + (H_late - H_min) * (r / R_d)^3
    H_r = H_min + (H_late - H_min) * (r_normalized ** 3)
    
    # Plotting configuration matching manuscript standards
    plt.figure(figsize=(9, 6), dpi=100)
    plt.plot(r_normalized, H_r, label=r'OCM Radial Gradient ($n=3$)', color='#0f172a', lw=3.0)
    
    # Explicit data points for early and late universe probes
    plt.scatter([0.2], [H_min], color='#ef4444', s=80, zorder=5, label=f'Early Universe (CMB): {H_min} km/s/Mpc')
    plt.scatter([1.0], [H_late], color='#3b82f6', s=80, zorder=5, label=f'Late Universe (Local): {H_late} km/s/Mpc')
    
    # Boundary marker for Relativistic Roche Limit (Rd)
    plt.axvline(x=1.0, color='#10b981', linestyle='--', label='Relativistic Roche Limit ($R_d$ Boundary)')
    
    plt.title("Hubble Tension Resolution via Radial $\kappa$-Flux Gradient", fontsize=12, fontweight='bold')
    plt.xlabel("Normalized Radial Position ($r / R_d$)", fontsize=10)
    plt.ylabel("Effective Expansion Rate $H(r)$ ($\text{km s}^{-1}\text{Mpc}^{-1}$)", fontsize=10)
    plt.xlim(0, 1.2)
    plt.ylim(65, 75)
    plt.legend(loc='upper left', frameon=True)
    plt.grid(True, linestyle=':', alpha=0.6)
    
    output_filename = "ocm_hubble_gradient_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Hubble gradient verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_hubble_gradient()
