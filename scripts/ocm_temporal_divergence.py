"""
OCM Hubble Tension Temporal Divergence & Terminal Limit Model
Author: Ashil S.
Description: Numerically simulates the evolutionary divergence between the 
             fossilized Laminar Core baseline (67.4) and the Turbulent Local Drift 
             approaching the Manifold Viscosity terminal limit (82.0 km/s/Mpc).
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_temporal_divergence():
    # Define cosmic time maturation array (Gyr from present)
    t = np.linspace(0, 15, 500)
    
    # Baseline constants
    H_laminar = 67.4  # CMB early-universe baseline (constant fossil)
    H_terminal = 82.0 # Manifold viscosity terminal expansion limit
    
    # OCM Turbulent Local Drift (Sigmoidal asymptotic saturation toward H_terminal)
    # H_local(t) = H_laminar + (H_terminal - H_laminar) / (1 + exp(-alpha * (t - t_0)))
    H_local = H_laminar + (H_terminal - H_laminar) / (1.0 + np.exp(-0.3 * (t - 5.0)))
    
    # Standard Model Convergence Reference
    H_lcdm_ref = 70.2 - 0.05 * t
    
    # Plotting configuration matching manuscript standards
    plt.figure(figsize=(10, 6.5), dpi=100)
    plt.plot(t, np.full_like(t, H_laminar), label=r'OCM: Laminar Core ($H_{\text{CMB}}$)', color='#3b82f6', lw=3.0)
    plt.plot(t, H_local, label=r'OCM: Turbulent Local Drift ($\to H_T \approx 82.0$)', color='#ef4444', lw=3.0)
    plt.plot(t, H_lcdm_ref, label=r'$\Lambda$CDM Convergence Reference', color='#0f172a', linestyle='--', lw=2.0)
    plt.axhline(y=H_terminal, color='#f59e0b', linestyle=':', label='Terminal Viscosity Limit ($H_T \approx 82.0$)')
    
    # Highlight widening tension at t = 10 Gyr
    t_target = 10.0
    h_lam_val = H_laminar
    h_loc_val = H_laminar + (H_terminal - H_laminar) / (1.0 + np.exp(-0.3 * (t_target - 5.0)))
    plt.annotate(f'Widening Tension Gap\n($\Delta H \approx {h_loc_val - h_lam_val:.1f}$)', 
                 xy=(t_target, (h_lam_val + h_loc_val)/2), xytext=(t_target - 2.5, 75.0),
                 arrowprops=dict(facecolor='#8b5cf6', shrink=0.05, width=1.5, headwidth=6),
                 fontsize=9, fontweight='bold', color='#8b5cf6')
    
    plt.title("Temporal Divergence Prediction: Widening of the Hubble Tension", fontsize=12, fontweight='bold')
    plt.xlabel("Cosmic Time Maturation ($t$ in Gyr from Present)", fontsize=10)
    plt.ylabel("Hubble Parameter $H_0$ ($\text{km s}^{-1}\text{Mpc}^{-1}$)", fontsize=10)
    plt.xlim(0, 15)
    plt.ylim(62, 88)
    plt.legend(loc='upper left', frameon=True, fontsize=8)
    plt.grid(True, linestyle=':', alpha=0.5)
    
    output_filename = "ocm_temporal_divergence_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Temporal divergence verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_temporal_divergence()
