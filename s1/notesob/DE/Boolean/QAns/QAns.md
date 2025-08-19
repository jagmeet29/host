> [!question] Q1) Which gates are called universal gates? Why?
> 
> > [!success]- Answer  
> > NAND and NOR gates are called universal gates.  
> > Because any other logical gate like AND, OR, NOT, XOR, XNOR, or any other Boolean function can be implemented only with NAND or NOR gates.

> [!question] Q2) How many minterms or maxterms will be there for n-inputs?
> 
> > [!success]- Answer  
> > For n inputs, the possible number of minterms or maxterms is 2^n.

> [!question] Q3) Give the minterm and maxterms corresponding to 6 and 15 numbers (4-inputs)?
> 
> > [!success]- Answer  
> > For 6 = (0110)₂:  
> > ‐ Minterm = A′ B C D′  
> > ‐ Maxterm = A + B′ + C′ + D  
> > For 15 = (1111)₂:  
> > ‐ Minterm = A B C D  
> > ‐ Maxterm = A′ + B′ + C′ + D′

> [!question] Q4) In how many ways can a NAND gate be converted into an inverter? Show all the possibilities?
> 
> > [!success]- Answer  
> > A NAND gate can be converted into an inverter by tying its two inputs together.  
> > Possibility 1: Connect both inputs of the NAND gate to the same input signal, so output = (A ⋅ A)′ = A′.  
> > Possibility 2: Use the NAND gate with one input tied to the signal and the other input also tied to that same signal (same concept repeated).

> [!question] Q5) How many number of 2-input AND gates are required to generate an N-input AND gate?
> 
> > [!success]- Answer  
> > You need N − 1 two-input AND gates to implement an N-input AND gate.  
> > For example, to implement a 4-input AND, you need three 2-input AND gates.

> [!question] Q6) State De Morgan’s Laws?
> 
> > [!success]- Answer  
> > (A + B + C + …)′ = A′ ⋅ B′ ⋅ C′ ⋅ …  
> > (A ⋅ B ⋅ C ⋅ …)′ = A′ + B′ + C′ + …

> [!question] Q7) 
> (a) If it is given that A & B will not be 1 at the same time, what will be the equivalent logical gate for an XOR gate?  
> (b) If any of the inputs of an XOR gate are inverted, XOR gate will work as _____?
> 
> > [!success]- Answer  
> > (a) OR gate.  
> > Since A = B = 1 cannot occur, AB = 0 always. Then A XOR B = A B′ + A′ B = A ⋅ (AB)′ + B ⋅ (AB)′ = A ⋅ (0)′ + B ⋅ (0)′ = A + B.  
> > (b) XNOR gate.  
> > A XOR B = A B′ + A′ B.  
> > A′ XOR B = A B + A′ B′ = A XNOR B.

> [!question] Q8) State the Shannon’s expansion theorem for representing a Boolean function by its co-factors?
> 
> > [!success]- Answer  
> > Any Boolean function F(A, B, C, D, …) can be represented as  
> > F = A Fₐ + A′ Fₐ′,  
> > where cofactor Fₐ = F(1, B, C, D, …) and Fₐ′ = F(0, B, C, D, …).

> [!question] Q9) Write the cofactors Fₐ and Fₐ′ for F(A, B, C, D) = A B D + B C D′ + A′ B′ C′?
> 
> > [!success]- Answer  
> > Fₐ (with A=1) = B D + B C D′  
> > Fₐ′ (with A=0) = B C D′ + B′ C′

> [!question] Q10) How many unique Boolean functions can exist for ‘n’ number of inputs?
> 
> > [!success]- Answer  
> > For n inputs, there are k = 2^n possible minterms.  
> > Any Boolean function is a combination of minterms, so the total number of Boolean functions is 2^k = 2^(2^n).

> [!question] Q11) Mention the logical gates for which the 3-input implementation cannot be obtained from two 2-input gates? How do you implement them?
> 
> > [!success]- Answer  
> > ![[DE/Boolean/QAns/Img/Ans11.png]]
> > The gates are NAND, NOR, and XNOR.  
> > To implement a 3-input NAND using only 2-input NAND gates, you cascade two gates: first NAND on two inputs, then NAND that result with the third input.  
> > The same cascade approach applies to 3-input NOR and 3-input XNOR.

> [!question] Q12) What is OUT in the circuit shown below?
> ![[QAns1.png]]
> > [!success]- Answer  
> > First XOR gate output = X XOR X′ = 1.  
> > Second XOR gate output = 1 XOR X = X′.  
> > Third XOR gate output = X′ XOR X = 1.  
> > Therefore, OUT = 1 irrespective of X.

> [!question] Q13) Give implementation of XOR using minimum number of NAND gates?
> 
> > [!success]- Answer  
> > ![[Ans13.png]]
> > A XOR B = A′ B + A B′ = A (AB)′ + B (AB)′.  
> > Using only NAND gates:
> > 
> > 1. NAND1 = A ⋅ B → (A B)′
> >     
> > 2. NAND2 = A ⋅ NAND1 → [A ⋅ (AB)′]′
> >     
> > 3. NAND3 = B ⋅ NAND1 → [B ⋅ (AB)′]′
> >     
> > 4. NAND4 = NAND2 ⋅ NAND3 → XOR output.
> >     

> [!question] Q14) An assembly line has 3 fail-safe sensors and one emergency shutdown switch. The line should keep moving unless any of the following conditions arise:  
> (i) If the emergency switch is pressed  
> (ii) If sensor1 and sensor2 are activated at the same time  
> (iii) If sensor2 and sensor3 are activated at the same time  
> (iv) If all the sensors are activated at the same time  
> Suppose a combinational circuit for the above case is to be implemented only with NAND gates. How many minimum number of 2-input NAND gates are required?
> 
> > [!success]- Answer  
> > ![[Ans14.png]]
> > Let A = emergency switch, B = sensor1, C = sensor2, D = sensor3 (1 = pressed/activated).  
> > Simplify using a Karnaugh map to get F = A + B C + C D.  
> > Implementing F with 2-input NAND gates requires 6 gates minimum.

> [!question] Q15) Majority function is the one which gives 1 if the input has more 1s than 0s. Show the truth table and give the AOI for 3-input majority function?
> 
> > [!success]- Answer  
> > Truth table:  
> > A B C | Y  
> > 0 0 0 | 0  
> > 0 0 1 | 0  
> > 0 1 0 | 0  
> > 0 1 1 | 1  
> > 1 0 0 | 0  
> > 1 0 1 | 1  
> > 1 1 0 | 1  
> > 1 1 1 | 1  
> > Boolean expression: Y = A B + B C + A C.  
> > AOI implementation uses three 2-input AND gates feeding a 3-input OR.
> > ![[Ans15.png]]

> [!question] Q16) N number of XNOR gates are connected as shown below. How does this circuit work? Explain?
> ![[QAns2.png]]
> > [!success]- Answer  
> > If N is odd, there are an even number of bubbles, which cancel out, so the overall behaves like XOR.  
> > If N is even, one extra bubble remains, so the overall behaves like XNOR.

> [!question] Q17) Show the implementation of XNOR gate using minimum number of NOR gates?
> 
> > [!success]- Answer  
> > Similar to the XOR-with-NAND construction:
> > 
> > 1. NOR1 = A + B → (A + B)′
> >     
> > 2. NOR2 = A + NOR1 → (A + (A + B)′)′ = A′ B
> >     
> > 3. NOR3 = B + NOR1 → (B + (A + B)′)′ = A B′
> >     
> > 4. NOR4 = NOR2 + NOR3 → XNOR output.
> > ![[Ans17.png]]
> >     

> [!question] Q18) Explain parity generation and its significance?
> 
> > [!success]- Answer  
> > Parity generation adds an extra bit to data indicating the parity (even or odd) of input data.  
> > Even-parity generator outputs 1 if the input has an odd number of 1s (so total becomes even).  
> > Odd-parity generator outputs 1 if the input has an even number of 1s (so total becomes odd).  
> > In data transmission, the channel can introduce errors. Parity bits allow single-bit error detection.

> [!question] Q19) Which logical gates can be used as parity generators?
> 
> > [!success]- Answer  
> > XOR gate can be used as an even-parity generator.  
> > XNOR gate can be used as an odd-parity generator.

> [!question] Q20) What is the parity of (i) 10111001 (ii) 11001010?
> 
> > [!success]- Answer  
> > (i) 10111001 has five 1s → odd → parity = ODD.  
> > (ii) 11001010 has four 1s → even → parity = EVEN.

> [!question] Q21) Give a circuit for 4-bit even parity checker? And explain the same how can it be re-used for parity generation?
> 
> > [!success]- Answer  
> > Inputs A, B, C are data bits; P is the even parity bit generated at transmitter: P = A XOR B XOR C.  
> > The receiver inputs A, B, C, P into a 4-input XOR; if no error, output O = 0; if error, O = 1.  
> > To reuse as a generator for three bits, tie P = 0 so the same XOR network outputs P = A XOR B XOR C.
> > ![[Ans21.png]]

> [!question] Q22) Design a combinational circuit using XOR gates that converts a 4-bit Gray code number to a 4-bit binary number?
> 
> > [!success]- Answer  
> > Let G₃ G₂ G₁ G₀ be Gray inputs and B₃ B₂ B₁ B₀ be binary outputs.  
> > B₃ = G₃  
> > B₂ = G₃ XOR G₂  
> > B₁ = G₃ XOR G₂ XOR G₁  
> > B₀ = G₃ XOR G₂ XOR G₁ XOR G₀.
> > ![[Ans22.png]]

> [!question] Q23) Draw the enable signal (CLK_EN) such that the OUT will get only the 2nd and 3rd pulses of CLK? The figure shows the circuit and CLK signal?
> 
> > [!success]- Answer  
> > CLK_EN is high only during the 2nd and 3rd clock pulses.  
> > That is, if CLK pulses are numbered starting at 1, then CLK_EN = 1 for pulses 2 and 3, and 0 otherwise.
> > ![[Ans23.png]]

> [!question] Q24) Which logical gate can be used to find out whether the two single bit inputs are equal or not?
> ![[QAns3.png]]
> > [!success]- Answer  
> > XNOR gate.  
> > It outputs 1 when both inputs are the same, 0 otherwise.

> [!question] Q25) What is the difference between NAND gate and negative AND gate?
> 
> > [!success]- Answer  
> > NAND gate: F₁ = (A ⋅ B)′ = A′ + B′.  
> > Negative AND gate: F₂ = A′ ⋅ B′ = (A + B)′ (which is actually a NOR gate).
> > ![[Ans25.png]]

> [!question] Q26) How to obtain the dual of a Boolean equation?
> 
> > [!success]- Answer  
> > Replace every AND (and NAND) with OR (and NOR), and every OR (and NOR) with AND (and NAND) in the given Boolean equation.

> [!question] Q27) Match the following:  
> a) Comparator  
> b) Half adder  
> c) Anyone input is 1, output is 0  
> d) Anyone input is 0, output is 1  
> (i) NAND  
> (ii) NOR  
> (iii) XOR  
> (iv) XNOR
> 
> > [!success]- Answer  
> > a → iv  
> > b → iii  
> > c → ii  
> > d → i

