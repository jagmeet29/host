```verilog 
module bin2bcd_behavioral(
    input  [7:0] binary,
    output reg [11:0] bcd   // 12-bit output: three BCD digits (hundreds, tens, ones)
);
    integer temp;
    always @(*) begin
        temp = binary;
        bcd[3:0]  = temp % 10;   // ones digit
        temp      = temp / 10;
        bcd[7:4]  = temp % 10;   // tens digit
        temp      = temp / 10;
        bcd[11:8] = temp % 10;   // hundreds digit
    end
endmodule

```