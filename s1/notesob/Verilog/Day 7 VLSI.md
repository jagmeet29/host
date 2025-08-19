## MUX 

```verilog
module mux (i,s,o);
parameter N=32;
input [N-1:0] i;
input [$clog2(N)-1:0] s;
output y;
assign y=i[s];
endmodule
```

What is defparameter ?

What are the three aproches of verification in testbench ? which when is best ?


```verilog
// Code your design here
module mux (i,s,y);
parameter N=32;
input [N-1:0] i;
  input [$clog2(N)-1:0] s;
output y;
assign y=i[s];
endmodule


// Code your testbench here
// or browse Examples


module tb;
  parameter N=32;
  reg [N-1:0] i;
  reg [$clog2(N):0] s;
  wire y;
  
  mux m1 (i,s,y);
  
  initial begin 
    i=$random;
    repeat (20)
    begin
      s=$random;
      #2;
    end
  end
  initial begin
    $monitor("i=%b,s=%d,y=%b",i,s,y);
  end
endmodule
```


What is you want to change the parameter inside dut without changing it manually ?
then use `defparam`


```verilog
// Code your testbench here
// or browse Examples
module tb;
  defparam m1.N=4;
  reg [m1.N-1:0] i;
  reg [$clog2(m1.N)-1:0] s;
  wire y;
  
  mux m1 (i,s,y);


  initial begin 
    i=$random;
    repeat (20)
    begin
      s=$random;
      #2;
    end
  end
  initial begin
    $monitor("i=%b,s=%b,y=%b",i,s,y);
  end
endmodule
```


## Decoder



# Structural 

breakdown of top module into smaller module
The smaller module can be in any modeling style

```verilog
// Code your design here
module dmux (i,s,o);
  parameter N=32;
  input [$clog2(N)-1:0] s;
  input i;
  output [N-1:0] o;
  assign   o  = {{N-1{0}},i} << s;
endmodule


// Code your testbench here
// or browse Examples
module tb;
  defparam dut.N=4;
  wire [dut.N-1:0] o;
  reg [$clog2(dut.N)-1:0] s;
  reg i;
  dmux dut (i,s,o);
  initial
  begin
    repeat (20)
      begin
   		 s=$random;
        i=1;
        #2;
      end
  
  begin 
    $monitor("i=%b,s=%b,o=%b",i,s,o);
  end
  end
endmodule
```



```verilog
module mux (i,s,y);
  input [1:0] i;
  input  s;
output y;
assign y=i[s];
endmodule

module mux8 (i,s,y);
  input [7:0] i;
  input [2:0] s;
  output y;
  wire [5:0] yi;
  mux m1 (i[1:0],s[0],yi[0]);
  mux m2(i[3:2],s[0],yi[1]);
  mux m3(i[5:4],s[0],yi[2]);
  mux m4(i[7:6],s[0],yi[3]);
                    mux m12(yi[1:0],s[1],yi[4]);
                    mux m34(yi[3:2],s[1],yi[5]);
  mux m(yi[5:4],s[2],y);
endmodule



module tb;
  parameter N=8;
  reg [N-1:0] i;
  reg [$clog2(N)-1:0] s;
  wire y;
  
  mux8 m1 (i,s,y);
  
  initial begin 
     i = 8'b00100100;
    repeat (20)
    begin
      s=$random;
      #2;
    end
  end
  initial begin
    $monitor("i=%b,s=%d,y=%b",i,s,y);
  end
endmodule
```

```verilog
module mux (i,s,y);
  input [1:0] i;
  input  s;
output y;
  bufif1 o1 (y,i[1],s);
  bufif0 z1 (y,i[0],s);
endmodule

module mux5 (i,s,y);
  input [4:0] i;
  input [2:0] s;
  output y;
  wire [4:0] yi;
  mux m1 (i[1:0],s[0],yi[0]);
  mux m2(i[3:2],s[0],yi[1]);
  mux m3(i[5:4],s[0],yi[3]);
  mux m12(yi[1:0],s[1],yi[2]);
  mux m({yi[3],yi[2]},s[2],y);
endmodule


module tb;
  parameter N=5;
  reg [N-1:0] i;
  reg [$clog2(N)-1:0] s;
  wire y;
  reg [N-1:0] t;
  
  mux5 m1 (i,s,y);
  
  initial begin 
     i = 8'b00100100;
    repeat (50)
    begin
      t=$random;
      if (t<5) 
        begin
        s=t;
        end
      else
        s=s;
      #2;
    end
  end
  initial begin
    $monitor("i=%b,s=%d,y=%b",i,s,y);
  end
endmodule
```
