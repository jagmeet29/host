# BCD to Binary and Binary to BCD Conversion

## What is BCD?

- **Binary Coded Decimal (BCD)** is a method for representing decimal numbers where each decimal digit (0-9) is encoded as a 4-bit binary number. For example:
    
    - Decimal 5 → BCD: `0101`
        
    - Decimal 39 → BCD: `0011 1001`
        

## Why Convert Between Binary and BCD?

- **BCD to Binary**: While BCD is useful for displaying numbers on devices like seven-segment displays, binary representation is more efficient for arithmetic operations in digital systems.
    
- **Binary to BCD**: Conversion to BCD is often needed when working with hardware that requires decimal digits, such as digital displays or financial systems.
    

## Steps for BCD to Binary Conversion

To convert an n-digit BCD number into binary:

1. **Convert Each BCD Digit to Decimal**: Decode each 4-bit BCD group into its decimal equivalent.
    
2. **Combine the Decimal Digits**: Form the complete decimal number by multiplying each digit by its positional weight (e.g., tens, hundreds).
    
3. **Convert Decimal to Binary**: Transform the resulting decimal number into binary.
    

## Example:

Convert `BCD = 1001 0111` (representing 97 in decimal) to binary:

1. Split into digits: `1001` (9) and `0111` (7).
    
2. Combine as decimal: 9×10+7=97
    
3. Convert 979797 to binary: `1100001`.
    

## Steps for Binary to BCD Conversion

To convert a binary number into BCD:

1. **Convert Binary to Decimal**: Translate the given binary number into its decimal equivalent.
    
2. **Convert Decimal to BCD**: Represent each decimal digit as a separate 4-bit binary code.
    

## Example:

Convert Binary=1100001 (97 in decimal) to BCD:

1. Convert Binary to Decimal: Binary=1100001→Decimal=97.
    
2. Convert Decimal to BCD:
    
    - Separate digits of 97 : 9 and 7.
        
    - Encode each digit in 4-bit binary:
        
        - 9→1001
            
        - 7→0111
            
    - Resulting BCD: `1001 0111`.
        
