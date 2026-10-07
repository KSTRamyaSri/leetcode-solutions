# Two Sum

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/two-sum/submissions/2165067998/](https://leetcode.com/problems/two-sum/submissions/2165067998/)
- **First Added:** 07 October 2026
- **Last Updated:** 07 October 2026

## What Is the Problem?

Given an array of numbers and a target sum, find the indices of the two numbers in the array that add up to the target sum.

### Example 1

**Input:**

```text
nums = [2, 7, 11, 15], target = 9
```

**Output:**

```text
[0, 1]
```

Because nums[0] + nums[1] == 2 + 7 == 9, we return their indices [0, 1].


---


## Approach 1 — Hash Map Complement Lookup

**Language:** Python  
**First Added:** 07 October 2026  
**Last Updated:** 07 October 2026

### How This Approach Works

The solution checks if the input array has fewer than 2 elements and returns an empty list if so. Otherwise, it iterates through the array while maintaining a hash map called 'seen' that stores each number and its index. For every number, it calculates its complement (target - number) and checks if that complement is already in the 'seen' map. If it is, the pair is found, and their indices are returned. If not, the current number and its index are added to the map, and the loop continues.

### Step-by-Step Trace

Example: nums = [2, 7, 11], target = 9
1. Initial check: len(nums) is 3, which is not less than 2. 'seen' is empty.
2. Iteration 1: current_index = 0, num = 2. complement = 9 - 2 = 7. Is 7 in 'seen'? No. Add seen[2] = 0. 'seen' is {2: 0}.
3. Iteration 2: current_index = 1, num = 7. complement = 9 - 7 = 2. Is 2 in 'seen'? Yes, at index 0. Return [seen[2], 1] which is [0, 1].

### Simple Flow

```mermaid
flowchart TD
A[Start twoSum] --> B{nums is empty or len < 2?}
B -- Yes --> C[Return []]
B -- No --> D[Initialize seen = {}]
D --> E[Loop through nums with enumerate]
E --> F[Calculate complement = target - num]
F --> G{Is complement in seen?}
G -- Yes --> H[Return [seen[complement], current_index]]
G -- No --> I[Store seen[num] = current_index]
I --> E
E -- Loop finishes --> J[Return []]
```

### Key Idea

Instead of checking every pair with nested loops, use a hash map to remember numbers we have already seen and instantly check if the required complement exists in O(1) time.

### Complexity

- **Time:** O(n)
- **Space:** O(n)

### Interview Note

Always mention that trading space for time by using a hash map reduces the brute-force O(n^2) approach down to a single pass O(n) solution.

### History

- 07 October 2026 — New accepted approach added.


## Code

Solution code is stored in the language-specific solution file in this folder.

## History

- 07 October 2026 — Accepted solution processed as ADD_NEW.
