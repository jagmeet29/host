[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)[](notUseDefparamm.md)## User-Defined Parameters in Verilog

### What is a Parameter? (Simple Explanation)
A **parameter** in Verilog is like a *named constant* you create. Think of it as a special variable whose value does not change during simulation. You use parameters to make your Verilog modules more **flexible** and **reusable** because you can change the module's behavior just by changing the parameter value during instantiation—without changing the code itself.

### How Do You Define a Parameter?
To create a parameter, use the `parameter` keyword, followed by a name and a value:

```verilog
parameter DATA_WIDTH = 8;
```

This sets up a constant called `DATA_WIDTH` with the value $8$.

### Where Do You Use Parameters?
- **Module configuration:** Such as setting data bus widths, address sizes, or timing constants.
- **Design reusability:** You can use the same module in different places with different settings.

### Types of Parameters
- **Local Parameter (`localparam`):** Only accessible within the module or block where it's defined.
- **Global Parameter:** Accessible throughout the module hierarchy when passed during instantiation.

|Parameter Type|Scope|Usage Example|
|---|---|---|
|parameter|Module/global|`parameter WIDTH = 8;`|
|localparam|Local to module/block|`localparam MIN_DELAY = 2;`|

### Assigning/Overriding Parameters
Parameters can be assigned a value when **instantiating** a module. There are two ways:
1. **Named Association:**
```verilog
mymodule #( .WIDTH(16) ) u1 (...);
```
2. **Positional Association:**
```verilog
mymodule #(16) u1 (...);
```

You can also use the legacy `defparam` keyword to override a parameter, but this is less preferred for modern code.

### Examples for Each Abstraction Level

#### Gate Level Example (not common, but possible for simple logic):
```verilog
// AND Gate Instance Using Parameters
module and_gate #(parameter WIDTH = 1) (input [WIDTH-1:0] a, b, output [WIDTH-1:0] y);
    assign y = a & b; // Dataflow style due to simplicity
endmodule
```

*You see, the parameter `WIDTH` decides how many AND gates are created.*

#### Dataflow Level:
```verilog
module adder #(parameter WIDTH = 8) ( input [WIDTH-1:0] a, b, output [WIDTH-1:0] sum );
    assign sum = a + b;
endmodule
```

*Here, parameter `WIDTH` lets you create an adder of any size.*

#### Behavioral Level:
```verilog
module counter #(parameter MAX_COUNT = 10) ( input clk, rst, output reg [$clog2(MAX_COUNT)-1:0] count );
    always @(posedge clk or posedge rst)
        if (rst)
            count <= 0;
        else if (count < MAX_COUNT-1)
            count <= count + 1;
        else
            count <= 0;
endmodule
```

*At this level, parameters let you control more complex behaviors, like count range.*

### Key Keywords (With Simple Explanation)
- `parameter`: Declares a named constant at the module level.
- `localparam`: Declares a constant that cannot be overridden outside the module.
- `defparam`: Old way to override a parameter’s value from outside (not recommended anymore).
- `#(...)`: Syntax for parameter passing during module instantiation.

### Why Use Parameters?
- **Reusability:** Same module, different sizes/behaviors.
- **Maintainability:** Change a value in one place only.
- **Scalability:** Eases building designs that must handle variable widths.

### Real-World Example
Let's say you want to create two adders: one for $8$-bit numbers, another for $16$-bit numbers. Instead of writing two new modules, you write one **parameterized adder** and then "customize" it when you use it, like this:

```verilog
adder #(8) adder8 (.a(a8), .b(b8), .sum(sum8));
adder #(16) adder16(.a(a16), .b(b16), .sum(sum16));
```

This saves coding time and helps avoid errors.

**Summary**: User-defined parameters in Verilog are a key feature for creating flexible, scalable, and reusable digital designs. They let you control constants such as widths, delays, or ranges directly at the module level, and adjust these easily during instantiation without changing the code structure.

If you need more code examples or want to understand parameter usage in a specific scenario, let me know!

