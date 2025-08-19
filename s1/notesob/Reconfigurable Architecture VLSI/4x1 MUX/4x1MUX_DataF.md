```verilog 
module mux4_1_dataflow(
    input  a, b, c, d,
    input  s0, s1,
    output out
);
    // Using a nested ternary operator to implement the MUX function
    assign out = s1 ? (s0 ? d : c) : (s0 ? b : a);
endmodule

```