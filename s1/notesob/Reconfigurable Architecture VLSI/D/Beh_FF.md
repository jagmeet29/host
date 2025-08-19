```verilog
module d_flipflop_behavioral (
    input D, 
    input CLK, 
    output reg Q
);
    always @ (posedge CLK)
        Q <= D;
endmodule
```