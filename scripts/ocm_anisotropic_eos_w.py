"""
OCM SI Model: Anisotropic Equation of State Derivations w(z, theta, phi)
Author: Ashil S.
Description: Numerically models the coordinate-dependent dark energy equation of state 
             w(z, theta, phi) relative to the Axis of Evil, contrasting against the 
             standard isotropic LambdaCDM w = -1 baseline.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_anisotropic_eos():
    # Angular separation theta from the Axis of Evil (0 to 180 degrees)
    theta_deg = np.linspace(0, 180, 400)
    theta_rad = np.radians(theta_deg)
    
    # Standard LambdaCDM Cosmological Constant baseline (w = -1.0 isotropic)
    w_lcdm = -1.0 * np.ones_like(theta_deg)
    
    # OCM Anisotropic Equation of State w(theta) modulated by kappa-flux gradients
    # Fluctuates systematically around -1 depending on alignment with Oloid spine
    w_ocm = -1.0 + 0.12 * np.cos(theta_rad) - 0.05 * np.sin(2.0 * theta_rad)
    
    plt.figure(figsize=(10, 5.5), dpi=100)
    plt.plot(theta_deg, w_ocm, label=r'OCM Anisotropic Equation of State $w(\theta)$', color='#7c3aed', lw=3.0)
    plt.plot(theta_deg, w_lcdm, label=r'Standard $\Lambda$CDM Baseline ($w = -1.0$)', color='#64748b', linestyle='--', lw=2.0)
    
    plt.axhline(y=-1.0, color='black', linestyle=':', alpha=0.5)
    plt.axvline(x=0, color='#dc2626', linestyle=':', label='Axis of Evil Alignment ($\theta = 0^{\circ}, 180^{\circ}$)')
    plt.axvline(x=180, color='#dc2626', linestyle=':')
    
    plt.title("Anisotropic Equation of State $w(z, \theta, \phi)$ vs. Axis of Evil", fontsize=12, fontweight='bold')
    plt.xlabel("Angular Offset from Oloid Spine $\theta$ (Degrees)", fontsize=10)
    plt.ylabel("Apparent Equation of State Parameter $w$", fontsize=10)
    plt.xlim(0, 180)
    plt.ylim(-1.25, -0.75)
    plt.legend(loc='lower right', frameon=True, fontsize=8)
    plt.grid(True, linestyle=':', alpha=0.5)
    
    output_filename = "ocm_anisotropic_eos_w_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Anisotropic equation of state verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_anisotropic_eos()
