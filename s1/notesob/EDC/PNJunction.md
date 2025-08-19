## PN Junction Basics

* **PN Junction Formation:** Created by joining p-type and n-type semiconductor regions within a *single crystal*.
- **Metallurgical junction** at $x = 0$
    - Large density gradient in hole and electron concentrations
    - Initial diffusion of holes and electrons across the junction
    - Charge separation creates an electric field
- **Thermal Equilibrium**
    - Diffusion of holes and electrons ceases
    - Electric field force balances the density gradient force
    - **Space-charge region (depletion region)**
        - Contains no mobile electrons or holes
        - Potential difference (built-in potential barrier, $V_{bi}$)

>[!question]  where does the Electric filed comes form ?
>
>>[!success]- Answer
>>The electric field forms due to **charge separation** at the PN junction. 
>>
>>Initially, holes diffuse from the P-side to the N-side, and electrons from N to P, *uncovering* fixed charges (positive ions in N, negative in P). This separation of charge creates an electric field pointing from the positive to negative charge.

| ![[PN Junction.png]] |
| -------------------- |
| ![[Diffusion.png]]   |
| ![[Thermal Eq.png]]  |

### Depletion Region & Built-in Potential

* **Diffusion:** 
    - Holes diffuse from p-region to n-region.
    - Electrons diffuse from n-region to p-region.
* **Charge Separation:** Diffusion uncovers ionized acceptor (p-side) and donor (n-side) atoms, creating a charge separation. 
* **Space Charge/Depletion Region:** Region depleted of mobile carriers due to charge separation.
* **Built-in Potential ($V_{bi}$):** Potential difference across the depletion region.  $$V_{bi} = \frac{kT}{e} \ln{\frac{N_a N_d}{n_i^2}} =VT \ln{\frac{N_a N_d}{n_i^2}}$$
    -  $VT = {kT \over e} \approx 0.026 V$ at $T = 300K$ (thermal voltage).
    - $Na$: Acceptor concentration (p-region).
    - $Nd$: Donor concentration (n-region).
    - $ni$: Intrinsic carrier concentration.
* **Measurement of $V_{bi}$:** Cannot be directly measured with a voltmeter due to new potential barriers forming at the probe contacts. It maintains equilibrium, hence no current.
* **Importance of $V_{bi}$:**  Crucial parameter when applying external bias (forward/reverse).


---

![[Reverse Bias.png]]
## Reverse-Biased pn Junction - Revision Notes

* **Reverse Bias Definition:** Applying a positive voltage to the n-region (or negative to p-region) of a pn junction.
* **Electric Field:**
    - Applied voltage $V_R$ induces electric field $E_A$.
    - $E_A$ adds to the existing E-field in the space-charge region.
    -  Increased $E_A$ hinders majority carrier flow, resulting in minimal current.
* **Space-Charge Region:**
    - Increasing $V_R$ increases the electric field & hence, the number of fixed charges in the space-charge region. 
    -  Since doping is constant, increased charge means increased space-charge width $W$. 
    - $W$ increases with $V_R$.
* **Junction Capacitance ($C_j$):**
    - Increased charges in the space-charge region create capacitance.
    - $$C_j = C_{jo} \left(1 + \frac{V_R}{V_{bi}}\right)^{-1/2}$$ 
    - $C_{jo}$ = Junction capacitance at zero applied voltage.
    - $V_{bi}$ = Built-in potential.
* **Impact of Capacitance:**
    - Affects switching characteristics (voltage change isn't instantaneous).
    - Useful in electrically tunable resonant circuits.
* **Varactor Diodes:** 
    - PN junctions designed for variable capacitance. 
    - Applications: tunable oscillators (Hartley), tuned amplifiers.
* **Breakdown:**
    - $E$-field and $V_R$ have limits.
    -  Exceeding these limits leads to breakdown and large reverse current. (Detailed later)

---

| ![[Forward Biased PN Junction.png]]           |
| --------------------------------------------- |
| ![[Steady State minority charge carrier.png]] |

## Forward Biased pn Junction 

**I. Equilibrium State**

*  n-region: High free electron concentration.
*  p-region: High hole concentration.
*  Built-in potential barrier: Prevents majority carrier diffusion, maintaining equilibrium.

**II. Forward Bias**

- The electric ﬁelds in the space-charge region are very large compared to those in the remainder of the p & n regions.
- essentially all of the applied voltage exists across the pn junction region.
* Positive voltage ($v_D$) applied to p-region *reduces* the potential barrier.
* Applied electric field ($E_A$) opposes the thermal equilibrium space-charge field. 
* Net electric field remains from n to p.
* Majority carriers diffuse across the junction, creating current. Analogy: lowering a dam wall.
* $v_D$ must be less than the built-in potential barrier ($V_{bi}$).
* Majority carriers become minority carriers in the opposite region, *increasing* minority carrier concentration.

## Current-Voltage Relationship

* Diode current equation: 
    $$i_D = I_S [e^{\frac{v_D}{n V_T}} - 1]$$ 
* $I_S$: Reverse-bias saturation current ($10^{-18}$ to $10^{-12}$ A for silicon). Depends on doping and junction area.
* $V_T$: Thermal voltage ≈ 0.026 V at room temperature.
* n: Emission coefficient (ideality factor), $1 \le n \le 2$.
    * Accounts for recombination in the space-charge region.
    * n ≈ 2 at very low currents (significant recombination).
    * n ≈ 1 at higher currents. (assume n=1 unless otherwise stated).

---


| ![[PN Junction Diode.png\|190]] | ![[VI of pn Junction.png\|500]] | ![[Forward Biased IV Ideal.png\|500]] |
| ----------------------------------------- | ------------------------------- | ------------------------------------- |
## pn Junction Diode 

* **Current-Voltage Characteristics:**
    
	- **Forward Bias:** 
	    - Current is an exponential function of voltage. Small voltage change leads to large current change.
	    - Small change in forward-bias voltage results in a significant increase in current.
	    * For $v_D > +0.1 V$, the $-ve$ term in $i_D$ can be neglected.
    - **Reverse Bias:** 
	    - Current is almost zero.

* **Diode as a Switch:**
    - Acts as a voltage-controlled switch: 
        - “Off” for reverse bias
        - “On” for forward bias 
    - Forward state: Large current for small voltage.
    - Reverse state: Very small current.

* **Reverse Bias Current:**
    -  $i_D = -I_S$ when $V_D < -0.1V$. (Ideal case) 
    - $I_S$ is the reverse saturation current.
    - Real diodes have additional 'generation current' due to electron-hole pair creation in depletion region.
    - Typical $I_S$ ~ $10^{-14}A$, but reverse current can be ~ $10^{-9}A$ (1nA) due to generation current.
    - Generation current is still generally small and negligible.

---

## Temperature Effects on Diode Characteristics

* Temperature impacts both $I_S$ and $V_T$, thus altering diode characteristics.
* For a given current, forward-bias voltage *decreases* with increasing temperature (approx. 2 mV/°C for silicon).
* $I_S$ is dependent on intrinsic carrier concentration ($n_i$), which is strongly temperature-dependent.
* $I_S$ approximately *doubles* for every 5°C increase in temperature.
* Actual Reverse-bias current approximately *doubles* for every 10°C rise in temperature.
*  Germanium diodes have large $I_S$ & are impractical due to significant reverse current increase with temperature.

## Breakdown Voltage

![[Forward and Revered VI.png]]

* Breakdown occurs when reverse bias causes electric field in depletion region to break covalent bonds, creating electron-hole pairs. 
* This leads to a large reverse current, limited by external circuit. 
*  Excessive current can cause device burnout.

* **Avalanche Breakdown:**
    * Occurs when carriers gain enough kinetic energy from high electric field to break bonds via collisions.
    *  Creates an *avalanche* of electron-hole pairs.
    * Breakdown voltage influenced by doping concentrations – *higher doping = lower breakdown voltage*.

![[Avalanche Breakdown.png]]

* **Zener Breakdown:**
    * Results from carrier *tunneling* across the junction.
    *  Prominent at very high doping concentrations ($< 5V$).

* Breakdown voltage typically ranges from 50-200V, but can vary widely (up to >1000V).
* **PIV (Peak Inverse Voltage):**  The maximum reverse voltage a diode can withstand without breakdown. *Must not be exceeded in circuit operation*.
* **Zener Diodes:** Specifically designed to operate in the breakdown region. 

---

## PN Junction Diode Transient Response - Revision Notes

**Forward Bias (t < 0):**
* Current: $i_D = I_F = \frac{V_F - v_D}{R_F}$

**Switching from Forward to Reverse Bias:**
* **Excess Minority Carrier Charge:** Stored in p & n regions during forward bias; must be removed during reverse switching.
* **Initial Reverse Current:** Due to excess carriers flowing back across the junction. Limited by $R_R$: $i_D = -I_R \approx -\frac{V_R}{R_R}$.
* **Storage Time ($t_s$):** Time for minority carrier concentrations at the space charge region edges to reach thermal equilibrium.
* **Fall Time ($t_f$):** Time for current to fall to 10% of its initial value. 
* **Total Turn-Off Time:** $t_s + t_f$
* **Junction Capacitance:** Prevents instantaneous voltage change.

**Key Factors for Fast Switching:**
* Small excess minority carrier lifetime.
* Large reverse current pulse.
* Circuit design *must* provide a path for this transient current.

**Turn-On Transient (Reverse to Forward Bias):**
* Time required to establish forward-bias minority carrier distributions.
* Voltage across junction gradually increases to steady-state value.
* Generally faster than turn-off time. 



