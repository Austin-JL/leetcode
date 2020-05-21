# Problem description 

```tex
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

```

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers `(h, k)`, where `h` is the height of the person and `k` is the number of people in front of this person who have a height greater than or equal to `h`. Write an algorithm to reconstruct the queue.



# Summary

- How to sort  **List[List[int]]** 
  - sort() can help us sort the list by it key. In this question, we wish to sort both key and value in descending order
  - we use lambda function converting value to negative, this will let us sort value in descending order
  - setting reverse = True will let us sort key in descending order

  ```python
  people.sort(key=lambda k: (k[0], -k[1]), reverse=True)
  ```



- Use inset(index,object)
  - List is in descending order. 
  - we can use k as index and insert the pair to a new list. 
  - Descending order will allow us insert shorter person in front of the taller people
