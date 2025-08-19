1. The size of decoder is same as the number of variables
2. Put the variable at the input of the decoder
3. As, the decoder output represents the Canonical form ([[Boolean.canvas|Notesofde]]) of the input .Each output corresponds to a specific minterm (a unique combination of input variable states)
4. To implement a specific function, identify the minterms (decoder outputs) where the function evaluates to "1" (true). Use an OR gate to combine these outputs. The OR gate will produce a high signal whenever any of these selected minterms are active, thereby implementing the desired function.

## Active High/Low - Min/Max terms Impact
### Active High
- Minterms $\rightarrow$   OR gate
- Maxterms $\rightarrow$ NOR gate
### Active Low
- Minterms $\rightarrow$ AND gate
- Maxterms $\rightarrow$ NANA gate

