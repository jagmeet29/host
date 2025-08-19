```verilog 
module comparator_gate_level (
    input [2:0] A,
    input [2:0] B,
    output A_gt_B,
    output A_eq_B,
    output A_lt_B
);
    wire [2:0] eq_bits, gt_bits, lt_bits;

    // Equality logic for each bit
    xnor(eq_bits[2], A[2], B[2]);
    xnor(eq_bits[1], A[1], B[1]);
    xnor(eq_bits[0], A[0], B[0]);
    
    // Greater-than logic
    assign gt_bits[2] = A[2] & ~B[2];
    assign gt_bits[1] = eq_bits[2] & (A[1] & ~B[1]);
    assign gt_bits[0] = eq_bits[2] & eq_bits[1] & (A[0] & ~B[0]);

    // Less-than logic
    assign lt_bits[2] = ~A[2] & B[2];
    assign lt_bits[1] = eq_bits[2] & (~A[1] & B[1]);
    assign lt_bits[0] = eq_bits[2] & eq_bits[1] & (~A[0] & B[0]);

    // Final outputs
    assign A_eq_B = eq_bits[2] & eq_bits[1] & eq_bits[0];
    assign A_gt_B = gt_bits[2] | gt_bits[1] | gt_bits[0];
    assign A_lt_B = lt_bits[2] | lt_bits[1] | lt_bits[0];
endmodule

```