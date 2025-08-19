## Notes on N-Type Semiconductor Physics

### Donor Level Ionization and Carrier Concentrations

**Basic Principles:**
- Due to donor level ionization, electrons in CB (conduction band) increases above $n_i$
- Due to this recombination rate increases and when equilibrium again establishes, then concentration of holes fall below $n_i$ and thus at equilibrium

**Key Relationship for N-Type:**
$$n > n_i > p$$

**Carrier Definitions:**
- **Electrons are majority charge carriers**
- **Holes are minority charge carriers**

### Mathematical Analysis

**Given Parameters:**
- $N_b$ → given (donor concentration)
- $n_i$ → given (intrinsic carrier concentration)

**Basic Equations:**
- $n = N_b + \Delta n$
- $p = \Delta p = \Delta n$
- $n \cdot p = n_i^2$

**Derivation Process:**
Starting from the mass action law:
$$(N_b + \Delta n) \cdot \Delta n = n_i^2$$

Expanding:
$$\Delta n^2 + N_b \Delta n = n_i^2$$

$$\Delta n^2 + N_b \Delta n - n_i^2 = 0$$

**Solution (Quadratic Formula):**
$$\Delta n = \frac{-N_b \pm \sqrt{N_b^2 + 4n_i^2}}{2}$$

**Final Result:**
$$\Delta n = \frac{-N_b + \sqrt{N_b^2 + 4n_i^2}}{2}$$

### Case Analysis

**Case 1: When $N_b > n_i$**
- If difference of power is ≥ 3 ($10^3$), then:
  - $n \approx N_b$
  - $p = \frac{n_i^2}{N_b}$

**Case 2: When $N_b < n_i$**
- Go for exact analysis using the complete quadratic solution

### Electrical Neutrality

**Charge Analysis:**
- $n = N_b + \Delta n$ → $(N_b + \Delta n) \times q$ → **negative charge**
- $p = \Delta p$ → $\Delta p \times q$ → **positive charge**
- $N_b$ → **positive ions** (donor ions) → $N_b \cdot q$ → **positive charge**

**Total Charges:**
- **Total positive charge:** $N_b q + \Delta p q = (N_b + \Delta p) q$
- **Total negative charge:** $(N_b + \Delta n) q$

**Neutrality Condition:**
Total positive charge = Total negative charge

**Conclusion:**
- **N-type semiconductor is electrically neutral**
- The material maintains overall charge neutrality despite having excess electrons as majority carriers

## Notes on N-Type Semiconductor Conductivity

### Conductivity Formula for N-Type Semiconductors

**General Conductivity Expression:**
$$(\sigma)_{n-SC} = \sigma_n + \sigma_p = q(N_D + \Delta n)\mu_n + q\Delta p\mu_p$$

**Expanded Form:**
$$(\sigma)_{n-SC} = qN_D\mu_n + q\Delta n\mu_n + q\Delta p\mu_p \to \text{exact}$$

**Simplified Approximation:**
$$(\sigma)_{n-SC} \approx qN_D\mu_n$$
(when $N_D >> n_i$)

**Condition for Approximation:**
- When $N_D >> n_i$, then $N_D >> \Delta n$ and $N_D >> \Delta p$

### Temperature Effects

**Temperature Increase ($T \uparrow$):**
- $\mu_n \downarrow$ (mobility decreases)
- $\sigma \downarrow$ (conductivity decreases)

**Key Insight:**
In n-type semiconductors, conductivity $\sigma$ decreases with increasing temperature (above room temperature)

### Numerical Example

**Given Values:**
- $N_D = 5 \times 10^{16}/\text{cm}^3$
- $n_i = 1.5 \times 10^{10}/\text{cm}^3$
- $n \approx N_D = 5 \times 10^{16}/\text{cm}^3$
- $p = 4.5 \times 10^3/\text{cm}^3$

**Calculation:**
$$(\sigma)_{n-SC} \approx qN_D\mu_n = 1.6 \times 10^{-19} \times 5 \times 10^{16} \times 1300 = 10.4 \, \Omega^{-1}\text{cm}^{-1}$$

### Hole Conductivity Calculation

**Formula:**
$$\sigma_p = qp\mu_p = 1.6 \times 10^{-19} \times 4.5 \times 10^3 \times 500$$

**Result:**
$$\sigma_p = 3.6 \times 10^{-13} \, \Omega^{-1}\text{cm}^{-1}$$

### Key Relationship

Since $\sigma_n >>> \sigma_p$:
$$(\sigma)_{n-SC} = \sigma_n + \sigma_p \approx \sigma_n$$

**Final Conclusion:**
The total conductivity of an n-type semiconductor is dominated by electron conductivity, as the hole contribution is negligible when the donor concentration is much larger than the intrinsic carrier concentration.

### Summary Points

1. **Dominant Term**: Electron conductivity dominates over hole conductivity in heavily doped n-type semiconductors
2. **Temperature Dependence**: Conductivity decreases with temperature due to reduced carrier mobility
3. **Approximation Validity**: When $N_D >> n_i$, the conductivity can be approximated as $\sigma \approx qN_D\mu_n$
4. **Practical Significance**: This relationship is fundamental for designing semiconductor devices and understanding their electrical behavior