# Week 2: Time Complexity and Recurrence Relations

## 🎯 Objectives
- Analyze time complexity from code
- Understand how loops and recursion affect complexity
- Solve recurrence relations using substitution and Master Theorem

## 🧠 Time Complexity Basics

### 1. Analyzing Code Constructs

| Code Pattern             | Time Complexity |
|--------------------------|-----------------|
| Single loop (n times)    | O(n)            |
| Nested loop (n x n)      | O(n²)           |
| Logarithmic (divide n)   | O(log n)        |
| Loop + Recursive call    | Depends – often O(n log n), etc. |

### 2. Example:

```python
for i in range(n):
    for j in range(n):
        print(i, j)   # O(n²)
