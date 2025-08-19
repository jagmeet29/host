```verilog
module d_latch_gate (
    input D, 
    input EN, 
    output Q
);
    wire n1, n2, n3, n4;
    nand (n1, D, EN);
    nand (n2, n1, EN);
    nand (n3, n2, n4);
    nand (n4, n3, D);
    assign Q = n3;
endmodule
```
