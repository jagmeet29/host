# SR Latch

> The SR latch (Set-Reset latch) is a fundamental digital storage element that serves as the building block for more complex sequential circuits. It consists of two cross-coupled logic gates that create a feedback loop, allowing the circuit to store one bit of information.

### Basic Structure and Types

The SR latch can be implemented using either:

1. **Two cross-coupled NOR gates**: In this configuration, both inputs are normally 0, and applying a 1 to either input changes the state.
2. **Two cross-coupled NAND gates**: Here, both inputs are normally 1, and applying a 0 to either input changes the state.

In both implementations, the circuit has two outputs, Q and Q′, which are normally complementary to each other.

![[SR_Latch_NOR.png]]NOR Based SR Latch

![[SR_Latch_NAND.png]]NAND Based SR Latch

### The Forbidden State

The input combination S=R=1 in a NOR-based latch causes both outputs to go to 0, violating the requirement that outputs be complementary. This is called the "forbidden state" or "invalid state".

When both inputs subsequently return to 0 from this forbidden state, the next state is unpredictable and depends on which input returns to 0 first. This can lead to:

- Race conditions
- Metastable states
- Unpredictable outputs

This condition should be avoided in practical applications.

###  NOR-Based SR Latch

The NOR-based SR latch operates as follows:

- **Set State**: When Q=1 and Q′=0, the latch is in the set state
- **Reset State**: When Q=0 and Q′=1, the latch is in the reset state

Under normal operation, both inputs remain at 0 unless a state change is desired. The latch's behavior follows this truth table:

|S|R|Q|Q'|State Description|
|---|---|---|---|---|
|0|0|Last Q|Last Q′|Memory state (holds previous value)|
|0|1|0|1|Reset state|
|1|0|1|0|Set state|
|1|1|0|0|Forbidden state|


### NAND-Based SR Latch

The NAND-based SR latch operates with inverted input logic compared to the NOR version:

- Normally both inputs are kept at 1
- S=0,R=1 puts the latch in the set state (Q=1,Q′=0)
- S=1,R=0 puts the latch in the reset state (Q=0,Q′=1)
- S=R=0 is the forbidden state

This implementation is sometimes referred to as an S′R′ latch to indicate that the inputs are active-low.

![[SR_Latch_Control.png]]SR Latch with Enable

### SR Latch with Control Input

The basic SR latch can be modified by adding a control input (also called Enable or En) that determines when the state of the latch can be changed. This creates a gated SR latch which:

- Uses an additional input to enable/disable the S and R inputs
- Prevents the latch from changing state when the enable input is inactive
- Allows state changes only when the enable signal is active

In the NAND implementation with enable:

- When En=0, the state of the latch cannot change regardless of S and R values
- When En=1, the S and R inputs can affect the latch state
- When En=1,S=1,R=0, the latch enters the set state
- When En=1,S=0,R=1, the latch enters the reset state

If En=1 and both S and R are 1 (for NAND implementation), the circuit enters an indeterminate state, which should be avoided.

## Why It Matters

The SR latch is a **fundamental memory element** in electronics. Even though it’s simple and not always used directly in modern systems, it forms the **building block for flip-flops and memory circuits**.

![[srall.png]]