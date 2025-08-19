## Form Truth Table
![[FormTruthTable.png|500]]
### 4 - Variable Function 8x1
1. Make the Truth Table
2. Use 3 LSBs for select lines
3. For the 4th Bit:
	1. Make a table like this
		
| X      | I0  | I1  | I2  | I3  | I4  | I5  | I6  | I7  |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| **A**  | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| **~A** | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  |
| **X**  |     |     |     |     |     |     |     |     |
|        |     |     |     |     |     |     |     |     |
4. For the 4th Bit:
	2. Circle the values which are 1 in the output of function
	3. Fulling the last column of Table we just created:
		1. It you circuited where in the column of  A the put A in the last column 
		2. It you circuited where in the column of  ~A the put ~A in the last column 
		3. It you circuited where in the column of  A and ~A the put 1 in the last column as it is always 1
5. So, Now you have every thing put the last column values to the input of MUX

**X** in Table means no value to be filled

![implementing boolean function using multiplexer - YouTube](https://www.youtube.com/watch?v=q3Nfq6v82t4)