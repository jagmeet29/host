The primary intent of **data-types** in the **Verilog** language is to represent **data storage elements** like **bits** in a **flip-flop** and **transmission elements** like **wires** that connect between **logic gates** and **sequential structures**.

Almost all **data-types** can only have one of the four different values as given below except for `real` and `event` data types.

## Value System

| Value | Description                                  |
| :---- | :------------------------------------------- |
| $0$   | represents a **logic zero**, or a **false condition** |
| $1$   | represents a **logic one**, or a **true condition**  |
| $x$   | represents an **unknown logic value** (can be zero or one) |
| $z$   | represents a **high-impedance state**        |

The following image shows how these values are represented in timing diagrams and simulation waveforms. Most simulators use this convention where _red_ stands for `X` and _orange_ in the middle stands for **high-impedance** or `Z`.

![[Logic values.png]]

Since **Verilog** is essentially used to describe **hardware elements** like **flip-flops** and **combinational logic** like **NAND** and **NOR**, it has to model the value system found in **hardware**. A **logic one** would represent the **voltage supply** **Vdd** which can range anywhere between $0.8V$ to more than $3V$ based on the **fabrication technology node**. A **logic zero** would represent **ground** and hence a value of $0V$.

`X` or `x` means that the value is simply **unknown** at the time, and could be either $0$ or $1$. This is quite different from the way `X` is treated in **boolean logic**, where it means "**don't care**".

As with any incomplete electric circuit, the **wire** that is not connected to anything will have a **high-impedance** at that node and is represented by `Z` or `z`. Even in **Verilog**, any unconnected **wire** will result in a **high impedance**.

## Data Type Categories: Nets and Variables

**Nets** and **variables** are the two main groups of **data types** which represent different **hardware structures** and differ in the way they are assigned and retain values.

### Nets

**Nets** are used to connect between **hardware entities** like **logic gates** and hence do not store any value on its own. In the image shown below, a **net** called `net_11` is used to connect between the output of the **AND gate** to the first input of the **flip-flop** called `data_0`. In a similar way, the two inputs of the **AND gate** are connected to **nets** `net_45` and `net_67`.

![[nets_variables.png]]
There are different types of **nets** each with different characteristics, but the most popular and widely used **net** in **digital designs** is of type `wire`.

#### Wire Type

A `wire` is a **Verilog data-type** used to connect **elements** and to connect **nets** that are driven by a **single gate** or **continuous assignment**. The `wire` is similar to the **electrical wire** that is used to connect two components on a **breadboard**.

#### Wire Vectors

When there is a requirement for multiple **nets**, they can be bunched together to form a single `wire`. In the image shown below, we have a $4$-bit `wire` that can send $4$ separate values on each one of the wires. Such entities with a width more than $1$ are called **vectors**.

```verilog
wire [3:0] 	n0; 		// 4-bit wire -> this is a vector
```

![[wire.png]]

It is illegal to redeclare a name already declared by a **net**, **parameter** or **variable** as shown in the code below.

```verilog
module design;
	wire    abc;
	wire 	a;
	wire 	b;
	wire 	c;

	wire    abc;   // Error: Identifier "abc" previously declared

	assign abc = a & b | c;
endmodule
```

![[reg vector.png]]
### Variables

A **variable** on the other hand is an abstraction of a **data storage element** and can hold values. A **flip-flop** is a good example of a **storage element**.

#### Reg Type

**Verilog data-type** `reg` can be used to model **hardware registers** since it can hold values between assignments. Does not necessarily mean that it will map to a hardware register during synthesis. Note that a `reg` need not always represent a **flip-flop** because it can also be used to represent **combinational logic**. 

In the image shown on the left, we have a **flip-flop** that can store $1$ bit and the **flip-flop** on the right can store $4$-bits.

![[variables.png]]
#### Integer Type

An `integer` is a general purpose **variable** of $32$-bits wide that can be used for other purposes while modeling **hardware** and stores **integer values**. Range: $-2^{31}$ to $2^{31}-1$

- Size optimization: Synthesis tools determine optimal size through data flow analysis
- Primary use: Loop counting and general-purpose register operations
- Convenience: More suitable than `reg` for mathematical operations


```verilog
integer     count;              // Count is an integer value > 0
```

#### Time and Realtime Types

A `time` **variable** is unsigned, $64$-bits wide and can be used to store **simulation time quantities** for **debugging purposes**. A `realtime` **variable** simply stores **time** as a **floating point quantity**.

```verilog
time        end_time;           // end_time can be stored a time value like 50ns
realtime    rtime;              // rtime = 40.25ps
```

#### Real Type

A `real` **variable** can store **floating point values** and can be assigned the same way as `integer` and `reg`.

```verilog
real        float;              // float = 12.344  - can store floating numbers
```

```verilog
module testbench;
  integer  	int_a; 				// Integer variable
  real 		real_b; 			// Real variable
  time 		time_c; 			// Time variable

  initial begin
    int_a 	= 32'hcafe_1234; 	// Assign an integer value
    real_b 	= 0.1234567; 		// Assign a floating point value

    #20; 						// Advance simulation time by 20 units
    time_c 	= $time; 			// Assign current simulation time

    // Now print all variables using $display system task
    $display ("int_a 	= 0x%0h", int_a);
    $display ("real_b 	= %0.5f", real_b);
    $display ("time_c 	= %0t", time_c);
  end
endmodule
```

Simulation Log

```
ncsim> run
int_a 	= 0xcafe1234
real_b 	= 0.12346
time_c 	= 20
ncsim: *W,RNQUIE: Simulation is complete.
```

#### Strings

**Strings** are stored in `reg`, and the width of the `reg` **variable** has to be large enough to hold the **string**. Each character in a **string** represents an **ASCII value** and requires $1$ byte. If the size of the **variable** is smaller than the **string**, then **Verilog** truncates the leftmost bits of the **string**. If the size of the **variable** is larger than the **string**, then **Verilog** adds zeros to the left of the **string**.

```verilog
// "Hello World" requires 11 bytes

reg [8*11:1] str = "Hello World";         // Variable can store 11 bytes, str = "Hello World"
reg [8*5:1]  str = "Hello World";         // Variable stores only 5 bytes (rest is truncated), str = "World"
reg [8*20:1] str = "Hello World";         // Variable can store 20 bytes (rest is padded with zeros), str = "         Hello World"
```

Here is a full example showing how the three **variables** given above can be simulated.

```verilog
module testbench;
  reg [8*11:1] str1;
  reg [8*5:1]  str2;
  reg [8*20:1] str3;

  initial begin
    str1 = "Hello World";
    str2 = "Hello World";
    str3 = "Hello World";

    $display ("str1 = %s", str1);
    $display ("str2 = %s", str2);
    $display ("str3 = %s", str3);
  end
endmodule
```

Simulation Log

```
ncsim> run
str1 = Hello World
str2 = World
str3 =          Hello World
ncsim: *W,RNQUIE: Simulation is complete.
```

Note that `str1` has the right size to store all $11$ bytes of the **string** "Hello World" and hence the whole **string** gets printed. However `str2` can store only $5$ bytes and hence the upper $6$ bytes get truncated and end up with storing only "World". The third **variable** `str3` is larger than $11$ bytes and pads empty spaces to the left and hence the value stored in it becomes " Hello World".


>[!question] What is the difference between `reg` and `wire`?
>>[!successs]- Answer
>>The fundamental difference lies in their purpose and how they can be assigned values:
>>
>>**Wire** represents physical connections between digital circuits, while **reg** represents data storage elements that can hold values.
>>
>>|Feature|`wire`|`reg`|`logic` (SystemVerilog)|
>>|---|---|---|---|
>>|**Purpose**|Connecting different elements|Data storage elements|Unified data type to replace reg confusion|
>>|**Physical Representation**|Actual physical wires|Not necessarily physical registers|No direct hardware equivalence|
>>|**Value Storage**|No values stored|Retains value until next assignment|Last assignment wins|
>>|**Assignment Methods**|Continuous **assign** statements, module ports|Procedural blocks (**always**/**initial**)|Both **assign** and procedural blocks|
>>|**Default Value**|`z` (high impedance)|`x` (unknown)|`x` (unknown)|
>>|**Default Size**|$1$-bit|$1$-bit|$1$-bit|
>>|**Multiple Drivers**|Allowed (creates **X** if conflicting)|Not typically used|Not permitted|
>>|**Synthesis**|Combinational logic only|**FF**, **latch**, or **combinational**|Depends on usage|

>[!question] What are the default sizes and values of all data types?
>>[!success]- Answer
>>|Data Type|Default Size|Default Value|Description|
>>|---|---|---|---|
>>|`wire`|$1$-bit|`z`|Net type for connections|
>>|`reg`|$1$-bit|`x`|Storage element|
>>|`integer`|$32$-bit|`x`|General-purpose register|
>>|`real`|$64$-bit (implementation dependent)|$0.0$|Floating-point numbers|
>>|`time`|$64$-bit minimum|$0$|Simulation time storage|
>>|`logic` (SystemVerilog)|$1$-bit|`x`|Unified data type|
