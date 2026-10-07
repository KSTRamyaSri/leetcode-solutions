# Two Sum

- **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/two-sum/submissions/2165033107/
- **First Added:** 07 October 2026
- **Last Updated:** 07 October 2026

## Approaches

## Approach 1 — Hash Map One-Pass

**Language:** unknown
**First Added:** 07 October 2026
**Last Updated:** 07 October 2026

### Explanation

The algorithm iterates through the list of numbers once. For each number, it calculates the complement required to reach the target sum. It checks if this complement already exists in the hash map. If it does, the indices of the complement and the current number are returned. If it does not, the current number and its index are stored in the hash map for future checks.

### Key Idea

Use a hash map to store previously seen numbers and their indices, enabling O(1) lookups to find the complement in a single pass.

### Complexity

- **Time:** O(n)
- **Space:** O(n)

### Advantages

- Single pass through the array makes it efficient
- Optimal time complexity for the problem
- Handles lookup and insertion in average O(1) time

### Disadvantages

- Requires extra space to store the hash map

### Concepts

- Hash Tables
- Array
- One-Pass

### Interview Note

Always mention the trade-off between the brute force O(n^2) approach and this optimal O(n) space-time tradeoff using a hash map.

### History

- 07 October 2026 — Existing approach updated after Gemini comparison.


## Review History

- 07 October 2026 — Accepted submission processed as ADD_NEW.
- 07 October 2026 — Exact duplicate accepted submission ignored.
- 07 October 2026 — Exact duplicate accepted submission ignored.
- 07 October 2026 — Exact duplicate accepted submission ignored.
- 07 October 2026 — Accepted submission processed as REPLACE_OLD.
