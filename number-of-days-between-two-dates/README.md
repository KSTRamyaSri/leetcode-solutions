<!-- LC_PROBLEM_META_START -->
{"slug":"number-of-days-between-two-dates","title":"Number of Days Between Two Dates","difficulty":"Easy","url":"https://leetcode.com/problems/number-of-days-between-two-dates/submissions/2164937938/","firstAdded":"2026-10-07","lastUpdated":"2026-10-07","approaches":[{"language":"java","name":"Absolute Epoch Day Count Conversion","firstAdded":"2026-10-07","lastUpdated":"2026-10-07","explanation":"The solution converts each date string into an absolute number of days elapsed since a fixed reference point (year 1971, January 1st). It does this by parsing the year, month, and day components, adding 365 or 366 days for each preceding year depending on leap year status, adding days for all completed months in the current year with an extra day if February has passed in a leap year, and finally adding the remaining days of the current month. The absolute difference between the two converted day counts gives the result.","keyIdea":"Transform both calendar dates into absolute day counters starting from a fixed anchor year and find the absolute difference.","timeComplexity":"O(Y) where Y is the number of years between 1971 and the target year, bounded by a constant maximum of 130 operations given the constraints (1971 to 2100), effectively O(1).","spaceComplexity":"O(1)","advantages":["Avoids importing external libraries like java.time which may be restricted in some coding environments","Straightforward implementation of calendar math using arrays and loops","Very predictable and constant time/space complexity due to bounded constraints"],"disadvantages":["Manual implementation of date math is prone to off-by-one errors or leap year oversights","Less concise compared to language-provided date-time APIs like LocalDate.parse()"],"concepts":["Date Manipulation","Leap Year Calculation","Math Absolute Difference","String Parsing"],"interviewNote":"While this manual approach demonstrates fundamental algorithmic competency with leap years and arrays, in a production setting or standard interview you should ask if built-in date libraries (like java.time.LocalDate) are allowed to avoid boilerplate code and potential bugs.","history":["07 October 2026 — New accepted approach added."]}],"reviewHistory":["07 October 2026 — Accepted submission processed as ADD_NEW."]}
<!-- LC_PROBLEM_META_END -->

# Number of Days Between Two Dates

- **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/number-of-days-between-two-dates/submissions/2164937938/
- **First Added:** 07 October 2026
- **Last Updated:** 07 October 2026

## Approaches

## Approach 1 — Absolute Epoch Day Count Conversion

**First Added:** 07 October 2026
**Last Updated:** 07 October 2026

### Explanation

The solution converts each date string into an absolute number of days elapsed since a fixed reference point (year 1971, January 1st). It does this by parsing the year, month, and day components, adding 365 or 366 days for each preceding year depending on leap year status, adding days for all completed months in the current year with an extra day if February has passed in a leap year, and finally adding the remaining days of the current month. The absolute difference between the two converted day counts gives the result.

### Key Idea

Transform both calendar dates into absolute day counters starting from a fixed anchor year and find the absolute difference.

### Complexity

- **Time:** O(Y) where Y is the number of years between 1971 and the target year, bounded by a constant maximum of 130 operations given the constraints (1971 to 2100), effectively O(1).
- **Space:** O(1)

### Advantages

- Avoids importing external libraries like java.time which may be restricted in some coding environments
- Straightforward implementation of calendar math using arrays and loops
- Very predictable and constant time/space complexity due to bounded constraints

### Disadvantages

- Manual implementation of date math is prone to off-by-one errors or leap year oversights
- Less concise compared to language-provided date-time APIs like LocalDate.parse()

### Concepts

- Date Manipulation
- Leap Year Calculation
- Math Absolute Difference
- String Parsing

### Interview Note

While this manual approach demonstrates fundamental algorithmic competency with leap years and arrays, in a production setting or standard interview you should ask if built-in date libraries (like java.time.LocalDate) are allowed to avoid boilerplate code and potential bugs.

### History

- 07 October 2026 — New accepted approach added.


## Review History

- 07 October 2026 — Accepted submission processed as ADD_NEW.
