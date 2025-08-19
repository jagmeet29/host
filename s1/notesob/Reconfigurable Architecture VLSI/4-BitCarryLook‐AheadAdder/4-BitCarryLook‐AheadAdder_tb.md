### Test Bench
```verilog 
`timescale 1ns/1ps

module CLA_TB;
  // Declare inputs as regs and outputs as wires.
  reg  [3:0] a, b;
  reg        cin;
  wire [3:0] sum;
  wire       cout;
  
  // Optional: integer loop variable for extended testing.
  integer i;
  
  // Instantiate the 4-bit Carry Look-Ahead Adder.
  // Ensure that your CLA module has port names: a, b, cin, sum, cout.
  CLA_Adder uut (
    .a(a),
    .b(b),
    .cin(cin),
    .sum(sum),
    .cout(cout)
  );
  
  // Initial block executes once at simulation start.
  initial begin
    // Print a header for the simulation output.
    $display("Time\t  a     b    cin  | sum   cout");
    // $monitor prints whenever any signal in its list changes.
    $monitor("%0t\t%b  %b  %b  |  %b    %b", $time, a, b, cin, sum, cout);
    
    // Provide a few fixed test cases.
    a = 4'b0000; b = 4'b0000; cin = 1'b0;  #10;
    a = 4'b0001; b = 4'b0010; cin = 1'b1;  #10;
    a = 4'b0101; b = 4'b0011; cin = 1'b0;  #10;
    a = 4'b1010; b = 4'b0101; cin = 1'b1;  #10;
    a = 4'b1111; b = 4'b1111; cin = 1'b0;  #10;
    
    // Optionally, for full coverage you can loop through some values.
    // This loop iterates over 16 values for A and B (using same value for both)
    // and alternates the cin value.
    for (i = 0; i < 16; i = i + 1) begin
      a   = i;
      b   = i;
      cin = i % 2;
      #10;
    end
    
    // End the simulation once all test cases are applied.
    $finish;
  end
endmodule

```