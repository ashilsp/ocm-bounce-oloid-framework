"""
OCM SI Model: Modified Pulsar Timing Array Hellings-Downs Correlations
Author: Ashil S.
Description: Numerically models standard Hellings-Downs spatial correlation curves 
             versus the OCM-modified anisotropic correlation incorporating Oloid 
             spine resonance kernel modulations (Gamma_OCM).
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_modified_hellings_downs():
    # Angular separation theta from 0 to 180 degrees
    theta_deg = np.linspace(0, 180, 400)
    theta_rad = np.radians(theta_deg)
    
    # x_ab = (1 - cos(theta_ab)) / 2
    x_ab = (1.0 - np.cos(theta_rad)) / 2.0
    
    # Standard Hellings-Downs spatial correlation curve
    # Gamma_HD = (3/2) * x * ln(x) - (1/4) * x + 1/2  (with delta_ab = 0 for off-diagonal pairs)
    # Handle x_ab = 0 case safely
    x_safe = np.clip(x_ab, 1e-5, 1.0)
    gamma_hd = 1.5 * x_safe * np.log(x_safe) - 0.25 * x_safe + 0.5
    gamma_hd[x_ab == 0] = 0.5 # Limit at theta = 0
    
    # OCM Anisotropic Modulation Kernel (introducing quadrupole/hexadecapole spine variance)
    # Gamma_OCM = Gamma_HD * [1 + A_res * Y_LM_modulation]
    A_res = 0.18
    modulation = 1.0 + A_res * (np.cos(2.0 * theta_rad) * np.sin(theta_rad))
    gamma_ocm = gamma_hd * modulation
    
    plt.figure(figsize=(10, 5.5), dpi=100)
    plt.plot(theta_deg, gamma_ocm, label=r'OCM Anisotropic PTA Correlation ($\Gamma_{\text{OCM}}$)', color='#7c3aed', lw=3.0)
    plt.plot(theta_deg, gamma_hd, label=r'Standard Hellings-Downs Curve ($\Gamma_{\text{HD}}$)', color='#64748b', linestyle='--', lw=2.0)
    
    plt.title("Modified Pulsar Timing Array Hellings-Downs Spatial Correlations", fontsize=12, fontweight='bold')
    plt.xlabel("Pulsar Angular Separation $\theta_{ab}$ (Degrees)", fontsize=10)
    plt.ylabel("Normalized Cross-Correlation $\Gamma_{ab}$", fontsize=10)
    plt.xlim(0, 180)
    plt.ylim(-0.3, 1.0)
    plt.legend(loc='upper right', frameon=True, fontsize=8)
    plt.grid(True, linestyle=':', alpha=0.5)
    
    output_filename = "ocm_modified_hellings_downs_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Modified Hellings-Downs verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_modified_hellings_downs()
