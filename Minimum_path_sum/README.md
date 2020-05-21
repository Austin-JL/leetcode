## Problem

```tex
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```

Given a *m* x *n* grid filled with non-negative numbers, find a path from top left to bottom right which *minimizes* the sum of all numbers along its path.



## Summary

- Simple dp question

- We start from the top left corner [0,0] :

  - [0,0], we store sum as itself
  - if i = 0 (first row), the sum of current cell equals previous column value in dp plus current value in grid
  - if j = 0 (first col), the sum of current cell equals previous row value in dp plus current value in grid
  - otherwise, sum equals current value in grid plus smaller value between previous row value and previous column value in dp

  
