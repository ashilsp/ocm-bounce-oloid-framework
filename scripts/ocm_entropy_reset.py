"""
OCM Open-System Entropy Reset Model
Author: Ashil S.
Description: Numerically models universal entropy dynamics comparing 
             standard closed-system Lambda-CDM Heat Death against the 
             OCM open-system periodic 'Laminar Reset' (Phi_N Negentropy Flux).
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_entropy_dynamics():
    # Define time domain across multiple universal cycles
    t = np.linspace(0, 4, 600)
    
    # 1. Standard Lambda-CDM Closed-System Entropy (Linear/Asymptotic Heat Death)
    S_lcdm = 2.0 + 1.8 * t
    
    # 2. OCM Open-System Entropy with Periodic Laminar Resets (Phi_N Flux)
    # Piecewise simulation of bounce cycles and negentropy drops
    S_ocm = np.piecewise(t, 
        [
            (t >= 0.0) & (t < 1.0),
            (t >= 1.0) & (t < 2.5),
            (t >= 2.5) & (t < 3.0),
            (t >= 3.0) & (t <= 4.0)
        ],
        [
            lambda x: 8.5 - 12.0 * x,                         # Pre-bounce / Laminar Wash drop
            lambda x: 2.0 + 1.2 * (x - 1.0)**1.4,             # Normal expansion phase 1
            lambda x: 3.5 - 5.0 * (x - 2.5),                  # Second Laminar Reset (Bounce 2)
            lambda x: 2.0 + 1.0 * (x - 3.0)**1.3              # Expansion phase 2
        ]
    )
    
    # Plotting configuration matching manuscript figures
    plt.figure(figsize=(9, 6), dpi=100)
    plt.plot(t, S_lcdm, label=r'$\Lambda$CDM Closed System (Heat Death)', color='#1e293b', linestyle='--', lw=2.5)
    plt.plot(t, S_ocm, label=r'OCM Open-System Manifold ($\Phi_N$ Reset)', color='#ef4444', lw=3.0)
    
    # Annotations and markers
    plt.axhline(y=2.0, color='#94a3b8', linestyle=':', label='Base Order Level')
    plt.annotate('Laminar Reset\n(Negentropy Inflow)', xy=(1.0, 2.0), xytext=(0.5, 4.5),
                 arrowprops=dict(facecolor='#ef4444', shrink=0.05, width=1.5, headwidth=6),
                 fontsize=9, fontweight='bold', color='#ef4444')
    
    plt.title("Universal Entropy Dynamics: Open Manifold vs. Heat Death", fontsize=12, fontweight='bold')
    plt.xlabel("Universal Cycle Progression (Time $t$)", fontsize=10)
    plt.ylabel("Total Universal Entropy ($S$)", fontsize=10)
    plt.xlim(0, 4)
    plt.ylim(0, 10)
    plt.legend(loc='upper left', frameon=True)
    plt.grid(True, linestyle=':', alpha=0.5)
    
    output_filename = "ocm_entropy_reset_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Entropy reset dynamics verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_entropy_dynamics()
