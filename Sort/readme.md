# Sorting

## Bubble sort

![Bubble Sort Steps](https://cdn.programiz.com/sites/tutorial2program/files/Bubble-sort-0.png)

`````python
n = len(arr)
for i in range(n):
  # the last i element are sorted
  for j in range(n-i-1):
     if array[j] > array[j + 1]:
        # to sort in increasing order, we swap if greater
        array[j], array[j + 1] = array[j + 1], array[j]
`````



- We can use a variable **swapped** to optimized Bubble Sort
  - if there is no swapping taking place, no need for further iteration
- Time complexity : O(n^2)



## Insertion sort

![Insertion Sort Steps](https://cdn.programiz.com/sites/tutorial2program/files/Insertion-sort-3_2.png)

```python
for i in range(n):
  # same value to key
  key = arr[i]
  # start from 1 element before current 
  j = i -1 
  while j >= 0 and key < nums[j]:
    arr[j+1] = arr[j]
    j = j - 1  
  arr[j+1] = key
```

- Time complexity: O(n^2)



## Selection sort

![Selection Sort Steps](https://cdn.programiz.com/sites/tutorial2program/files/Selection-sort-0.png)

```python
for i in range(n):
  # set current as min
  min = i
  for j in range(i+1,n):
    if arr[j] < arr[min]:
      min =j
  arr[i],arr[min] = arr[min],arr[i]
```

- In selection sort, we divide our array to two separate parts : sorted and unsorted.
- At iteration, we find smallest element in unsorted part and put it at the end of the sorted part.
- Time complexity: O(n^2)



## quick sort

```python
def partition(arr,low,high):
  pivot = arr[high]
  i = low - 1
  for j in range(low,high):
    if arr[j] <= pivot:
      i = i+1
      arr[i], arr[j] = arr[j],arr[i]
  arr[i+1],arr[high] = arr[high],arr[i+1]

def quickSort(arr,low,high):
  if low<high:
    pi = pratition(arr,low,high)
    quickSort(arr,low,pi-1)
    quickSort(arr, pi+1,high)

```

- Quicksort is an algorithm based on divide and conquer approach in which the array is split into subarrays and these sub-arrays are recursively called to sort the elements.
- A pivot element is chosen from the array. The elements smaller than the pivot element are put on the left and the elements greater than the pivot element are put on the right. 