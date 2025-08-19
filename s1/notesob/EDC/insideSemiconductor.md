## What is an Intrinsic Semiconductor?

An **intrinsic semiconductor** is a pure semiconductor material without any impurities. In the case of silicon:
- Silicon has $4$ valence electrons in its outer shell
- Each silicon atom forms four covalent bonds with neighboring silicon atoms to complete its octet
- This creates a regular crystal lattice structure where all electrons are bound in covalent bonds

## Temperature Effects on Semiconductor Behavior

## At Absolute Zero ($T = 0K$)

At absolute zero temperature, pure silicon acts as a **perfect insulator**:
- **Valence Band (VB)**: Completely filled with electrons
- **Conduction Band (CB)**: Completely empty
- **Band Gap Energy**: $E_g = 1.21$ eV
- **Carrier Concentrations**: $n = 0$ (no free electrons), $p = 0$ (no holes)

The thermal energy available is extremely small, so no covalent bonds break, and no charge carriers are generated.

## At Room Temperature ($T \neq 0K$)

When temperature increases above absolute zero:
- **Thermal energy becomes available** to break covalent bonds
- At $300K$ (room temperature):
  - Thermal voltage: $V_T = 0.026V$
  - Thermal energy: $kT = 0.026$ eV
  - Band gap energy: $E_g = 1.1$ eV (temperature-dependent)

## Charge Carrier Generation and Movement

## Ionization Process

**Ionization** is the process of breaking a covalent bond, which:
- Generates a **free electron** that moves to the conduction band
- Creates a **hole** (positive charge) in the valence band
- Results in an **electron-hole pair (EHP)**

## The Concept of Holes

When a covalent bond breaks:
- One electron becomes free and mobile
- The remaining deficiency of electrons creates a **hole**
- A hole behaves as a **positive charge** with magnitude $1.6 \times 10^{-19}$ coulombs
- Holes can move through the crystal as electrons from neighboring atoms fill the vacancy

## Thermal Generation and Recombination

## Thermal Generation

At a **fixed temperature**, thermal energy is constantly supplied to the crystal:
- **Thermal generation rate**: The number of electron-hole pairs generated per second due to thermal energy
- This rate depends on temperature and increases with increasing temperature
- The process is continuous as long as thermal energy is available

## Recombination Process

**Recombination** is the opposite of ionization:
- Free electrons and holes **attract each other** due to opposite charges
- An electron **falls from the conduction band to the valence band**
- This **eliminates both** the free electron and the hole
- **Recombination rate**: The number of electron-hole pairs that recombine per second

## Equilibrium in Intrinsic Semiconductors

In an intrinsic semiconductor at thermal equilibrium:
- The **generation rate equals the recombination rate**
- The number of free electrons equals the number of holes: $n = p$
- This maintains a constant carrier concentration at a given temperature
- As temperature increases, both generation and the equilibrium carrier concentrations increase

This fundamental understanding of intrinsic semiconductors forms the basis for understanding how doped semiconductors work and how electronic devices like diodes and transistors function.

## Recombination Rate in Pure Semiconductors

**Key Formula**

**Recombination rate = $α_r × n_i × n_i = α_r n_i^2$**

Where:
- $α_r$ = recombination constant
- $n_i$ = intrinsic carrier concentration
- At thermal equilibrium: $n = p = n_i$

## Important Note

The **thermal generation rate** at any temperature $T$ is $α_r n_i^2$, which applies to:
- Pure semiconductors
- Doped semiconductors

This is a fundamental relationship that remains constant regardless of doping.

## Conductivity and Temperature Relationship

**Conductivity Formula**

$σ_i = σ_n + σ_p = q n_i μ_n + q n_i μ_p$

Simplified to:

$σ_i = q n_i [μ_n + μ_p]$

## For Silicon at Room Temperature

$σ_i = 4.32 × 10^{-6} Ω^{-1} cm^{-1}$

This is a **very low value**, making intrinsic silicon practically useless for most electronic applications.

## Mobility Values for Silicon

- **Electron mobility ($μ_n$)**: $1300 cm^2/V-sec$ at room temperature
- **Hole mobility ($μ_p$)**: $500 cm^2/V-sec$ at room temperature

## Temperature Effects on Semiconductor Properties

As Temperature Increases ($T↑$):

1. **Carrier Concentration ($n_i↑$)**:
   - More thermal energy available to break covalent bonds
   - Exponential increase in intrinsic carrier concentration

2. **Mobility Decreases ($μ↓$)**:
   - Increased thermal motion causes more scattering
   - Reduced carrier mobility due to lattice vibrations

## Net Effect on Conductivity

Despite mobility decreasing with temperature, the **dramatic increase in carrier concentration** dominates, resulting in:

$T↑ → σ_i↑$ (Overall conductivity increases with temperature)

This is expressed in the boxed relationship:

$T↑, σ_i↑$

## Practical Implications

### Why Intrinsic Silicon Has Limited Use

1. **Extremely low conductivity** ($4.32 × 10^{-6} Ω^{-1} cm^{-1}$)
2. **Strong temperature dependence** makes it unreliable
3. **Cannot be controlled** for practical applications

### The Need for Doping

The low and uncontrollable conductivity of intrinsic semiconductors necessitates **doping** (adding impurities) to:
- Increase conductivity to useful levels
- Control electrical properties
- Create the foundation for electronic devices

## Dynamic Equilibrium

At any given temperature, the semiconductor maintains **dynamic equilibrium** where:
- **Generation rate = Recombination rate**
- Constant average number of charge carriers
- Continuous creation and annihilation of electron-hole pairs
- The balance shifts with temperature changes

This understanding of thermal equilibrium and generation-recombination processes is crucial for comprehending how temperature affects semiconductor behavior and why doping is essential for practical semiconductor devices.

