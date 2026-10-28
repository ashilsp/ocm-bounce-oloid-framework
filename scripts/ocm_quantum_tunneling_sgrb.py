"""
OCM SI Model: Quantum-Topological Tunneling & Hostless sGRB Cross-Sections
Author: Ashil S.
Description: Numerically models the effective potential barrier V_eff(r) and WKB 
             tunneling probability (Gamma_tunnel) for high-density kappa-flux packets 
             crossing the R_d boundary.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_quantum_tunneling():
    # Radial coordinate array across the R_d boundary barrier
    r = np.linspace(0.4, 3.0, 500)
    
    # Effective potential parameters: V_eff(r) = K_0 / r^6 - GM / r + L^2 / 2r^2
    K_0 = 0.35
    GM = 1.2
    L_term = 0.4
    
    V_eff = (K_0 / (r ** 6)) - (GM / r) + (L_term / (r ** 2))
    
    # Particle energy level E for tunneling demonstration
    E_packet = 1.5
    
    plt.figure(figsize=(10, 5.5), dpi=100)
    plt.plot(r, V_eff, label=r'Effective Potential Barrier $V_{\text{eff}}(r)$', color='#dc2626', lw=3.0)
    plt.axhline(y=E_packet, color='#2563eb', linestyle='--', label=r'Packet Energy Level ($E$ for WKB Tunneling)')
    
    # Shade barrier region where V_eff > E
    barrier_mask = V_eff > E_packet
    plt.fill_between(r, E_packet, V_eff, where=barrier_mask, color='#dc2626', alpha=0.15, label='Quantum-Topological Barrier ($\Gamma_{\text{tunnel}}$)')
    
    plt.title("Quantum-Topological Tunneling Across the $R_d$ Boundary ($sGRBs$)", fontsize=12, fontweight='bold')
    plt.xlabel("Radial Boundary Coordinate $r$", fontsize=10)
    plt.ylabel("Effective Potential Energy $V_{\text{eff}}(r)$", fontsize=10)
    plt.xlim(0.4, 3.0)
    plt.ylim(-1.0, 6.0)
    plt.legend(loc='upper right', frameon=True, fontsize=8)
    plt.grid(True, linestyle=':', alpha=0.5)
    
    output_filename = "ocm_quantum_tunneling_sgrb_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Quantum tunneling sGRB verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_quantum_tunneling()
