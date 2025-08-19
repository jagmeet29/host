```verilog 
module decoder_gate(
  input en,
  input A, B, C,
  output y0, y1, y2, y3, y4, y5, y6, y7
);
  // Each output is driven by an AND gate with its proper combination of inverted inputs.
  and (y0, en, ~A, ~B, ~C);
  and (y1, en, ~A, ~B, C);
  and (y2, en, ~A, B, ~C);
  and (y3, en, ~A, B, C);
  and (y4, en, A, ~B, ~C);
  and (y5, en, A, ~B, C);
  and (y6, en, A, B, ~C);
  and (y7, en, A, B, C);
endmodule

```