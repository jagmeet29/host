[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)[](Why%20Verilog.md)
| ![[1Representation.png\|400]] | ![[2Representation.png\|450]] |
| ----------------------------- | ----------------------------- |
# Digital IC Design Representation

A design can be represented at various levels from three different points of view:

1. **Behavioral**
2. **Structural**    
3. **Physical**

![[Ydiagram.png]]

These can be conveniently expressed by the Y-diagram, which shows the relationship between behavioral domain (algorithms, finite state machines), structural domain (processors, ALUs, gates), and geometrical layout domain (chip floorplans, cell placement, masks).

## Behavioral Representation

Specifies how a particular design should respond to a given set of inputs. May be specified by:

- Boolean equations    
- Tables of input and output values 
- Algorithms written in standard HLL like C  
- Algorithms written in special HDL like Verilog or VHDL
    

## Behavioral Representation Example

**Full Adder:**

- Two operand inputs A and B    
- A carry input C 
- A carry output Cy   
- A sum output S   

**Express in terms of Boolean expressions:**

`S = A.B'.C' + A'.B'.C + A'.B.C' + A.B.C = A ⊕ B ⊕ C Cy = A.B + A.C + B.C`

**Express in Verilog in terms of Boolean expressions:**

```verilog
module carry (S, Cy, A, B, C);     
    input A, B, C;    
    output S, Cy;    
    assign S = A ^ B ^ C;    
    assign Cy = (A & B) | (B & C) | (C & A); 
endmodule
```

**Express in Verilog in terms of truth table (only Cy is shown):**

```verilog
primitive carry (Cy, A, B, C);     
    input A, B, C;    
    output Cy;    
    table       
        // A  B  C     Cy          
        1  1  ?  :   1 ;          
        1  ?  1  :   1 ;          
        ?  1  1  :   1 ;          
        0  0  ?  :   0 ;          
        0  ?  0  :   0 ;          
        ?  0  0  :   0 ;    
    endtable 
endprimitive
```

## Structural Representation

Specifies how components are interconnected. In general, the description is a list of modules and their interconnection, called a **netlist**. Can be specified at various levels.

At the structural level, the levels of abstraction are:

- The module (functional) level
- The gate level
- The transistor level
- Any combination of above   

In each successive level more detail is revealed about the implementation.

## Example: A 4-bit Ripple Carry Adder

![[RippleCarryAdder.png]]

The design consists of four full adders, where each full adder consists of a sum circuit and a carry circuit.

```
carry = A.B + B.C + C.A sum = A ⊕ B ⊕ C
```

We instantiate carry and sum circuits to create a full adder, then instantiate four full adders to create the 4-bit adder.

```verilog
module add4 (s, cy4, cy_in, x, y);     
    input [3:0] x, y;    
    input cy_in;    
    output [3:0] s;    
    output cy4;    
    wire [2:0] cy_out;    
    add B0 (cy_out[0], s[0], x[0], y[0], ci);    
    add B1 (cy_out[1], s[1], x[1], y[1], cy_out[0]);    
    add B2 (cy_out[2], s[2], x[2], y[2], cy_out[1]);    
    add B3 (cy4, s[3], x[3], y[3], cy_out[2]); 
endmodule module add (cy_out, sum, a, b, cy_in);     
    input a, b, cy_in;    
    output sum, cy_out;    
    sum s1 (sum, a, b, cy_in);    
    carry c1 (cy_out, a, b, cy_in); 
endmodule module sum (sum, a, b, cy_in);     
    input a, b, cy_in;    
    output sum;    
    wire t;    
    xor x1 (t, a, b);    
    xor x2 (sum, t, cy_in); 
endmodule module carry (cy_out, a, b, cy_in);     
    input a, b, cy_in;    
    output cy_out;    
    wire t1, t2, t3;    
    and g1 (t1, a, b);    
    and g2 (t2, a, c);    
    and g3 (t3, b, c);    
    or g4 (cy_out, t1, t2, t3); 
endmodule
```

![[RippleCarryAdderBlocksVLSI.png]]

## Physical Representation

The lowest level of physical specification involving photo-mask information required by the various processing steps in the fabrication process.

At the module level, the physical layout for the 4-bit adder may be defined by a rectangle or polygon, and a collection of ports. At the layout level, there can be a large number of rectangles or polygons.

## Partial physical description for 4-bit adder in Verilog:

```verilog
module add4;     
    input x[3:0], y[3:0], cy_in;    
    output s[3:0], cy4;    
    boundary [0, 0, 130, 500];    
    port x[0] aluminum width = 1 origin = [0, 35];    
    port y[0] aluminum width = 1 origin = [0, 85];    
    port cy_in polysilicon width = 2 origin = [70, 0];    
    port s[0] aluminum width = 1 origin = [120, 65];         
    add a0 origin = [0, 0];    
    add a1 origin = [0, 120]; 
endmodule
```

The design flow progresses through logical design (front-end CAD) including design entry, logic synthesis, and partitioning, followed by physical design (back-end CAD) covering floorplanning, placement, and routing.

![[DigitalIDDedesignFlow.png]]