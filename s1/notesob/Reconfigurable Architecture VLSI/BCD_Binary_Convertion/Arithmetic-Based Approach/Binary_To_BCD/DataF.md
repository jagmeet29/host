```verilog 
module bin2bcd_dataflow(
    input  [7:0] binary,
    output [3:0] ones,     // Least significant BCD digit
    output [3:0] tens,     
    output [3:0] hundreds
);
    assign ones     = binary % 10;
    assign tens     = (binary / 10) % 10;
    assign hundreds = (binary / 100);
endmodule


```