"""
OCM SI Model: Kappa-Flux Tow-Cable Bridge Mechanics & Local Collisions
Author: Ashil S.
Description: Numerically models the effective potential V_eff(r) for inter-nodal 
             kappa-flux bridges, demonstrating how inward flux-tension overcomes 
             outward Hubble expansion below critical separation r_crit.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_tow_cable_bridge():
    # Radial distance array r between two nodes (e.g., in Mpc from 0.1 to 3.0)
    r = np.linspace(0.1, 3.0, 500)
    
    # Model parameters
    GM_tot = 1.2     # Combined mass-gravitational scaling
    flux_term = 0.8  # Kappa-flux tension parameter (kappa_0 * rho_kappa / lambda_kappa)
    R_d = 2.5        # Relativistic Roche Limit boundary
    H_0_term = 0.5   # Hubble expansion coefficient scaling
    
    # Effective Potential V_eff(r) = - (GM_tot / r) - flux_term * ln(r / R_d) + 0.5 * H_0_term * r^2
    # Handle log safely for r > 0
    V_grav = - (GM_tot / r)
    V_flux = - flux_term * np.log(r / R_d)
    V_hubble = 0.5 * H_0_term * (r ** 2)
    
    V_eff = V_grav + V_flux + V_hubble
    
    # Standard LambdaCDM expansion-only potential reference (outward runaway)
    V_lcdm_expansion = V_hubble + 1.0
    
    plt.figure(figsize=(10, 5.5), dpi=100)
    plt.plot(r, V_eff, label=r'OCM Tow-Cable Effective Potential $V_{\text{eff}}(r)$', color='#2563eb', lw=3.0)
    plt.plot(r, V_lcdm_expansion, label=r'Standard Cosmological Expansion ($H_0^2 r^2$ dominant)', color='#dc2626', linestyle='--', lw=2.0)
    
    # Mark the critical turning point / collision boundary r_crit
    # Minimum of V_eff or crossover where inward force dominates
    idx_crit = np.argmin(V_eff)
    r_crit = r[idx_crit]
    
    plt.scatter([r_crit], [V_eff[idx_crit]], color='#059669', s=100, zorder=5, 
                label=r'Critical Collision Threshold ($r_{\text{crit}}$)')
    
    # Shaded Collision Zone (r < r_crit)
    plt.axvspan(0.1, r_crit, color='#10b981', alpha=0.15, label='Inward Flux-Tension Collision Zone ($r < r_{\text{crit}}$)')
    
    plt.title("$\kappa$-Flux Tow-Cable Bridge Mechanics & Local Collisions", fontsize=12, fontweight='bold')
    plt.xlabel("Inter-Nodal Separation Distance $r$ (Mpc)", fontsize=10)
    plt.ylabel("Effective Potential Magnitude $V_{\text{eff}}(r)$", fontsize=10)
    plt.xlim(0.1, 3.0)
    plt.ylim(-6.0, 4.0)
    plt.legend(loc='upper right', frameon=True, fontsize=8)
    plt.grid(True, linestyle=':', alpha=0.5)
    
    output_filename = "ocm_tow_cable_bridge_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Tow-cable bridge verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_tow_cable_bridge()
