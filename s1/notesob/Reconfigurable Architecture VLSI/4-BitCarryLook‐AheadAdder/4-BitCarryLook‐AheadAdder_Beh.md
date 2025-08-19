```verilog 
module CLA_Behavioral(
  input  [3:0] A,
  input  [3:0] B,
  input        Cin,
  output reg [3:0] Sum,
  output reg       Cout
);
  reg [3:0] p, g;
  reg c1, c2, c3;
  
  always @(*) begin
    // Compute propagate and generate signals
    p = A ^ B;  // Propagate term
    g = A & B;  // Generate term

    // Compute carry signals using look-ahead logic
    c1 = g[0] | (p[0] & Cin);
    c2 = g[1] | (p[1] & g[0]) | (p[1] & p[0] & Cin);
    c3 = g[2] | (p[2] & g[1]) | (p[2] & p[1] & g[0]) | (p[2] & p[1] & p[0] & Cin);
    Cout = g[3] | (p[3] & g[2]) | (p[3] & p[2] & g[1]) |
           (p[3] & p[2] & p[1] & g[0]) | (p[3] & p[2] & p[1] & p[0] & Cin);

    // Compute sum bits for each bit position
    Sum[0] = p[0] ^ Cin;
    Sum[1] = p[1] ^ c1;
    Sum[2] = p[2] ^ c2;
    Sum[3] = p[3] ^ c3;
  end
endmodule

```