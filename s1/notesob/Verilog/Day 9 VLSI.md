```verilog
module TL (input t,clk, reset ,output reg q);
  always@(t,clk,reset)
   begin
    if (reset)
      q<=0;
     else
       
         if(clk)
           begin
       if (t)
          q<=~q;
           end
   end
endmodule

module test;
  reg clk;
  reg t,reset;
  wire q;
  
  
  TL dut(t,clk,reset,q);
  
 
  
  initial
    begin
      clk=0;
      reset=1;
      #2 t=0;
      #5t=0;
      reset=0;
      #4t=1;
      #6t=0;
      #10 t=1;#6t=0;
      #5 $finish;
    end
      
      
      always
        #5 clk=~clk;
      
      
      initial
        begin
          $dumpfile("dump.vcd");
          $dumpvars(0,clk,t,reset,q);
        end
      endmodule
```

```verilog
module TL (input t,clk, reset ,output reg q);
reg temp;
  assign temp=q;
  always@(posedge clk)
    begin
      if(reset)
        q<=0;
      else if (t)
        q<=~temp;
    end
endmodule

module test;
  reg clk;
  reg t,reset;
  wire q;
  
  
  TL dut(t,clk,reset,q);
  
  initial
    begin
      clk=0;
      reset=1;
      #2 t=0;
      #5t=0;
      reset=0;
      #4t=1;
      #6t=0;
      #10 t=1;#6t=0;
      #5 $finish;
    end
      
      always
        #5 clk=~clk;
      
      initial
        begin
          $dumpfile("dump.vcd");
          $dumpvars(0,clk,t,reset,q);
        end
      endmodule  
```


```verilog

module TL (input t,clk, reset ,output reg q);
wire temp;
  assign temp=q;
  always@(negedge clk , reset)
    begin
      if(reset)
        q<=0;
      else if (t)
        q<=~temp;
    end
endmodule

module counter (clk,reset,q);
  input clk,reset; 
  output [3:0] q;
  TL c1 (1'b1,clk,reset,q[0]);
  TL c2 (1'b1,q[0],reset,q[1]);
  TL c3 (1'b1,q[1],reset,q[2]);
  TL c4 (1'b1,q[2],reset,q[3]);
endmodule
  


  


module test;
  reg clk;
  reg reset;
  wire [3:0] q;
  
  counter dut ( clk,reset, q);
  
  initial begin
    clk=0;
  	    reset=1;
    #10 reset=0;
  
      #100 $finish;
    end
      
      
      always
        #2 clk=~clk;
      
      
      initial
        begin
          $dumpfile("dump.vcd");
          $dumpvars(0,clk,reset,q);
        end
      endmodule

```


# Regions of Verilog

1. Preponed
	- Every initialization and delay will be executed 
2. Active
	- Continuous assignment
	- Blocking assignment
	- RHS part of non blocking assignment will be evaluated
	- All the functions
	- `$display` and `$write`
3. Inactive (`#0` only )
	- 
4. NBA 
	- Updating the LHS of non blocking assignment
5. Postponed 
	- `$monitor` and `$stop`
 
- These regions are for current simulation time 
- every change it will execute 
- These regions are in sequence as mentioned

There are four types of system printing tasks
1. `$display`
	- runs once
	- runs in active region
2. `$write`
	- runs once
	- runs in active region
3. `$monitor`
	- runs in a loop 
	- added newline `\n`
	- runs in postponed region
4. `$strobe`
	- added newline `\n`
	- runs in postponed region

> [!question] 1. what will be the output
> 
> ```verilog
> module test;
>  integer a, b = 2, c = 3;
>  initial begin
>    a = b + c;
>    $display("a=0%d", a);
>  end
> endmodule
> ```
> 
> > [!success]- Answer: a=5

> [!question] 2. what will be the output
> 
> ```verilog
> module test;
>  integer a, b = 2, c = 3;
>  initial begin
>    a <= b + c;
>    $display("a=%0d", a);
>  end
> endmodule
> ```
> 
> > [!success]- Answer: a = x

> [!question] 3. what will be the output
> 
> ```verilog
> module test;
>  integer a, b = 2, c = 3;
>  initial begin
>    a <= b + c;
>    $strobe("a=%0d", a);
>  end
> endmodule
> ```
> 
> > [!success]- Answer: a = 5

> [!question] 4. swap two variables **with** and **without** a third variable  
> _(no code block provided)_

> [!question] 5. swap two variables using **blocking assignment** without a third variable
> 
> > [!success]- Answer:
> > 
> > 1. XOR
> >     
> > 2. +/-
> >     

> [!question] 6. Output?
> 
> ```verilog
> module example;
>  integer a;
>  initial begin
>    #5 a = 6;
>    $strobe($time, "strobe", a);
>    $display($time, "display", a);
>    a = 12;
>  end
> endmodule
> ```

> [!question] 7. What will be the output
> 
> ```verilog
> module test;
>  int a = 1, b = -2;
>  initial begin
>    a = b;
>  end
>  initial begin
>    b = a;
>  end
> endmodule
> ```
> 
> > [!success]- Answer: This will result in race around condition

> [!question] 8. What will be the output
> 
> ```verilog
> module test;
>  int a = 1, b = -2;
>  initial begin
>    a = b;
>  end
>  initial begin
>    #0 b = a;
>  end
> endmodule
> ```
> 
> > [!success]- Answer: This will **not** result in race around condition

> [!question] 9. what will be the output
> 
> ```verilog
> module tb;
>  reg [2:0] a = 3'b000, b = 3'b000;
>  initial begin
>    #10 3'b101: // Comment for context
>      Sdisplay("display1: Sim time=%t, a=%b b=%b", $time, a, b);
>      Sstrobe("strobe1: Sim time=%t, a=%b b=%b", $time, a, b);
>      b = 3'b011;
>      #10 $strobe("strobe2: Sim time=%t, a=%b b=%b", $time, a, b);
>      b = 3'b100;
>      $display("display1: Sim time=%t, a=%b b=%b", $time, a, b);
>      a = 3'b111;
>  end
> endmodule
> ```

> [!question] 10. What will be the output
> 
> ```verilog
> module example3;
>  integer a, b, c, d;
>  initial begin
>    a <= 6;  $display("%0t %d %d %d %d", $time, a, b, c, d);
>    b <= 12; $display("%0t %d %d %d %d", $time, a, b, c, d);
>  end
>  initial begin
>    c <= 20; $display("%0t %d %d %d %d", $time, a, b, c, d);
>    d <= 25; $display("%0t %d %d %d %d", $time, a, b, c, d);
>  end
> endmodule
> ```

> [!question] 11. what will be the output
> 
> ```verilog
> module tb;
>  integer a = 0, b = 0, c = 0, d = 0, e = 0;
>  initial fork
>    begin
>      #15-9; $display("%d-%d-%d-%d-%d", $time, d, a, b, c);
>      #4; d = 3;
>      #1; a = 2;
>      #1; b = 7;
>      #1; c = 4;
>    end
>    begin
>      #9; $display("%d-%d-%d-%d-%d", $time, e, d, a, b);
>      #-10; e = 9;
>    end
>  join
> endmodule
> ```

> [!question] 12. what will be the output
> 
> ```verilog
> module test;
>  integer a = 0, b = 0, c = 0, d = 0, e = 0;
>  initial begin
>    $monitor($time, a, b, c, d, e);
>    a = 5;  #5
>    b = 7;
>    #1 a -= 9; #4 d -= 3; #5 c += 8;
>    fork
>      #1 a -= 9; #4 d -= 3; #5 c += 8;
>    join
>    # d = 10; #2 e = 9;
>  end
> endmodule
> ```