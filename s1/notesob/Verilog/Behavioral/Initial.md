A set of Verilog statements are usually executed sequentially in a simulation. These statements are placed inside a _procedural_ block. There are mainly two types of _procedural_ blocks in Verilog - **initial** and **always**.

## The `initial` Block

```verilog
initial
	[single statement]

initial begin
	[multiple statements]
end
```

An `initial` block is not [**synthesizable**](https://www.chipverify.com/verilog/asic-soc-chip-design-flow) and hence cannot be converted into a hardware schematic with digital elements. Hence `initial` blocks do not serve much purpose than to be used in simulations. These blocks are primarily used to initialize variables and drive design ports with specific values.

### Characteristics and Usage

An `initial` block is started at the beginning of a simulation at **time 0 unit**. This block will be **executed only once** during the entire simulation. Execution of an `initial` block finishes once all the statements within the block are executed.

![verilog-initial-block](https://www.chipverify.com/images/verilog/initial-flash-1.PNG)

The image shown above has a `module` called `behave` which has two internal signals called `a` and `b`. The `initial` block has only one statement and hence it is not necessary to place the statement within `begin` and `end`. This statement assigns the value `2'b10` to `a` when the `initial` block is started at time **0 units**.

The code shown below has an additional statement that assigns some value to the signal `b`. However this happens only after **10 time units** from execution of previous statement. This means that `a` is assigned first with the given value and then after **10 time units**, `b` is assigned to `0`.

![verilog-initial-block-begin-end](https://www.chipverify.com/images/verilog/initial-flash-3.png)

## Multiple `initial` Blocks

There are **no limits** to the number of `initial` blocks that can be defined inside a module.

The code shown below has _three_ `initial` blocks all of which are **started at the same time and run in parallel**. However, depending on the statements and the delays within each `initial` block, the time taken to finish the block may vary.

![verilog-multiple-initial-blocks](https://www.chipverify.com/images/verilog/initial-flash-2.PNG)

In this example, the first block has a delay of **20 units**, while the second has a total delay of **50 units** (`10 + 40`) and the last block has a delay of **60 units**. Hence the simulation takes **60 time units** to complete since there is at least one `initial` block still running until **60 time units**.

## Terminating Simulation with `$finish`

`$finish` is a Verilog system task that tells the simulator to **terminate the current simulation**.

If the last block had a delay of **30 time units** like shown below, the simulation would have ended at **30 time units** thereby **killing all the other `initial` blocks** that are active at that time.

```verilog
initial begin
	#30 $finish;
end
```

## Synthesizability of `initial` Blocks

An `initial` block is **not synthesizable**.
