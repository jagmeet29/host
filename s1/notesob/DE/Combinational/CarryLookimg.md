![[CarryLookAheadAdder_1.png]]
![[CarryLookAheadAdder_2.png]]
**Carry Generation (G)**
When both A and B are high Cout is 1 even when there is no carry form previous bit
$$G=A \cdot B$$![[CarryLookAheadAdder_3.png]]**Carry Propagating (P)**
From the AND gate we can say:
Cin will be 1 only is there is a carry form previous bit and sum of A,B (A $\oplus$ B) is 1 $$P=(A \oplus B)\cdot C_{in}$$![[CarryLookAheadAdder_4.png]]![[CarryLookAheadAdder_5.png]]![[CarryLookAheadAdder_6.png]]![[CarryLookAheadAdder_7.png]]![[CarryLookAheadAdder_8.png]]![[CarryLookAheadAdder_9.png]]![[CarryLookAheadAdder_10.png]]