## Difference Between Verilog and C

## Difference Between Verilog and HDL

### Identifier

*   Name of module or Testbench
*   Cannot start with a number or the symbol `$`
*   Must start with an alphabet
*   Must not be a reserved keyword
*   Case-sensitive

```verilog
integer a; // ok
reg $adder; // no
integer 90; // no
wire 9div; // no
wire my_module; // ok
```

> In Verilog, identifiers starting with `$` are system tasks.

### Number Representation

1.  Sized Number
2.  Unsized Number

*   Default size of the number: 32
*   Representation: `size'<base>Number`
*   If more bits are written than the specified size, truncation occurs (e.g., `3'b1001` becomes `3'b001`)
*   Negative numbers (e.g., `-4'b2`) are represented using 2's complement

**Example:**

```verilog
12'b1010_1011_0001
12'hAB1
```

>[!question] What will be the decimal value of `-8'b1`?
>>[!success]- Answer
>>`00000001` → `11111110` (1's complement)
>>`11111110` → `11111111` (adding 1 as 2's complement)
>>-128

*   If `a = 10'bx1001`, 'x' will be padded to fill the remaining bits.
*   If `a = 10'b1001x`, 'x' will not be padded. Padding starts from LSB. This applies also for `z`.
*   `?` and `_` are both used for clear representation.

![[20250620_104412.jpg]]
### Net

*   Used to connect components
*   Does not store values
*   Most common type: `wire`
*   Other types: wand, wor, supply0, supply1
*   Default value: `z`
*   Default size: 1 bit

### Reg

*   Used to store values
*   Does not have continuous driving capability
*   Default value: `x`
*   Default size: 1 bit

### Integer

*   32-bit size
*   Range: $-2^{31}$ to $2^{31}-1$
*   Default value: x

### Time

*   64-bit size
*   Default value: 0

### Real

*   64-bit size
*   Default value: 0

### Realtime

*   64-bit size
*   Default value: 0

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

# Format Specifiers for Verilog/SystemVerilog 

The `$display`, `$write`, and `$sprintf` functions utilize format specifiers to control the output of variables.

|Format Specifier|Type Example|Description/Output Example|
|---|---|---|
|`%b`|`int`, `reg`, `bit`|Binary (e.g., `$display("%b", a);` → 1010)|
|`%d`|`int`, `shortint`|Decimal (e.g., `$display("%d", a);` → 42)|
|`%h`|`int`, `logic`|Hexadecimal (e.g., `$display("%h", a);` → A)|
|`%o`|`int`, `reg`|Octal (e.g., `$display("%o", a);` → 12)|
|`%c`|`char` (SV)|Character (e.g., `$display("%c", 'A');` → A)|
|`%s`|`string` (SV)|String (e.g., `$display("%s", "Hello");`)|
|`%t`|`$time`|Time (e.g., `$display("%t", $time);`)|
|`%v`|Any type|Variable value (no format conversion)|

**Note:**

- **Integer types** (`int`, `shortint`, `longint`, `byte`, `integer`) are commonly used with `%d`, `%h`, `%b`, and `%o`.
- `%v` displays the value as-is, without base conversion.
- `%0d`, `%0h`, etc., suppress leading zeros.

## Integer Data Types in SystemVerilog

|Data Type|Width (bits)|Signed/Unsigned|State (2/4)|
|---|---|---|---|
|`byte`|8|Signed|2-state|
|`shortint`|16|Signed|2-state|
|`int`|32|Signed|2-state|
|`longint`|64|Signed|2-state|
|`integer`|32|Signed|4-state|
|`bit`|User-defined|Unsigned|2-state|
|`logic`|User-defined|Unsigned*|4-state|
|`reg`|User-defined|Unsigned*|4-state|
|`time`|64|Unsigned|4-state|

*`logic` and `reg` are unsigned by default but can be made signed.

## Summary

- Use `%d` for decimal, `%b` for binary, `%h` for hexadecimal, `%o` for octal, and `%v` for raw value.
- All integer types in SystemVerilog can use these specifiers.
- For time, use `%t`; for string, use `%s`; for character, use `%c`.

These specifiers are supported in both Verilog and SystemVerilog. SystemVerilog extends this with more data types and string/character support.

# codes

```verilog
module test;
reg a;
wire b;
integer c;
real d
realtime e;
time f;

initial 
begin
$display("a=%b,b=%b,c=%b,d=%b,e=%b,f=%b");
endmodule
```

Diff bw vector and array

| vector                   | array                                                 |
| ------------------------ | ----------------------------------------------------- |
| continuous set of bits   | set of randomized data types                          |
| size is just before name | size written after name                               |
| eg `reg [size] name`     | `reg name [size]`                                     |
| can only be wire or reg  | could be reg, wire, integer                           |
|                          | memory wastage due to 32 bit is converted to size bit |


`reg [7:0] a` $\rightarrow$ verbos declaration  (more control )
`reg[7] a` $\rightarrow$ compact declaration

How to make 1kb memory in verilog ?
`reg [7:0] memory [0:1025]` 

```verilog
module test;
  reg [3:0]a;
  reg [0:3]b;

initial 
begin
  a=4'b1010;
  b=4'b0101;
end
  initial
    begin
      $display("a[2]=%b,b[2]=%b",a[2],b[2]);
    end
endmodule

//a= 1010 -> place 3210
//b= 0101 -> place 0123
```

```verilog
module test;
  reg [3:0]mem[0:3];


initial 
begin
  mem[0]=4'b1001;
  mem[1]=4'b1011;
  mem[2]=4'b1111;
  mem[3]=4'b1011;
end
  initial
    begin
      $display("%d,%d,%d,%d",mem[0],mem[1],mem[2],mem[3]);
      $display("mem[3][1:0]=%b",mem[3][1:0]);
    end
endmodule

// here 32 bits are wasted due to only use of 4 bits in array
```

![[20250620_115613.jpg|300]]

# Memory Waste
## Array Declaration Analysis

The statement about "32 bits are wasted" is **not entirely accurate**.

The Verilog declaration `reg [3:0]mem[0:3];` creates an unpacked array with:

- **4 elements**
- Each element is **4 bits wide**
- **Total useful data: 16 bits**

## Actual Memory Waste in Simulation

The memory waste is likely **much more than 112 bits** due to simulator storage methods.

**Word Alignment Waste**: Most simulators store array elements in 32-bit word boundaries.

- Each 4-bit element occupies a full 32-bit word
- **4 elements × 32 bits = 128 bits total storage**
- Only 16 bits are actually used
- **112 bits wasted** 

**4-State Storage Overhead**: Since `reg` is a 4-state data type, each bit requires 2 bits of storage in the simulator to represent 0, 1, X, and Z states.

- 4 bits per element × 2 = 8 storage bits per element
- 4 elements × 8 = 32 storage bits total
- **16 additional bits** needed for 4-state representation



## More Efficient Alternatives

To reduce waste, you could use:

1. **Packed Array**: `reg [15:0] mem_packed;` - Uses exactly 16 bits (plus 4-state overhead)
2. **2-State Data Types**: `bit [3:0] mem[0:3];` - Eliminates 4-state storage overhead



## Conclusion

The actual waste is likely **112 bits** from word alignment, not 32 bits. The inefficiency comes from the simulator's storage method, not from the Verilog declaration itself.


# 2

### String

- used to store characters
- first need to create ==sdjai==
- Eg `reg [8*no. of alphabets] name of string`
- 8 is multiplied because alphabets are stored in ASCI codes

```verilog
module test;
  reg [8*7:1]name;


initial 
	begin
  		name="Jagmeet";
      $display("first \n name=%s",name);
    end
  initial
  	begin
  		name="jagmeet_Singh";
      $display("Second \n name=%s",name);
    end
endmodule

//first  
//name=Jagmeet  
//Second  
//name=t_Singh because storage starts form LSB to MSB 
// here J was MSB
```

if we have declared `


---

```verilog
module test;
reg a=4'b100x;
reg b=4'b0x00;

initial begin
$display("1. a&&b=%d",a&&b);
$display("2. a||b=%d",a||b);
$display("3. a|b=%d",a|b);
$display("4. a^b=%d",a^b);
$display("5. a<<b=%d",a<<b);
$display("6. a>>b=%d",a>>b);
$display("7. {a,b}=%d",{a,b});
$display("8. {{2{b}},a}=%d",{{2{b}},a});
$display("9. &a=%d",&a);
$display("10. &b=%d",&b);
$display("11. |b=%d",|b);
$display("12. |a=%d",|a);
$display("13. ^b=%d",^b);
$display("14. ^a=%d",^a);
$display("15. a&&b=%d",a&&b);
end
endmodule
```
