```verilog 
module full_subtractor_behavioral(
    input a, b, bin,
    output reg diff, bout
);
    // The always block is sensitive to any change in a, b, or bin.
    always @(*) begin
        case ({a, b, bin})
            3'b000: begin diff = 0; bout = 0; end
            3'b001: begin diff = 1; bout = 1; end
            3'b010: begin diff = 1; bout = 1; end
            3'b011: begin diff = 0; bout = 1; end
            3'b100: begin diff = 1; bout = 0; end
            3'b101: begin diff = 0; bout = 0; end
            3'b110: begin diff = 0; bout = 0; end
            3'b111: begin diff = 1; bout = 1; end
            default: begin diff = 0; bout = 0; end
        endcase
    end
endmodule


```