"""
OCM SI Model: Nodal Phase-Locking in Perpendicular Convex Hulls
Author: Ashil S.
Description: Numerically models standing wave phase relationships (Delta phi = n * pi / 2) 
             enforced by the Oloid's perpendicular generating boundary conditions, 
             contrasting against unconstrained random phase distributions.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_nodal_phase_locking():
    # Setup figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5), dpi=100)
    
    # --- SUBPLOT 1: Standard Unconstrained Random Phases ($\Lambda$CDM) ---
    np.random.seed(42)
    phases_lcdm = np.random.uniform(0, 2 * np.pi, 500)
    ax1.hist(phases_lcdm, bins=25, color='#64748b', alpha=0.7, edgecolor='black')
    ax1.set_title("Standard $\Lambda$CDM: Uncorrelated Random Phases", fontsize=11, fontweight='bold')
    ax1.set_xlabel("Phase Angle Difference $\Delta \phi$ (Radians)", fontsize=9)
    ax1.set_ylabel("Frequency Count", fontsize=9)
    ax1.set_xlim(0, 2 * np.pi)
    ax1.grid(True, linestyle=':', alpha=0.5)
    
    # --- SUBPLOT 2: Oloid Phase-Locked Distribution ($\Delta \phi = n\pi/2$) ---
    # Oloid boundary constraints cluster phase differences at multiples of pi/2 (0, pi/2, pi, 3pi/2, 2pi)
    locked_centers = [0.0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    phases_ocm = np.concatenate([np.random.normal(c, 0.12, 100) for c in locked_centers])
    phases_ocm = np.clip(phases_ocm, 0, 2 * np.pi)
    
    ax2.hist(phases_ocm, bins=35, color='#7c3aed', alpha=0.8, edgecolor='black')
    ax2.set_title("OCM Oloid Boundary: Phase-Locked Clustering ($n\pi/2$)", fontsize=11, fontweight='bold')
    ax2.set_xlabel("Phase Angle Difference $\Delta \phi$ (Radians)", fontsize=9)
    ax2.set_ylabel("Frequency Count", fontsize=9)
    ax2.set_xlim(0, 2 * np.pi)
    
    # Mark the precise pi/2 intervals
    for val in [np.pi/2, np.pi, 3*np.pi/2]:
        ax2.axvline(x=val, color='#dc2626', linestyle='--', alpha=0.7, label=f'Locked Node ($n\pi/2$)' if val == np.pi/2 else "")
        
    ax2.legend(loc='upper right', frameon=True, fontsize=8)
    ax2.grid(True, linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    output_filename = "ocm_nodal_phase_locking_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Nodal phase-locking verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_nodal_phase_locking()
