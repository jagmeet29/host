```verilog
// JK Flip-Flop using behavioral modeling
module jk_flipflop_behavioral(
    input J, K, clk, reset,
    output reg Q, Qbar
);
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            Q <= 1'b0;
            Qbar <= 1'b1;
        end
        else begin
            case ({J, K})
                2'b00: begin  // No change
                    Q <= Q;
                    Qbar <= Qbar;
                end
                2'b01: begin  // Reset
                    Q <= 1'b0;
                    Qbar <= 1'b1;
                end
                2'b10: begin  // Set
                    Q <= 1'b1;
                    Qbar <= 1'b0;
                end
                2'b11: begin  // Toggle
                    Q <= ~Q;
                    Qbar <= ~Qbar;
                end
            endcase
        end
    end
endmodule

// JK Latch using behavioral modeling
module jk_latch_behavioral(
    input J, K, enable,
    output reg Q, Qbar
);
    always @(J, K, enable) begin
        if (enable) begin
            case ({J, K})
                2'b00: begin  // No change
                    Q = Q;
                    Qbar = Qbar;
                end
                2'b01: begin  // Reset
                    Q = 1'b0;
                    Qbar = 1'b1;
                end
                2'b10: begin  // Set
                    Q = 1'b1;
                    Qbar = 1'b0;
                end
                2'b11: begin  // Toggle
                    Q = ~Q;
                    Qbar = ~Qbar;
                end
            endcase
        end
        // If enable is low, outputs don't change
    end
endmodule
```
