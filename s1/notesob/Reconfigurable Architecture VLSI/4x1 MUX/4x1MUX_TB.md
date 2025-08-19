### Test Bench
```verilog 
`timescale 1ns/1ps

module mux4_1_tb;
    // Declare inputs as registers and output as wire
    reg a, b, c, d;
    reg s0, s1;
    wire out;

    // Instantiate the multiplexer module under test (replace "mux4_1" with your module name)
    // Ensure your multiplexer module has the ports: a, b, c, d, s0, s1, and out.
    mux4_1 uut (
        .a(a),
        .b(b),
        .c(c),
        .d(d),
        .s0(s0),
        .s1(s1),
        .out(out)
    );

    // Dump simulation data for waveform viewing
    initial begin
        $dumpfile("mux4_1_tb.vcd");
        $dumpvars(0, mux4_1_tb);
    end

    // Apply stimulus to the inputs and select lines
    initial begin
        // Initialize all inputs
        a  = 1'b0;
        b  = 1'b0;
        c  = 1'b0;
        d  = 1'b0;
        s0 = 1'b0;
        s1 = 1'b0;
        #10;  // Wait for 10 ns
        
        // Test Case 1: Select input a (s1s0 = 00)
        a  = 1'b1; b = 1'b0; c = 1'b0; d = 1'b0;
        s0 = 1'b0; s1 = 1'b0;
        #10;
        
        // Test Case 2: Select input b (s1s0 = 01)
        a  = 1'b0; b = 1'b1; c = 1'b0; d = 1'b0;
        s0 = 1'b1; s1 = 1'b0;
        #10;

        // Test Case 3: Select input c (s1s0 = 10)
        a  = 1'b0; b = 1'b0; c = 1'b1; d = 1'b0;
        s0 = 1'b0; s1 = 1'b1;
        #10;
        
        // Test Case 4: Select input d (s1s0 = 11)
        a  = 1'b0; b = 1'b0; c = 1'b0; d = 1'b1;
        s0 = 1'b1; s1 = 1'b1;
        #10;
        
        // End simulation
        $finish;
    end

    // Monitor inputs and output changes during simulation
    initial begin
        $monitor("Time = %0t ns | a = %b, b = %b, c = %b, d = %b | s1 = %b, s0 = %b | out = %b", 
                 $time, a, b, c, d, s1, s0, out);
    end
endmodule

```