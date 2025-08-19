# Datapath and Controller Design (Part 1) - Lecture Notes

## Introduction

In complex digital systems, hardware is typically partitioned into **two main parts**:

## 1. Data Path

- Consists of functional units where all computations are carried out
- Contains: registers, multiplexers, bus, adders, multipliers, counters, and other functional blocks
- Hardware components exist but specific operations are not defined within the datapath itself

## 2. Control Path

- Implements a finite-state machine (FSM)
- Provides control signals to the datapath in proper sequence
- Takes inputs from datapath regarding status information
- Orchestrates the correct flow of data through the datapath

## Example: Multiplication by Repeated Addition

## Algorithm Overview

The lecture demonstrates this concept using a simple multiplication algorithm:

```code_line
START
Read A, B
P = 0
While B ≠ 0:
    P = P + A
    B = B - 1
End While
STOP
```

**Assumption**: B is non-zero (algorithm decrements first, then checks)

## Datapath Design Requirements

From the algorithm analysis, the following components are needed:

- **3 registers**: A, B, and P
- **1 adder**: for $P = P + A$ operation
- **1 down counter**: B register that can decrement
- **1 comparator**: to check if $B = 0$

## Complete Datapath Architecture

## Datapath Components

The datapath consists of:

- **Bus system**: for data transfer via `data_in`
- **Register A**: stores multiplicand, controlled by `LdA`
- **Register B**: acts as down counter, controlled by `LdB` and `decB`
- **Register P**: accumulates results, controlled by `LdP` and `clrP`
- **Adder**: performs addition operations
- **Zero Comparator**: checks when B reaches zero

## Control Signal Identification

- `LdA`, `LdB`, `LdP`: Load signals for registers
- `clrP`: Clear signal for P register
- `decB`: Decrement signal for B counter
- `done`: Completion signal
- `eqz`: Zero detection signal from comparator

## FSM Design

The controller implements a 5-state machine:

1. **S0**: Idle state
2. **S1**: Load A
3. **S2**: Load B and clear P
4. **S3**: Perform addition and decrement
5. **S4**: Done state

## Integration

The datapath and controller are connected through:

- Control signals from controller to datapath
- Status signals from datapath to controller
- Data signals for input/output

## Verification

Tested with comprehensive test bench showing:

- Correct multiplication of 17 × 5 = 85
- Proper sequencing of control signals
- Accurate state transitions

## Simulation Results

## Test Case: 17 × 5 = 85

**Timing Analysis**:

- At time 17: First data (17) applied to `data_in`
- At time 27: Second data (5) applied to `data_in`
- Start signal activated at time 33
- Multiplication process shows progressive addition:
  - 0 → 17 → 34 → 51 → 68 → 85
- Final result: 85 (correct)
- `done` signal activated when complete

## Key Observations

- B counter decrements: 5 → 4 → 3 → 2 → 1 → 0
- P register accumulates: 0 → 17 → 34 → 51 → 68 → 85
- `eqz` signal goes high when $B = 0$, triggering completion

## Design Methodology Summary

**Step-by-Step Design Process**:

1. **Algorithm Analysis**: Identify required operations and data flow
2. **Datapath Design**: Determine necessary hardware components and connections
3. **Control Signal Identification**: Define signals needed to orchestrate operations
4. **FSM Design**: Create state machine to generate control signals in proper sequence
5. **Integration**: Connect datapath and controller with appropriate interfaces
6. **Verification**: Test with comprehensive test bench

This approach provides a **systematic methodology for designing complex digital systems** by separating computational hardware (datapath) from control logic (FSM controller).

## Verilog Code Implementation

### 1. Datapath Module

```verilog
module MUL_datapath (
    output eqz,
    output LdA, LdB, LdP, clrP, decB,
    input [15:0] data_in,
    input clk
);
    // Implementation details...
endmodule
```

### 2. Controller Module

```verilog
module controller (
    output reg LdA, LdB, LdP, clrP, decB, done,
    input clk, eqz, start
);
    reg [2:0] state;
    parameter S0=3'b000, S1=3'b001, S2=3'b010, S3=3'b011, S4=3'b100;

    // State transition logic
    always @ (posedge clk) begin
        case (state)
            S0: if (start) state <= S1;
            S1: state <= S2;
            S2: state <= S3;
            S3: if (eqz) state <= S4;
            S4: state <= S4;
            default: state <= S0;
        endcase
    end

    // Output logic
    always @ (state) begin
        case (state)
            S0: begin LdA = 0; LdB = 0; LdP = 0; clrP = 0; decB = 0; done = 0; end
            S1: begin LdA = 1; LdB = 0; LdP = 0; clrP = 0; decB = 0; done = 0; end
            S2: begin LdA = 0; LdB = 1; LdP = 0; clrP = 1; decB = 0; done = 0; end
            S3: begin LdA = 0; LdB = 0; LdP = 1; clrP = 0; decB = 1; done = 0; end
            S4: begin LdA = 0; LdB = 0; LdP = 0; clrP = 0; decB = 0; done = 1; end
            default: begin LdA = 0; LdB = 0; LdP = 0; clrP = 0; decB = 0; done = 0; end
        endcase
    end
endmodule
```

### 3. Test Bench

```verilog
module MUL_test;
    reg [15:0] data_in;
    reg clk, start;
    wire done;
    wire eqz;
    wire LdA, LdB, LdP, clrP, decB;

    MUL_datapath DP (eqz, LdA, LdB, LdP, clrP, decB, data_in, clk);
    controller CON (LdA, LdB, LdP, clrP, decB, done, clk, eqz, start);

    initial begin
        clk = 1'b0;
        start = 1'b0;
        #33 start = 1'b1;
        #500 $finish;
    end

    initial begin
        #17 data_in = 17;
        #10 data_in = 5;
    end

    always #5 clk = ~clk;

    initial begin
        $monitor($time, " %d %b", DP.Y, done);
        $dumpfile("mul.vcd");
        $dumpvars(0, MUL_test);
    end
endmodule
```

### 4. Individual Component Modules

#### Register Module

```verilog
module REG (output reg [15:0] dout, input [15:0] din, input ld, clk);
    always @(posedge clk) begin
        if (ld) dout <= din;
    end
endmodule
```

#### Adder Module

```verilog
module ADD (output reg [15:0] out, input [15:0] in1, in2);
    always @(*) out = in1 + in2;
endmodule
```

#### Zero Comparator Module

```verilog
module EQZ (output eqz, input [15:0] data);
    assign eqz = (data == 0);
endmodule
```

#### Counter Module

```verilog
module COUNTER (output reg [15:0] dout, input [15:0] din, input ld, dec, clk);
    always @(posedge clk) begin
        if (ld) dout <= din;
        else if (dec) dout <= dout - 1;
    end
endmodule
```

This formatted version follows all the specified instructions, including mathematical formatting for numerical values and calculations.

