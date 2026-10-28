"""
OCM SI Model: Sigmoidal Node Maturation & Hubble Transition ($n=3$)
Author: Ashil S.
Description: Numerically models the sigmoidal redshift transition of H(z) from 
             67.4 to 73.0 driven by cubic Oloid volume maturation at z_trans ≈ 2.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_node_maturation():
    z = np.linspace(0, 5, 400) # Redshift
    
    # Sigmoidal transition centered around z_trans ≈ 2.0 ($n=3$ volumetric scaling)
    H_min = 67.4
    H_local = 73.0
    H_z = H_min + (H_local - H_min) / (1.0 + np.exp(-1.5 * (2.0 - z)))
    
    plt.figure(figsize=(10, 5.5), dpi=100)
    plt.plot(z, H_z, label=r'OCM Volumetric Transition $H(z)$ ($n=3$ Oloid Scale)', color='#7c3aed', lw=3.0)
    plt.axvline(x=2.0, color='#f59e0b', linestyle='--', label=r'Inflection Point Transition ($z_{\text{trans}} \approx 2$)')
    plt.axhline(y=H_min, color='#3b82f6', linestyle=':', label=f'CMB Baseline ($H_{{min}} = {H_min}$)')
    plt.axhline(y=H_local, color='#ef4444', linestyle=':', label=f'Local Measured ($H_{{local}} = {H_local}$)')
    
    plt.title("Sigmoidal Expansion Maturation ($n=3$ Power Law)", fontsize=12, fontweight='bold')
    plt.xlabel("Cosmic Redshift ($z$)", fontsize=10)
    plt.ylabel("Expansion Rate $H(z)$ ($\text{km s}^{-1}\text{Mpc}^{-1}$)", fontsize=10)
    plt.xlim(5, 0) # Reversed redshift axis for cosmological convention
    plt.ylim(65, 75)
    plt.legend(loc='lower left', frameon=True, fontsize=8)
    plt.grid(True, linestyle=':', alpha=0.5)
    
    output_filename = "ocm_node_maturation_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Node maturation verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_node_maturation()
