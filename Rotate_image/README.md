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

- Reverse each row 



```tex
[
  [1,4,7],
  [2,5,8],
  [3,6,9]
],

Reverse

[
  [7,4,1],
  [8,5,2],
  [9,6,3]
],
```
