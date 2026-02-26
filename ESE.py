# Enhanced Stokes-Einstein (ESE): ESE.py
# ESE Ensemble
# ---
# Jens Wagner, 05.11.2025
# ----------------------------------------------------------------------------------------------------------------------

# Import Packages and Modules
from functions.driver import drive

# === INPUT ===
solute = 'COCCOCCOC'     # SMILES Solute i
solvent = 'CCCCCCCCCCCC'   # SMILES Solvent j
T = 298.15  # Temperature Solvent j [K]
v = 1.348       # Viscosity Solvent j [mPas]
# ===

# === Run ESE ===
data = {'SMILES_i': solute,
        'SMILES_j': solvent,
        'T_j': T,
        'vis_j': v,
        }

data, warnings = drive(data)

# === OUTPUT ===
block = ''
if warnings:
    lines = "\n".join(warnings)
    block = f"\nWarning!\n--------\n{lines}\n"

txt = f'''ESE - Enhanced Stokes-Einstein
-------------------------

Input
-----
Solute i: {data['SMILES_i']}
Solvent j: {data['SMILES_j']}
Temperature / K: {data['T_j']}
Viscosity / mPas: {data['vis_j']}
{block}
Results for D^inf_ij / m^2s * 10^9
-----
{data['D_ESE'] * 1e9:.2f}
'''

print(txt)
