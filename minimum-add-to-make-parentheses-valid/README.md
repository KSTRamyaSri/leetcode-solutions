<!-- LC_PROBLEM_META_START -->
{"slug":"minimum-add-to-make-parentheses-valid","title":"Minimum Add to Make Parentheses Valid","difficulty":"Unknown","url":"https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/submissions/2164508008/?envType=daily-question&envId=2026-10-06","firstAdded":"2026-10-06","lastUpdated":"2026-10-06","approaches":[{"language":"java","name":"Greedy Counting with Balance Tracking","firstAdded":"2026-10-06","lastUpdated":"2026-10-06","explanation":"The algorithm iterates through the string character by character. It maintains a count of unmatched opening parentheses (oc) and unmatched closing parentheses (cc). When it encounters an opening parenthesis, it increments oc. When it encounters a closing parenthesis, it checks if there is an available unmatched opening parenthesis (oc > 0) to pair it with; if so, it decrements oc. Otherwise, it increments cc. Finally, it returns the sum of remaining unmatched opening and closing parentheses (oc + cc).","keyIdea":"Track the running balance of opening and closing parentheses to determine deficits without using an explicit stack.","timeComplexity":"O(N)","spaceComplexity":"O(1)","advantages":["Optimal linear time complexity","Constant auxiliary space usage","Single pass through the string"],"disadvantages":["Comments in the code indicate the presence of informal thoughts or placeholder notes"],"concepts":["Greedy algorithms","String parsing","Parentheses matching"],"interviewNote":"Using two integer counters instead of a stack is a classic space-optimization technique for balanced parenthesis problems when tracking nesting depth isn't strictly required.","history":["06 October 2026 — New accepted approach added."]}],"reviewHistory":["06 October 2026 — Accepted submission processed as ADD_NEW."]}
<!-- LC_PROBLEM_META_END -->

# Minimum Add to Make Parentheses Valid

- **Difficulty:** Unknown
- **LeetCode:** https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/submissions/2164508008/?envType=daily-question&envId=2026-10-06
- **First Added:** 06 October 2026
- **Last Updated:** 06 October 2026

## Approaches

## Approach 1 — Greedy Counting with Balance Tracking

**First Added:** 06 October 2026
**Last Updated:** 06 October 2026

### Explanation

The algorithm iterates through the string character by character. It maintains a count of unmatched opening parentheses (oc) and unmatched closing parentheses (cc). When it encounters an opening parenthesis, it increments oc. When it encounters a closing parenthesis, it checks if there is an available unmatched opening parenthesis (oc > 0) to pair it with; if so, it decrements oc. Otherwise, it increments cc. Finally, it returns the sum of remaining unmatched opening and closing parentheses (oc + cc).

### Key Idea

Track the running balance of opening and closing parentheses to determine deficits without using an explicit stack.

### Complexity

- **Time:** O(N)
- **Space:** O(1)

### Advantages

- Optimal linear time complexity
- Constant auxiliary space usage
- Single pass through the string

### Disadvantages

- Comments in the code indicate the presence of informal thoughts or placeholder notes

### Concepts

- Greedy algorithms
- String parsing
- Parentheses matching

### Interview Note

Using two integer counters instead of a stack is a classic space-optimization technique for balanced parenthesis problems when tracking nesting depth isn't strictly required.

### History

- 06 October 2026 — New accepted approach added.


## Review History

- 06 October 2026 — Accepted submission processed as ADD_NEW.
