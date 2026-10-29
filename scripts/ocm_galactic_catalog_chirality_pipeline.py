"""
OCM SI Model: Galactic Catalog Statistical Pipelines & Hemispherical Chirality Asymmetry
Author: Ashil S.
Description: Numerically models the extraction of the Fractional Excess Parameter (A) 
             across celestial orientation bins, contrasting OCM topological torque chirality 
             against the standard isotropic LambdaCDM zero baseline (A -> 0).
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_galactic_chirality_pipeline():
    # Setup figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5), dpi=100)
    
    # --- SUBPLOT 1: Fractional Excess Parameter (A) vs. Orientation Angle ---
    # Angular coordinate relative to the Axis of Evil (0 to 180 degrees)
    theta_aoe = np.linspace(0, 180, 300)
    
    # OCM Topological Torque Model: pronounced fractional excess peaking along spine alignment
    # A = (N_S - N_Z) / (N_S + N_Z)
    A_ocm = 0.045 * np.cos(np.radians(theta_aoe)) + 0.012 * np.sin(np.radians(2 * theta_aoe))
    
    # Standard LambdaCDM Isotropic Baseline (Parity invariance -> A = 0)
    np.random.seed(42)
    A_lcdm = np.random.normal(0.0, 0.003, size=len(theta_aoe))
    
    ax1.plot(theta_aoe, A_ocm, label=r'OCM Topological Chirality ($A \neq 0$ along Axis of Evil)', color='#7c3aed', lw=3.0)
    ax1.plot(theta_aoe, A_lcdm, label=r'Standard Isotropic $\Lambda$CDM Baseline ($A \to 0$)', color='#64748b', linestyle='--', lw=2.0)
    ax1.axhline(y=0, color='black', linestyle=':', alpha=0.5)
    ax1.axvline(x=0, color='#dc2626', linestyle=':', label='Axis of Evil Alignment ($\theta = 0^{\circ}, 180^{\circ}$)')
    ax1.axvline(x=180, color='#dc2626', linestyle=':')
    
    ax1.set_title("Fractional Excess Parameter ($A$) vs. Axis of Evil", fontsize=11, fontweight='bold')
    ax1.set_xlabel("Angular Offset from Axis of Evil (Degrees)", fontsize=9)
    ax1.set_ylabel("Fractional Excess Parameter ($A$)", fontsize=9)
    ax1.set_xlim(0, 180)
    ax1.set_ylim(-0.06, 0.06)
    ax1.legend(loc='upper right', frameon=True, fontsize=8)
    ax1.grid(True, linestyle=':', alpha=0.5)
    
    # --- SUBPLOT 2: Hemispherical Partitioning Comparison (N_S vs N_Z counts) ---
    hemispheres = ['North Hemisphere\n($\mathcal{H}_{\text{North}}$)', 'South Hemisphere\n($\mathcal{H}_{\text{South}}$)']
    ns_counts = [52400, 47600]
    nz_counts = [47800, 52100]
    
    x = np.arange(len(hemispheres))
    width = 0.35
    
    ax2.bar(x - width/2, ns_counts, width, label='Clockwise Spirals ($N_{\text{S}}$)', color='#2563eb')
    ax2.bar(x + width/2, nz_counts, width, label='Counter-Clockwise Spirals ($N_{\text{Z}}$)', color='#f59e0b')
    
    ax2.set_title("Hemispherical Enantiomorph Population Counts", fontsize=11, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(hemispheres, fontsize=9)
    ax2.set_ylabel("Galaxy Population Count", fontsize=9)
    ax2.set_ylim(40000, 56000)
    ax2.legend(loc='upper center', frameon=True, fontsize=8)
    ax2.grid(True, axis='y', linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    output_filename = "ocm_galactic_catalog_chirality_pipeline_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Galactic catalog chirality pipeline verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_galactic_chirality_pipeline()
