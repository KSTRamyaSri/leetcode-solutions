# Two Sum

- **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/two-sum/submissions/2165033631/
- **First Added:** 07 October 2026
- **Last Updated:** 07 October 2026

## Approaches

## Approach 1 — One-Pass Hash Table

**Language:** unknown
**First Added:** 07 October 2026
**Last Updated:** 07 October 2026

### Explanation

The algorithm iterates through the list of numbers once. For each element, it calculates its complement by subtracting the current number from the target. It then checks if this complement already exists in the hashmap. If it does, the indices of the complement and the current number are returned. If it does not, the current number and its index are stored in the hashmap, and the loop continues.

### Key Idea

Use a hash map to store previously visited numbers and their indices, allowing O(1) lookups for the required complement.

### Complexity

- **Time:** O(n)
- **Space:** O(n)

### Advantages

- Operates in a single pass through the array
- Optimal time complexity for the problem
- Avoids nested loops

### Disadvantages

- Requires extra memory to store elements in the hash map

### Concepts

- Array
- Hash Table

### Interview Note

Always mention the trade-off between time and space complexity when discussing the hash map approach versus the brute force O(n^2) approach.

### History

- 07 October 2026 — Existing approach updated after Gemini comparison.


## Review History

- 07 October 2026 — Accepted submission processed as ADD_NEW.
- 07 October 2026 — Exact duplicate accepted submission ignored.
- 07 October 2026 — Exact duplicate accepted submission ignored.
- 07 October 2026 — Exact duplicate accepted submission ignored.
- 07 October 2026 — Accepted submission processed as REPLACE_OLD.
- 07 October 2026 — Accepted submission processed as REPLACE_OLD.
