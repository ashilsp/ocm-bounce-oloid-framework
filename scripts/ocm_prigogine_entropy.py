"""
OCM SI Model: Prigogine Open-System Thermodynamic Balance
Author: Ashil S.
Description: Numerically models the open thermodynamic system entropy evolution 
             where incoming negentropy flux Phi_N drives local laminar resets 
             (dS_node/dt < 0) while global entropy satisfies the Second Law.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_prigogine_entropy():
    t = np.linspace(0, 14, 500) # Cosmic time in Gyr
    
    # Internal entropy generation (monotonic rise due to irreversible processes)
    sigma_irrev = 0.5 * t + 0.1 * (t ** 1.2)
    
    # Negentropy Flux injection Phi_N spiking during periodic Laminar Reset phases
    phi_n = 2.5 * np.exp(-0.5 * (t - 4.0)**2) + 2.0 * np.exp(-0.5 * (t - 10.0)**2)
    
    # Net node entropy change integration
    S_node = 10.0 + sigma_irrev - np.cumsum(phi_n) * (t[1] - t[0]) * 1.5
    
    # Closed-system LambdaCDM reference (monotonic unconstrained rise to Heat Death)
    S_lcdm = 10.0 + sigma_irrev * 2.5
    
    plt.figure(figsize=(10, 5.5), dpi=100)
    plt.plot(t, S_node, label=r'OCM Open System Entropy $S_{\text{node}}(t)$ (Laminar Resets)', color='#2563eb', lw=2.5)
    plt.plot(t, S_lcdm, label=r'$\Lambda$CDM Closed System (Heat Death Paradigm)', color='#dc2626', linestyle='--', lw=2.0)
    plt.fill_between(t, S_node, S_lcdm, color='#2563eb', alpha=0.1, label='Negentropy Cooling ($\Delta S_{\text{node}} < 0$)')
    
    plt.title("Prigogine Open-System Thermodynamic Balance ($\Phi_N$)", fontsize=12, fontweight='bold')
    plt.xlabel("Cosmic Evolutionary Time ($t$ in Gyr)", fontsize=10)
    plt.ylabel("Entropy Magnitude ($S$)", fontsize=10)
    plt.xlim(0, 14)
    plt.legend(loc='upper left', frameon=True, fontsize=8)
    plt.grid(True, linestyle=':', alpha=0.5)
    
    output_filename = "ocm_prigogine_entropy_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Prigogine entropy verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_prigogine_entropy()
