 Binary Search Algorithm

1. Introduction

Binary Search is an efficient searching algorithm used to find a specific element in a sorted array.

Instead of checking every element individually, Binary Search repeatedly divides the search interval into two halves.

Main requirement: The input array must be sorted.

2. How It Works

Binary Search uses three variables:

- "low": Starting index of the search range.
- "high": Ending index of the search range.
- "mid": Middle index of the search range.

Algorithm Steps

1. Initialize "low = 0".
2. Initialize "high = len(arr) - 1".
3. Calculate the middle index.
4. Compare the middle element with the target.
5. If equal, return its index.
6. If the target is smaller, search the left half.
7. If the target is larger, search the right half.
8. Repeat until the element is found or the search range becomes empty.

3. Visual Example

Consider the following sorted array:

Array = [2, 5, 8, 12, 16, 23, 38]
Target = 16

Iteration 1

low = 0
high = 6
mid = 3

arr[3] = 12

Since 16 > 12, search the right half.

Iteration 2

low = 4
high = 6
mid = 5

arr[5] = 23

Since 16 < 23, search the left half.

Iteration 3

low = 4
high = 4
mid = 4

arr[4] = 16

Target found!

Output: Index 4

4. Pseudocode

START

low = 0
high = length(array) - 1

WHILE low <= high:

    mid = (low + high) // 2

    IF array[mid] == target:
        RETURN mid

    ELSE IF array[mid] < target:
        low = mid + 1

    ELSE:
        high = mid - 1

RETURN -1

END

5. Complexity Analysis

Case| Time Complexity
Best Case| O(1)
Average Case| O(log N)
Worst Case| O(log N)

Space Complexity:

- Iterative Binary Search: O(1)
- Recursive Binary Search: O(log N)

6. Binary Search vs Linear Search

Feature| Linear Search| Binary Search
Data Requirement| Unsorted or sorted| Sorted
Best Case| O(1)| O(1)
Worst Case| O(N)| O(log N)
Approach| Sequential| Divide and Conquer
Efficiency| Slower for large datasets| Faster for large sorted datasets

7. Real-World Applications

- Searching in sorted databases.
- Finding elements in sorted arrays.
- Dictionary and index lookups.
- Finding lower and upper bounds.
- Search space optimization problems.

8. Key Takeaways

- Binary Search follows the Divide and Conquer approach.
- It requires sorted input for the standard algorithm.
- It reduces the search space by half in every iteration.
- Its worst-case time complexity is O(log N).
- Iterative implementation requires O(1) auxiliary space.

9. Practice Challenges

1. Implement Binary Search using Python.
2. Find the first occurrence of a duplicate element.
3. Find the last occurrence of a duplicate element.
4. Find the insertion position of a target.
5. Implement Binary Search using recursion.

Learning Log: Day 13 | 14 November 2026

Topic: Searching Algorithms

Concept: Binary Search

Objective: Understand Divide and Conquer and logarithmic time complexity.

Keep Learning. Keep Building. 