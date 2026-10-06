<!-- LC_PROBLEM_META_START -->
{"slug":"minimum-add-to-make-parentheses-valid","title":"Minimum Add to Make Parentheses Valid","difficulty":"Unknown","url":"https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/submissions/2164509255/?envType=daily-question&envId=2026-10-06","firstAdded":"2026-10-06","lastUpdated":"2026-10-06","approaches":[{"language":"java","name":"Greedy Balance Counter","firstAdded":"2026-10-06","lastUpdated":"2026-10-06","explanation":"Iterate through each character of the string. Maintain a count of unmatched opening parentheses (oc) and unmatched closing parentheses (cc). When encountering an opening parenthesis '(', increment oc. When encountering a closing parenthesis ')', decrement oc if there is an available unmatched opening parenthesis; otherwise, increment cc. The final result is the sum of remaining unmatched opening and closing parentheses.","keyIdea":"Track the running balance of open and close parentheses to greedily match them on the fly without using an explicit stack.","timeComplexity":"O(N)","spaceComplexity":"O(1)","advantages":["Optimal linear time complexity","Constant space complexity by avoiding stack usage","Simple and concise single-pass implementation"],"disadvantages":["Contains unpolished code comments","Variable names (oc, cc) could be more descriptive"],"concepts":["Greedy algorithms","String parsing","Parentheses matching"],"interviewNote":"Always mention that while a stack is a natural fit for parenthesis problems, tracking counts achieves the exact same result with O(1) space.","history":["06 October 2026 — New accepted approach added."]}],"reviewHistory":["06 October 2026 — Accepted submission processed as ADD_NEW."]}
<!-- LC_PROBLEM_META_END -->

# Minimum Add to Make Parentheses Valid

- **Difficulty:** Unknown
- **LeetCode:** https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/submissions/2164509255/?envType=daily-question&envId=2026-10-06
- **First Added:** 06 October 2026
- **Last Updated:** 06 October 2026

## Approaches

## Approach 1 — Greedy Balance Counter

**First Added:** 06 October 2026
**Last Updated:** 06 October 2026

### Explanation

Iterate through each character of the string. Maintain a count of unmatched opening parentheses (oc) and unmatched closing parentheses (cc). When encountering an opening parenthesis '(', increment oc. When encountering a closing parenthesis ')', decrement oc if there is an available unmatched opening parenthesis; otherwise, increment cc. The final result is the sum of remaining unmatched opening and closing parentheses.

### Key Idea

Track the running balance of open and close parentheses to greedily match them on the fly without using an explicit stack.

### Complexity

- **Time:** O(N)
- **Space:** O(1)

### Advantages

- Optimal linear time complexity
- Constant space complexity by avoiding stack usage
- Simple and concise single-pass implementation

### Disadvantages

- Contains unpolished code comments
- Variable names (oc, cc) could be more descriptive

### Concepts

- Greedy algorithms
- String parsing
- Parentheses matching

### Interview Note

Always mention that while a stack is a natural fit for parenthesis problems, tracking counts achieves the exact same result with O(1) space.

### History

- 06 October 2026 — New accepted approach added.


## Review History

- 06 October 2026 — Accepted submission processed as ADD_NEW.
