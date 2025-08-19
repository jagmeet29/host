```verilog 
module comparator_dataflow (
    input [2:0] A,
    input [2:0] B,
    output A_gt_B,
    output A_eq_B,
    output A_lt_B
);
    // Boolean expressions for comparison
    assign A_eq_B = (A == B);
    assign A_gt_B = (A > B);
    assign A_lt_B = (A < B);
endmodule
```