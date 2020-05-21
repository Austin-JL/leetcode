## Problem 

```tex
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```

Given a linked list, remove the *n*-th node from the end of list and return its head.

## Summary

- Two pointer method 
  - The fast pointer advances the list by n+1 steps from the beginning, 
  - slow and fast pointer are separated n nodes
  - We maintain this constant gap by advancing both pointers together until the fast pointer arrives past the last node
  - slow pointer will be pointing at the nnnth node counting from the last

