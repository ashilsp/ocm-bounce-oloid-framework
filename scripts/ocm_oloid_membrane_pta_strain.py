"""
OCM SI Model: Oloid Elastic Membrane Resonance & PTA Strain Spectra
Author: Ashil S.
Description: Numerically models the characteristic strain amplitude h_c(f) 
             contrasting standard stochastic SMBHB background (h_c proportional to f^(-2/3)) 
             against the OCM elastic membrane narrowband acoustic resonance peak (nu_OCM).
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_oloid_membrane_pta():
    f = np.linspace(0.1, 10.0, 500) # Frequency domain
    
    # Standard stochastic SMBHB background strain spectrum (h_c ~ f^(-2/3))
    h_smbhb = 1.0 * (f / 1.0) ** (-2.0 / 3.0)
    
    # OCM Elastic Oloid Membrane Resonance peak superimposed
    nu_ocm = 4.5 # Resonant eigenmode frequency
    delta_f = 0.4 # Resonance width
    h_resonance = 1.8 * np.exp(-((f - nu_ocm) ** 2) / (2.0 * delta_f ** 2))
    
    h_ocm_total = h_smbhb + h_resonance
    
    plt.figure(figsize=(10, 5.5), dpi=100)
    plt.loglog(f, h_ocm_total, label=r'OCM Total Strain Spectrum ($h_c \propto f^{-2/3}$ + $\nu_{\text{OCM}}$ Peak)', color='#7c3aed', lw=3.0)
    plt.loglog(f, h_smbhb, label=r'Standard SMBHB Stochastic Background ($h_c \propto f^{-2/3}$)', color='#64748b', linestyle='--', lw=2.0)
    
    plt.axvline(x=nu_ocm, color='#dc2626', linestyle=':', label=r'Oloid Membrane Resonance ($\nu_{\text{OCM}}$)')
    
    plt.title("Oloid Elastic Membrane Resonance & PTA Strain Spectra", fontsize=12, fontweight='bold')
    plt.xlabel("Gravitational Wave Frequency $f$ (Arbitrary Units / nHz scale)", fontsize=10)
    plt.ylabel("Characteristic Strain Amplitude $h_c(f)$", fontsize=10)
    plt.xlim(0.1, 10.0)
    plt.ylim(0.2, 5.0)
    plt.legend(loc='upper right', frameon=True, fontsize=8)
    plt.grid(True, which="both", linestyle=':', alpha=0.5)
    
    output_filename = "ocm_oloid_membrane_pta_strain_model.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Oloid membrane PTA strain verification plot saved as '{output_filename}'")

if __name__ == "__main__":
    simulate_oloid_membrane_pta()
