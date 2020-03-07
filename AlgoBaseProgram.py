# Fibonacci using Dynamic programing:
'''DP: Breaking problem into subproblems and stores the results of subproblems to avoid computing the same results again
Two main properties of a problem that suggests that the given problem can be solved using Dynamic programming.
1) Overlapping Subproblems
2) Optimal Substructure
DP is not useful when there are no common (overlapping) subproblems because there is no point storing
the solutions if they are not needed again
There are following two different ways to store the values so that these values can be reused:
a) Memoization (Top Down)
b) Tabulation (Bottom Up)

Steps to solve a DP
1) Identify if it is a DP problem
2) Decide a state expression with
   least parameters
3) Formulate state relationship
4) Do tabulation (or add memoization)

'''
def fibonacci(n):
    # Taking 1st two fibonacci nubers as 0 and 1
    FibArray = [0, 1]

    while len(FibArray) < n + 1:
        FibArray.append(0)
        print(FibArray)

    if n <= 1:
        return n
    else:
        if FibArray[n - 1] == 0:
            FibArray[n - 1] = fibonacci(n - 1)

        if FibArray[n - 2] == 0:
            FibArray[n - 2] = fibonacci(n - 2)

    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]
    return FibArray[n]
print(fibonacci(7))

#Bubble sort, using swaping in python
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1 Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubbleSort(arr))

