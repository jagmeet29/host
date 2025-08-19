```verilog 
module bcd2bin_behavioral(
    input  [15:0] bcd,    
    // Four BCD digits: bcd[15:12] is thousands, [11:8] is hundreds, [7:4] is tens, [3:0] is ones.
    output reg [13:0] binary   
    // Binary output (sufficient to represent numbers up to 9999).
);
    always @(*) begin
        // Multiply each BCD nibble by its positional weight and sum the results.
        binary = (bcd[15:12] * 10'd1000) +
                 (bcd[11:8]  * 10'd100)  +
                 (bcd[7:4]   * 10'd10)   +
                  bcd[3:0];
    end
endmodule

```