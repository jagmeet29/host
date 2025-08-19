An **array** declaration of a net or variable can be either scalar or vector. Any number of dimensions can be created by specifying an address range after the identifier name and is called a **multi-dimensional array**. Arrays are allowed in Verilog for `reg`, `wire`, `integer`, and `real` data types.

```verilog
reg        y1 [11:0];        // y is an scalar reg array of depth=12, each 1-bit wide
wire [0:7] y2 [3:0];         // y is an 8-bit vector net with a depth of 4
reg  [7:0] y3 [0:1][0:3];    // y is a 2D array rows=2,cols=4 each 8-bit wide
```

An **index** for every dimension has to be specified to access a particular element of an array and can be an expression of other variables. An array can be formed for any of the different data-types supported in Verilog.

Note that a **memory** of $n$ 1-bit `reg` is not the same as an $n$-bit **vector reg**.

## Declaration and Access

```verilog
y1 = 0; 						// Illegal - All elements can't be assigned in a single go

y2[0] = 8'ha2; 			// Assign 0xa2 to index=0
y2[2] = 8'h1c; 			// Assign 0x1c to index=2
y3[1][2] = 8'hdd; 	// Assign 0xdd to rows=1 cols=2
y3[0][0] = 8'haa; 	// Assign 0xaa to rows=0 cols=0
```

### Example

The code shown below simply shows how different arrays can be modeled, assigned, and accessed. `mem1` is an 8-bit vector, `mem2` is an 8-bit array with a depth of 4 (specified by the range `[0:3]`), and `mem3` is a 16-bit vector 2D array with 4 rows and 2 columns. These variables are assigned different values and printed.

```verilog
module des ();
  reg [7:0]  mem1; 							// reg vector 8-bit wide
  reg [7:0]  mem2 [0:3]; 				// 8-bit wide vector array with depth=4
  reg [15:0] mem3 [0:3][0:1]; 	// 16-bit wide vector 2D array with rows=4,cols=2

  initial begin
    int i;

    mem1 = 8'ha9;
    $display ("mem1 = 0x%0h", mem1);

    mem2[0] = 8'haa;
    mem2[1] = 8'hbb;
    mem2[2] = 8'hcc;
    mem2[3] = 8'hdd;
    for(i = 0; i < 4; i = i+1) begin
      $display("mem2[%0d] = 0x%0h", i, mem2[i]);
    end

    for(int i = 0; i < 4; i += 1) begin
      for(int j = 0; j < 2; j += 1) begin
        mem3[i][j] = i + j;
        $display("mem3[%0d][%0d] = 0x%0h", i, j, mem3[i][j]);
      end
    end
  end
endmodule
```

### Simulation Log

```
ncsim> run
mem1 = 0xa9
mem2[0] = 0xaa
mem2[1] = 0xbb
mem2[2] = 0xcc
mem2[3] = 0xdd
mem3[0][0] = 0x0
mem3[0][1] = 0x1
mem3[1][0] = 0x1
mem3[1][1] = 0x2
mem3[2][0] = 0x2
mem3[2][1] = 0x3
mem3[3][0] = 0x3
mem3[3][1] = 0x4
ncsim: *W,RNQUIE: Simulation is complete.
```

## Memories

**Memories** are **digital storage elements** that help store data and information in digital circuits. **RAMs** and **ROMs** are good examples of such **memory** elements.

### Modeling Memories

**Storage elements** can be modeled using **one-dimensional arrays** of type `reg` and is called a **memory**. Each element in the **memory** may represent a **word** and is referenced using a single **array index**.

![[memory.png]]
### Verilog Vectors vs. Memory Arrays

**Verilog vectors** are declared using a **size range** on the left side of the variable name and these get realized into **flops** that match the size of the variable. In the code shown below, the design module accepts clock, reset, and some control signals to read and write into the block.

#### Single Register Example

It contains a 16-bit **storage element** called **register** which simply gets updated during writes and returns the current value during reads. The **register** is written when `sel` and `wr` are high on the same clock edge. It returns the current data when `sel` is high and `wr` is low.

```verilog
module des (    input           clk,
                input           rstn,
                input           wr,
                input           sel,
                input [15:0]    wdata,
                output [15:0]   rdata
                );

	reg [15:0] register;

	always @ (posedge clk) begin
    if (!rstn)
    	register <= 0;
    else begin
    	if (sel & wr)
      	register <= wdata;
    	else
      	register <= register;
    end
	end

	assign rdata = (sel & ~wr) ? register : 0;
endmodule
```

The hardware schematic shows that a 16-bit **flop** is updated when control logic for writes are active and the current value is returned when control logic is configured for reads.

![[verilog_arrays_register_schematic.png]]
#### Register Array Example

In this example, **register** is an **array** that has four locations with each having a width of 16-bits. The design module accepts an additional input signal which is called **addr** to access a particular **index** in the **array**.

```verilog
module des (    input           clk,
                input           rstn,
                input  [1:0]    addr,
                input           wr,
                input           sel,
                input [15:0]    wdata,
                output [15:0]   rdata);

reg [15:0] register [0:3];
integer i;

always @ (posedge clk) begin
    if (!rstn) begin
        for (i = 0; i < 4; i = i+1) begin
            register[i] <= 0;
        end
    end else begin
        if (sel & wr)
            register[addr] <= wdata;
        else
            register[addr] <= register[addr];
    end
end

assign rdata = (sel & ~wr) ? register[addr] : 0;
endmodule
```

It can be seen in the hardware schematic that each **index** of the **array** is a 16-bit **flop** and the input **address** is used to access a particular set of **flops**.

![[verilog_array_schematic.png]]

>[!question] What is the difference between Array and Vector
>>[!success]- Answer
>> ![[Memory Waste]]