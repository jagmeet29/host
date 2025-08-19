### Test Bench
```verilog 
`timescale 1ns/1ps

module decoder_dataflow_tb;
  // Declare testbench signals
  reg en;
  reg [2:0] in;
  wire [7:0] out;
  
  // Instantiate the dataflow decoder module
  decoder_dataflow uut (
    .en(en),
    .in(in),
    .out(out)
  );
  
  // Testbench stimulus
  initial begin
    // Test case 1: Disable the decoder (en = 0); output should be all zeros.
    en = 0;
    in = 3'd0;
    #10;
    
    // Test case 2: Enable the decoder (en = 1) and check all possible input combinations.
    en = 1;
    for (in = 0; in < 8; in = in + 1) begin
      #10;
    end
    
    // Test case 3: Disable the decoder after testing; output should go back to zero.
    en = 0;
    in = 3'd3; // Set 'in' arbitrarily while disabled
    #10;
    
    // End the simulation.
    $stop;
  end
endmodule

```