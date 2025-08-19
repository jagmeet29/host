## Mass Action Law in Semiconductors

The **mass action law** is a fundamental principle in semiconductor physics that describes the relationship between electron and hole concentrations in a semiconductor at thermal equilibrium.

## Core Principle

At thermal equilibrium and constant temperature, the **product of electron concentration ($n$) and hole concentration ($p$) is constant** and equals the square of the intrinsic carrier concentration:

$$n \cdot p = n_i^2$$

This relationship holds regardless of doping type or concentration, making it a universal law for semiconductors.

## Applications in Different Semiconductor Types

### Intrinsic (Pure) Semiconductors
- **Electron concentration**: $n = n_i$
- **Hole concentration**: $p = n_i$
- **Verification**: $n \cdot p = n_i \cdot n_i = n_i^2$ ✓

### N-Type Semiconductors
- **Majority carriers**: Electrons
- **Minority carriers**: Holes
- **Electron concentration**: $n \approx N_D$ (doping concentration)
- **Hole concentration**: $p = \frac{n_i^2}{N_D}$

**Key relationship**: $p \propto \frac{1}{N_D} \propto \frac{1}{\text{majority concentration}}$

### P-Type Semiconductors
- **Majority carriers**: Holes
- **Minority carriers**: Electrons
- **Hole concentration**: $p \approx N_A$ (doping concentration)
- **Electron concentration**: $n = \frac{n_i^2}{N_A}$

**Key relationship**: $n \propto \frac{1}{N_A} \propto \frac{1}{\text{majority concentration}}$

## Primary Application

The mass action law is **primarily used to determine minority carrier concentrations** in doped semiconductors. This is crucial because:
- Minority carrier concentration is **inversely proportional** to doping concentration
- Higher doping reduces minority carrier concentration
- This relationship is essential for understanding semiconductor device behavior

## Physical Significance

The law demonstrates that increasing the concentration of one type of carrier (through doping) automatically decreases the concentration of the other type, while maintaining the constant product $n_i^2$ at a given temperature. This balance is fundamental to semiconductor device operation and design.
