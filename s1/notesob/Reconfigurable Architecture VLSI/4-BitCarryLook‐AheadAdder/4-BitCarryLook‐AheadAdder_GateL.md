```verilog 
module CLA_Gate_Level(
  input  [3:0] A,
  input  [3:0] B,
  input        Cin,
  output [3:0] Sum,
  output       Cout
);
  // Propagate and generate signals using gate primitives
  wire p0, p1, p2, p3;
  wire g0, g1, g2, g3;
  wire c1, c2, c3;
  
  // Compute propagate signals (p = A XOR B)
  xor (p0, A[0], B[0]);
  xor (p1, A[1], B[1]);
  xor (p2, A[2], B[2]);
  xor (p3, A[3], B[3]);
  
  // Compute generate signals (g = A AND B)
  and (g0, A[0], B[0]);
  and (g1, A[1], B[1]);
  and (g2, A[2], B[2]);
  and (g3, A[3], B[3]);
  
  // Calculate carry signals using the CLA equations:
  // c1 = g0 + (p0 & Cin)
  wire temp_c1;
  and (temp_c1, p0, Cin);
  or  (c1, g0, temp_c1);
  
  // c2 = g1 + (p1 & g0) + (p1 & p0 & Cin)
  wire temp1, temp2;
  and (temp1, p1, g0);
  and (temp2, p1, p0, Cin);
  or  (c2, g1, temp1, temp2);
  
  // c3 = g2 + (p2 & g1) + (p2 & p1 & g0) + (p2 & p1 & p0 & Cin)
  wire temp3, temp4, temp5;
  and (temp3, p2, g1);
  and (temp4, p2, p1, g0);
  and (temp5, p2, p1, p0, Cin);
  or  (c3, g2, temp3, temp4, temp5);
  
  // Cout = g3 + (p3 & g2) + (p3 & p2 & g1) + (p3 & p2 & p1 & g0) 
  //       + (p3 & p2 & p1 & p0 & Cin)
  wire temp6, temp7, temp8, temp9;
  and (temp6, p3, g2);
  and (temp7, p3, p2, g1);
  and (temp8, p3, p2, p1, g0);
  and (temp9, p3, p2, p1, p0, Cin);
  or  (Cout, g3, temp6, temp7, temp8, temp9);
  
  // Finally, compute the sum bits (Sum = p XOR carry-in for that bit)
  xor (Sum[0], p0, Cin);
  xor (Sum[1], p1, c1);
  xor (Sum[2], p2, c2);
  xor (Sum[3], p3, c3);
  
endmodule

```