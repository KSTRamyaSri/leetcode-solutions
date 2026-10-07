# Two Sum

- **Difficulty:** Unknown
- **LeetCode:** https://leetcode.com/problems/two-sum/submissions/2164963599/
- **First Added:** 07 October 2026
- **Last Updated:** 07 October 2026

## Approaches

## Approach 1 — One-pass Hash Map

**First Added:** 07 October 2026
**Last Updated:** 07 October 2026

### Explanation

Iterate through the array once. For each element, calculate its complement (target - num). Check if this complement already exists in the hash map. If it does, return the index of the complement and the current index. If not, store the current number and its index in the hash map and move to the next element.

### Key Idea

Use a hash map to keep track of previously seen numbers and their indices, allowing us to find the complement in O(1) average time complexity.

### Complexity

- **Time:** O(n)
- **Space:** O(n)

### Advantages

- Achieves linear time complexity by avoiding the nested loops of a brute-force approach.
- Performs the lookup and insertion in a single pass through the array.

### Disadvantages

- Requires extra space proportional to the number of elements stored in the hash map.

### Concepts

- Hash Map
- Array
- One-pass

### Interview Note

This is the optimal solution for the Two Sum problem. Be prepared to explain why trading space for time (using a hash map) improves the complexity from O(n^2) to O(n).

### History

- 07 October 2026 — Initial accepted solution added.
- 07 October 2026 — Existing approach updated after Gemini comparison.


## Review History

- 07 October 2026 — Accepted submission processed as REPLACE_OLD.
- 07 October 2026 — Exact duplicate accepted submission ignored.
- 07 October 2026 — Exact duplicate accepted submission ignored.
