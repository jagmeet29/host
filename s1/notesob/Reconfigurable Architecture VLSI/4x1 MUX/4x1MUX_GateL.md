```verilog 
module mux4_1_gate(
    output y,
    input i0, i1, i2, i3,
    input s0, s1
);
    // Internal wires for inverted select signals and intermediate outputs
    wire s0_bar, s1_bar;
    wire w1, w2, w3, w4;
    
    // Invert the select signals
    not n1(s0_bar, s0);
    not n2(s1_bar, s1);
    
    // AND gates produce intermediate outputs based on the conditions:
    // For i0: When s1 = 0 and s0 = 0
    and a1(w1, i0, s0_bar, s1_bar);
    // For i1: When s1 = 0 and s0 = 1
    and a2(w2, i1, s0, s1_bar);
    // For i2: When s1 = 1 and s0 = 0
    and a3(w3, i2, s0_bar, s1);
    // For i3: When s1 = 1 and s0 = 1
    and a4(w4, i3, s0, s1);
    
    // OR gate combines the outputs to produce the final output y
    or a5(y, w1, w2, w3, w4);
endmodule

```