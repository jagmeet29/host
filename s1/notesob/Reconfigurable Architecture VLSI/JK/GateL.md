```verilog
// JK Flip-Flop using basic gates
module jk_flipflop_gate(
    input J, K, clk, reset,
    output Q, Qbar
);
    wire w1, w2, w3, w4, w5, w6;
    
    // Master latch
    nand n1(w1, J, clk, Qbar);
    nand n2(w2, K, clk, Q);
    nand n3(w3, w1, w4);
    nand n4(w4, w2, w3);
    
    // Slave latch
    wire clk_not;
    not inv1(clk_not, clk);
    nand n5(w5, w3, clk_not);
    nand n6(w6, w4, clk_not);
    nand n7(Q, w5, Qbar, reset);
    nand n8(Qbar, w6, Q);
    
    // Reset functionality
    wire reset_not;
    not inv2(reset_not, reset);
    and a1(Q, Q, reset_not);
endmodule

// JK Latch using basic gates
module jk_latch_gate(
    input J, K, enable,
    output Q, Qbar
);
    wire w1, w2;
    
    nand n1(w1, J, enable, Qbar);
    nand n2(w2, K, enable, Q);
    nand n3(Q, w1, Qbar);
    nand n4(Qbar, w2, Q);
endmodule
```