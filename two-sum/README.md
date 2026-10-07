# Two Sum

- **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/two-sum/submissions/2165034420/
- **First Added:** 07 October 2026
- **Last Updated:** 07 October 2026

## Approaches

## Approach 1 — One-pass Hash Map

**Language:** unknown
**First Added:** 07 October 2026
**Last Updated:** 07 October 2026

### Explanation

The algorithm iterates through the list of numbers once. For each element, it calculates the complement needed to reach the target. It checks if this complement already exists in the hash map. If it does, the indices of the complement and the current number are returned immediately. If it does not, the current number and its index are stored in the hash map for future lookups.

### Key Idea

Use a hash map to store previously seen numbers and their indices, enabling O(1) lookups for the required complement during a single pass.

### Complexity

- **Time:** O(n)
- **Space:** O(n)

### Advantages

- Operates in a single pass over the array
- Optimal time complexity compared to the brute-force O(n^2) approach

### Disadvantages

- Requires extra space to store elements in the hash map

### Concepts

- Hash Map
- Array
- Complement Lookup

### Interview Note

Always mention that while the space complexity increases to O(n), trading space for time reduces the time complexity from O(n^2) to O(n), which is the optimal pattern for this problem.

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
