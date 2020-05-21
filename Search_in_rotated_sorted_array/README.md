## Problem

```tex
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

You are given a target value to search. If found in the array return its index, otherwise return `-1`.



## Summary

- In this question, we have to locate pivot point, Knowing our target either in left or right ascending sequence can help us move pointers

- Using two pointers (low and high ) method and binary search
  - low = 0 , hight = len(list)-1 and mid = (low + high)/2
  - if mid >= low : mid is at left ascending sequence
    - if target between low and mid, change high pointing to mid -1
    - otherwise, low = mid + 1
  - if mid < low : mid is at right ascending sequence
    - if target between mid and high, change low pointing to mid + 1
    - otherwise, high = mid -1
  - Iter until low > high