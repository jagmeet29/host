[](Operators%20Precedence.md)[](Operators%20Precedence.md)[](Operators%20Precedence.md)
In **Verilog**, the **strength** of driving a net refers to the relative power or capability of a driver to influence the value of a net.

## Types of Strengths

Two types of **strengths** can be specified in a net declaration:

### Charge Strength

**Charge strength** is specifically used with **`trireg`** nets to model charge storage. It indicates the relative size of the capacitance associated with the net indicated by either **`small`**, **`medium`**, or **`large`**.

This strength determines how quickly a charge can decay on the net when it is not actively driven, allowing for more accurate simulation of real-world behavior in circuits that involve capacitive elements. The default charge strength of a **`trireg`** net is **`medium`**.

The simulation time for charge decay should be defined in the delay specification for the **`trireg`** net.

```verilog
trireg                          a_net;    // strength medium by default
trireg   (medium) #(0, 0, 100)  cap1;     // strength medium, charge decay time of 100 time units
trireg   (large)  [3:0]         cap2;     // strength large, no decay time
```

### Drive Strength

**Drive strength** refers to the capability of a driver to influence the value of a net. It indicates how strongly a signal is driven on the output terminals of a gate or net.

**Drive strength** is crucial in resolving conflicts when multiple drivers attempt to control a net. The net will take on the value from the strongest driver, and if there are conflicting values from drivers of the same strength, the result will be unknown (x).

When using the **`assign`** statement, you can specify the driving strength explicitly. The syntax for this is:

```verilog
assign  (strength1, strength0) net = expression;
```

*   **`strength1`**: The strength when the net is driven to logic **`1`**.
*   **`strength0`**: The strength when the net is driven to logic **`0`**.

If no strengths are specified, the default drive strength is typically **`strong`**, which means that the net will take on the value from a strong driver if multiple drivers are present.

If multiple drivers with different strengths attempt to drive a net, the net will take on the value of the strongest driver. If two or more drivers have the same strength but different values, the result will be unknown (x).

```verilog
wire out;

assign (strong1, weak0) out = a & b; // Drives 'out' with strong1 when true
```

In this example, if `a & b` evaluates to **`1`**, `out` will be driven with a strong signal; if it evaluates to **`0`**, it will be driven weakly.

## Specific Drive Strengths

### `supply0` and `supply1`

The **`supply0`** net is a net that is always driven to a logic low (**`0`**) value. It is typically used to represent a ground connection or a negative power supply in a circuit. When connected to other components, it ensures that those components see a consistent low voltage level. If no other driver is present, the value of a **`supply0`** net remains **`0`**. It can be used in simulations to model scenarios where certain parts of the circuit are grounded.

The **`supply1`** net is a net that is always driven to a logic high (**`1`**) value. It represents a positive power supply connection, ensuring that connected components receive a consistent high voltage level. Similar to **`supply0`**, if no other driver is present, the value of a **`supply1`** net remains **`1`**. This is useful for modeling scenarios where certain parts of the circuit are powered.

### `strong0` and `strong1`

The **`strong0`** keyword indicates that the driver will actively drive the net to a logic low (**`0`**) with **`strong`** strength. When a net is assigned a value using **`strong0`**, it signifies that the driver has a robust capability to pull the net down to **`0`**, overriding weaker drivers.

The **`strong1`** keyword signifies that the driver will actively drive the net to a logic high (**`1`**) with **`strong`** strength. When a net is assigned a value using **`strong1`**, it indicates that the driver can effectively pull the net up to **`1`**, overpowering any weaker drivers.

If multiple drivers are connected to the same net, the net will take on the value from the strongest driver. If there are conflicting values from drivers of equal strength, the result will be unknown (x).

```verilog
assign (strong1, weak0) my_net = some_signal;    // Drives my_net high with strong strength
assign (weak1, strong0) my_net = another_signal; // Drives my_net low with strong strength
```

### `pull0` and `pull1`

The **`pull0`** strength indicates that a net has a resistive pull-down device connected to it. When a net is assigned the **`pull0`** strength, it will be driven to a logic low (**`0`**) when no other drivers are actively driving it high. This ensures that the net defaults to **`0`** if left floating. If no drivers are present or if all drivers are in a high-impedance state (z), the net will resolve to **`0`** due to the pull-down effect.

The **`pull1`** strength signifies that a net has a resistive pull-up device connected to it. When assigned the **`pull1`** strength, the net will be driven to a logic high (**`1`**) when no other drivers are actively driving it low. This ensures that the net defaults to **`1`** if left floating. Similar to **`pull0`**, if no drivers are present or all are in high-impedance state (z), the net will resolve to **`1`** due to the pull-up effect.

If a net with pull strengths experiences conflicting values from active drivers, the strongest driver will take precedence. If two drivers of equal strength drive different values, the result will be unknown (x).

```verilog
assign (pull1, pull0) my_net = some_signal; // Pulls up to 1 unless driven low
```

### `weak0` and `weak1`

The **`weak0`** strength indicates that a net will be driven to a logic low (**`0`**) with a weak driving capability. When a net is assigned the **`weak0`** strength, it signifies that the driver can pull the net down to **`0`**, but it is not as strong as other driving strengths like **`strong0`** or **`pull0`**. This is useful in situations where you want to allow for the possibility of other stronger drivers to take precedence. If no stronger drivers are present, the net will resolve to **`0`** when driven by **`weak0`**.

The **`weak1`** strength indicates that a net will be driven to a logic high (**`1`**) with a weak driving capability. When assigned the **`weak1`** strength, it means that the driver can pull the net up to **`1`**, but again, it is weaker than other driving strengths like **`strong1`** or **`pull1`**. This allows for potential overriding by stronger drivers. If no stronger drivers are present, the net will resolve to **`1`** when driven by **`weak1`**.

In cases where multiple drivers are connected to a single net, the net will take on the value from the strongest driver. If two or more drivers of equal strength drive conflicting values, the result will be unknown (x).

```verilog
assign (weak1, weak0) my_net = some_signal; // Drives my_net with weak strengths
```

### `highz0` and `highz1`

The **`highz0`** strength indicates that a net is in a high-impedance state while being driven to a logic low (**`0`**). It is typically used when modeling nets that can be disconnected or tri-stated, allowing the net to effectively "float" at **`0`** when no active drivers are present. When a net is assigned the **`highz0`** strength, it means that it can be driven to **`0`** but will also enter a high-impedance state if no active drivers are present.

The **`highz1`** strength signifies that a net is in a high-impedance state while being driven to a logic high (**`1`**). Similar to **`highz0`**, this strength is used in scenarios where the net can be tri-stated and should float at **`1`** when not actively driven. When assigned the **`highz1`** strength, the net can be driven to **`1`** but will enter a high-impedance state if there are no active drivers.

```verilog
assign (highz1, pull0) my_net = some_signal; // Drives my_net with high impedance when not driven
```

## Drive Strength Rules and Constraints

The following two rules shall constrain the use of drive strength specifications:

*   The strength specifications (**`highz1`**, **`highz0`**) and (**`highz0`**, **`highz1`**) shall be treated as illegal constructs.
*   If drive strength is not specified, it shall default to (**`strong1`**, **`strong0`**).

## Example and Simulation

### Verilog Example

```verilog
module tb;

    // Declare nets with different strengths
    reg a, b, c, d;

    wire strong0_net, strong1_net;
    wire pull0_net, pull1_net;
    wire weak0_net, weak1_net;
    wire highz0_net, highz1_net;

    // Assign strong drivers
    assign (strong1, weak0) strong1_net = a; // Strongly drives high if 'a' is 1
    assign (weak1, strong0) strong0_net = b; // Strongly drives low if 'b' is 0

    // Assign pull drivers
    assign (pull1, pull0) pull1_net = c; // Pulls up to 1 unless driven low
    assign (pull0, pull1) pull0_net = d; // Pulls down to 0 unless driven high

    // Assign weak drivers
    assign (weak1, weak0) weak1_net = a; // Weakly drives high if 'a' is 1
    assign (weak0, weak1) weak0_net = b; // Weakly drives low if 'b' is 0

    // Assign high impedance drivers
    assign (highz1, pull0) highz1_net = a; // High impedance when not driven
    assign (highz0, pull1) highz0_net = b; // High impedance when not driven

    initial begin
      reg [1:0] values = {1'b1, 1'b0};

      repeat (10) begin
        integer idx;

        #10;
        idx = $random % 2;
        a = values[idx];
        idx = $random % 2;
        b = values[idx];
        idx = $random % 2;
        c = values[idx];
        idx = $random % 2;
        d = values[idx];
      end
    end

    initial
      $monitor("[%0t] a=%0b b=%0b c=%0b d=%0b strong1=%0b strong0=%0b pull1=%0b pull0=%0b weak1=%0b weak0=%0b highz1=%0b highz0=%0b", $time, a, b, c, d, strong1_net, strong0_net, pull1_net, pull0_net, weak1_net, weak0_net, highz1_net, highz0_net);

endmodule
```

### Simulation Log

```text
xcelium> run
[0] a=x b=x c=x d=x strong1=x strong0=x pull1=x pull0=x weak1=x weak0=x highz1=x highz0=x
[10] a=0 b=x c=x d=x strong1=0 strong0=x pull1=x pull0=x weak1=0 weak0=x highz1=0 highz0=x
[20] a=1 b=1 c=x d=0 strong1=1 strong0=1 pull1=x pull0=0 weak1=1 weak0=1 highz1=z highz0=1
[30] a=1 b=1 c=0 d=1 strong1=1 strong0=1 pull1=0 pull0=1 weak1=1 weak0=1 highz1=z highz0=1
[40] a=1 b=0 c=1 d=0 strong1=1 strong0=0 pull1=1 pull0=0 weak1=1 weak0=0 highz1=z highz0=z
[50] a=x b=0 c=1 d=x strong1=x strong0=0 pull1=1 pull0=x weak1=x weak0=0 highz1=x highz0=z
[60] a=0 b=1 c=0 d=0 strong1=0 strong0=1 pull1=0 pull0=0 weak1=0 weak0=1 highz1=0 highz0=1
[70] a=0 b=x c=0 d=x strong1=0 strong0=x pull1=0 pull0=x weak1=0 weak0=x highz1=0 highz0=x
[80] a=x b=x c=x d=0 strong1=x strong0=x pull1=x pull0=0 weak1=x weak0=x highz1=x highz0=x
[90] a=0 b=0 c=0 d=x strong1=0 strong0=0 pull1=0 pull0=x weak1=0 weak0=0 highz1=0 highz0=z
[100] a=0 b=x c=x d=x strong1=0 strong0=x pull1=x pull0=x weak1=0 weak0=x highz1=0 highz0=x
xmsim: *W,RNQUIE: Simulation is complete.
```

