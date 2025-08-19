```verilog
module d_latch_behavioral (
    input D, 
    input EN, 
    output reg Q
);
    always @ (D or EN)
        if (EN)
            Q <= D;
endmodule
```