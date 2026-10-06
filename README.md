# ESE

## Overview

![ESE](images/TOC.png)

This repository contains the implementation of the Enhanced Stokes–Einstein (ESE) model for predicting diffusion coefficients at infinite dilution in pure solvents.
Details are provided in the associated [paper](https://doi.org/10.1039/d6cp00793g).

---

## Repository Structure
```text
ese/
│
├── functions/
│   ├── driver.py       # Prediction workflow logic
│   ├── models.py       # Neural network architecture
│   └── parser.py       # Input processing and validation
│
├── images/
│   └── TOC.png         # TOC figure
│
├── params/
│   ├── ESE_0.pt        # Ensemble member weights
│   ├── ESE_1.pt
│   ├── ...
│   └── ESE_9.pt
│
├── ESE.py              # Main execution script
│
├── LICENSE
├── README.md
└── requirements.txt

```

---

## Installation
```bash
git clone https://github.com/jenswag/ese.git
cd ese
pip install -r requirements.txt
```
---

## Usage
### Define Input
Inputs must be defined directly in ESE.py before execution.<br>
Specify:
```bash
solute = '<SMILES>'     # SMILES Solute i
solvent = '<SMILES>'    # SMILES Solvent j
T = <float>             # Temperature Solvent j [K]
v = <float>             # Viscosity Solvent j [mPas]
```

### Run ESE
```bash
python ESE.py
```

---

## Requirements
All dependencies are listed in requirements.txt

---

## License
This project is licensed under the MIT License. See LICENSE file for details.

---

## Citation
If you use the ESE model in scientific research, please cite the following paper:
```bibtex
@article{Wagner2026ESE,
  title = {Hybrid machine learning for enhanced prediction of diffusion coefficients in liquids},
  ISSN = {1463-9084},
  url = {http://dx.doi.org/10.1039/d6cp00793g},
  DOI = {10.1039/d6cp00793g},
  journal = {Physical Chemistry Chemical Physics},
  publisher = {Royal Society of Chemistry (RSC)},
  author = {Wagner,  Jens and Romero,  Zeno and Münnemann,  Kerstin and Schmitt,  Sebastian and Specht,  Thomas and Hasse,  Hans and Jirasek,  Fabian},
  year = {2026}
}
```