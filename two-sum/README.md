# Two Sum

- **Difficulty:** Unknown
- **LeetCode:** https://leetcode.com/problems/two-sum/submissions/2164981717/
- **First Added:** 07 October 2026
- **Last Updated:** 07 October 2026

## Approaches

## Approach 1 — One-pass Hash Map

**Language:** Python
**First Added:** 07 October 2026
**Last Updated:** 07 October 2026

### Explanation

The algorithm iterates through the list of numbers once while keeping track of each number and its index in a hash map. For each number, it calculates the complement needed to reach the target sum. It checks if this complement already exists in the hash map. If it does, the indices of the complement and the current number are returned immediately. If not, the current number and its index are added to the hash map for future lookups.

### Key Idea

Use a hash map to store previously visited elements and their indices, enabling O(1) lookups for the required complement of the current number.

### Complexity

- **Time:** O(n)
- **Space:** O(n)

### Advantages

- Single-pass solution which is more efficient than a two-pass approach
- Optimal time complexity for the Two Sum problem
- Clean and readable implementation

### Disadvantages

- Requires extra space to store the hash map

### Concepts

- Hash Table
- Array
- One-pass

### Interview Note

Always mention the trade-off between time and space: this approach trades additional O(n) space to reduce the time complexity from O(n^2) to O(n).

### History

- 07 October 2026 — New accepted approach added.


## Review History

- 07 October 2026 — Accepted submission processed as ADD_NEW.
