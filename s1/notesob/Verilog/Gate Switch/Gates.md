## How to Use Primitive Gates - Single Line Examples

Let me show you **simple, practical examples** of how to use each primitive gate in real Verilog code. Think of these as the "building blocks" you can copy and use immediately.

## And/Or Gate Examples (Simple One-Liners)

```verilog
// Basic AND gate - output is 1 only when ALL inputs are 1
and gate1(output_signal, input_a, input_b);

// 3-input AND gate - you can have as many inputs as needed
and gate2(result, a, b, c);

// OR gate - output is 1 when ANY input is 1
or gate3(output_signal, input_x, input_y);

// NAND gate - opposite of AND (output is 0 only when all inputs are 1)
nand gate4(output_signal, input_a, input_b);

// NOR gate - opposite of OR (output is 1 only when all inputs are 0)
nor gate5(output_signal, input_a, input_b);

// XOR gate - output is 1 when inputs are different
xor gate6(output_signal, input_a, input_b);

// XNOR gate - output is 1 when inputs are same
xnor gate7(output_signal, input_a, input_b);
```

## Buf/Not Gate Examples (Buffer and Inverter)

```verilog
// Buffer - simply passes input to output (like a wire with delay)
buf buffer1(output_signal, input_signal);

// Buffer with multiple outputs - same input goes to many outputs
buf buffer2(out1, out2, out3, input_signal);

// NOT gate - inverts the input (0 becomes 1, 1 becomes 0)
not inverter1(output_signal, input_signal);

// NOT gate with multiple outputs - all outputs are inverted input
not inverter2(out1, out2, out3, input_signal);
```

## Tristate Gate Examples (Enable/Disable Control)

```verilog
// Tristate buffer - output follows input when enable=1, otherwise high-Z
bufif1 tri_buf1(output_signal, input_signal, enable);

// Tristate buffer - output follows input when enable=0, otherwise high-Z
bufif0 tri_buf2(output_signal, input_signal, enable_n);

// Tristate inverter - output is inverted input when enable=1, otherwise high-Z
notif1 tri_inv1(output_signal, input_signal, enable);

// Tristate inverter - output is inverted input when enable=0, otherwise high-Z
notif0 tri_inv2(output_signal, input_signal, enable_n);
```

## With Delays (For Simulation)

```verilog
// AND gate with 5 time unit delay
and #5 delayed_and(output_sig, in_a, in_b);

// NAND gate with different rise/fall delays
nand #(3, 2) timing_nand(output_sig, in_a, in_b);

// Buffer with minimum:typical:maximum delays
buf #(1:2:3) timing_buf(output_sig, input_sig);
```

## Array Instantiation Examples

```verilog
// Create 8 AND gates at once for 8-bit operation
wire [7:0] result, data_a, data_b;
and and_array[7:0](result, data_a, data_b);

// Create 4 NOT gates for 4-bit inversion
wire [3:0] inverted_data, original_data;
not inv_array[3:0](inverted_data, original_data);
```

## Complete Examples: All Three Modeling Levels

## Gate Level Implementation

```verilog
module full_adder_gates(output sum, carry_out, input a, b, carry_in);
    wire w1, w2, w3;
    // Using primitive gates only
    xor gate1(w1, a, b);        // First XOR
    xor gate2(sum, w1, carry_in); // Second XOR for sum
    and gate3(w2, a, b);        // AND for carry
    and gate4(w3, w1, carry_in); // AND for carry
    or gate5(carry_out, w2, w3); // OR for final carry
endmodule
```

## Dataflow Level Implementation

```verilog
module full_adder_dataflow(output sum, carry_out, input a, b, carry_in);
    // Using continuous assignment
    assign sum = a ^ b ^ carry_in;
    assign carry_out = (a & b) | (carry_in & (a ^ b));
endmodule
```

## Behavioral Level Implementation

```verilog
module full_adder_behavioral(output reg sum, carry_out, input a, b, carry_in);
    // Using always block
    always @(a or b or carry_in)
    begin
        {carry_out, sum} = a + b + carry_in;
    end
endmodule
```

## Key Points in Simple Language

|Keyword|What It Does|Remember This|
|---|---|---|
|`and`|All inputs must be 1 for output to be 1|"**All** must be true"|
|`or`|Any input can be 1 for output to be 1|"**Any** can be true"|
|`not`|Flips the input (0→1, 1→0)|"**Opposite** of input"|
|`nand`|Opposite of AND gate|"**Not** AND"|
|`xor`|Output is 1 when inputs are different|"**Different** inputs"|
|`bufif1`|Acts like wire when control=1, disconnected otherwise|"**Buffer** **if** control is **1**"|

## When to Use Each Level

- **Gate Level**: When you need exact control over hardware implementation
- **Dataflow Level**: When you want to describe logic equations simply
- **Behavioral Level**: When you want to describe what the circuit should do, not how

**Quick Tip**: Start with behavioral level for functionality, then move to gate level for optimization!

