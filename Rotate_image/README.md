## Problem

```tex
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

You are given an *n* x *n* 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).



## Summary

- Transpose matrix first 

```tex
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

Transpose

[
  [1,4,7],
  [2,5,8],
  [3,6,9]
],
```

- For each row, swap first and last element



```tex
[
  [1,4,7],
  [2,5,8],
  [3,6,9]
],

Swap

[
  [7,4,1],
  [8,5,2],
  [9,6,3]
],
```

