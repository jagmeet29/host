# Behavioral

- like algorithm
- works on functionality
- output should always be register type
- input can be wire type
- procedural
	1. `initial`
		1. runs once as $0$ time
		2. non synthesizable 
		3. used in testbench
		4. delays can be added in testbench
	2. `always`
		1. runs in a loop
		2. synthesizable
		3. used in dut
		4. can not write delays 
- multiple statements has to be enclosed in `begin` and `end`
- all will starts at 0 simulation time
- nesting of `initial` and `always` is not allowed sensitivity 

```verilog
always@(sensitivity_list)
```

>[!question] what is the meaning of @ ?
>>[!success]- Answer
>>it holds the simulation until there is a change in sensitivity list.

>[!question] what is sensitivity list ?


```verilog
// Code your design here
module half_adder (A,B,c,s);
  input A,B;
  output  reg c,s;
  
  always@(A,B)
    begin
      s=A^B;
      c=A&B;
    end
endmodule


// Code your testbench here
// or browse Examples
module testbench;
reg a,b;
wire s,c;

  half_adder dut (.A(a),.B(b),.s(s),.c(c));
initial begin
a=1'b0; b=1'b0;
#2
a=1'b0; b=1'b1;
#2 
a=1'b1; b=1'b0;
#2 
a=1'b1; b=1'b1;
end
initial 
begin 
$monitor("a=%b,b=%b,s=%b,c=%b",a,b,s,c);
end
initial begin
$dumpfile("dump.vcd");
$dumpvars(0,a,b,s,c);
end

endmodule
```

```verilog
// Code your design here
module sub (a,b,cin,d,cout);
  input a,b,cin;
  output  reg cout,d;
  
  always@(a,b,cin)
    begin
      d=a^b^cin;
      cout=(~a)&b | (~a)&cin | b&cin;
    end
endmodule


// Code your testbench here
// or browse Examples
module testbench;
reg a,b,cin;
wire d,cout;

  sub dut (.a(a),.b(b),.cin(cin),.d(d),.cout(cout));
initial begin
a=1'b0; b=1'b0; cin=1;
#2
a=1'b0; b=1'b1; cin=0;
#2 
a=1'b1; b=1'b0; cin=1;
#2 
a=1'b1; b=1'b1;
end
initial 
begin 
  $monitor("a=%b,b=%b,cin=%b,d=%b,cout=%b",a,b,cin,d,cout);
end
initial begin
$dumpfile("dump.vcd");
$dumpvars(0,a,b,cin,d,cout);
end

endmodule
```
## conditional statements

1. if else

```verilog
if (condition)
begin
// statements when true
end
else
begin
// statement when false
end
```

- nesting of if else is allowed

2. case

```verilog

```

>[!question] Difference bw if else and ternary operator ?
>>[!success]- Answer
>> in ternary operator if the condition value return x then both the answers will be compared for true and false. if the answer is same then same is printed other wise x will be printed.
>>
>>for if statement if the condition is x then the answer is else part only.
>>


```verilog
module mux (a,b,s,y);
  input a,b,s;
  output reg y;
  
  always@(*)
    begin 
      if (s)
        y=b;
      else
        y=a;
    end
endmodule

module tb;
  reg [1:0] i;
  reg s;
  wire y;
  
  mux m1 (i[1],i[0],s,y);
  
  initial begin 
    repeat (20)
    begin
      i=$random %2;
      s=$random;
      #2;
    end
  end
  initial begin
    $monitor("i=%b,s=%d,y=%b",i,s,y);
  end
endmodule
```

>[!question] what will be the output of this code
>```verilog
>module test;
>reg [2:0] a;
>initial begin
>for ( a=0; a<8;a=a+1)
>begin
>$display("a=%d",a);
>end
>end 
>```
>>[!success]- Answer
>>infinite

>[!question] what is the output of 
>```verilog
module test;
reg [2:0] a=-4'b1001;
initial begin
begin
$display("a=%d",a);
end
end 
>```
>>[!success]- Answer
>>output is `-7` because 1 bit is truncated 


```verilog
module decoder (i,o);
  input [3:0] i ;
  output reg [1:0] o;
  
  always@(*)
    begin 
      if (i==4'b0000)
        o=2'b00;
      else if (i==4'b0010)
        o=2'b01;
      else if (i==4'b0100)
        o=2'b10;
      else 
        o=2'b11;
    end
endmodule


module tb;
  reg [3:0] i;
  wire [1:0]o;
  
decoder x1 (i,o);
  
  initial begin 
	i=4'b0010;
   #2 i=4'b0010;
   #2 i=4'b0100;
   #2 i=4'b1000;
        
  end
  initial begin
    $monitor("i=%b,y=%b",i,o);
  end
endmodule
```

```verilog
module ecoder (i,o);
  input [3:0] i ;
  output reg [1:0] o;
  
  always@(*)
    begin 
      if (i===4'b0001)
        o=2'b00;
      else if (i===4'b0010)
        o=2'b01;
      else if (i===4'b0100)
        o=2'b10;
      else if (i===4'b1000)
      o=2'b11;
      else
        o=2'bxx;
    end
endmodule


module tb;
  reg [3:0] i;
  wire [1:0]o;
  
ecoder x1 (i,o);
  
  initial begin 
    repeat (200)
	#2 i=$random%2;
        
  end
  initial begin
    $monitor("i=%b,y=%b",i,o);
  end
endmodule
```

```verilog
module tb;
  reg [3:0] i;
  wire [1:0]o;
  
ecoder x1 (i,o);
  
  initial begin 
    repeat (200)
	#2 i=$random%2;
        
  end
  initial begin
    $monitor("i=%b,y=%b",i,o);
  end
endmodule

module tb;
  reg [3:0] i;
  wire [1:0]o;
  
pecoder x1 (i,o);
  
  initial begin 
    repeat (200)
	#2 i=$random%2;
        
  end
  initial begin
    $monitor("i=%b,y=%b",i,o);
  end
endmodule
```


How simulator distributes the statement ?



## Case Statement Variants

### Standard Case

Performs exact matching between the **case expression** and **case items**.

### Casez Statement

**Casez statement** treats `z` values as don't cares in both the case expression and case items. This allows for wildcard matching where `z` or `?` can match any value:

```verilog
casez (opcode)
    4'b01??: statement1;  // Matches 4'b0100, 4'b0101, 4'b0110, 4'b0111
    4'b1zzz: statement2;  // Matches any pattern starting with 1
endcase
```

### Casex Statement

**Casex statement** treats both `x` and `z` values as don't cares. However, `casex` is **not recommended** for synthesizable code because it can cause simulation and synthesis mismatches.


