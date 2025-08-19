```verilog 
module bcd2bin_dataflow(
    input  [15:0] bcd,
    output [13:0] binary
);
    // Use continuous assignment with arithmetic operators.
    assign binary = (bcd[15:12] * 10'd1000) +
                    (bcd[11:8]  * 10'd100)  +
                    (bcd[7:4]   * 10'd10)   +
                     bcd[3:0];
endmodule

```