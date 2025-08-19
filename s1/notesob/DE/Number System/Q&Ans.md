# Binary Representation

>[!question] Q1. Minimum bits required to represent 100,000 
>>[!success]- Answer
>>### Minimum Bits to Represent 100,000
>>
>>To find the minimum number of bits required to represent 100,000 in binary, we use the formula: $$\lceil log_2(n+1)\rceil$$ where $n$ is the number to represent.
>>
>>For 100,000:
>>- $log_2(100,000) ≈ 16.61$
>>
>>Therefore, we need 17 bits minimum to represent 100,000.
>>
>>This can be verified by noting that:
>>- $2^{16} = 65,536$ (insufficient)
>>- $2^{17} = 131,072$ (sufficient to represent 100,000)

>[!question] Q2. Minimum Bits to Represent -16
>>[!success]- Answer
>>### Minimum Bits to Represent -16 Using 1's Complement
>>
>>In 1's complement, the range for $n$ bits is: $$-(2^{n-1} - 1) to +(2^{n-1} - 1)$$
>>
>>For -16:
>>- 5 bits: range is -15 to +15 (insufficient)
>>- 6 bits: range is -31 to +31 (sufficient)
>>
>>Answer: 6 bits minimum for 1's complement

>[!question] Q3. Minimum Bits to Represent -16 Using 2's Complement & 1's Complement 
>>[!success]- Answer
>>### Minimum Bits to Represent -16 Using 2's Complement
>>
>>In 2's complement, the range for $n$ bits is: $$-2^{n-1} to +(2^{n-1} - 1)$$
>>
>>For -16:
>>- 4 bits: range is -8 to +7 (insufficient)
>>- 5 bits: range is -16 to +15 (sufficient)
>>
>>Answer: 5 bits minimum for 2's complement

>[!question] Q4. Which is the preferred method for representing negative numbers
>>[!success]- Answer
>>## Preferred Method for Representing Negative Numbers
>>
>>2's complement is the preferred method for representing negative numbers in modern computer systems.
>>
>>### Key Advantages of 2's Complement:
>>
>>1. Unified Arithmetic Operations: The same hardware can perform addition and subtraction for both signed and unsigned numbers without special handling.
>>
>>2. Single Zero Representation: Unlike sign magnitude and 1's complement, 2's complement has only one representation for zero, eliminating the complexity of handling both +0 and -0.
>>
>>3. Extended Range: 2's complement can represent one additional negative number compared to other methods (e.g., in 8 bits: -128 to +127 vs -127 to +127).
>>
>>4. Hardware Efficiency: No special logic is required to handle different signs during arithmetic operations, making the hardware implementation simpler and faster.

>[!question] Q5. Represent -64 and -46 in all methods 
>>[!success]- Answer
>>## Representation of -64 and -46
>>
>>Using 8-bit representation for clarity:
>>
>>### -64 Representations
>>
>>| Method         | Binary Representation | Calculation                              |
>>| -------------- | --------------------- | ---------------------------------------- |
>>| Sign Magnitude | 11000000              | Sign bit (1) + magnitude of 64 (1000000) |
>>| 1's Complement | 10111111              | Flip all bits of +64 (01000000)          |
>>| 2's Complement | 11000000              | Flip bits of +64 and add 1: 10111111 + 1 |
>>
>>### -46 Representations
>>
>>| Method        | Binary Representation | Calculation                                                                 |
>>|---------------|-----------------------|-----------------------------------------------------------------------------|
>>| Sign Magnitude| 10101110             | Sign bit (1) + magnitude of 46 (0101110)                                     |
>>| 1's Complement| 11010001             | Flip all bits of +46 (00101110)                                             |
>>| 2's Complement| 11010010             | Flip bits of +46 and add 1: 11010001 + 1                                    |
>>
>>### Verification Process
>>
>>For 2's Complement (-46):
>>- +46 in binary: 00101110
>>- Flip all bits: 11010001
>>- Add 1: 11010010
>>
>>For 1's Complement (-46):
>>- +46 in binary: 00101110
>>- Flip all bits: 11010001 (final result)

