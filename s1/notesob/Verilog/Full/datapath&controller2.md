# Datapath and Controller Design (Part 2) - Lecture Notes

## Improved FSM Coding Style

### Previous Approach vs. Better Approach

**Previous Style**:

- Single `always` block activated by clock edge
- Both state change AND next state computation performed in same block
- Mixed sequential and combinational logic


**Better Recommended Style**:

- **Clock-triggered block**: Only handles state transitions
- **Separate combinational block**: Computes next state using blocking assignments
- **Third block**: Generates control signals for datapath
- Cleaner separation of concerns and better synthesis results


## Example 2: GCD Computation Using Repeated Subtraction

### Algorithm Overview

**GCD Algorithm using Repeated Subtraction**:

```
START
Read A, B
While A ≠ B:
    If A < B: B = B - A
    If A > B: A = A - B
    If A = B: Output A (GCD found)
STOP
```

**Example**: GCD(143, 78)

- $143 > 78 \implies 143 - 78 = 65$
- $65 < 78 \implies 78 - 65 = 13$
- $65 > 13 \implies 65 - 13 = 52$
- $52 > 13 \implies 52 - 13 = 39$
- $39 > 13 \implies 39 - 13 = 26$
- $26 > 13 \implies 26 - 13 = 13$
- $13 = 13 \implies$ **GCD = 13**


## Datapath Architecture

### Required Components

- **2 Registers**: A and B for storing numbers
- **1 Subtractor**: for A-B or B-A operations
- **3 Multiplexers**:
    - MUX1: Select between Aout/Bout for X input
    - MUX2: Select between Aout/Bout for Y input
    - MUX3: Select between SubOut/data_in for Bus
- **1 Comparator**: Generate LT, GT, EQ status signals


### Control Signals

- `LdA`, `LdB`: Load controls for registers A and B
- `sel1`, `sel2`: Select inputs for subtractor multiplexers
- `sel_in`: Select between external data and subtractor output


### Status Signals

- `lt`: A < B
- `gt`: A > B
- `eq`: A = B


## Complete Verilog Implementation

### 1. GCD Datapath Module

```verilog
module GCD_datapath (gt, lt, eq, ldA, ldB, sel1, sel2, sel_in, data_in, clk);
  input ldA, ldB, sel1, sel2, sel_in, clk;
  input [15:0] data_in;
  output gt, lt, eq;
  wire [15:0] Aout, Bout, X, Y, Bus, SubOut;
  PIPO A (Aout, Bus, ldA, clk);
  PIPO B (Bout, Bus, ldB, clk);
  MUX MUX_in1 (X, Aout, Bout, sel1);
  MUX MUX_in2 (Y, Aout, Bout, sel2);
  MUX MUX_load (Bus, SubOut, data_in, sel_in);
  SUB SB (SubOut, X, Y);
  COMPARE COMP (lt, gt, eq, Aout, Bout);
endmodule
```

### 2. Component Modules

#### Register Module (PIPO)

```verilog
module PIPO (data_out, data_in, load, clk);
  input [15:0] data_in;
  input load, clk;
  output reg [15:0] data_out;
  always @ (posedge clk)
    if (load) data_out <= data_in;
endmodule
```

#### Subtractor Module

```verilog
module SUB (out, in1, in2);
  input [15:0] in1, in2;
  output reg [15:0] out;
  always @(*)
    out = in1 - in2;
endmodule
```

#### Comparator Module

```verilog
module COMPARE (lt, gt, eq, data1, data2);
  input [15:0] data1, data2;
  output lt, gt, eq;
  assign lt = data1 < data2;
  assign gt = data1 > data2;
  assign eq = data1 == data2;
endmodule
```

#### Multiplexer Module

```verilog
module MUX (out, in0, in1, sel);
  input [15:0] in0, in1;
  input sel;
  output [15:0] out;
  assign out = sel ? in1 : in0;
endmodule
```

### 3. FSM Controller - Original Style

```verilog
module controller (ldA, ldB, sel1, sel2, sel_in, done, clk, lt, gt, eq, start);
  input clk, lt, gt, eq, start;
  output reg ldA, ldB, sel1, sel2, sel_in, done;
  reg [2:0] state;
  parameter S0=3'b000, S1=3'b001, S2=3'b010, S3=3'b011, S4=3'b100, S5=3'b101;
  // State transition logic
  always @ (posedge clk) begin
    case (state)
      S0: if (start) state <= S1;
      S1: state <= S2;
      S2: if (eq) state <= S5; else if (lt) state <= S3; else if (gt) state <= S4;
      S3: if (eq) state <= S5; else if (lt) state <= S3; else if (gt) state <= S4;
      S4: if (eq) state <= S5; else if (lt) state <= S3; else if (gt) state <= S4;
      S5: state <= S5;
      default: state <= S0;
    endcase
  end
  // Output logic
  always @(state) begin
    case (state)
      S0: begin ldA = 0; ldB = 0; done = 0; end
      S1: begin sel_in = 1; ldA = 1; ldB = 0; done = 0; end
      S2: begin sel_in = 1; ldA = 0; ldB = 1; done = 0; end
      S3: if (eq) done = 1; else if (lt) begin sel1 = 1; sel2 = 0; sel_in = 0; ldA = 0; ldB = 1; end else if (gt) begin sel1 = 0; sel2 = 1; sel_in = 0; ldA = 1; ldB = 0; end
      S4: if (eq) done = 1; else if (lt) begin sel1 = 1; sel2 = 0; sel_in = 0; ldA = 0; ldB = 1; end else if (gt) begin sel1 = 0; sel2 = 1; sel_in = 0; ldA = 1; ldB = 0; end
      S5: begin done = 1; sel1 = 0; sel2 = 0; ldA = 0; ldB = 0; end
      default: begin ldA = 0; ldB = 0; end
    endcase
  end
endmodule
```

### State Transition Diagram

| State | Operation             | Next State Conditions |
|-------|----------------------|-----------------------|
| **S0** | Wait for start       | `start = 1` → S1      |
| **S1** | Load A from data_in | Always → S2           |
| **S2** | Load B from data_in | `eq` → S5, `lt` → S3, `gt` → S4 |
| **S3** | A < B: B = B - A     | `eq` → S5, `lt` → S3, `gt` → S4 |
| **S4** | A > B: A = A - B     | `eq` → S5, `lt` → S3, `gt` → S4 |
| **S5** | Done, output result | Stay in S5            |


## Improved FSM Style - Alternate Approach

### Key Improvements

**Separate State Variables**:

```verilog
reg [2:0] state, next_state;
```

**Simplified Clock Block**:

```verilog
always @ (posedge clk) begin
  state <= next_state;
end
```

**Separate Next State Computation**:

```verilog
always @(state) begin
  case (state)
    S0: begin
      sel_in = 1; ldA = 1; ldB = 0; done = 0;
      next_state = S1;
    end
    S1: begin
      sel_in = 1; ldA = 0; ldB = 1;
      next_state = S2;
    end
    S2: if (eq) begin done = 1; next_state = S5; end else if (lt) begin sel1 = 1; sel2 = 0; sel_in = 0; next_state = S3; ldA = 0; ldB = 1; end else if (gt) begin sel1 = 0; sel2 = 1; sel_in = 0; next_state = S4; ldA = 1; ldB = 0; end
    // Similar for S3, S4, S5...
  endcase
end
```

### Test Bench

```verilog
module GCD_test;
  reg [15:0] data_in;
  reg clk, start;
  wire done;
  GCD_datapath DP (gt, lt, eq, ldA, ldB, sel1, sel2, sel_in, data_in, clk);
  controller CON (ldA, ldB, sel1, sel2, sel_in, done, clk, lt, gt, eq, start);
  initial begin
    clk = 1'b0;
    start = 1'b0;
    #3 start = 1'b1;
    #1000 $finish;
  end
  always #5 clk = ~clk;
  initial begin
    #12 data_in = 143;
    #10 data_in = 78;
  end
  initial begin
    $monitor($time, " %d %b", DP.Aout, done);
    $dumpfile("gcd.vcd");
    $dumpvars(0, GCD_test);
  end
endmodule
```

### Simulation Results

**Test Case**: GCD(143, 78) = 13

**Progressive Values**:

- Time 0: XX (undefined)
- Time 15: 143 (loaded A)
- Time 35: 65 ($143 - 78$)
- Time 55: 52 ($78 - 65 = 13$, then $65 - 13 = 52$)
- Time 65: 39 ($52 - 13$)
- Time 75: 26 ($39 - 13$)
- Time 85: 13 ($26 - 13$)
- Time 87: 13 with done=1 ✓


## Main Differences Between FSM Coding Styles

### Original Style Problems

- **Mixed Logic**: Sequential and combinational logic in same block
- **Complex Debugging**: Harder to trace state transitions
- **Synthesis Issues**: Tools may not optimize effectively
- **Maintenance**: Difficult to modify without introducing bugs


### Improved Style Benefits

| Aspect         | Original Style      | Improved Style       |
|-----------------|----------------------|-----------------------|
| **Separation**   | Mixed sequential/combinational | Clean separation      |
| **Debugging**   | Complex, hard to trace | Easier state tracking |
| **Synthesis**   | Suboptimal results   | Better optimization   |
| **Maintainability** | Error-prone modifications | Cleaner, safer changes |
| **Readability** | Verbose, confusing   | More structured, clear |


## Best Practices

1. **Use separate `always` blocks** for different logic types
2. **Clock block**: Only handle state register updates
3. **Combinational block**: Compute next state and outputs using blocking assignments
4. **Clear naming**: Use descriptive state and signal names
5. **Proper initialization**: Always include reset/default conditions


The improved FSM coding style provides **better synthesis results, easier debugging, and more maintainable code** while maintaining the same functionality as the original approach.
