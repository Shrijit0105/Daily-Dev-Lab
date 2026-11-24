# Big O Notation in Data Structures and Algorithms

## 1. Introduction

When we write a program, getting the correct output is only one part of the job. We also need to think about how efficiently the program works, especially when the amount of input becomes larger.

For example, imagine searching for a particular number in a list containing 10 elements. Now imagine doing the same task with 10,000 or even 1 million elements. Will the program take the same amount of time?

This is where **Big O Notation** becomes useful.

Big O notation helps us describe how the performance of an algorithm changes as the input size increases. It gives us a way to compare algorithms without depending on a particular computer, processor, or programming language.

## 2. What Does Big O Actually Represent?

Big O notation describes the growth rate of an algorithm's resource requirements as its input size increases.

The resource we usually analyse is:

- **Time Complexity:** How the number of operations grows with the input size.
- **Space Complexity:** How the additional memory requirements grow with the input size.

One important thing to understand is that Big O does not directly tell us the exact execution time in seconds. It describes the rate at which the work or memory requirement grows.

For example, an algorithm with linear time complexity may perform roughly twice as many operations when its input size doubles.

## 3. Understanding Input Size

Before analysing an algorithm, we need to understand what `n` represents.

In most DSA problems, `n` represents the size of the input.

For example:

```python
numbers = [10, 20, 30, 40, 50]
```

Here, the input size is 5 because the list contains five elements.

If we add more elements, the value of `n` increases. We use this value to study how the algorithm behaves as the input grows.

## 4. Common Types of Time Complexity

### O(1) - Constant Time

An algorithm has constant time complexity when the number of operations does not depend on the input size.

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[2])
```

Accessing an element using its index in a Python list takes constant time.

Even if the list contains thousands of elements, accessing an element at a known index still takes approximately the same number of operations.

### O(log n) - Logarithmic Time

Logarithmic complexity occurs when an algorithm reduces the problem size significantly at each step.

A common example is Binary Search.

Binary Search works on a sorted collection and repeatedly divides the search area into two halves.

For example, if we have 16 elements, Binary Search can narrow down the search area like this:

```text
16 → 8 → 4 → 2 → 1
```

Instead of checking every element, it keeps reducing the search space.

This makes it much more efficient than checking every element individually when the input is large.

### O(n) - Linear Time

An algorithm has linear time complexity when the number of operations grows proportionally with the input size.

Example:

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
```

The loop visits every element once.

If the list contains 5 elements, the loop executes 5 times. If it contains 100 elements, it executes 100 times.

This is the basic idea behind linear time complexity.

Linear Search is another common example.

### O(n log n) - Linearithmic Time

This complexity commonly appears in efficient sorting algorithms.

Merge Sort is a good example.

It divides the input into smaller parts, sorts those parts, and then combines them.

Its performance grows faster than linear time but much slower than quadratic time for large inputs.

This is why algorithms with O(n log n) complexity are commonly used for sorting large datasets.

### O(n²) - Quadratic Time

Quadratic complexity usually appears when an algorithm performs nested iterations over the same input.

Example:

```python
numbers = [10, 20, 30, 40]

for i in numbers:
    for j in numbers:
        print(i, j)
```

The outer loop runs 4 times, and for each iteration, the inner loop also runs 4 times.

Total operations:

```text
4 × 4 = 16
```

If the input size becomes 100, the total number of iterations becomes 10,000.

This is why nested loops can become expensive when working with large inputs.

### O(2ⁿ) - Exponential Time

Exponential complexity occurs when the amount of work grows exponentially with the input size.

A common example is a simple recursive solution to the Fibonacci sequence that repeatedly calculates the same values.

As the input increases, the number of recursive calls can grow very quickly.

Such algorithms can become extremely slow even with relatively small input sizes.

## 5. Comparing Common Time Complexities

The following is a general comparison, from slower growth to faster growth:

| Complexity | Name | General behaviour |
|---|---|---|
| O(1) | Constant | Does not grow with input size |
| O(log n) | Logarithmic | Grows very slowly |
| O(n) | Linear | Grows proportionally |
| O(n log n) | Linearithmic | Grows faster than linear |
| O(n²) | Quadratic | Grows rapidly |
| O(2ⁿ) | Exponential | Grows extremely quickly |

This order is useful when comparing algorithms for sufficiently large input sizes.

## 6. How to Calculate Big O Notation

Let's take a few simple examples.

### Example 1: A Single Loop

```python
for i in range(n):
    print(i)
```

The loop executes `n` times.

Therefore:

**Time Complexity: O(n)**

### Example 2: Two Separate Loops

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

The first loop executes `n` times, and the second loop also executes `n` times.

Total operations:

```text
n + n = 2n
```

We ignore constant multipliers in Big O notation.

**Time Complexity: O(n)**

### Example 3: Nested Loops

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

The outer loop runs `n` times, and the inner loop runs `n` times for each outer iteration.

Total operations:

```text
n × n = n²
```

**Time Complexity: O(n²)**

### Example 4: A Loop That Divides the Input

```python
i = n

while i > 1:
    i = i // 2
```

The value of `i` is divided by 2 during every iteration.

The number of iterations grows logarithmically with `n`.

**Time Complexity: O(log n)**

## 7. Important Rules of Big O Notation

While analysing an algorithm, a few rules make the process easier.

**Rule 1: Ignore constant values**

O(2n) becomes O(n).

The constant multiplier does not change the overall growth category.

**Rule 2: Keep the fastest-growing term**

O(n² + n + 10) becomes O(n²).

For large input sizes, the quadratic term dominates the other terms.

**Rule 3: Analyse separate operations**

If two loops execute one after another, their complexities are added before simplifying.

For example:

```text
O(n) + O(n) = O(2n) = O(n)
```

**Rule 4: Nested loops usually multiply**

If one loop runs `n` times and another nested loop also runs `n` times, the total work is generally proportional to n².

However, not every nested loop automatically has O(n²) complexity. We need to examine how many times each loop actually executes.

## 8. Best, Average and Worst Case

An algorithm can behave differently depending on the input it receives.

Let's take Linear Search as an example.

Suppose we are searching for the number 40:

```python
numbers = [10, 20, 30, 40, 50]
```

- **Best Case:** The element is at the first position. Only one comparison is required. O(1).
- **Average Case:** The element is somewhere in the middle. Several comparisons are required. O(n).
- **Worst Case:** The element is at the last position or is not present. The algorithm may need to check every element. O(n).

Understanding these cases helps us analyse how an algorithm behaves under different conditions.

## 9. Time Complexity vs Space Complexity

Time and space complexity measure two different things.

| Time Complexity | Space Complexity |
|---|---|
| Measures how the number of operations grows | Measures how additional memory usage grows |
| Focuses on computational work | Focuses on memory requirements |
| Loops and recursive calls can affect it | Extra arrays, data structures and recursion can affect it |

For example:

```python
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)
```

The loop takes O(n) time.

However, the loop itself uses only a constant amount of additional memory, so its auxiliary space complexity is O(1).

This distinction is important because an algorithm can be fast but require a lot of memory, or use very little memory but take longer to execute.

## 10. Common Mistakes to Avoid

While learning Big O notation, I think these are some mistakes worth watching out for:

1. Assuming Big O gives the exact execution time in seconds.
2. Thinking every nested loop automatically means O(n²).
3. Forgetting to ignore constant multipliers.
4. Confusing time complexity with space complexity.
5. Assuming an algorithm with better Big O will always be faster for every input size.
6. Ignoring the effect of the input structure on an algorithm's performance.

Big O is a useful theoretical tool, but actual performance can also depend on implementation, hardware, memory access and input size.

## 11. What I Learned

Big O notation is not just about memorising O(1), O(n), or O(n²). The real objective is to understand how an algorithm behaves when the amount of data increases.

It also changes how I look at code. Instead of only asking whether a program produces the correct output, I should also ask how much work it performs and whether that work will remain reasonable for larger inputs.

This is an important foundation for choosing better algorithms and writing efficient programs.

## 12. Practice Questions

Try solving these without immediately looking up the answers.

1. What is the time complexity of accessing an element using an index in a Python list?
2. What is the complexity of a loop that runs from 0 to n?
3. What happens to the complexity when two independent O(n) loops execute one after another?
4. Why is Binary Search O(log n) instead of O(n)?
5. What is the time complexity of two nested loops, each running n times?
6. What is the difference between time complexity and space complexity?
7. Can an algorithm with O(n²) complexity be faster than an O(n) algorithm for a small input size? Explain why.
8. Analyse the time complexity of a loop that repeatedly divides a variable by 2 until it reaches 1.

---

**My next learning target:** Practise analysing the time and space complexity of small Python programs before moving towards more complex DSA problems.
