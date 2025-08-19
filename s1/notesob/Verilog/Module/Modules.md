A `module` is a block of Verilog code that implements a certain functionality. **Modules** can be embedded within other **modules**, and a higher-level **module** can communicate with its lower-level **modules** using their input and output **ports**.

## What is a Module?

A **module** should be enclosed within `module` and `endmodule` keywords. The name of the **module** should be given right after the `module` keyword, and an optional list of **ports** may be declared as well. Note that **ports** declared in the list of port declarations cannot be redeclared within the body of the **module**.

## Module Declaration

```verilog
module <name> ([port_list]);
	// Contents of the module
endmodule

// A module can have an empty portlist
module name;
	// Contents of the module
endmodule
```

## Module Contents

All variable declarations, dataflow statements, functions or tasks, and lower **module** instances, if any, must be defined within the `module` and `endmodule` keywords. There can be multiple **modules** with different names in the same file and can be defined in any order.

# Module Examples and Applications

## D Flip-Flop (DFF) Module Example

![[dff_module.png]]

The **module** `dff` represents a **D flip flop** which has three input **ports** (`d`, `clk`, `rstn`) and one output **port** (`q`). Contents of the **module** describe how a **D flip flop** should behave for different combinations of inputs. Here, input `d` is always assigned to output `q` at the positive edge of `clk` if `rstn` is high because it is an active low reset.

```verilog
// Module called "dff" has 3 inputs and 1 output port
module dff ( 	input d, clk, rstn, output reg	q);

	// Contents of the module
	always @ (posedge clk) begin
		if (!rstn)
			q <= 0;
		else
			q <= d;
	end
endmodule
```

This **module** will be converted into the following digital circuit during **synthesis**.

![[dff_sync_reset_schematic.png]]

Note that you cannot have any code written outside a `module`!

A **module** represents a **design unit** that implements certain behavioral characteristics and will get converted into a digital circuit during **synthesis**. Any combination of inputs can be given to the **module**, and it will provide a corresponding output. This allows the same **module** to be reused to form bigger **modules** that implement more complex hardware.

## Hierarchical Design (GPU Engine Example)

Instead of building up from smaller blocks to form bigger design blocks, the reverse can also be done. Consider the breakdown of a simple **GPU engine** into smaller components such that each can be represented as a **module** that implements a specific feature. The **GPU engine** shown below can be divided into five different **sub-blocks** where each performs a specific functionality. The bus interface unit gets data from outside into the **design**, which gets processed by another unit to extract instructions. Other units down the line process data provided by the previous unit.

![[gpu_modules2.png]]

Each **sub-block** can be represented as a `module` with a certain set of input and output signals for communication with other **modules**, and each **sub-block** can be further divided into more finer blocks as required.

# Module Hierarchy

## Top-Level Modules

A **top-level module** is one which contains all other **modules**. A **top-level module** is not instantiated within any other **module**.

For example, design **modules** are normally instantiated within **top-level testbench modules** so that **simulation** can be run by providing input stimulus. But, the **testbench** is not instantiated within any other **module** because it is a block that encapsulates everything else and hence is the **top-level module**.

The **design** code shown below has a **top-level module** called `design`. This is because it contains all other **sub-modules** required to make the **design** complete. The **sub-modules** can have more nested **sub-modules** like `mod3` inside `mod1` and `mod4` inside `mod2`. Anyhow, all these are included into the **top-level module** when `mod1` and `mod2` are instantiated. So this makes the **design** complete and is the **top-level module** for the **design**.

```verilog
//---------------------------------
//  Design code
//---------------------------------
module mod3 ( [port_list] );
	reg c;
	// Design code
endmodule

module mod4 ( [port_list] );
	wire a;
	// Design code
endmodule

module mod1 ( [port_list] );	 	// This module called "mod1" contains two instances
	wire 	y;

	mod3 	mod_inst1 ( ... ); 	 		// First instance is of module called "mod3" with name "mod_inst1"
	mod3 	mod_inst2 ( ... );	 		// Second instance is also of module "mod3" with name "mod_inst2"
endmodule

module mod2 ( [port_list] ); 		// This module called "mod2" contains two instances
	mod4 	mod_inst1 ( ... );			// First instance is of module called "mod4" with name "mod_inst1"
	mod4 	mod_inst2 ( ... );			// Second instance is also of module "mod4" with name "mod_inst2"
endmodule

// Top-level module
module design ( [port_list]); 		// From design perspective, this is the top-level module
	wire 	_net;
	mod1 	mod_inst1 	( ... ); 			// since it contains all other modules and sub-modules
	mod2 	mod_inst2 	( ... );
endmodule
```

The **testbench** **module** contains stimulus to check functionality of the **design** and is primarily used for **functional verification** using **simulation** tools. Hence, the **design** is instantiated and called `d0` inside the **testbench** **module**. From a simulator perspective, **testbench** is the **top-level module**.

```verilog
//-----------------------------------------------------------
// Testbench code
// From simulation perspective, this is the top-level module
// because 'design' is instantiated within this module
//-----------------------------------------------------------
module testbench;
	design d0 ( [port_list_connections] );

	// Rest of the testbench code
endmodule
```

## Design Hierarchy and Hierarchical Naming

A **hierarchical structure** is formed when **modules** can be instantiated inside one another, and hence the **top-level module** is called the **root**. Since each lower **module** instantiation within a given **module** is required to have different identifier names, there will not be any ambiguity in accessing signals. A **hierarchical name** is constructed by a list of these identifiers separated by dots `.` for each level of the **hierarchy**. Any signal can be accessed within any **module** using the **hierarchical path** to that particular signal.

```verilog
// Take the example shown above in top level modules
design.mod_inst1 					// Access to module instance mod_inst1
design.mod_inst1.y 					// Access signal "y" inside mod_inst1
design.mod_inst2.mod_inst2.a		// Access signal "a" within mod4 module

testbench.d0._net; 					// Top level signal _net within design modu
```