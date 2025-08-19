```verilog 
// Structural building block for one stage of the Double Dabble algorithm.
module dd_stage(
    input  [11:0] in,    // Current BCD intermediate (12 bits for 3 digits)
    input         in_bit, // Next binary bit to be shifted in
    output [11:0] out   // Updated BCD after shifting
);
    wire [3:0] thousands, hundreds, tens;
    wire [3:0] thousands_adj, hundreds_adj, tens_adj;
    
    // Split the 12-bit input into three BCD digits.
    assign thousands = in[11:8];
    assign hundreds  = in[7:4];
    assign tens      = in[3:0];
    
    // For each nibble, add 3 if its value is 5 or greater.
    assign thousands_adj = (thousands >= 4'd5) ? (thousands + 4'd3) : thousands;
    assign hundreds_adj  = (hundreds  >= 4'd5) ? (hundreds  + 4'd3) : hundreds;
    assign tens_adj      = (tens      >= 4'd5) ? (tens      + 4'd3) : tens;
    
    // Concatenate the adjusted nibbles and perform a left shift with the new bit cascaded into LSB.
    assign out = {thousands_adj, hundreds_adj, tens_adj} << 1 | in_bit;
endmodule

// Top-level gate-level Binary to BCD converter using the Double Dabble algorithm.
module bin2bcd_gate(
    input  [7:0] binary,
    output [11:0] bcd   // 12-bit BCD output (hundreds, tens, ones)
);
    // Wire declarations for each stage's intermediate result.
    wire [11:0] stage0, stage1, stage2, stage3, stage4, stage5, stage6, stage7, stage8;
    
    // Initial stage: start with 0, then concatenate 8 binary bits.
    assign stage0 = 12'b0;
    
    // Unroll the Double Dabble algorithm for each bit of the binary input.
    dd_stage s1(.in(stage0), .in_bit(binary[7]), .out(stage1));
    dd_stage s2(.in(stage1), .in_bit(binary[6]), .out(stage2));
    dd_stage s3(.in(stage2), .in_bit(binary[5]), .out(stage3));
    dd_stage s4(.in(stage3), .in_bit(binary[4]), .out(stage4));
    dd_stage s5(.in(stage4), .in_bit(binary[3]), .out(stage5));
    dd_stage s6(.in(stage5), .in_bit(binary[2]), .out(stage6));
    dd_stage s7(.in(stage6), .in_bit(binary[1]), .out(stage7));
    dd_stage s8(.in(stage7), .in_bit(binary[0]),

```