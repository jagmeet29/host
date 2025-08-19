1. 1. 1. ## XOR Gate Properties Table

         | Property Name         | Expression/Identity                                          | Description/Proof                                            |
         | --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
         | Self-Annulment        | A⊕A=0A \oplus A = 0A⊕A=0                                     | Proof: A⊕A=Aˉ⋅A+A⋅Aˉ=0+0=0A \oplus A = \bar{A} \cdot A + A \cdot \bar{A} = 0 + 0 = 0A⊕A=Aˉ⋅A+A⋅Aˉ=0+0=0. A variable XORed with itself is 0. |
         | Complement            | A⊕Aˉ=1A \oplus \bar{A} = 1A⊕Aˉ=1                             | Proof: A⊕Aˉ=Aˉ⋅Aˉ+A⋅A=Aˉ+A=1A \oplus \bar{A} = \bar{A} \cdot \bar{A} + A \cdot A = \bar{A} + A = 1A⊕Aˉ=Aˉ⋅Aˉ+A⋅A=Aˉ+A=1. A variable XORed with its complement is 1. |
         | Identity (with 0)     | A⊕0=AA \oplus 0 = AA⊕0=A                                     | Proof: A⊕0=Aˉ⋅0+A⋅1=0+A=AA \oplus 0 = \bar{A} \cdot 0 + A \cdot 1 = 0 + A = AA⊕0=Aˉ⋅0+A⋅1=0+A=A. XOR with 0 leaves the value unchanged. |
         | Complement (with 1)   | A⊕1=AˉA \oplus 1 = \bar{A}A⊕1=Aˉ                             | Proof: A⊕1=Aˉ⋅1+A⋅0=Aˉ+0=AˉA \oplus 1 = \bar{A} \cdot 1 + A \cdot 0 = \bar{A} + 0 = \bar{A}A⊕1=Aˉ⋅1+A⋅0=Aˉ+0=Aˉ. XOR with 1 inverts the value. |
         | Commutative           | A⊕B=B⊕AA \oplus B = B \oplus AA⊕B=B⊕A                        | Proof: Both expand to Aˉ⋅B+A⋅Bˉ\bar{A} \cdot B + A \cdot \bar{B}Aˉ⋅B+A⋅Bˉ, which is symmetric. Order doesn't matter. |
         | Associative           | A⊕(B⊕C)=(A⊕B)⊕CA \oplus (B \oplus C) = (A \oplus B) \oplus CA⊕(B⊕C)=(A⊕B)⊕C | Grouping doesn't affect the result; extends to multiple inputs. |
         | Exchange              | A⊕B=C  ⟹  A⊕C=BA \oplus B = C \implies A \oplus C = BA⊕B=C⟹A⊕C=B | Proof: A⊕C=A⊕(A⊕B)=(A⊕A)⊕B=0⊕B=BA \oplus C = A \oplus (A \oplus B) = (A \oplus A) \oplus B = 0 \oplus B = BA⊕C=A⊕(A⊕B)=(A⊕A)⊕B=0⊕B=B. Makes XOR reversible. |
         | Self-Inverse          | A⊕A⊕B=BA \oplus A \oplus B = BA⊕A⊕B=B                        | Proof: (A⊕A)⊕B=0⊕B=B(A \oplus A) \oplus B = 0 \oplus B = B(A⊕A)⊕B=0⊕B=B. XOR is its own inverse. |
         | Double Complement     | A⊕Bˉ=Aˉ⊕B=(A⊕B)‾A \oplus \bar{B} = \bar{A} \oplus B = \overline{(A \oplus B)}A⊕Bˉ=Aˉ⊕B=(A⊕B) | Proof: Substituting complements yields the negation of the original XOR. |
         | Distributive-like     | A⊕B⊕C=A⊕(B⊕C)A \oplus B \oplus C = A \oplus (B \oplus C)A⊕B⊕C=A⊕(B⊕C) | This is a form of the associative property for multiple variables. |
         | Equivalence with XNOR | A⊕B=(A⊙B)‾A \oplus B = \overline{(A \odot B)}A⊕B=(A⊙B)       | XOR is the complement of XNOR.                               |
      
         ## XNOR Gate Properties Table
      
         | Property Name           | Expression/Identity                                          | Description/Proof                                            |
         | ----------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
         | Self-Equivalence        | A⊙A=1A \odot A = 1A⊙A=1                                      | Proof: A⊙A=A⋅A+Aˉ⋅Aˉ=A+Aˉ=1A \odot A = A \cdot A + \bar{A} \cdot \bar{A} = A + \bar{A} = 1A⊙A=A⋅A+Aˉ⋅Aˉ=A+Aˉ=1. A variable XNORed with itself is 1. |
         | Complement              | A⊙Aˉ=0A \odot \bar{A} = 0A⊙Aˉ=0                              | Proof: A⊙Aˉ=A⋅Aˉ+Aˉ⋅A=0+0=0A \odot \bar{A} = A \cdot \bar{A} + \bar{A} \cdot A = 0 + 0 = 0A⊙Aˉ=A⋅Aˉ+Aˉ⋅A=0+0=0. A variable XNORed with its complement is 0. |
         | Complement (with 0)     | A⊙0=AˉA \odot 0 = \bar{A}A⊙0=Aˉ                              | Proof: A⊙0=A⋅0+Aˉ⋅1=0+Aˉ=AˉA \odot 0 = A \cdot 0 + \bar{A} \cdot 1 = 0 + \bar{A} = \bar{A}A⊙0=A⋅0+Aˉ⋅1=0+Aˉ=Aˉ. XNOR with 0 inverts the value. |
         | Identity (with 1)       | A⊙1=AA \odot 1 = AA⊙1=A                                      | Proof: A⊙1=A⋅1+Aˉ⋅0=A+0=AA \odot 1 = A \cdot 1 + \bar{A} \cdot 0 = A + 0 = AA⊙1=A⋅1+Aˉ⋅0=A+0=A. XNOR with 1 leaves the value unchanged. |
         | Commutative             | A⊙B=B⊙AA \odot B = B \odot AA⊙B=B⊙A                          | Proof: Both expand to A⋅B+Aˉ⋅BˉA \cdot B + \bar{A} \cdot \bar{B}A⋅B+Aˉ⋅Bˉ, which is symmetric. Order doesn't matter. |
         | Associative             | A⊙(B⊙C)=(A⊙B)⊙CA \odot (B \odot C) = (A \odot B) \odot CA⊙(B⊙C)=(A⊙B)⊙C | Grouping doesn't affect the result; extends to multiple inputs. |
         | Self-Inverse (Modified) | A⊙A⊙B=BˉA \odot A \odot B = \bar{B}A⊙A⊙B=Bˉ                  | Proof: (A⊙A)⊙B=1⊙B=Bˉ(A \odot A) \odot B = 1 \odot B = \bar{B}(A⊙A)⊙B=1⊙B=Bˉ. XNOR with 1 inverts B. |
         | Double Complement       | A⊙Bˉ=Aˉ⊙B=(A⊙B)‾A \odot \bar{B} = \bar{A} \odot B = \overline{(A \odot B)}A⊙Bˉ=Aˉ⊙B=(A⊙B) | Proof: Substituting complements yields the negation of the original XNOR. |
         | Distributive-like       | A⊙B⊙C=A⊙(B⊙C)A \odot B \odot C = A \odot (B \odot C)A⊙B⊙C=A⊙(B⊙C) | This is a form of the associative property for multiple variables. |
         | Equivalence with XOR    | A⊙B=(A⊕B)‾A \odot B = \overline{(A \oplus B)}A⊙B=(A⊕B)       | XNOR is the complement of XOR.                               |
         | No Exchange Property    | N/A (Does not hold)                                          | Unlike XOR, XNOR is not reversible in the same way; e.g., A⊙B=CA \odot B = CA⊙B=C does not imply A⊙C=BA \odot C = BA⊙C=B. |
