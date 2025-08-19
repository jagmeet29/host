```verilog 
module full_subtractor_dataflow(
    input a, b, bin,
    output diff, bout
);
    // Difference is computed using XOR on all three inputs.
    assign diff = a ^ b ^ bin;
    // Borrow out is computed by combining two product terms.
    // The formula here is: bout = (~a & b) | ((~(a ^ b)) & bin)
    assign bout = ((~a) & b) | ((~(a ^ b)) & bin);
endmodule

```