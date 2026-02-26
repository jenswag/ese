# Enhanced Stokes-Einstein (ESE): functions/driver.py
# Driver
# ---
# Jens Wagner, 05.11.2025
# ----------------------------------------------------------------------------------------------------------------------

# Import Packages and Modules
import torch
import glob

from functions.parser import parse
from functions.models import NN, SE


# Driver
def drive(data):

    data, X, warnings = parse(data)

    data['D_SE'] = SE(data['M_i'] * 1e-3, data['vis_j'] * 1e-3, data['T_j'])
    # data['D_SEGWE'] = SEGWE(data['M_i'] * 1e-3, data['M_j'] * 1e-3, data['vis_j'] * 1e-3, data['T_j'])

    ese = NN()
    params = sorted(glob.glob(f'./params/*.pt'))

    preds = []
    for p in params:
        ese.load_state_dict(torch.load(p, map_location='cpu'))
        with torch.no_grad():
            preds.append(ese(torch.tensor(X, dtype=torch.float)))

    data['D_ESE'] = (torch.mean(torch.stack(preds), dim=0) * SE(data['M_i'] * 1e-3, data['vis_j'] * 1e-3, data['T_j'])).item()
    data['std_ESE'] = (torch.std(torch.stack(preds), dim=0) * SE(data['M_i'] * 1e-3, data['vis_j'] * 1e-3, data['T_j'])).item()

    return data, warnings
