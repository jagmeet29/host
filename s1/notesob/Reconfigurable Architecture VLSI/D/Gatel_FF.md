```verilog
// Master-Slave D Flip-Flop using two D latches
module d_flipflop_gate (
    input D, 
    input CLK, 
    output Q
);
    wire Qm;
    d_latch_gate master (.D(D), .EN(~CLK), .Q(Qm));
    d_latch_gate slave  (.D(Qm), .EN(CLK),  .Q(Q));
endmodule
```