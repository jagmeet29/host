```verilog
// JK Flip-Flop using dataflow modeling
module jk_flipflop_dataflow(
    input J, K, clk, reset,
    output reg Q, Qbar
);
    wire next_Q;
    
    // Next state logic using continuous assignment
    assign next_Q = reset ? 1'b0 : 
                   (J & ~K) ? 1'b1 :
                   (~J & K) ? 1'b0 :
                   (J & K) ? ~Q : Q;
    
    // Clock edge detection
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            Q <= 1'b0;
            Qbar <= 1'b1;
        end
        else begin
            Q <= next_Q;
            Qbar <= ~next_Q;
        end
    end
endmodule

// JK Latch using dataflow modeling
module jk_latch_dataflow(
    input J, K, enable,
    output reg Q, Qbar
);
    wire next_Q;
    
    assign next_Q = ~enable ? Q :
                   (J & ~K) ? 1'b1 :
                   (~J & K) ? 1'b0 :
                   (J & K) ? ~Q : Q;
    
    always @(next_Q) begin
        Q = next_Q;
        Qbar = ~next_Q;
    end
endmodule
```