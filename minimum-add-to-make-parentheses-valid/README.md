<!-- LC_PROBLEM_META_START -->
{"slug":"minimum-add-to-make-parentheses-valid","title":"Minimum Add to Make Parentheses Valid","difficulty":"Unknown","url":"https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/submissions/2164502069/?envType=daily-question&envId=2026-10-06","firstAdded":"2026-10-06","lastUpdated":"2026-10-06","approaches":[{"language":"java","name":"Greedy Counting Approach","firstAdded":"2026-10-06","lastUpdated":"2026-10-06","explanation":"The algorithm iterates through the string character by character while maintaining two counters: 'oc' for open parentheses and 'cc' for required closing parentheses. When an opening parenthesis '(' is encountered, 'oc' is incremented. When a closing parenthesis ')' is encountered, if there is an unmatched open parenthesis available ('oc > 0'), we match them by decrementing 'oc'. Otherwise, if 'oc' is 0, it means we have an unmatched closing parenthesis, so we increment 'cc'. Finally, the total minimum additions needed is the sum of remaining unmatched opening and closing parentheses ('oc + cc').","keyIdea":"Track unmatched opening and closing brackets on the fly using a running balance to determine missing counterparts.","timeComplexity":"O(n)","spaceComplexity":"O(1)","advantages":["Optimal linear time complexity","Constant extra space without using an explicit stack","Simple and concise single-pass implementation"],"disadvantages":["Contains unnecessary commented-out placeholder text in the source code","Variable names ('oc', 'cc') lack descriptive clarity"],"concepts":["Greedy Algorithm","String Manipulation","Parentheses Matching"],"interviewNote":"Always strive for O(1) space optimization for parenthesis validation problems by using counters instead of an explicit stack when only the count of additions is required.","history":["06 October 2026 — New accepted approach added."]}],"reviewHistory":["06 October 2026 — Accepted submission processed as ADD_NEW."]}
<!-- LC_PROBLEM_META_END -->

# Minimum Add to Make Parentheses Valid

- **Difficulty:** Unknown
- **LeetCode:** https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/submissions/2164502069/?envType=daily-question&envId=2026-10-06
- **First Added:** 06 October 2026
- **Last Updated:** 06 October 2026

## Approaches

## Approach 1 — Greedy Counting Approach

**First Added:** 06 October 2026
**Last Updated:** 06 October 2026

### Explanation

The algorithm iterates through the string character by character while maintaining two counters: 'oc' for open parentheses and 'cc' for required closing parentheses. When an opening parenthesis '(' is encountered, 'oc' is incremented. When a closing parenthesis ')' is encountered, if there is an unmatched open parenthesis available ('oc > 0'), we match them by decrementing 'oc'. Otherwise, if 'oc' is 0, it means we have an unmatched closing parenthesis, so we increment 'cc'. Finally, the total minimum additions needed is the sum of remaining unmatched opening and closing parentheses ('oc + cc').

### Key Idea

Track unmatched opening and closing brackets on the fly using a running balance to determine missing counterparts.

### Complexity

- **Time:** O(n)
- **Space:** O(1)

### Advantages

- Optimal linear time complexity
- Constant extra space without using an explicit stack
- Simple and concise single-pass implementation

### Disadvantages

- Contains unnecessary commented-out placeholder text in the source code
- Variable names ('oc', 'cc') lack descriptive clarity

### Concepts

- Greedy Algorithm
- String Manipulation
- Parentheses Matching

### Interview Note

Always strive for O(1) space optimization for parenthesis validation problems by using counters instead of an explicit stack when only the count of additions is required.

### History

- 06 October 2026 — New accepted approach added.


## Review History

- 06 October 2026 — Accepted submission processed as ADD_NEW.
