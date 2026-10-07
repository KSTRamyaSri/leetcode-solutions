<!-- LC_PROBLEM_META_START -->
{"slug":"count-negative-numbers-in-a-sorted-matrix","title":"Count Negative Numbers in a Sorted Matrix","difficulty":"Easy","url":"https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/2164939428/","firstAdded":"2026-10-07","lastUpdated":"2026-10-07","approaches":[{"language":"java","name":"Staircase Search","firstAdded":"2026-10-07","lastUpdated":"2026-10-07","explanation":"The algorithm starts at the bottom-left corner of the matrix (grid[m-1][0]). It uses a two-pointer-like approach by maintaining the row and column indices. If the current element is negative, all elements to the right of it in the same row are also negative because the matrix is sorted in non-increasing order. Thus, it adds the count of remaining elements in that row (n - col) to the total count and moves up to the previous row. If the current element is non-negative, it moves right to the next column.","keyIdea":"Exploiting the sorted matrix properties by starting from the bottom-left corner to eliminate an entire row or column in each step.","timeComplexity":"O(m + n)","spaceComplexity":"O(1)","advantages":["Achieves the optimal O(m + n) time complexity requested in the follow-up.","Uses constant extra space O(1).","Avoids redundant checks by leveraging sorted properties."],"disadvantages":["Mutates traversal based on specific properties; not generally applicable to unsorted matrices."],"concepts":["Matrix Traversal","Greedy Approach","Two Pointers","Binary Search Alternative"],"interviewNote":"When dealing with row-wise and column-wise sorted matrices, always look for corner-starting strategies (top-right or bottom-left) that allow you to eliminate a row or column at each step, matching the O(m + n) optimal bound.","history":["07 October 2026 — New accepted approach added."]}],"reviewHistory":["07 October 2026 — Accepted submission processed as ADD_NEW."]}
<!-- LC_PROBLEM_META_END -->

# Count Negative Numbers in a Sorted Matrix

- **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/2164939428/
- **First Added:** 07 October 2026
- **Last Updated:** 07 October 2026

## Approaches

## Approach 1 — Staircase Search

**First Added:** 07 October 2026
**Last Updated:** 07 October 2026

### Explanation

The algorithm starts at the bottom-left corner of the matrix (grid[m-1][0]). It uses a two-pointer-like approach by maintaining the row and column indices. If the current element is negative, all elements to the right of it in the same row are also negative because the matrix is sorted in non-increasing order. Thus, it adds the count of remaining elements in that row (n - col) to the total count and moves up to the previous row. If the current element is non-negative, it moves right to the next column.

### Key Idea

Exploiting the sorted matrix properties by starting from the bottom-left corner to eliminate an entire row or column in each step.

### Complexity

- **Time:** O(m + n)
- **Space:** O(1)

### Advantages

- Achieves the optimal O(m + n) time complexity requested in the follow-up.
- Uses constant extra space O(1).
- Avoids redundant checks by leveraging sorted properties.

### Disadvantages

- Mutates traversal based on specific properties; not generally applicable to unsorted matrices.

### Concepts

- Matrix Traversal
- Greedy Approach
- Two Pointers
- Binary Search Alternative

### Interview Note

When dealing with row-wise and column-wise sorted matrices, always look for corner-starting strategies (top-right or bottom-left) that allow you to eliminate a row or column at each step, matching the O(m + n) optimal bound.

### History

- 07 October 2026 — New accepted approach added.


## Review History

- 07 October 2026 — Accepted submission processed as ADD_NEW.
