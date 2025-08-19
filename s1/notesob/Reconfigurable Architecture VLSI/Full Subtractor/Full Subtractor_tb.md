### Test Bench
```verilog 
// Testbench for Full Subtractor
module tb_full_subtractor;
    // Declare inputs as registers and outputs as wires
    reg a, b, Bin;
    wire D, Bout;

    // Instantiate the full subtractor module
    full_subtractor uut (
        .a(a),
        .b(b),
        .Bin(Bin),
        .D(D),
        .Bout(Bout)
    );

    // Apply test vectors with a monitor to see the outputs
    initial begin
        $monitor("Time=%0t: a=%b, b=%b, Bin=%b, Difference=%b, Borrow=%b", 
                  $time, a, b, Bin, D, Bout);

        // Test all possible combinations of a, b, and Bin
        a = 0; b = 0; Bin = 0; #10;
        a = 0; b = 0; Bin = 1; #10;
        a = 0; b = 1; Bin = 0; #10;
        a = 0; b = 1; Bin = 1; #10;
        a = 1; b = 0; Bin = 0; #10;
        a = 1; b = 0; Bin = 1; #10;
        a = 1; b = 1; Bin = 0; #10;
        a = 1; b = 1; Bin = 1; #10;
        $finish;
    end
endmodule

```