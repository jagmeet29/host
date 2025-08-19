```verilog
// SR Latch using continuous assignments
module sr_latch_dataflow(Q, Qbar, S, R);
    output Q, Qbar;
    input S, R;
    
    assign Q = ~(R | Qbar);      // NOR gate logic
    assign Qbar = ~(S | Q);      // NOR gate logic
endmodule

// Gated SR Latch
module sr_latch_gated_dataflow(Q, Qbar, S, R, G);
    output Q, Qbar;
    input S, R, G;
    wire s1, r1;
    
    assign s1 = ~(S & G);        // NAND logic
    assign r1 = ~(R & G);        // NAND logic
    assign Q = ~(s1 & Qbar);     // Cross-coupled logic
    assign Qbar = ~(r1 & Q);     // Cross-coupled logic
endmodule
```
