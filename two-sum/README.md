# Two Sum

- **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/two-sum/submissions/2165040755/
- **First Added:** 07 October 2026
- **Last Updated:** 07 October 2026

## Approaches

## Approach 1 — Hash Map One-Pass

**Language:** unknown
**First Added:** 07 October 2026
**Last Updated:** 07 October 2026

### Explanation

Iterate through the list of numbers once using enumerate. For each number, calculate its complement by subtracting it from the target. Check if this complement already exists in the hash map. If it does, return the index of the complement and the current index. If it does not, store the current number and its index in the hash map and continue.

### Key Idea

Use a hash map to store previously seen numbers and their indices, allowing O(1) lookups for the required complement during a single traversal of the array.

### Complexity

- **Time:** O(n)
- **Space:** O(n)

### Advantages

- Optimal time complexity by reducing the search time to O(1) using a hash map
- Performs the operation in a single pass through the array

### Disadvantages

- Requires extra space to store elements in the hash map

### Concepts

- Arrays
- Hash Tables
- One-Pass

### Interview Note

Always mention the trade-off between the brute-force O(n^2) nested loop approach and this optimal O(n) hash map approach.

### History

- 07 October 2026 — Existing approach updated after Gemini comparison.


## Review History

- 07 October 2026 — Accepted submission processed as ADD_NEW.
- 07 October 2026 — Exact duplicate accepted submission ignored.
- 07 October 2026 — Exact duplicate accepted submission ignored.
- 07 October 2026 — Exact duplicate accepted submission ignored.
- 07 October 2026 — Accepted submission processed as REPLACE_OLD.
- 07 October 2026 — Accepted submission processed as REPLACE_OLD.
- 07 October 2026 — Accepted submission processed as REPLACE_OLD.
- 07 October 2026 — Accepted submission processed as REPLACE_OLD.
