# Remove Invalid Parentheses

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/remove-invalid-parentheses/submissions/2165319023/?envType=daily-question&envId=2026-10-07](https://leetcode.com/problems/remove-invalid-parentheses/submissions/2165319023/?envType=daily-question&envId=2026-10-07)
- **First Added:** 07 October 2026
- **Last Updated:** 07 October 2026

## What Is the Problem?

Given a string containing letters and parentheses, remove the minimum number of parentheses so that the remaining string has balanced and valid parentheses. Return all unique valid strings you can form.

### Example 1

**Input:**

```text
s = "()())()"
```

**Output:**

```text
["(())()", "()()()"]
```

We can remove either the first extra closing parenthesis or the second extra closing parenthesis to get a valid string with minimum removals.


---


## Approach 1 — Backtracking with Pruning

**Language:** Java  
**First Added:** 07 October 2026  
**Last Updated:** 07 October 2026

### How This Approach Works

First, we count how many excess left '(' and right ')' parentheses exist in the string using a simple pass. These counts represent the exact number of removals we need to perform. Then, we use a backtracking function to try removing each excess parenthesis one by one. We skip duplicate adjacent characters to avoid generating duplicate strings. Once our counts for left and right removals reach zero, we check if the resulting string is valid. If it is, we add it to our result list.

### Step-by-Step Trace

Let's trace s = ")(". First pass: left = 0, right = 1 because ')' has no matching '(' before it. Then we call backtrack(s, 0, 0, 1, result). In backtrack, index = 0, i = 0, c = ')'. Since rightRemove > 0, we form next = "" (by removing s[0]). We recurse with backtrack("", 0, 0, 0, result). Since leftRemove == 0 and rightRemove == 0, we check if isValid("") which returns true, so "" is added to the result. Return final result [""]

### Simple Flow

```mermaid
flowchart TD
Start([Start]) --> Count[Count Excess Left and Right Parentheses]
Count --> BT[Call Backtrack]
BT --> CheckCount{leftRemove == 0 and rightRemove == 0?}
CheckCount -- Yes --> Validate{Is String Valid?}
Validate -- Yes --> AddResult[Add String to Result]
Validate -- No --> Return
AddResult --> Return
CheckCount -- No --> Loop[Iterate over characters from index]
Loop --> SkipCheck{Duplicate adjacent char?}
SkipCheck -- Yes --> Loop
SkipCheck -- No --> MatchLeft{c == '(' and leftRemove > 0?}
MatchLeft -- Yes --> RecurseLeft[Remove char and Recurse with leftRemove - 1]
MatchLeft -- No --> MatchRight{c == ')' and rightRemove > 0?}
MatchRight -- Yes --> RecurseRight[Remove char and Recurse with rightRemove - 1]
RecurseLeft --> Loop
RecurseRight --> Loop
Return([End of branch]) --> End([End])
```

### Key Idea

Precompute the exact number of invalid left and right parentheses, then use backtracking to branch on removing each possible candidate while skipping duplicates.

### Complexity

- **Time:** O(2^(N)) where N is the length of the string, due to the subsets of choices for removal.
- **Space:** O(N) for the recursion stack and substring creations.

### Interview Note

Always precompute the exact deficit of left and right parentheses before backtracking to avoid exploring invalid branch depths.

### History

- 07 October 2026 — New accepted approach added.


## Code

Solution code is stored in the language-specific solution file in this folder.

## History

- 07 October 2026 — Accepted solution processed as ADD_NEW.
