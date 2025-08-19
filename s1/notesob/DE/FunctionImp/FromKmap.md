## Form K-Map

![[FromKmap.png]]
### 4 - Variable Function on 4x1 
1. Make the K-Map ([[Boolean.canvas|Notesofde]])
2. The two variable can be used as select lines but should be on the same side of K-Map for simplicity
3. So if $A,B$ are select lines then we can also say they are $S_1,S_0$ 
	
	| AB \ CD  | 00  | 01  | 11  | 10  |
	| -------- | --- | --- | --- | --- |
	| **A̅B̅** |     |     |     |     |
	| **A̅B**  |     |     |     |     |
	| **AB**   |     |     |     |     |
	| **AB̅**  |     |     |     |     |
4. When se say $A=0,B=0$ or $S_1=0,S_0=0$ then it is true for entire row. So the entire row is representing $I_0$ input of MUX. 
5. Now we have to make groups horizontally and write down the Boolean expression. This expression is the input of the input line of MUX 
![Sip, scan and win](https://www.youtube.com/watch?v=vOFeSu6Zr94&source_ve_path=Mjg2NjY)