Logic gates are the **fundamental building blocks of digital electronics** that perform logical operations on binary inputs ($0$s and $1$s) to produce specific outputs based on predetermined rules. These electronic devices manipulate binary data using Boolean algebra principles and form the foundation of all digital circuits, from simple calculators to complex processors.



<content>



## Laws

Here are the fundamental laws in logic gates defined in simple terms:

**Commutative Law**: The order of inputs doesn't affect the output.

_That means you can interchange the position of variable and get the same output._

**Associative Law**: The grouping of operations doesn't matter as priority is the same.

_That means you can make  3/N input gate with 2 input gate_

**Distributive Law**: Defines how operations distribute over parentheses.

**Identity Law**: Variables remain unchanged when combined with specific constants.

**Idempotent Law**: A variable combined with itself yields the same variable.

**De Morgan's Laws**: The complement of a compound operation equals the operation of complements with the operator flipped.

**Complement Law**: A variable combined with its opposite always produces a predictable result.

**Absorption Law**: A variable absorbs redundant terms involving itself.

**Null Law**: A variable combined with certain constants produces that constant regardless of the variable's value.

**Double Negation Law**: Applying NOT twice to a variable returns the original variable.

**Involution Law**: The complement of a complement equals the original variable.

These laws form the mathematical foundation for designing and simplifying digital logic circuits.



</content>



## Basic Logic Gates

<img src="..\notesob\DE\Boolean\img\logicGates.jpeg">

<content>

## AND Gate

The AND gate performs **logical multiplication** and outputs $1$ only when **all inputs are $1$**.

**Disable Input** : 0 (as if any input is zero then output is always zero i.e. NO CHANGE) 

**Boolean Expression**: 

$$\begin{align*}Y &= A \cdot B \ (SOP) \newline Y &= (A+B)\cdot (A+\bar B) \cdot (\bar A+ B) \ (SOP)\end{align*}$$



**Truth Table**:

| A    | B    | Output |
| ---- | ---- | ------ |
| $0$  | $0$  | $0$    |
| $0$  | $1$  | $0$    |
| $1$  | $0$  | $0$    |
| $1$  | $1$  | $1$    |

</content>

<content>

## OR Gate

The OR gate outputs $1$ when **at least one input is $1$**.

**Disable Input** : 1 (as if any input is one then output is always one i.e. NO CHANGE) 

**Boolean Expression**: 

$$\begin{align*}Y &= A + B \ (SOP) \newline Y &= (A\cdot B) + (A \cdot \bar B) + (\bar A \cdot B) \ (SOP)\end{align*}$$



**Truth Table**:

| A    | B    | Output |
| ---- | ---- | ------ |
| $0$  | $0$  | $0$    |
| $0$  | $1$  | $1$    |
| $1$  | $0$  | $1$    |
| $1$  | $1$  | $1$    |



</content>

<content>



## NOT Gate (Inverter)

The NOT gate has **only one input** and produces the **inverse of that input**.

**Boolean Expression**: $Y = A'$

**Truth Table**:

| A    | Output |
| ---- | ------ |
| $0$  | $1$    |
| $1$  | $0$    |





</content>



## Drived Logic Gates



<content>



## NAND Gate (Universal Gate)

The NAND gate combines an **AND gate followed by a NOT gate**. It's called a **universal gate** because any Boolean function can be implemented using only NAND gates.

**Boolean Expression**: $Y = (A \cdot B)'$

**Truth Table**:

| A    | B    | Output |
| ---- | ---- | ------ |
| $0$  | $0$  | $1$    |
| $0$  | $1$  | $1$    |
| $1$  | $0$  | $1$    |
| $1$  | $1$  | $0$    |

**Key Property**: Produces a low output ($0$) **only when all inputs are high**.

</content>

<content>

## NOR Gate (Universal Gate)

The NOR gate combines an **OR gate followed by a NOT gate** and is another **universal gate**.

**Boolean Expression**: $Y = (A + B)'$

**Truth Table**:

| A    | B    | Output |
| ---- | ---- | ------ |
| $0$  | $0$  | $1$    |
| $0$  | $1$  | $0$    |
| $1$  | $0$  | $0$    |
| $1$  | $1$  | $0$    |

**Key Property**: Outputs $1$ **only when all inputs are $0$**.

</content>

<content>

## XOR Gate (Exclusive OR)

The XOR gate outputs $1$ when inputs are **different** from each other. _Also, XOR gate is A for odd number A inputs._

**Boolean Expression**: 

$$\begin{align*} Y &= A \oplus B  =\bar A\cdot B + A \cdot \bar B\ (SOP) \newline Y&= (A+B) \cdot (\bar A + \bar B) \ (POS)\newline \end{align*}$$



**Disable Input** : There is no disable input in XOR gate as for every input changes visible at the output.

- **Buffer** - For zero
- **Inviter** - For one



**Truth Table**:

| A    | B    | Output |
| ---- | ---- | ------ |
| $0$  | $0$  | $0$    |
| $0$  | $1$  | $1$    |
| $1$  | $0$  | $1$    |
| $1$  | $1$  | $0$    |

>[!Note]
>XOR and XNOR gates are self dual [[DE/Boolean/duality.md|What is Dual ?]]

</content>

<content>

## XNOR Gate (Exclusive NOR)

The XNOR gate outputs $1$ when **both inputs are the same** (both $0$ or both $1$).

**Boolean Expression**: 

$$\begin{align*} Y &= \overline{ A \oplus B } =\bar A \cdot \bar B + A \cdot  B\ (SOP) \newline Y&= (\bar A+B) \cdot ( A + \bar B) \ (POS)\newline \end{align*}$$



**Disable Input** : There is no disable input in XOR gate as for every input changes visible at the output.

- **Buffer** - For one
- **Inviter** - For zero



**Truth Table**:

| A    | B    | Output |
| ---- | ---- | ------ |
| $0$  | $0$  | $1$    |
| $0$  | $1$  | $0$    |
| $1$  | $0$  | $0$    |
| $1$  | $1$  | $1$    |

>[!Info] 
>XOR gate is also called **Equivalence detector**

>[!Important]
>XNOR gate is 1 for :
>
>- Even number of 1's for even number of inputs
>- Odd number of 1's for odd number of inputs
>
>**That is why:** 
>
>$$\begin{align*} A\oplus B \oplus C &= A\odot B \odot C \newline A\oplus B \oplus C \oplus D &= \overline { A\odot B \odot C \odot D}\end{align*}$$ 

</content>

> [!question] What the output for $1\odot 1 \odot 0 \odot 1 \odot 0 \odot 1 = $ ?
> > [!success] - Answer
> > 1



## Special Properties and Applications

### Universal Gates

**NAND and NOR gates** are called universal gates because **any Boolean function can be implemented using only these gates**. This property makes them extremely valuable in digital circuit design as they can replace all other gate types.

<img src="..\notesob\DE\Boolean\img\Boolean_UniversalGatesNOR.png">

<img src="..\notesob\DE\Boolean\img\Boolean_UniversalGatesNAND.png">

### Real-World Applications

Logic gates are essential components in:

- **Computer processors** for arithmetic operations and data processing
- **Memory devices** for data storage and retrieval
- **Communication systems** for encoding and decoding digital signals
- **Control systems** in robotics and automation
- **Consumer electronics** like smartphones, calculators, and digital watches

These gates can be **combined to create complex circuits** such as adders for arithmetic operations, multiplexers for signal selection, and flip-flops for data storage, enabling the sophisticated digital systems we use today.