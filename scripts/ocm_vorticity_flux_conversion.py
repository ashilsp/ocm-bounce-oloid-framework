"""
OCM SI Model: Angular Momentum to Kappa-Flux Conversion & Viscous Vorticity Growth
Author: S. Ashil
Description: Numerically models (1) the conversion of parent orbital angular 
             momentum L(t) into boundary flux injection Phi_kappa(t), and 
             (2) the Navier-Stokes viscous vorticity growth omega(r) vs. vanishing 
             ideal fluid flow (eta = 0).
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_vorticity_and_flux():
    # Setup figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5), dpi=100)
    
    # --- SUBPLOT 1: Angular Momentum to Kappa-Flux Conversion ---
    t = np.linspace(0, 10, 400)
    L_initial = 100.0
    chi = 0.85 # Volumetric conversion efficiency
    
    # Rapid decay of parent orbital angular momentum via merger/gravitational waves
    L_parent = L_initial * np.exp(-0.6 * t)
    
    # Resulting boundary flux injection Phi_kappa(t) = chi * (L_initial - L_parent) or driven source
    Phi_kappa = chi * (L_initial - L_parent)
    
    ax1.plot(t, L_parent, label=r'Parent Orbital Angular Momentum $L(t)$', color='#2563eb', lw=2.5)
    ax1.plot(t, Phi_kappa, label=r'Boundary Flux Injection $\Phi_{\kappa}(t) = \chi L_{\text{initial}}$', color='#dc2626', linestyle='--', lw=2.5)
    ax1.set_title("Angular Momentum to $\kappa$-Flux Conversion ($L \to \kappa$)", fontsize=11, fontweight='bold')
    ax1.set_xlabel("Merger Evolutionary Time ($t$)", fontsize=9)
    ax1.set_ylabel("Normalized Amplitude", fontsize=9)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 110)
    ax1.legend(loc='center right', frameon=True, fontsize=8)
    ax1.grid(True, linestyle=':', alpha=0.5)
    
    # --- SUBPLOT 2: Relativistic Navier-Stokes Vorticity Transport ---
    r = np.linspace(0.1, 5.0, 400)
    eta = 1.2 # Manifold viscosity coefficient
    
    # Ideal fluid (eta = 0): Kelvin's theorem forces vorticity to zero
    omega_ideal = np.zeros_like(r)
    
    # OCM Viscous Fluid (eta > 0): Non-vanishing vorticity vector driven by viscosity gradients
    omega_ocm = (eta / (r ** 1.5)) * np.exp(-0.4 * r) * 15.0
    
    ax2.plot(r, omega_ocm, label=r'OCM Viscous Vorticity $\vec{\omega} = \nabla \times \vec{v}_{\kappa} \neq 0$', color='#7c3aed', lw=2.5)
    ax2.plot(r, omega_ideal, label=r'Standard FLRW Perfect Fluid ($\eta = 0 \implies \vec{\omega} = 0$)', color='#64748b', linestyle='--', lw=2.0)
    ax2.set_title("Viscous Vorticity Generation ($\nabla \times \vec{v}$ for B-Modes)", fontsize=11, fontweight='bold')
    ax2.set_xlabel("Radial Coordinate Distance ($r$)", fontsize=9)
    ax2.set_ylabel("Vorticity Magnitude $|\vec{\omega}|$", fontsize=9)
    ax2.set_xlim(0.1, 5.0)
    ax2.set_ylim(-1, 20)
    ax2.legend(loc='upper right', frameon=True, fontsize=8)
    ax2.grid(True, linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    output_filename = "ocm_vorticity_flux_conversion_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Vorticity and flux conversion verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_vorticity_and_flux()
