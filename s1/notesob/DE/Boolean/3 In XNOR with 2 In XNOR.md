# Constructing 3-Input XNOR Using 2-Input XNOR Gates

## Understanding 3-Input XNOR Behavior

A 3-input XNOR gate outputs 1 when an even number of inputs are 1 ($0$, $2$, or all 3 inputs are 1). This is shown in the truth table:

| A | B | C | 3-input XNOR |
|---|---|---|--------------|
| 0 | 0 | 0 | 1            |
| 0 | 0 | 1 | 0            |
| 0 | 1 | 0 | 0            |
| 0 | 1 | 1 | 1            |
| 1 | 0 | 0 | 0            |
| 1 | 0 | 1 | 1            |
| 1 | 1 | 0 | 1            |
| 1 | 1 | 1 | 0            |

## The Solution

To implement a 3-input XNOR using 2-input XNOR gates, you need:

3-input XNOR = NOT(XNOR(XNOR(A,B), C))

This requires:
- Two 2-input XNOR gates
- One NOT gate (inverter)

![[XNOR with XNOR.svg]]
## Step-by-Step Construction

### Step 1: First XNOR Gate

Apply the first 2-input XNOR to inputs A and B:
$$ XNOR₁ = XNOR(A, B) $$

### Step 2: Second XNOR Gate

Apply the second 2-input XNOR to the output of the first gate and input C:
$$ XNOR₂ = XNOR(XNOR₁, C) = XNOR(XNOR(A,B), C) $$

### Step 3: Invert the Result

Apply a NOT gate to get the final 3-input XNOR:
$$ 3-input XNOR = NOT(XNOR₂) = NOT(XNOR(XNOR(A,B), C)) $$

## Verification

The implementation is verified by comparing the truth tables:

| A | B | C | XNOR(A,B) | XNOR(XNOR(A,B),C) | NOT(XNOR(XNOR(A,B),C)) | 3-input XNOR |
|---|---|---|-----------|-------------------|------------------------|--------------|
| 0 | 0 | 0 | 1         | 0                 | 1                      | 1 ✓          |
| 0 | 0 | 1 | 1         | 1                 | 0                      | 0 ✓          |
| 0 | 1 | 0 | 0         | 1                 | 0                      | 0 ✓          |
| 0 | 1 | 1 | 0         | 0                 | 1                      | 1 ✓          |
| 1 | 0 | 0 | 0         | 1                 | 0                      | 0 ✓          |
| 1 | 0 | 1 | 0         | 0                 | 1                      | 1 ✓          |
| 1 | 1 | 0 | 1         | 0                 | 1                      | 1 ✓          |
| 1 | 1 | 1 | 1         | 1                 | 0                      | 0 ✓          |

## Circuit Diagram Representation

```
A ──┐     
	├─ XNOR₁ ──┐ 
B ──┘          ├─ XNOR₂ ── NOT ── Output (3-input XNOR)
               │ 
C ─────────────┘
```

## Alternative Understanding

The reason we need the NOT gate is because:

- XNOR(XNOR(A,B), C) produces the complement of the desired 3-input XNOR function
- Adding the NOT gate inverts this complement back to the correct 3-input XNOR behavior

## Key Points

1. Direct cascading of 2-input XNOR gates doesn't work - it produces the inverted result
2. The NOT gate is essential to get the correct 3-input XNOR functionality
3. This method uses minimal hardware - only 2 XNOR gates and 1 inverter
4. The logic is systematic and can be extended for higher-input XNOR functions with appropriate corrections

This implementation provides an efficient way to construct multi-input XNOR functionality using only 2-input XNOR gates and basic logic inverters.