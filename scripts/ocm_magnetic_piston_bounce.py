"""
OCM Microscopic Fluid-Dynamics: Magnetic Piston Bounce Pressure Model
Author: Ashil S.
Description: Numerically models the pressure crossover where repulsive OCM 
             pressure (P_kappa ~ r^-6) overtakes gravitational collapse pressure 
             (P_grav ~ r^-4) near the Planck scale, yielding a non-zero r_bounce.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_magnetic_piston():
    # Define radial coordinate array approaching Planck scale (r from 0.2 to 2.0)
    r = np.linspace(0.2, 2.0, 500)
    
    # Constants for simulation scaling
    G_M2 = 2.0  # Combined gravitational mass scaling parameter
    K_0 = 1.0   # OCM coupling constant for repulsive flux density
    
    # 1. Inward Gravitational Collapse Pressure (P_grav ~ r^-4)
    P_grav = - (G_M2) / (r ** 4)
    
    # 2. Repulsive Magnetic Piston Pressure (P_kappa ~ r^-6)
    P_kappa = K_0 / (r ** 6)
    
    # Total Dynamic Pressure
    P_total = P_grav + P_kappa
    
    # Analytical solution for equilibrium bounce point where P_total = 0 -> r_bounce = sqrt(K_0 / G_M2) * scaling
    # For our chosen parameters: r_bounce = sqrt(1.0 / 2.0) = 1/sqrt(2) approx 0.707
    r_bounce = np.sqrt(K_0 / (2.0)) * np.sqrt(2.0) # exact root balance point
    
    # Plotting configuration matching manuscript standards
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(r, np.abs(P_grav), label=r'Gravitational Collapse Pressure ($P_{\text{grav}} \propto r^{-4}$)', color='#2563eb', lw=2.5)
    plt.plot(r, P_kappa, label=r'Repulsive Magnetic Piston Pressure ($P_{\kappa} \propto r^{-6}$)', color='#dc2626', linestyle='--', lw=2.5)
    plt.plot(r, P_total, label=r'Total Dynamic Pressure ($P_{\text{total}}$)', color='#0f172a', lw=3.0)
    
    # Mark the equilibrium bounce radius
    idx_bounce = np.argmin(np.abs(P_total))
    plt.scatter([r[idx_bounce]], [P_kappa[idx_bounce]], color='#059669', s=100, zorder=5, 
                label=r'Equilibrium Bounce Radius ($r_{\text{bounce}}$)')
    
    plt.axvline(x=r[idx_bounce], color='#059669', linestyle=':', label='Singularity Prevention Threshold')
    
    plt.title("Magnetic Piston Pressure Crossover: Preventing Point Singularities", fontsize=12, fontweight='bold')
    plt.xlabel("Normalized Radial Coordinate $r$ (Approaching Planck Scale $\to 0$)", fontsize=10)
    plt.ylabel("Thermodynamic Pressure Magnitude (Log Scale)", fontsize=10)
    plt.yscale('log')
    plt.xlim(0.2, 2.0)
    plt.ylim(0.1, 1000)
    plt.legend(loc='upper right', frameon=True, fontsize=8)
    plt.grid(True, linestyle=':', alpha=0.5)
    
    output_filename = "ocm_magnetic_piston_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Magnetic piston pressure balance verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_magnetic_piston()
