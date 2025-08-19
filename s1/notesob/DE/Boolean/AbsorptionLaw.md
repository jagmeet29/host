# Boolean Algebra Absorption Law: Proof

The Absorption Law in Boolean algebra consists of two fundamental identities that demonstrate how certain terms can be "absorbed" in Boolean expressions:

1. $A + (A \cdot B) = A$ (First absorption identity)
    
2. $A \cdot (A + B) = A$ (Second absorption identity)
    

Let's prove both identities using algebraic methods and Boolean properties.

## First Absorption Identity: $A + (A \cdot B) = A$

**Method 1:**

- $A + (A \cdot B)$
- $= A \cdot 1 + A \cdot B$ (using Identity law: $A = A \cdot 1$)
- $= A(1 + B)$ (using Distributive law)
- $= A \cdot 1$ (since $1 + B = 1$ in Boolean algebra)
- $= A$ (using Identity law: $A \cdot 1 = A$)

**Method 2:**

- $A + AB$
    
- $= A(1 + B)$ (factoring out the common term $A$)
    
- $= A \cdot 1$ (since $1 + B = 1$ in Boolean algebra)
    
- $= A$
    

## Second Absorption Identity: $A \cdot (A + B) = A$

**Method 1:**

- $A \cdot (A + B)$
    
- $= A \cdot A + A \cdot B$ (using Distributive law)
    
- $= A + A \cdot B$ (using Idempotent law: $A \cdot A = A$)
    
- $= A$ (by the first absorption identity that we just proved)
    

**Method 2:**

- $A(A + B)$
    
- $= AA + AB$ (using Distributive law)
    
- $= A + AB$ (using Idempotent law: $AA = A$)
    
- $= A(1 + B)$ (using Distributive law)
    
- $= A \cdot 1$ (since $1 + B = 1$)
    
- $= A$
    

These proofs demonstrate why the Absorption Law is a fundamental property in Boolean algebra, which is widely used in digital logic design, set theory, and mathematical logic. The law shows how certain terms can be "absorbed" without changing the overall value of the expression[5](https://en.wikipedia.org/wiki/Absorption_law).

