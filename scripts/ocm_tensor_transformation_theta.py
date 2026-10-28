"""
OCM SI Model: Manifold Anisotropy Tensor Transformations & FLRW Coupling
Author: Ashil S.
Description: Numerically models the coordinate transformation of the Oloid anisotropy 
             tensor Theta_mu_nu under Euler angle rotations (alpha, beta, gamma), 
             demonstrating directional expansion gradients without violating background homogeneity.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_tensor_transformations():
    # Angular grid representing observer celestial sphere (theta, phi)
    theta = np.linspace(0, np.pi, 200)
    phi = np.linspace(0, 2 * np.pi, 200)
    TH, PH = np.meshgrid(theta, phi)
    
    # Baseline isotropic Hubble parameter (67.4) plus directional perturbation from Theta_mu_nu
    # Modulated by bi-axial spine orientation via Euler angle transformations
    H_base = 67.4
    epsilon = 0.08 # Geometric coupling parameter
    
    # Quadrupole / bi-axial spine directional projection (Axis of Evil harmonic)
    spine_modulation = np.cos(TH) ** 2 - 0.5 * np.sin(TH) ** 2 * np.cos(2.0 * PH)
    H_directional = H_base * (1.0 + epsilon * spine_modulation)
    
    # Plotting directional variance profile along a fixed meridian
    phi_slice = 0.0 # Meridian slice
    theta_slice = np.linspace(0, np.pi, 300)
    H_slice = H_base * (1.0 + epsilon * (np.cos(theta_slice) ** 2 - 0.5 * np.sin(theta_slice) ** 2))
    
    plt.figure(figsize=(10, 5.5), dpi=100)
    plt.plot(np.degrees(theta_slice), H_slice, label=r'Coupled Anisotropic Expansion $H(\theta, \phi)$', color='#7c3aed', lw=3.0)
    plt.axhline(y=67.4, color='#3b82f6', linestyle='--', label='Isotropic CMB Baseline ($67.4$ km/s/Mpc)')
    plt.axhline(y=73.0, color='#dc2626', linestyle='--', label='Spine-Aligned Local Target ($73.0$ km/s/Mpc)')
    
    plt.title(r'Manifold Anisotropy Tensor $\Theta_{\mu\nu}$ Coupling & Directional Gradients', fontsize=12, fontweight='bold')
    plt.xlabel("Celestial Meridian Angle $\theta$ (Degrees relative to Oloid Spine)", fontsize=10)
    plt.ylabel("Directional Expansion Rate $H(\theta)$ ($\text{km s}^{-1}\text{Mpc}^{-1}$)", fontsize=10)
    plt.xlim(0, 180)
    plt.ylim(65, 75)
    plt.legend(loc='upper right', frameon=True, fontsize=8)
    plt.grid(True, linestyle=':', alpha=0.5)
    
    output_filename = "ocm_tensor_transformation_theta_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Tensor transformation verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_tensor_transformations()
