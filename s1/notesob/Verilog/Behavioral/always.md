An **always** block is one of the **procedural** blocks in Verilog. Statements inside an **always** block are executed sequentially.

```verilog
always @ (event)
	[statement]

always @ (event) begin
	[multiple statements]
end
```

## Understanding the `always` Block

The **always** block is executed at some particular **event**. The **event** is defined by a **sensitivity list**.

A **sensitivity list** is the expression that defines when the **always** block should be executed and is specified after the `@` operator within parentheses `( )`. This list may contain either one or a group of signals whose value change will execute the **always** block.

In the code shown below, all statements inside the **always** block get executed whenever the value of signals `a` or `b` change.

```verilog
// Execute always block whenever value of "a" or "b" change
always @ (a or b) begin
	[statements]
end
```

### Timing Control and Continuous Execution

An **always** block can be used to realize **combinational** or **sequential** elements. A **sequential** element like **flip flop** becomes active when it is provided with a **clock** and **reset**. Similarly, a **combinational** block becomes active when one of its input values change. These hardware blocks are all working **concurrently** independent of each other. The connection between each is what determines the flow of data. To model this behavior, an **always** block is made as a **continuous process** that gets triggered and performs some action when a signal within the **sensitivity list** becomes active.

In the following example, all statements within the **always** block get executed at every **positive edge** of the signal `clk`.

```verilog
// Execute always block at positive edge of signal "clk"
always @ (posedge clk) begin
	[statements]
end
```

The **always** block repeats continuously throughout the duration of a **simulation**. The **sensitivity list** brings along a certain sense of timing i.e. whenever any signal in the **sensitivity list** changes, the **always** block is triggered. If there are no timing control statements within an **always** block, the **simulation** will hang because of a zero-delay infinite loop!

The example shown below is an **always** block that attempts to invert the value of the signal `clk`. The statement is executed after every $0$ **time units**. Hence, it executes forever because of the absence of a delay in the statement.

```verilog
// always block is started at time 0 units
// But when is it supposed to be repeated ?
// There is no time control, and hence it will stay and
// be repeated at 0 time units only. This continues
// in a loop and simulation will hang !
always clk = ~clk;
```

Even if the **sensitivity list** is empty, there should be some other form of **time delay**. **Simulation** time is advanced by a **delay statement** within the **always** construct as shown below. Now, the clock inversion is done after every $10$ **time units**.

```verilog
always #10 clk = ~clk;
```

**Note**: Explicit **delays** are not **synthesizable** into logic gates!

Hence real Verilog design code always require a **sensitivity list**.

## `always` Block for Sequential Logic: T Flip-Flop Example

The code shown below defines a **module** called `tff` that accepts a data **input**, **clock** and active-low **reset**. The **output** gets inverted whenever `d` is found to be $1$ at the **positive edge** of **clock**. Here, the **always** block is triggered either at the **positive edge** of `clk` or the **negative edge** of `rstn`.

The following events happen at the **positive edge** of **clock** and are repeated for all **positive edges** of **clock**:

1.  First `if` block checks value of active-low **reset** `rstn`.
2.  If `rstn` is zero, then **output** `q` should be **reset** to default value of $0$.
3.  If `rstn` is one, then it means **reset** is not applied and should follow default behavior.
4.  If the previous step is false:
5.  Check value of `d` and if it is found to be one, then invert value of `q`.
6.  If `d` is $0$, then maintain value of `q`.

```verilog
module tff (input d, clk, rstn,	output reg 	q);

	always @ (posedge clk or negedge rstn) begin
		if (!rstn)
			q <= 0;
		else
			if (d)
				q <= ~q;
			else
				q <= q;
	end
endmodule
```

The following events happen at **negative edge** of `rstn` and happen at all such occurrences:

1.  First `if` block checks value of active-low **reset** `rstn`. At **negative edge** of the signal, its value is $0$.
2.  If value of `rstn` is $0$, then it means **reset** is applied and **output** should be **reset** to default value of $0$.
3.  The case where value of `rstn` is $1$ is not considered because the current **event** is **negative edge** of the `rstn`.

## `always` Block for Combinational Logic Example

An **always** block can also be used in the design of **combinational** blocks. For example the following digital circuit represents a combination of three different logic gates that provide a certain **output** at signal `o`.

![[assign-combo.png]]

The code shown below is a **module** with four **input** ports and a single **output** port called `o`. The **always** block is triggered whenever any of the signals in the **sensitivity list** changes in value. **Output** signal is declared as type **`reg`** in the **module** port list because it is used in a **procedural block**. All signals used in a **procedural block** should be declared as type **`reg`**.

```verilog
module combo (	input 	a,
      			input	b,
              	input	c,
              	input	d,
  	            output reg o);

  always @ (a or b or c or d) begin
    o <= ~((a & b) | (c^d));
  end

endmodule
```

See that the signal `o` becomes $1$ whenever the **combinational expression** on the RHS becomes true. Similarly `o` becomes $0$ when RHS is false.

Simulation Output
![combo-gates-wave](https://www.chipverify.com/images/verilog/assign-combo-wave.PNG)

## Synthesis Guidelines for `always` Blocks

It is possible for an **always** block to not be **synthesis friendly**, if it does not follow one of the following templates.

```verilog
// Template #1: Use for combinational logic, all inputs mentioned in
// sensitivity list ensures that it infers a combo block
always @ (all_inputs) begin
	// Combinational logic
end

// Template #2: Use of a if condition without else can cause a latch
// because the previous value has to be held since new value is not
// defined by a missing else clause
always @ (all_inputs) begin
	if (enable) begin
		// latch value assignments
	end
end

// Template #3: Use clock in sensitivity list for sequential elements
always @ (posedge clk) begin
	// behavior to do at posedge clock
end

// Template #4: Use clock and async reset in sensitivity list
always @ (posedge clk or negedge resetn) begin
	if (! resetn) begin
		// behavior to do during reset
	end else begin
		// behavior when not in reset
	end
end
```

