> [!question] Q1) (a) Show the AOI implementation of a 2:1 Mux?  
> (b) Convert this to 2-input NAND implementation?
> 
> > [!success]- Answer  
> > (a) For a 2:1 mux with inputs I0, I1 and select line S, the output is:
> > 
> > ```
> > Out = S’·I0 + S·I1
> > ```
> > 
> > The AND-OR (AOI) implementation uses two AND gates and one OR gate: one AND gate implements S’·I0, another implements S·I1, and their outputs feed into an OR gate.
> > 
> > (b) The NAND-only implementation uses De Morgan’s laws. First implement the AND terms with NAND gates followed by negation, then feed into a NAND to realize the OR. Concretely:
> > 
> > 1. Generate A1 = NAND(S’, I0)
> >     
> > 2. Generate A2 = NAND(S, I1)
> >     
> > 3. Then Out = NAND(A1, A2)
> >     


> [!question] Q2) Design the following gates using the minimum number of 2:1 Muxes:  
> (a) NOT  
> (b) AND  
> (c) OR  
> (d) XOR
> 
> > [!success]- Answer  
> > (a) **NOT Gate**  
> > Use a single 2:1 Mux with select tied to the input A. Tie I0 = 1, I1 = 0. Then Out = A’ (because when A=0, select=0 → I0=1, when A=1, select=1 → I1=0).
> > 
> > (b) **AND Gate**  
> > Use two 2:1 Muxes:
> > 
> > 4. First Mux: select = A, I0 = 0, I1 = B → outputs A·B.  
> >     That single Mux already implements AND (because when A=0, Out=0; when A=1, Out=B). So only one Mux is needed.
> >     
> > 
> > (c) **OR Gate**  
> > Use two 2:1 Muxes:
> > 
> > 5. First Mux: select = A, I0 = B, I1 = 1.
> >     
> >     - When A=0 → Out=B; when A=1 → Out=1.  
> >         This yields A + B. So only one Mux suffices.
> >         
> > 
> > (d) **XOR Gate**  
> > Use two 2:1 Muxes:
> > 
> > 1. First Mux: select = A, I0 = B, I1 = B’ → produces A⊕B.  
> >     Actually, to compute A⊕B:
> >     
> > 
> > - When A=0 → Out = B
> >     
> > - When A=1 → Out = B’  
> >     Then Out = A⊕B. But B’ requires another Mux (or inverter) in front. Using a second 2:1 Mux as inverter on B: select = B, I0 = 1, I1 = 0 yields B’.  
> >     Thus total = 2 Muxes.
> >     


> [!question] Q3) Construct a 16:1 Mux with two 8:1 Muxes and one 2:1 Mux.
> 
> > [!success]- Answer  
> > Label the four select lines S₃,S₂,S₁,S₀ such that S₃ = MSB.
> > 
> > 1. Feed inputs I₀…I₇ into the first 8:1 Mux with select lines S₂,S₁,S₀. Call its output Y₀.
> >     
> > 2. Feed inputs I₈…I₁₅ into the second 8:1 Mux with the same selects S₂,S₁,S₀. Call its output Y₁.
> >     
> > 3. Finally, use a 2:1 Mux with select = S₃, I0 = Y₀, I1 = Y₁. Output = Y.  
> >     When S₃=0, the top 8:1 Mux output is chosen; when S₃=1, the bottom 8:1 Mux output is chosen.
> >     


> [!question] Q4) Find the simplified expression for Y in terms of A, B and C.
> 
> > [!success]- Answer  
> > Given:
> > 
> > ```
> > Y = A’B’C + A’BC’ + AB’C’ + ABC
> > ```
> > 
> > Group terms: those with exactly one or three variables true. That simplifies to:
> > 
> > ```
> > Y = A ⊕ B ⊕ C
> > ```


> [!question] Q5) Design a circuit for the 3-input majority function using a 4:1 Mux.
> 
> > [!success]- Answer  
> > The majority function is 1 when at least two inputs are 1. Let A, B, C be inputs. Observe:
> > 
> > - If A = B = 0 → output = 0 (regardless of C).
> >     
> > - If A = B = 1 → output = 1 (regardless of C).
> >     
> > - If A ≠ B → output = C.  
> >     Use A and B as the two select lines for a 4:1 Mux (say S₁ = A, S₀ = B). Then set:
> >     
> > 
> > ```
> > I₀ (A=0,B=0) → 0  
> > I₁ (A=0,B=1) → C  
> > I₂ (A=1,B=0) → C  
> > I₃ (A=1,B=1) → 1
> > ```
> > 
> > The Mux output is then the majority: Y = AB + BC + AC.


> [!question] Q6) (a) Expand the Boolean function f(x,y,z) = x’z’ + xy + xz in terms of x using Shannon’s expansion.  
> (b) Implement f using a 2:1 Mux and external gates.
> 
> > [!success]- Answer  
> > (a) Compute cofactors:
> > 
> > ```
> > f(1,y,z) = (1)’·z’ + 1·y + 1·z = y + z  
> > f(0,y,z) = (0)’·z’ + 0·y + 0·z = z’  
> > ```
> > 
> > So by Shannon’s theorem:
> > 
> > ```
> > f(x,y,z) = x·(y + z) + x’·(z’)
> > ```
> > 
> > (b) Use x as the select line of a 2:1 Mux:
> > 
> > - When x = 1 → Mux outputs (y + z) (computed by an OR gate on y, z).
> >     
> > - When x = 0 → Mux outputs z’ (computed by an inverter on z).  
> >     Thus f is realized with one Mux, one OR gate, one inverter.
> >     


> [!question] Q7) There is a single telephone which needs to transmit data from 8 different users to the receiving end. Give a design that accomplishes this task.
> 
> > [!success]- Answer  
> > Use an 8:1 Mux at the transmitter side to time-division-multiplex the 8 user data lines into the single telephone line. On the receiver side, use an 1:8 demultiplexer (or 3-bit counter plus de-Mux) to select which user’s data is forwarded at each time slot. A common 3-bit counter running at the same clock on both ends drives the Mux select and Demux select lines, ensuring correct user selection.


> [!question] Q8) You are given a 2:4 decoder, a 2-input OR gate, and a 3-input OR gate. Using these components, design a system which takes A & B as inputs and generates the following four outputs: AB, (AB)’, A+B, (A+B)’.
> 
> > [!success]- Answer
> > 
> > 1. The 2:4 decoder with inputs A, B produces outputs:
> >     
> >     - D₀ = A’·B’ = (A + B)’
> >         
> >     - D₁ = A’·B = A’B
> >         
> >     - D₂ = A·B’ = AB’
> >         
> >     - D₃ = A·B = AB
> >         
> > 2. AB is directly available at D₃.
> >     
> > 3. (A + B)’ = A’·B’ is directly available at D₀.
> >     
> > 4. A + B is generated by feeding A, B into the 2-input OR gate.
> >     
> > 5. (AB)’ = A’ + B’ = A’B + AB’ + A’B’. Use the 3-input OR gate with inputs: D₁ (A’B), D₂ (AB’), and D₀ (A’B’).  
> >     Thus all four outputs are realized.
> >     


> [!question] Q9) Give the truth table for (a) a half-adder and (b) a half-subtractor.
> 
> > [!success]- Answer  
> > (a) **Half-Adder** (inputs A, B; outputs Sum, Cout)
> > 
> > ```
> > A B | Cout Sum  
> > 0 0 |  0    0  
> > 0 1 |  0    1  
> > 1 0 |  0    1  
> > 1 1 |  1    0  
> > ```
> > 
> > (b) **Half-Subtractor** (inputs A, B; outputs Diff, Bout)
> > 
> > ```
> > A B | Bout Diff  
> > 0 0 |  0    0  
> > 0 1 |  1    1  
> > 1 0 |  0    1  
> > 1 1 |  0    0  
> > ```


> [!question] Q10) Design a circuit for a half-subtractor using basic gates.
> 
> > [!success]- Answer  
> > From Q9(b):
> > 
> > ```
> > Diff = A ⊕ B  
> > Bout = A’ · B  
> > ```
> > 
> > Implement Diff using one XOR gate. Implement Bout using one AND gate with inputs (A’, B), where A’ comes from an inverter on A.


> [!question] Q11) Design an "OR" gate using half-adders.
> 
> > [!success]- Answer  
> > Let HA₁ and HA₂ be two half-adders.
> > 
> > 6. Feed A and B into HA₁: Sum₁ = A ⊕ B, Cout₁ = A·B.
> >     
> > 7. Feed Sum₁ and Cout₁ into HA₂: Sum₂ = Sum₁ ⊕ Cout₁. One can verify:
> >     
> > 
> > ```
> > Sum₂ = (A ⊕ B) ⊕ (A·B) = A + B.  
> > ```
> > 
> > Thus the Sum output of HA₂ is A OR B. (Cout outputs can be ignored.)


> [!question] Q12) Design a full‐adder using two half-adders and the minimum number of external gates.
> 
> > [!success]- Answer  
> > Let A, B, C be inputs.
> > 
> > 8. HA₁: inputs A, B → Sum₁ = A ⊕ B, Cout₁ = A·B.
> >     
> > 9. HA₂: inputs Sum₁, C → Sum = (A ⊕ B) ⊕ C, Cout₂ = Sum₁·C.
> >     
> > 10. Final Cout = Cout₁ + Cout₂ (OR gate).  
> >     So we use two half-adders and one 2-input OR gate.
> >     


> [!question] Q13) Implement a full‐adder using two 4:1 Muxes.
> 
> > [!success]- Answer  
> > A full‐adder has Sum = A ⊕ B ⊕ C and Cout = AB + BC + AC. One can implement each output using a 4:1 Mux as follows:
> > 
> > **Sum Mux**: Let S₁ = A, S₀ = B. Define inputs:
> > 
> > ```
> > I₀ = C    (when A=0,B=0 → Sum = C)  
> > I₁ = C’   (when A=0,B=1 → Sum = ¬C)  
> > I₂ = C’   (when A=1,B=0 → Sum = ¬C)  
> > I₃ = C    (when A=1,B=1 → Sum = C) xor’d with 1?  
> > ```
> > 
> > Actually simpler: implement X = A⊕B by one 4:1 Mux (select=A,B, inputs {0,1,1,0}). Then feed X, C into another Mux to do X⊕C.
> > 
> > **Cout Mux**: implement AB + BC + AC by feeding two Muxes in a similar style. For brevity:
> > 
> > - Use first 4:1 Mux with select=A,B and I₀=0, I₁=C, I₂=C, I₃=1 → this outputs M = BC + AC.
> >     
> > - Use second 4:1 Mux: select = M, C (treat M as MSB, C as LSB) and inputs {0,1,1,1} → outputs Cout.  
> >     (Any equivalent two-Mux realization earning minimal logic qualifies.)
> >     


> [!question] Q14) A full-adder can be implemented using basic gates in many ways. Show the efficient implementation that needs minimal hardware.
> 
> > [!success]- Answer  
> > Use the equations:
> > 
> > ```
> > Sum = (A ⊕ B) ⊕ C  
> > Cout = AB + (A ⊕ B)·C  
> > ```
> > 
> > 1. Compute P = A ⊕ B (one XOR).
> >     
> > 2. Compute Sum = P ⊕ C (second XOR).
> >     
> > 3. Compute G = A · B (one AND).
> >     
> > 4. Compute H = P · C (one AND).
> >     
> > 5. Compute Cout = G + H (one OR).  
> >     Total: 2 XORs, 2 ANDs, 1 OR.
> >     


> [!question] Q15) Implement a circuit for adding two 4-bit numbers using (a) Ripple-carry adder, (b) Carry-look-ahead (CLA) adder.
> 
> > [!success]- Answer  
> > (a) **Ripple-carry adder**: Cascade four full-adder blocks. Let inputs be A₃…A₀, B₃…B₀, and C₀ (initial carry).
> > 
> > - FA₀ adds A₀,B₀,C₀ → produces Sum₀ and C₁.
> >     
> > - FA₁ adds A₁,B₁,C₁ → produces Sum₁ and C₂.
> >     
> > - FA₂ adds A₂,B₂,C₂ → produces Sum₂ and C₃.
> >     
> > - FA₃ adds A₃,B₃,C₃ → produces Sum₃ and C₄ (final carry).
> >     
> > 
> > (b) **Carry-look-ahead (CLA) adder**:  
> > For each bit i = 0..3:
> > 
> > ```
> > Pᵢ = Aᵢ ⊕ Bᵢ  
> > Gᵢ = Aᵢ · Bᵢ
> > ```
> > 
> > Then compute carries in parallel:
> > 
> > ```
> > C₁ = G₀ + P₀·C₀  
> > C₂ = G₁ + P₁·G₀ + P₁·P₀·C₀  
> > C₃ = G₂ + P₂·G₁ + P₂·P₁·G₀ + P₂·P₁·P₀·C₀  
> > C₄ = G₃ + P₃·G₂ + P₃·P₂·G₁ + P₃·P₂·P₁·G₀ + P₃·P₂·P₁·P₀·C₀  
> > ```
> > 
> > Then Sumᵢ = Pᵢ ⊕ Cᵢ for each i.


> [!question] Q16) Compare the two implementations of Q15.
> 
> > [!success]- Answer
> > 
> > - **Ripple-carry adder**
> >     
> >     - Hardware: 4 full-adders.
> >         
> >     - Delay: Worst-case carry must propagate through four stages → 4·(XOR+XOR+OR) delays.
> >         
> >     - Advantage: Simple, low gate count.
> >         
> >     - Disadvantage: Slow for wide bit-widths.
> >         
> > - **CLA adder**
> >     
> >     - Hardware: Additional AND/OR gates to compute P and G and intermediate carry formulas.
> >         
> >     - Delay: Generates all carries in two levels (generate P/G in one level, combine in next) plus final XOR → much faster. For 4 bits, overall about 3 gate delays vs. 4 stages in ripple.
> >         
> >     - Advantage: High speed.
> >         
> >     - Disadvantage: More complex, more hardware.
> >         


> [!question] Q17) If each XOR gate has a propagation delay of 10 ns and each AND/OR gate has a delay of 5 ns (irrespective of the number of inputs), what is the total propagation delay in adding two 4-bit numbers for:  
> (a) Normal full-adder (ripple), (b) Carry-look-ahead adder?
> 
> > [!success]- Answer  
> > (a) **Ripple-carry adder**: Using the efficient full-adder from Q14:
> > 
> > - Each full-adder = 2·(XOR) + 2·(AND) + 1·(OR) = 10 + 10 + 5 = 25 ns.
> >     
> > - Four such in series → 4 · 25 ns = 100 ns.
> >     
> > 
> > (b) **CLA adder (4-bit)**:
> > 
> > - Compute Pᵢ = Aᵢ ⊕ Bᵢ (10 ns) in parallel for all i.
> >     
> > - Compute Gᵢ = Aᵢ·Bᵢ (5 ns) in parallel.
> >     
> > - Compute carries: first combine G₀ and P₀·C₀ → one AND (5 ns) + one OR (5 ns) = 10 ns to get C₁. Similarly, deeper levels (C₂, C₃, C₄) each add at most two levels of AND+OR in series, but can be pipelined in lookahead logic. For 4 bits, worst sale = 2 levels of AND+OR = 10 + 10 = 20 ns.
> >     
> > - Finally, Sumᵢ = Pᵢ ⊕ Cᵢ (10 ns).  
> >     Total ≈ 10 ns (P/G) + 10 ns (carry logic first level) + 10 ns (Sum XOR) = 30 ns.
> >     


> [!question] Q18) Explain how a full-adder can be used as a majority function.
> 
> > [!success]- Answer  
> > A full-adder’s carry output is:
> > 
> > ```
> > Cout = AB + BC + AC.
> > ```
> > 
> > This is exactly the 3-input majority function (output=1 if at least two inputs are 1). So tie the full-adder’s inputs to A, B, C and take Cout as Y.


> [!question] Q19) Give the truth table of a full-subtractor. Design the same using a full-adder.
> 
> > [!success]- Answer  
> > **Full-Subtractor Truth Table** (inputs A, B, Bin; outputs Diff, Bout)
> > 
> > ```
> > A B Bin | Bout Diff  
> > 0 0  0  |  0    0  
> > 0 0  1  |  1    1  
> > 0 1  0  |  1    1  
> > 0 1  1  |  1    0  
> > 1 0  0  |  0    1  
> > 1 0  1  |  0    0  
> > 1 1  0  |  0    0  
> > 1 1  1  |  1    1  
> > ```
> > 
> > Equations:
> > 
> > ```
> > Diff = A ⊕ B ⊕ Bin  
> > Bout = B·Bin + A’·(B ⊕ Bin)
> > ```
> > 
> > To implement with a full-adder:
> > 
> > 1. Compute B’ = B ⊕ 1 (invert B via XOR with 1).
> >     
> > 2. Feed A, B’, Bin into a full-adder: it computes Sum = A ⊕ B’ ⊕ Bin = A ⊕ ¬B ⊕ Bin = Diff, and Cout = A·B’ + B’·Bin + A·Bin = Bout.
> >     


> [!question] Q20) There is a sixteen-bit adder with ripple-carry. Which of the following gives minimum delay for the output (fastest output)?  
> • F0 + F1  
> • FF + FF  
> • FF + F1
> 
> > [!success]- Answer  
> > Interpret notation: “F0” means a 16-bit value with MSB=1, rest 0; “F1” means MSB=1, LSB=1, others 0; “FF” means MSB and next bits all 1? Actually “F” in hex is 4 bits of 1. So:
> > 
> > - F0 (1111 0000… in hex) + F1 (1111 0001) → the low 4 bits: 0000 + 0001 produces carry through only 1 stage.
> >     
> > - FF (1111 1111) + FF (1111 1111) → low-order hex addition generates carry that ripples through many bits until a 0 is encountered. Here all bits are 1, so carry propagates through 8 bits at least.
> >     
> > - FF + F1 → the addition of 1111 1111 + 1111 0001 produces carry through most bits.  
> >     The combination generating the fewest ripple stages is F0 + F1 (only one carry-propagate bit), so it has the minimum delay.
> >     


> [!question] Q21) What is overflow? Under what conditions will it occur?
> 
> > [!success]- Answer  
> > (a) **Unsigned Addition Overflow**: In N bits, representable range is 0 to 2ᴺ–1. If adding two N-bit unsigned numbers yields a result > 2ᴺ–1, a carry-out from MSB indicates overflow.
> > 
> > (b) **Signed (Two’s-Complement) Overflow**: In N bits, range is –2ⁿ⁻¹ to 2ⁿ⁻¹–1. Overflow occurs if:
> > 
> > 1. Adding two positive numbers yields a negative result (MSB of sum=1).
> >     
> > 2. Adding two negative numbers yields a positive result (MSB of sum=0).
> >     
> > 3. Subtracting a positive from a negative yields positive overflow, or subtracting a negative from a positive yields negative overflow.
> >     


> [!question] Q22) Using a 4-bit binary adder, design a circuit which multiplies the input by 3.
> 
> > [!success]- Answer  
> > Let the 4-bit input be A (A₃…A₀). Then 3·A = 2·A + A.
> > 
> > - 2·A is just A shifted left by 1 (with LSB = 0).
> >     
> > - Feed 2·A and A into a 4-bit adder. Set the initial carry-in to 0.  
> >     The sum outputs are 3·A.
> >     


> [!question] Q23) Design a subtractor unit using a 4-bit comparator, 4-bit binary adder, and some external gates, which performs A – B if A > B and else B – A. A and B are two 4-bit binary numbers.
> 
> > [!success]- Answer
> > 
> > 1. Use a 4-bit comparator to generate a high output when A > B. Let that signal be M.
> >     
> > 2. Compute two’s complement of B: B’ = ¬B + 1 (use 4-bit adder with inputs ¬B, 1). Compute two’s complement of A similarly: A’ = ¬A + 1.
> >     
> > 3. Use a 2:1 Mux gated by M:
> >     
> >     - If M=1 (A>B) → feed A and B’ into the 4-bit adder → produces A – B.
> >         
> >     - If M=0 (A≤B) → feed B and A’ into the adder → produces B – A.
> >         
> > 4. Output the adder’s sum; no final sign is needed since magnitude is positive.
> >     


> [!question] Q24) Design an adder/subtractor unit using a 4-bit binary adder and some external gates, which gives A + B if C = 0 and A – B if C = 1. Also provide an overflow indicator.
> 
> > [!success]- Answer
> > 
> > 5. Let C be the control (0 for add, 1 for subtract).
> >     
> > 6. Invert B only if C = 1: feed each Bi through an XOR gate with C → Bi ⊕ C.
> >     
> > 7. Connect Aᵢ and (Bᵢ ⊕ C) to the 4-bit adder. Set initial carry-in = C.
> >     
> >     - If C=0: Bi⊕0 = Bᵢ, Cin=0 → sum = A+B.
> >         
> >     - If C=1: Bi⊕1 = ¬Bᵢ, Cin=1 → adder computes A + ¬B + 1 = A – B.
> >         
> > 4. **Overflow indicator**: For two’s-complement, overflow = Cₙ ⊕ Cₙ₋₁, where Cₙ = final carry out, Cₙ₋₁ = carry into MSB. XOR those two signals to detect signed overflow.
> >     


> [!question] Q25) Use the above designed circuit (from Q24) as a block and give a scheme for finding the absolute value of a 4-bit number.
> 
> > [!success]- Answer  
> > Let the 4-bit number be A (two’s-complement). Its MSB, A₃, indicates sign:
> > 
> > - If A₃ = 0 → A ≥ 0, output = A.
> >     
> > - If A₃ = 1 → A < 0, output = –A.  
> >     Feed A into the adder/subtractor from Q24 as follows:
> >     
> > - C = A₃ (control = MSB).
> >     
> > - When A₃ = 0 → adder adds A + 0 → outputs A.
> >     
> > - When A₃ = 1 → adder computes A – 0? Instead, tie B = 0, so adder does A + ¬0 + 1 = A + 1 → not correct. Actually, to compute –A: Feed B = A (through XOR with C), so when C=1: B_input = A ⊕ 1 (bitwise), Cin = 1 → computes A + ¬A + 1 = 0 + 1 = 1?  
> >     Simpler: Use Q24 with A as input and B = A. Then:
> >     
> > - If MSB=0, C=0 → output = A + A = 2A (not wanted).  
> >     Instead: The absolute-value scheme:
> >     
> > 
> > 1. Connect Aᵢ and Ai ⊕ A₃ to adder.
> >     
> > 2. Cin = A₃.  
> >     Then:
> >     
> > 
> > - If A₃=0: Ai⊕0 = Ai; Cin=0 → sum = A + 0 = A.
> >     
> > - If A₃=1: Ai⊕1 = ¬Ai; Cin=1 → sum = A + ¬A + 1 = 0 – 1 + 1 = –A.  
> >     So pass B = A, but XOR each bit with MSB, Cin = MSB. Adder outputs |A|.
> >     


> [!question] Q26) Design a circuit that generates the 9’s complement of a BCD digit using a binary adder.
> 
> > [!success]- Answer  
> > Let d be a 4-bit BCD digit (0–9). The 9’s complement is 9 – d. Note 9 = 1001₂.
> > 
> > 1. Compute ¬d (bitwise inversion) → gives 15 – d.
> >     
> > 2. Use 4-bit adder: Inputs = ¬d and 1001 (i.e., 9), Cin=0.  
> >     Output = (15 – d) + 9 = 24 – d. Since BCD digit ≤ 9, result ≤ 15, so actually you get 9 – d properly (carry out ignored).
> >     


> [!question] Q27) Give the circuit that adds two BCD numbers and outputs a BCD result.
> 
> > [!success]- Answer
> > 
> > 3. Add two BCD digits D₁,D₀ via a 4-bit binary adder → sum S (4 bits), carry-out = C₄.
> >     
> > 4. If S > 1001 (9) or C₄ = 1, then add 6 (0110₂) to S to correct.
> >     
> >     - Overflow detection: K = C₄ + (S₃·S₂) + (S₃·S₁).
> >         
> >     - If K=1 → feed S and Cin=0 into a second 4-bit adder that adds 0110.
> >         
> > 3. If K=0, output = S; if K=1, output = S + 0110, carry-out from this second adder is ignored (unused).
> >     


> [!question] Q28) How will you count the number of 1’s present in a given 3-bit input using a full-adder?
> 
> > [!success]- Answer  
> > Let inputs be A, B, C. Feed them into a full-adder:
> > 
> > - Sum bit = A ⊕ B ⊕ C = least significant bit of the count.
> >     
> > - Cout = majority(A,B,C) = higher bit of the count (either 0,1,2,3 → requires two bits).  
> >     Table:
> >     
> > 
> > ```
> > A B C | Cout Sum | Count of 1’s  
> > 0 0 0 |  0    0  | 00 (0)  
> > 0 0 1 |  0    1  | 01 (1)  
> > 0 1 0 |  0    1  | 01 (1)  
> > 0 1 1 |  1    0  | 10 (2)  
> > 1 0 0 |  0    1  | 01 (1)  
> > 1 0 1 |  1    0  | 10 (2)  
> > 1 1 0 |  1    0  | 10 (2)  
> > 1 1 1 |  1    1  | 11 (3)  
> > ```
> > 
> > Concatenate (Cout, Sum) to get the 2-bit count.


> [!question] Q29)  
> In the above circuit, the inverters have delays T₁ and T₂ respectively. IN is a clock signal with 50% duty cycle and period T. It is given that T₁ + T₂ < T/2.  
> (a) What is the functionality of the circuit shown?  
> (b) Derive the duty cycle of the output waveform.  
> (c) What is the condition to get 50% duty cycle at the output?
> 
> > [!success]- Answer  
> > (a) The circuit is a frequency doubler: it outputs a clock at twice the input frequency (f_out = 2f_in).
> > 
> > (b) Let IN have period T and 50% duty cycle. The output is asserted for the cumulative delay of the two inverters each half-cycle. Thus:
> > 
> > - Half-period of IN = T/2.
> >     
> > - Output pulse width = T₁ + T₂ each half-cycle.
> >     
> > - Since two pulses per full period, output period = T/2. But each pulse width = (T₁ + T₂). Therefore duty cycle =
> >     
> >     ```
> >     ((T₁ + T₂) / (T/2)) × 100% = (2·(T₁ + T₂) / T) × 100%.
> >     ```
> >     
> > 
> > (c) For 50% output duty cycle:
> > 
> > ```
> > 2·(T₁ + T₂) / T = 0.5  ⇒  T₁ + T₂ = T/4.
> > ```


> [!question] Q30) Give the truth table for a 4:2 priority encoder in which LSB (D0) has the highest priority and MSB (D3) has the lowest.
> 
> > [!success]- Answer  
> > Inputs D₃ (lowest priority), D₂, D₁, D₀ (highest). Outputs: X (MSB), Y (LSB).
> > 
> > ```
> > D₃ D₂ D₁ D₀ | X Y | Comment  
> >  0  0  0  0 |  X  X | No input asserted (invalid)  
> >  0  0  0  1 |  0  0 | D₀ has highest priority → code 00  
> >  0  0  1  X |  0  1 | D₁ asserted, D₀=0 → code 01  
> >  0  1  X  X |  1  0 | D₂ asserted, D₁,D₀=0 → code 10  
> >  1  X  X  X |  1  1 | D₃ asserted, D₂,D₁,D₀=0 → code 11  
> > ```
> > 
> > ‘X’ means don’t-care in that row because a higher-priority input overrides.


> [!question] Q31) You have three delay elements D₁, D₂, D₃ that delay a clock by 25%, 50%, and 75% respectively. Design a frequency-doubling (f_out = 2·f_in) circuit that uses these delay elements plus any combinational logic.
> 
> > [!success]- Answer  
> > Let IN be a clock of period T. Use two delay paths and an XOR:
> > 
> > 1. Path1: Delay by 25%T (D₁) → yields IN delayed by T/4.
> >     
> > 2. Path2: Delay by 75%T (D₃) → yields IN delayed by 3T/4.
> >     
> > 3. XOR the two delayed signals.  
> >     The rising edge of IN at t = 0 passes through D₁ to appear at t = T/4, and through D₃ to appear at t = 3T/4. XORing them produces pulses at T/4 and 3T/4 within each period, doubling the frequency.  
> >     (Alternatively, any two delays differing by T/2 with XOR yields frequency doubling; e.g., use D₂ (T/2) and undelayed IN, XORing gives a 50% duty cycle at 2f₀.)
> >     


> [!question] Q32) Give a combinational circuit which checks whether two 4-bit input signals are the same or not.
> 
> > [!success]- Answer  
> > Let A₃…A₀ and B₃…B₀ be the inputs. For each bit i, compute Xᵢ = Aᵢ ⊕ Bᵢ. Then feed all four Xᵢ into a 4-input NOR gate. If any Xᵢ =1 (bits differ), NOR output =0 → “not equal”. If all Xᵢ=0 → inputs equal → NOR output=1. Equivalent: equality = ¬(A⊕B) for each bit, then AND all.


> [!question] Q33) Using a 4:16 decoder and the minimum number of external gates, implement the following Boolean functions:  
> (a) F(A,B,C,D) = Σ (5,7,9,14)  
> (b) G(A,B,C,D) = Σ (0,1,2,3,4,6,7,8,9,10,11,14,15)
> 
> > [!success]- Answer  
> > **General approach**: A 4:16 decoder outputs one “1” on the line corresponding to the 4-bit input’s binary value (0 to 15). To implement a sum-of-minterms, OR the decoder outputs for those minterms = 1. If most minterms are 1, better to use NOR on the zero-minterms for minimal gates.
> > 
> > (a) F has minterms {5,7,9,14}. Directly OR decoder outputs: F = D₅ + D₇ + D₉ + D₁₄. Use a 4-input OR gate (since exactly four terms).
> > 
> > (b) G has minterms {0,1,2,3,4,6,7,8,9,10,11,14,15} → that’s 13 ones, so only zero-minterms are {5,12,13}. Use a 3-input NOR on D₅, D₁₂, D₁₃, then invert: G = ¬(D₅ + D₁₂ + D₁₃). Equivalently, feed D₅, D₁₂, D₁₃ into a 3-input NOR → that output is “1” only when all three are 0, i.e., input ∈ {0,1,2,3,4,6,7,8,9,10,11,14,15}. Thus G is the NOR output directly. (No inverter needed.)