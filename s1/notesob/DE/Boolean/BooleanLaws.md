# Important Laws of Boolean Algebra

| **Law**                  | **Expression**                                                                                                                           | **Explanation**                                                               |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Identity Law**         | $A + 0 = A$, $A \cdot 1 = A$                                                                                                             | Adding 0 or multiplying by 1 doesn't change the value of A.                   |
| **Null Law**             | $A + 1 = 1$, $A \cdot 0 = 0$                                                                                                             | Adding 1 always results in 1; multiplying by 0 always results in 0.           |
| **Idempotent Law**       | $A + A = A$, $A \cdot A = A$                                                                                                             | Repeating the same operation doesn't change the result.                       |
| **Complement Law**       | $A + \bar{A} = 1$, $A \cdot \bar{A} = 0$                                                                                                 | A variable ORed with its complement is 1, and ANDed with its complement is 0. |
| **Double Negation**      | $\bar{\bar{A}} = A$                                                                                                                      | Negating twice gives back the original value.                                 |
| **Commutative Law**      | $A + B = B + A$, $A \cdot B = B \cdot A$                                                                                                 | Order of variables doesn’t matter in AND or OR operations.                    |
| **Associative Law**      | $(A + B) + C = A + (B + C)$, $(A \cdot B) \cdot C = A \cdot (B \cdot C)$                                                                 | Grouping doesn’t affect the result.                                           |
| **Distributive Law**     | $A \cdot (B + C) = A \cdot B + A \cdot C$<br>$A+(B \cdot C) = (A+B) \cdot (A+C)$                                                         | AND distributes over OR.                                                      |
| **Absorption Law**       | $A + (A \cdot B) = A$, $A \cdot (A + B) = A$                                                                                             | A term absorbs a combination of itself with another term.                     |
| **De Morgan’s Theorems** | $\overline{A + B} = \bar{A} \cdot \bar{B}$, $\overline{A \cdot B} = \bar{A} + \bar{B}$                                                   | Complement of an OR is the AND of complements, and vice versa.                |
| **Consensus Theorem**    | $A \cdot B + \bar{A} \cdot C + B \cdot C = A \cdot B + \bar{A} \cdot C$<br>$A + B \cdot \bar A + C \cdot B + C = (A+B) \cdot (\bar A+C)$ | Eliminates redundant terms in expressions.                                    |

*De Morgan's Law enables us to convert AND gate $\rightarrow$ OR gate using NOT gate*

### Important Laws

1. **Distribution Law**  
   $A+B \cdot C \cdot D \rightarrow A+(B \cdot C \cdot D)$
   It is imp. when $A+\bar A \text{ _ _ _ }$   because $A+\bar A = 1$ 

2. **Redundancy Removal or Consensus Theorem**

3. **De Morgan's Theorem**

4. **Duality Theorem**

---


>[!question] 1. What is the value of $1+A+\bar A \cdot B + B \cdot A = ? \ (0/1)$
>>[!success]- Answer
>>$1$
>>$1+\text{anything} = 1$



>[!question] 2. What is the value of $0 \cdot A \cdot B \cdot \bar C \cdot D = ? \ (0/1)$
>>[!success]- Answer
>>$0$
>>$0 \cdot \text{anything} = 0$



>[!question] 3. What is the value of $A+B \cdot C \cdot D =?$ (Distribution law)
>>[!success]- Answer
>>$(A+B) \cdot (A+C) \cdot (A+D)$



>[!question] 4. What is the value of $A + (\bar A \cdot B \cdot D) =?$ (Distribution law)
>>[!success]- Answer
>>$(A+B) \cdot (A+D)$



>[!question] 5. What is the value of $\overline{A \cdot B} + A \cdot C + \bar B \cdot C =?$ (Consensus Theorem)
>>[!success]- Answer
>>$\overline {A \cdot B} + A \cdot C$



>[!question] 6. What is the value of $\bar A \cdot B + A \cdot C \cdot D + B \cdot C \cdot D= ?$ (Consensus Theorem)
>>[!success]- Answer
>>$\bar A \cdot B + A \cdot C \cdot D$
>>![[Ans6.jpg|200]]



>[!question] 7. What is the value of $\overline {A \cdot B} + \bar A \cdot B \cdot C + \bar A \cdot C=?$ (Consensus Theorem)
>>[!success]- Answer
>>$\overline{A \cdot B} + \bar A \cdot B \cdot C$
>>![[Ans7.jpg|200]]



>[!question] 8. What is the value of $\overline {A+B+C+D} = ?$ (De Morgan Theorem)
>>[!success]- Answer
>>$\overline{A+B} \cdot \overline{C+D} = \bar A \cdot \bar B \cdot \bar C \cdot \bar D$



>[!question] 9. What is the value of $A+B \cdot C+\bar A \cdot C= ?$`
>>[!success]- Answer
>>$A+C$



>[!question] 10. What is the value of $\overline {\bar A \cdot \bar B + C \cdot D} = ?$`
>>[!success]- Answer
>>$A+B \cdot \bar C + \bar D$



>[!question] 10. What is the value of $\bar A \cdot B + A \cdot C + \bar B \cdot C = ?$`
>>[!success]- Answer
>> The original expression is:
>> $$ \bar A \cdot B + (A+\bar B) \ C $$
>>
>> Let's simplify it step-by-step:
>>
>> 1.  **Define a substitution:**
>>     Let $X = \bar A \cdot B$
>>
>> 2.  **Find the complement of X:**
>>     Using De Morgan's Theorem $(XY)' = X' + Y'$:
>>     $$ \bar X = (\bar A \cdot B)' $$
>>     $$ \bar X = \bar{\bar A} + \bar B $$
>>      $$ \bar X = A + \bar B $$
>>
>> 3.  **Substitute into the original expression:**
>>     Now replace $\bar A \cdot B$ with $X$ and $(A+\bar B)$ with $\bar X$:
>>      $$ X + \bar X \cdot C $$
>>
>> 4.  **Apply Boolean Algebra Identity:**
>>     This expression $X + \bar X \cdot C$ can be simplified using the Distributive Law $A + BC = (A+B)(A+C)$ or a specific identity $X + \bar X Y = X + Y$. Let's show the full derivation:
>>      $$ X + \bar X \cdot C $$
>>      $$ (X + \bar X) \cdot (X + C) \quad \text{ (Using Distributive Law: } A+BC = (A+B)(A+C) \text{ where } A=X, B=\bar X, C=C \text{)} $$
>>     $$ 1 \cdot (X + C) \quad \text{ (Since } X + \bar X = 1 \text{)} $$
>>      $$ X + C $$
>>
>> 5.  **Substitute back the original variables:**
>>      Now, replace $X$ with its original definition ($\bar A \cdot B$):
>>     $$ \bar A \cdot B + C $$
>>
>> **Final Simplified Expression:**
>> $$ \bar A \cdot B + C $$
