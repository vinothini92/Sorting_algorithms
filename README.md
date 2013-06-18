Sorting_algorithms
==================

Implementation of Various sorting algorithms in python


1) Given sorted list-A and another sorted list-B.Sort the both list to get A+B sorted list

solution:
since both the list are sorted already,Bubble sort and insertion sort works fine.
complexity for both algorithms when given list sorted is
number of comparisions-O(n)
number of exchanges-O(1) 
in bubble sort it needs extra temporary variable to exchanges whereas in 
insertion sort it can be done with varaibles and it reduces number of exchanges.
insertion sort works better for this problem.

2) Given sorted list-A and each item is added by user

solution:
As per the given condition the list is already sorted.it means we can find the position to be inserted using binary search 
and insert the element at the appropriate position using insertion sort.
