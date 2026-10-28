"""
OCM-Bounce Magnetic Piston Pressure Balance Model
Author: OCM Research Team
Description: Computes gravitational collapse pressure vs. OCM repulsive 
             negentropy flux pressure near the Inner Rd limit.
"""

import numpy as np
import matplotlib.pyplot as plt

def compute_pressure_balance():
    # Define radial distance array approaching the inner Rd floor
    r = np.linspace(0.2, 2.0, 500)
    
    # Gravitational pressure (attractive, ~ r^-2)
    P_grav = 15.0 / (r**2)
    
    # OCM Repulsive Negentropy Flux pressure (higher order scaling, ~ r^-4)
    P_kappa = 2.0 / (r**4)
    
    # Net total pressure at the boundary
    P_total = P_grav - P_kappa
    
    # Identify the bounce point where P_kappa overtakes P_grav
    bounce_idx = np.argmin(np.abs(P_total))
    r_bounce = r[bounce_idx]
    
    print(f"[INFO] Critical Inner R_d Bounce Point detected at r = {r_bounce:.3f}")
    
    # Plotting configuration
    plt.figure(figsize=(8, 6), dpi=100)
    plt.plot(r, P_grav, label=r'$P_{\text{grav}}$ (Attractive)', color='#3b82f6', lw=2)
    plt.plot(r, P_kappa, label=r'$P_{\kappa}$ (OCM Repulsive Flux)', color='#ef4444', lw=2.5)
    
    plt.axvline(x=r_bounce, color='#10b981', linestyle='--', label=f'Bounce Threshold ($R_d$): {r_bounce:.2f}')
    
    plt.title("OCM-Bounce: The Magnetic Piston Pressure Balance", fontsize=12, fontweight='bold')
    plt.xlabel("Normalized Radial Distance ($r / R_d$)", fontsize=10)
    plt.ylabel("Pressure Magnitude ($P$)", fontsize=10)
    plt.ylim(0, 100)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle=':', alpha=0.6)
    
    output_filename = "ocm_bounce_pressure_curve.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Pressure balance verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    compute_pressure_balance()
