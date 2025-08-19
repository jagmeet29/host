### Test Bench
```verilog 
module tb_comparator();
    reg [2:0] A, B;
    wire gt_gate, eq_gate, lt_gate;
    wire gt_data, eq_data, lt_data;
    wire gt_behav, eq_behav, lt_behav;

    // Instantiate all three models
    comparator_gate_level u1 (.A(A), .B(B), .A_gt_B(gt_gate), .A_eq_B(eq_gate), .A_lt_B(lt_gate));
    comparator_dataflow u2 (.A(A), .B(B), .A_gt_B(gt_data), .A_eq_B(eq_data), .A_lt_B(lt_data));
    comparator_behavioral u3 (.A(A), .B(B), .A_gt_B(gt_behav), .A_eq_B(eq_behav), .A_lt_B(lt_behav));

    initial begin
        $monitor("Time=%t | A=%b, B=%b | Gate: GT=%b EQ=%b LT=%b | Data: GT=%b EQ=%b LT=%b | Behav: GT=%b EQ=%b LT=%b",
                 $time, A, B, gt_gate, eq_gate, lt_gate, gt_data, eq_data, lt_data, gt_behav, eq_behav, lt_behav);

        // Test cases
        #5  A = 3'b000; B = 3'b000; // Equal case
        #5  A = 3'b101; B = 3'b011; // Greater case
        #5  A = 3'b010; B = 3'b110; // Less case
        #5  $finish;
    end
endmodule

```