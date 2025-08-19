# Why We Add 6 to BCD Code After Addition

## The Core Problem

In BCD (Binary Coded Decimal), each decimal digit (0-9) is represented using 4 bits. However, 4 bits can represent 16 different values (0000 to 1111), but BCD only uses 10 of these combinations (0000 to 1001). This creates **6 invalid BCD combinations**: 1010, 1011, 1100, 1101, 1110, and 1111.

## When Correction is Needed

BCD addition requires correction in two scenarios:

1. When the sum exceeds 9 (results in invalid BCD code)
2. When a carry is generated from the 4-bit addition.

## Why Specifically 6?

### The Gap Between Binary and BCD

The fundamental reason for adding 6 is the discrepancy between binary and BCD counting:

- **4-bit binary**: Can count from 0 to 15 (16 total values)
- **BCD**: Only uses values 0 to 9 (10 total values)
- **Difference**: $16 - 10 = 6$ invalid combinations.

### Skipping Invalid Values

When we add 6 (0110) to an invalid BCD result, we effectively skip over the 6 forbidden combinations and land in the correct BCD representation.

## Practical Examples

### Example 1: Simple Invalid Result

```
8 (1000) + 5 (0101) = 1101 (13 in binary - INVALID in BCD)
Correction:
1101 (invalid result) + 0110 (add 6) 
------ 
1 0011 (carry=1, digit=3)
```

Result: 13 in BCD = 0001 0011 ✓

### Example 2: Multiple Digit Addition

```
678₁₀ = 0110 0111 1000 (BCD) 
+ 535₁₀ = 0101 0011 0101 (BCD) 
-------        
1011 1010 1101 (all invalid!)
+ 0110 0110 0110 (add 6 to each) 
-------     
1 0001 1 0000 1 0011  
+    1    1    (propagate carries) 
-------     
0001 0010 0001 0011 = 1213₁₀
```

## Mathematical Explanation

### Weight Discrepancy Correction

In BCD, when a digit overflows:

- **Binary interpretation**: Next position has weight 16
- **BCD requirement**: Next position should have weight 10
- **Correction needed**: $16 - 10 = 6$.

### Two's Complement Perspective

Adding 6 is equivalent to subtracting 10 using 2's complement arithmetic:

- To subtract 10: add 2's complement of 10
- $10_{10} = 1010_2$
- 2's complement of 1010 = 0110 (which is 6)
- Therefore, adding 6 effectively subtracts 10 while generating the proper carry.

## The Algorithm

**BCD Addition Correction Process:**

1. Perform standard 4-bit binary addition.
2. Check if result > 9 OR carry generated.
3. If yes: Add 6 (0110) to the result.
4. Propagate any new carry to next digit group.

## Why Not Other Numbers?

The choice of 6 is mathematically precise, not arbitrary:

- Adding 5 would leave some invalid codes uncorrected.
- Adding 7 or higher would skip valid BCD codes unnecessarily.
- Only 6 perfectly bridges the gap between invalid binary results and valid BCD representation.

## Summary

Adding 6 to BCD after addition serves two critical functions:

1. Skips the 6 invalid BCD combinations (1010 through 1111)
2. Generates proper carry behavior to maintain decimal arithmetic properties.

This correction ensures that BCD arithmetic produces the same results as decimal arithmetic while maintaining the 4-bit-per-digit binary representation format.