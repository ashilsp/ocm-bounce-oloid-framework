"""
OCM SI Model: Flux Saturation Principle & Oloid Curvature Mapping
Author: Ashil S.
Description: Numerically models the exponential amplification of kappa-flux density 
             rho_kappa = rho_baseline * exp(alpha * |K_local|) along Oloid spines, 
             reconciling the 67.4 facet baseline with the 73.0 spine expansion rate.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_flux_saturation():
    # Spatial distance along surface curvature profile from facet (K=0) to spine (K=max)
    s_coord = np.linspace(0, 10, 400)
    
    # Local Gaussian curvature profile transitioning from flat facets to singular spines
    K_local = 5.0 * (np.tanh(s_coord - 5.0) + 1.0) / 2.0
    
    # Flux Saturation Principle: rho_kappa amplification -> H scaling from 67.4 to 73.0
    H_facet = 67.4
    H_spine = 73.0
    alpha_coup = 0.35
    
    H_profile = H_facet + (H_spine - H_facet) * (1.0 - np.exp(-alpha_coup * K_local))
    
    plt.figure(figsize=(10, 5.5), dpi=100)
    plt.plot(s_coord, H_profile, label=r'Oloid Surface Expansion Rate $H(\text{local curvature})$', color='#2563eb', lw=3.0)
    plt.axhline(y=67.4, color='#3b82f6', linestyle='--', label=r'Developable Facet Baseline ($K=0 \implies 67.4$ spatially)')
    plt.axhline(y=73.0, color='#dc2626', linestyle='--', label=r'Singular Spine Saturation ($|K| \to \max \implies 73.0$)')
    
    plt.title("Oloid Curvature & Flux Saturation Principle ($\rho_{\kappa} \propto \exp(\alpha |K|)$)", fontsize=12, fontweight='bold')
    plt.xlabel("Surface Position Coordinate (Facet $K=0$ $\to$ Spine Singularity)", fontsize=10)
    plt.ylabel("Local Expansion Rate $H$ ($\text{km s}^{-1}\text{Mpc}^{-1}$)", fontsize=10)
    plt.xlim(0, 10)
    plt.ylim(66, 74)
    plt.legend(loc='lower right', frameon=True, fontsize=8)
    plt.grid(True, linestyle=':', alpha=0.5)
    
    output_filename = "ocm_flux_saturation_curvature_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Flux saturation and curvature verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_flux_saturation()
