## Hardware Modeling in Verilog Synthesis

The hardware realization of Verilog code depends on how variables are declared and assigned, with synthesis tools mapping different constructs to specific hardware elements.

## Net vs Register Data Types

**Net Data Types (wire)**

- Always map to physical wires during synthesis.
- Represent connections between structural entities without storing values.
- Cannot hold values - their value is derived from what drives them.

**Register Data Types (reg)**

- Map to either wires or storage cells depending on assignment context.
- Can represent both combinational and sequential logic.
- Despite the name, don't necessarily correspond to physical registers.

## Code Example Analysis

**Example 1: Register Maps to Wire**

```verilog
module reg_maps_to_wire (A, B, C, f1, f2);
    input   A, B, C;
    output  f1, f2;
    wire    A, B, C;
    reg     f1, f2;
    always  @(A or B or C)
    begin
        f1 = ~(A & B);
        f2 = f1 ^ C;
    end
endmodule
```

In this case, both `f1` and `f2` are synthesized as wires because:

- The always block is purely combinational (sensitive to all inputs)
- All outputs are defined for every input combination
- No storage behavior is implied

**Example 2: Mixed Wire and Storage**

```verilog
module a_problem_case (A, B, C, f1, f2);
    input   A, B, C;
    output  f1, f2;
    wire    A, B, C;
    reg     f1, f2;
    always  @(A or B or C)
    begin
        f2 = f1 ^ f2;  // f2 depends on its previous value
        f1 = ~(A & B);
    end
endmodule
```

Here the synthesis results differ:

- `f1` maps to a wire (purely combinational)
- `f2` requires a storage cell because it depends on its previous value (`f2 = f1 ^ f2`)

## Latch Inference

**Incomplete Assignment Problem**

```verilog
module simple_latch (data, load, d_out);
    input   data, load;
    output  d_out;
    always @(load or data)
    begin
        if (!load)
            t = data;
        d_out = !t;
    end
endmodule
```

This code creates an unintended latch because:

- The `if` statement lacks an `else` clause
- Variable `t` is not assigned when `load` is high
- This creates incomplete assignment, forcing synthesis tools to infer a latch to hold the previous value

## Best Practices

To avoid unintended hardware generation:

- Always include `else` statements in combinational always blocks
- Use `default` cases in case statements
- Ensure all outputs are assigned under all possible input conditions
- Remember that latches are only inferred in combinational logic, not in sequential (clocked) processes