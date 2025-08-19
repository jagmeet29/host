[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)[](decoderMuxWithAssignment.md)
Signals of type **wire** or a similar **wire**-like **data type** requires the **continuous assignment** of a value. For example, consider an electrical **wire** used to connect pieces on a breadboard. As long as the **$+5V$** battery is applied to one end of the **wire**, the component connected to the other end of the **wire** will get the required voltage.

In **Verilog**, this concept is realized by the **assign statement** where any **wire** or other similar **wire**-like **data-types** can be driven continuously with a value. The value can either be a constant or an **expression** comprising of a group of signals.

## Syntax of `assign` Statement

The assignment syntax starts with the keyword `assign` followed by the signal name which can be either a single signal or a **concatenation** of different signal **nets**. The **drive strength** and **delay** are optional and are mostly used for **dataflow modeling** than **synthesizing** into real hardware. The **expression** or signal on the **right hand side (RHS)** is evaluated and assigned to the **net** or **expression** of **nets** on the **left hand side (LHS)**.

`assign <net_expression> = [drive_strength] [delay] <expression of different signals or constant value>`

**Delay values** are useful for specifying delays for **gates** and are used to model **timing behavior** in real hardware because the value dictates when the **net** should be assigned with the evaluated value.

## Rules for `assign` Statement

There are some rules that need to be followed when using an **assign statement**:
*   **LHS** should always be a **scalar** or **vector net** or a **concatenation** of **scalar** or **vector nets** and never a **scalar** or **vector register**.
*   **RHS** can contain **scalar** or **vector registers** and **function calls**.
*   Whenever any operand on the **RHS** changes in value, **LHS** will be updated with the new value.
*   **assign statements** are also called **continuous assignments** and are always active.

## Examples of `assign` Statement Usage

In the following example, a **net** called `out` is driven continuously by an **expression** of signals. `i1` and `i2` with the **logical AND** (`&`) form the **expression**.

If the **wires** are instead converted into **ports** and **synthesized**, we will get an **RTL schematic** like the one shown below after **synthesis**.

**Continuous assignment statements** can be used to represent **combinational gates** in **Verilog**.

### Verilog Module Example with `assign`

The module shown below takes two inputs and uses an **assign statement** to drive the output `z` using **part-select** and multiple **bit concatenations**. Treat each case as the only code in the module, else many **assign statements** on the same signal will definitely make the output become **X**.

```verilog
module xyz (input [3:0] x,		// x is a 4-bit vector net
			input y, 		// y is a scalar net (1-bit)
			output [4:0] z ); 	// z is a 5-bit vector net

wire [1:0] a;
wire b;

// Assume one of the following assignments are chosen in real design
// If x='hC and y='h1 let us see the value of z

// Case #1: 4-bits of x and 1 bit of y is concatenated to get a 5-bit net
// and is assigned to the 5-bit nets of z. So value of z='b11001 or z='h19
assign z = {x, y};

// Case #2: 4-bits of x and 1 bit of y is concatenated to get a 5-bit net
// and is assigned to selected 3-bits of net z. Remaining 2 bits of z remains
// undriven and will be high-imp. So value of z='bZ001Z
assign z[3:1] = {x, y};

// Case #3: The same statement is used but now bit4 of z is driven with a constant
// value of 1. Now z = 'b1001Z because only bit0 remains undriven
assign z[3:1] = {x, y};
assign z[4] = 1;

// Case #4: Assume bit3 is driven instead, but now there are two drivers for bit3,
// and both are driving the same value of 0. So there should be no contention and
// value of z = 'bZ001Z
assign z[3:1] = {x, y};
assign z[3] = 0;

// Case #5: Assume bit3 is instead driven with value 1, so now there are two drivers
// with different values, where the first line is driven with the value of X which
// at the time is 0 and the second assignment where it is driven with value 1, so
// now it becomes unknown which will win. So z='bZX01Z
assign z[3:1] = {x, y};
assign z[3] = 1;

// Case #6: Partial selection of operands on RHS is also possible and say only 2-bits
// are chosen from x, then z = 'b00001 because z[4:3] will be driven with 0
assign z = {x[1:0], y};

// Case #7: Say we explicitly assign only 3-bits of z and leave remaining unconnected
// then z = 'bZZ001
assign z[2:0] = {x[1:0], y};

// Case #8: Same variable can be used multiple times as well and z = 'b00111
// 3{y} is the same as {y, y, y}
assign z = {3{y}};

// Case #9: LHS can also be concatenated: a is 2-bit vector and b is scalar
// RHS is evaluated to 11001 and LHS is 3-bit wide so first 3 bits from LSB of RHS
// will be assigned to LHS. So a = 'b00 and b ='b1
assign {a, b} = {x, y};

// Case #10: If we reverse order on LHS keeping RHS same, we get a = 'b01 and b='b0
assign {a, b} = {x, y};

endmodule
```

## `reg` vs `wire` with `assign`

It is illegal to drive or assign **reg type variables** with an **assign statement**. This is because a **reg variable** is capable of storing data and does not require to be driven continuously. **reg signals** can only be driven in **procedural blocks** like `initial` and `always`.

## Explicit vs. Implicit Assignment

When an **assign statement** is used to assign the given **net** with some value, it is called **explicit assignment**. **Verilog** also allows an assignment to be done when the **net** is declared and is called **implicit assignment**.

```verilog
wire [1:0] a;
assign a = x & y; 			// Explicit assignment

wire [1:0] a = x & y; 	// Implicit assignment
```

## `assign` Statement for Combinational Logic

Consider the following **digital circuit** made from **combinational gates** and the corresponding **Verilog** code.

**Combinational logic** requires the inputs to be continuously driven to maintain the output unlike **sequential elements** like **flip-flops** where the value is captured and stored at the edge of a **clock**. So an **assign statement** fits the purpose well because the output `o` is updated whenever any of the inputs on the **right hand side** change.

```verilog
// This module takes four inputs and performs a boolean
// operation and assigns output to o. The combinational
// logic is realized using assign statement.

module combo (	input 	a, b, c, d,
								output  o);

  assign o = ~((a & b) | c ^ d);

endmodule
```

After **design elaboration** and **synthesis**, we do get to see a **combinational circuit** that would behave the same way as modeled by the **assign statement**.

See that the signal `o` becomes $1$ whenever the **combinational expression** on the **RHS** becomes true. Similarly `o` becomes $0$ when **RHS** is false. Output `o` is **X** from $0ns$ to $10ns$ because inputs are **X** during the same time.



