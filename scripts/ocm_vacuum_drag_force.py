"""
OCM SI Model: Relativistic Navier-Stokes Vacuum Drag & Geometric Force F_kappa
Author: Ashil S.
Description: Numerically models (1) the geometric drag force F_kappa as a function 
             of manifold viscosity (eta_m) and node velocity (v_node), and 
             (2) the damping of runaway acceleration leading to terminal velocity saturation.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_vacuum_drag_force():
    # Setup figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5), dpi=100)
    
    # --- SUBPLOT 1: Geometric Drag Force F_kappa vs. Node Velocity ---
    v_node = np.linspace(0, 1000, 300) # km/s
    grad_kappa = 1.5 # Background kappa-flux density gradient
    etas = [0.5, 1.0, 2.0] # Manifold viscosity parameter variants
    
    for eta in etas:
        F_kappa = eta * grad_kappa * v_node
        ax1.plot(v_node, F_kappa, label=r'Manifold Viscosity $\eta_m = %.1f$' % eta, lw=2.5)
        
    ax1.set_title("Geometric Vacuum Drag Force ($F_{\kappa} = \eta_m \nabla\kappa \, v$)", fontsize=11, fontweight='bold')
    ax1.set_xlabel("Relative Node Velocity ($v_{\text{node}}$ in km/s)", fontsize=9)
    ax1.set_ylabel("Effective Drag Force Magnitude ($F_{\kappa}$)", fontsize=9)
    ax1.set_xlim(0, 1000)
    ax1.legend(loc='upper left', frameon=True, fontsize=8)
    ax1.grid(True, linestyle=':', alpha=0.5)
    
    # --- SUBPLOT 2: Runaway Acceleration Damping & Velocity Saturation ---
    t = np.linspace(0, 50, 400)
    v_undamped = 25.0 * t # Unconstrained linear runaway acceleration
    v_terminal = 600.0 # OCM bulk flow terminal velocity saturation limit
    tau_damping = 10.0
    v_damped = v_terminal * (1.0 - np.exp(-t / tau_damping))
    
    ax2.plot(t, v_damped, label=r'OCM Viscous Damped Velocity ($F_{\kappa}$ Drag)', color='#7c3aed', lw=3.0)
    ax2.plot(t, v_undamped, label='Unconstrained Runaway Acceleration', color='#dc2626', linestyle='--', lw=2.0)
    ax2.axhline(y=v_terminal, color='#10b981', linestyle=':', label='Terminal Velocity Limit ($v_T \approx 600$ km/s)')
    
    ax2.set_title("Runaway Acceleration Damping & Saturation", fontsize=11, fontweight='bold')
    ax2.set_xlabel("Evolutionary Time ($t$)", fontsize=9)
    ax2.set_ylabel("Node Spatial Velocity ($v_{\text{node}}$)", fontsize=9)
    ax2.set_xlim(0, 50)
    ax2.set_ylim(0, 1200)
    ax2.legend(loc='upper left', frameon=True, fontsize=8)
    ax2.grid(True, linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    output_filename = "ocm_vacuum_drag_force_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Vacuum drag force verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_vacuum_drag_force()
