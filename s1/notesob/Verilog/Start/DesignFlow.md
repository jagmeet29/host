[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)[](Design%20Representation.md)## Two Competing HDLs 

1. Verilog 
2. VHDL 

Designs are created typically using HDLs, which get transformed from one level of abstraction to the next as the design ﬂow progresses. 

There are other HDLs like SystemC, SystemVerilog, and many more … 

![[Simpledesignflow.png]]
## Steps in the Design Flow

### Behavioral Design Specification

**Behavioral design** captures the intended functionality of a hardware system in a high-level, abstract form. The “faciality” (i.e., the outward characteristics or behavior) of a design can be specified in several ways:

- **Boolean Expression or Truth Table:**
    - Used for combinational logic.
    - Describes output as a function of inputs.
    - Truth tables list all input combinations and corresponding outputs.

- **Finite-State Machine (FSM) Behavior:**
    - Used for sequential logic.
    - Described via state transition diagrams or tables.
    - Clearly shows state changes and outputs based on inputs and current state.

- **High-Level Algorithm:**
    - Written in hardware description languages (HDLs) or pseudocode.
    - Captures complex, multi-step operations in a procedural manner.

Behavioral specifications must be synthesized into more detailed forms (e.g., RTL, gate-level) for hardware realization.

### Data Path Design

**Data path design** involves generating a netlist of register transfer level (RTL) components:

- **Netlist Structure:**
    - A directed graph where vertices are components (registers, adders, multipliers, multiplexers, decoders, etc.).
    - Edges represent interconnections between components.

- **Structural Design:**
    - Also called netlist specification.
    - Components may be functional modules, gates, or transistors, depending on the abstraction level.

- **Transformation:**
    - Netlists are systematically transformed from higher to lower levels (e.g., module → gate → transistor).

## Logic Design

**Logic design** refines the netlist to the gate or standard cell level:

- **Standard Cells:**
    - Pre-designed circuit modules (gates, flip-flops, multiplexers) at the layout level.

- **Optimization:**
    - Techniques to minimize cost, delay, or power.
    - Conflicting requirements may include:
        - Minimizing the number of gates.
        - Minimizing the number of gate levels (reducing delay).
        - Minimizing signal transition activity (reducing dynamic power).

### Physical Design and Manufacturing

**Physical design** generates the final layout for fabrication or FPGA programming:

- **Layout Generation:**
    - Consists of geometric shapes corresponding to different fabrication layers.

- **FPGA Mapping:**
    - For FPGAs, gate-level netlists are mapped to programmable logic blocks.
    - Offers flexibility but less speed compared to custom ICs.

### Verification and Testing

**Verification and Testing**

- **Simulation:**
    - Performed at logic, switch, and circuit levels to verify correct behavior.
    - Switch-level simulation models transistors as switches, assigning discrete states (0, 1, X) to nodes and switches.

- **Formal Verification:**
    - Uses mathematical analysis to ensure the design meets specifications under all possible scenarios.
    - More exhaustive than simulation, which tests only specific scenarios.

- **Testability Analysis and Test Pattern Generation:**
    - Ensures manufactured devices can be tested for defects.
    - Automatic Test Pattern Generation (ATPG) creates input sequences to detect faults.

---

### Summary Table

|Step|Description|
|---|---|
|Behavioral Design|Specifies functionality via Boolean, FSM, or algorithm; abstract, needs synthesis|
|Data Path Design|Netlist of RTL components (registers, adders, etc.); structural, graph-based|
|Logic Design|Netlist of gates/standard cells; optimized for cost, delay, power|
|Physical Design|Layout generation for fabrication or FPGA mapping|
|Verification & Testing|Simulation (logic/switch/circuit), formal verification, testability analysis, ATPG|
