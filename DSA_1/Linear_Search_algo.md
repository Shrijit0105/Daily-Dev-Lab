 Linear Search Algorithm

1. Introduction

Linear Search is a simple searching algorithm that sequentially checks every element in a collection until the required element is found or the collection ends.

It is also known as Sequential Search.

Unlike Binary Search, Linear Search does not require sorted data.

2. How It Works

Linear Search examines elements one by one, starting from the first element.

Algorithm Steps

1. Start from the first element of the array.
2. Compare the current element with the target.
3. If both elements match, return the index.
4. Otherwise, move to the next element.
5. Repeat until the target is found or the array ends.
6. If the target is not found, return -1.

3. Visual Example

Consider the following array:

Array = [12, 45, 23, 67, 89, 34]
Target = 67

Searching Process

Iteration 1

12 != 67

Move to the next element.

Iteration 2

45 != 67

Move to the next element.

Iteration 3

23 != 67

Move to the next element.

Iteration 4

67 == 67

Target found!

Output: Index 3

4. Pseudocode

START

FOR i = 0 TO length(array) - 1:

    IF array[i] == target:
        RETURN i

RETURN -1

END

5. Complexity Analysis

Case| Time Complexity
Best Case| O(1)
Average Case| O(N)
Worst Case| O(N)

Space Complexity: O(1)

Linear Search uses constant auxiliary space because it does not require additional data structures.

6. Linear Search vs Binary Search

Feature| Linear Search| Binary Search
Data Requirement| Any order| Sorted
Best Case| O(1)| O(1)
Average Case| O(N)| O(log N)
Worst Case| O(N)| O(log N)
Approach| Sequential| Divide and Conquer
Implementation| Simple| Comparatively complex

7. Advantages

- Easy to understand and implement.
- Works with sorted and unsorted collections.
- Does not require additional memory.
- Suitable for small datasets.

8. Disadvantages

- Becomes inefficient for large datasets.
- May require checking every element.
- Slower than Binary Search for large sorted arrays.

9. Real-World Applications

- Searching for an item in an unsorted list.
- Finding a particular name in a small collection.
- Checking whether a specific value exists.
- Searching through simple datasets.
- Sequential record inspection.

10. Practice Challenges

1. Implement Linear Search using Python.
2. Find all occurrences of a target element.
3. Find the first and last occurrence of an element.
4. Count the number of occurrences of a target.
5. Find the minimum and maximum elements using traversal.

11. Key Takeaways

- Linear Search checks elements sequentially.
- It works without sorting the input.
- Its worst-case time complexity is O(N).
- Its auxiliary space complexity is O(1).
- It is useful for small or unsorted datasets.

---

Learning Log

Detail| Information
Day| 14
Date| 15 November 2026
Subject| Data Structures and Algorithms
Topic| Linear Search
Category| Searching Algorithms
Difficulty| Beginner

Learn. Practise. Analyse. Improve.

One algorithm at a time, one step closer to becoming a better developer. 