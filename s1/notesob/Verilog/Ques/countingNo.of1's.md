# Verilog Code for Counting Ones in Digital Circuits

Here are the Verilog implementations for each method described previously:

## **1. Full Adders (Combinational Approach)**

For a 7-bit input using direct addition:

```verilog
module count_ones_fulladder(
    input [6:0] in,
    output [2:0] count
);
    wire [6:0] bits;
    assign bits = in;

    // Use binary addition of bits
    assign count = bits[0] + bits[1] + bits[2] + bits[3] + bits[4] + bits[5] + bits[6];
endmodule
```

## **2. Lookup Table (LUT) Method**

### Basic 3-bit LUT Module:

```verilog
module count_ones_lut_3bit(
    input [2:0] in,
    output reg [2:0] count
);
    always @(*) begin
        case (in)
            3'b000: count = 3'd0;
            3'b001: count = 3'd1;
            3'b010: count = 3'd1;
            3'b011: count = 3'd2;
            3'b100: count = 3'd1;
            3'b101: count = 3'd2;
            3'b110: count = 3'd2;
            3'b111: count = 3'd3;
            default: count = 3'd0;
        endcase
    end
endmodule
```

### Complete 7-bit LUT-based Counter:

```verilog
module count_ones_lut_7bit(
    input [6:0] in,
    output [2:0] count
);
    wire [2:0] count0, count1;
    wire [2:0] count_last;

    count_ones_lut_3bit lut0(.in(in[2:0]), .count(count0));
    count_ones_lut_3bit lut1(.in(in[5:3]), .count(count1));

    // For the last bit, just pass its value to a 3-bit count
    assign count_last = in[6] ? 3'd1 : 3'd0;

    assign count = count0 + count1 + count_last;
endmodule
```

## **3. Tree Structure Design**

For an 8-bit input with optimized delay:

```verilog
module count_ones_tree(
    input [7:0] in,
    output [3:0] count
);
    wire [1:0] pair_count0, pair_count1, pair_count2, pair_count3;
    wire [3:0] sum0, sum1;

    // Count ones in each pair
    assign pair_count0 = in[1] + in[0];
    assign pair_count1 = in[3] + in[2];
    assign pair_count2 = in[5] + in[4];
    assign pair_count3 = in[7] + in[6];

    // Add pairs to get sums of 4 bits
    assign sum0 = pair_count0 + pair_count1;
    assign sum1 = pair_count2 + pair_count3;

    // Final count
    assign count = sum0 + sum1;
endmodule
```

## **Key Implementation Notes**

- **Full Adder Approach**: Simplest to implement but may have longer propagation delay for large inputs.
- **LUT Method**: More efficient for FPGA implementations, breaks large problems into smaller lookup operations.
- **Tree Structure**: Provides the best timing performance by minimizing the critical path delay.
- **Output Width**: Each design uses appropriate output bit width based on the maximum possible count ($\lceil \log_2(n+1) \rceil$ bits for $n$-bit input).

Each approach has different trade-offs in terms of **area**, **timing**, and **implementation complexity** depending on your target hardware platform.
