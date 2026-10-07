# Two Sum

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/two-sum/submissions/2165052796/](https://leetcode.com/problems/two-sum/submissions/2165052796/)
- **First Added:** 07 October 2026
- **Last Updated:** 07 October 2026

## What Is the Problem?

Problem explanation unavailable.



---


## Approach 1 — Sorting with Two Pointers

**Language:** Python  
**First Added:** 07 October 2026  
**Last Updated:** 07 October 2026

### How This Approach Works

First, the algorithm pairs each number with its original index and sorts the list based on the values. Then, it uses two pointers, one starting at the beginning (left) and one at the end (right) of the sorted list. It calculates the sum of the values at both pointers. If the sum equals the target, it returns the original indices. If the sum is less than the target, it increments the left pointer to increase the sum. If the sum is greater than the target, it decrements the right pointer to decrease the sum.

### Step-by-Step Trace

Trace unavailable.

### Simple Flow

Flow diagram unavailable.

### Key Idea

Sort the array while preserving original indices, then use the two-pointer technique to find the pair that adds up to the target.

### Complexity

- **Time:** O(n log n)
- **Space:** O(n)

### Interview Note

While this works, interviewers typically expect the O(n) hash map approach for Two Sum rather than O(n log n) sorting.

### History

- 07 October 2026 — New accepted approach added.


## Code

Solution code is stored in the language-specific solution file in this folder.

## History

- 07 October 2026 — Initial accepted solution added.
