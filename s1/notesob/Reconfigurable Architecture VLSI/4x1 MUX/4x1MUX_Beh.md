```verilog 
module mux4_1_behavioral(
    input a, b, c, d,
    input s0, s1,
    output reg out
);
    always @(*) begin
        // Check the combination of select signals and assign output accordingly
        if (!s1 && !s0)         // when s1=0, s0=0 select input a
            out = a;
        else if (!s1 && s0)      // when s1=0, s0=1 select input b
            out = b;
        else if (s1 && !s0)      // when s1=1, s0=0 select input c
            out = c;
        else                     // when s1=1, s0=1 select input d
            out = d;
    end
endmodule

```