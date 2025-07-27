# Week 1: Asymptotic Notation and Algorithm Growth

## 🎯 Objectives
- Understand the purpose of analyzing algorithms
- Learn standard asymptotic notations (O, Ω, Θ)
- Apply notation to describe best, worst, and average-case scenarios

## 📘 Key Concepts

### 1. Why Analyze Algorithms?
- To compare algorithm efficiency
- Focuses on growth rate as input size n increases
- Abstracts away from machine-specific details

### 2. Asymptotic Notation
These notations help to express how an algorithm’s runtime or space requirements grow.

| Notation | Meaning                     | Purpose                 |
|----------|-----------------------------|-------------------------|
| O(f(n))  | Upper bound (worst-case)    | Max time an algorithm takes |
| Ω(f(n))  | Lower bound (best-case)     | Minimum time it takes   |
| Θ(f(n))  | Tight bound (average-case)  | Precise growth rate     |

#### Examples:
- `Linear search`: O(n), Ω(1), Θ(n)
- `Binary search`: O(log n), Ω(1), Θ(log n)
- `Bubble sort`: O(n²), Ω(n), Θ(n²)

## 📐 Visualizing Growth
Plotting f(n) for different functions shows that:
- O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)

## ✅ Summary
- Asymptotic notation provides a high-level view of efficiency.
- Big O is most commonly used in performance discussions.

---

📚 Next week: We’ll dive into concrete time complexity analysis using code and recurrence relations.
