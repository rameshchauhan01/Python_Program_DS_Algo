### Dynamic programing:
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
## Fibonacci + DP + Recursion
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
## Number of Subarray with given sum and array
def ar_sum_dp(ar,total,i,mem):
    key=str(total) + ":"+ str(i)
    if key in mem:
        return mem[key]
    #Base case
    if total==0:
        return 1
    elif total<0:
        return 0
    elif i<0:
        return 0
    elif total<ar[i]:
        to_return=ar_sum_dp(ar,total,i-1,mem)
    else:
        to_return=(ar_sum_dp(ar,total-ar[i],i-1,mem) + ar_sum_dp(ar,total,i-1,mem))
        mem[key]=to_return
    return to_return   

def count_set_sub( ar,total):
    mem={}
    return ar_sum_dp(ar,total,len(ar)-1,mem)

### Bubble sort, using swaping in python
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

# Binary Search function 
# Print the search value index in the sequence
def binary_search(array, t):
    l = 0
    h = len(array) - 1

    while (l <= h):
        m = (l + h) // 2
        if (array[m] == t):
            return m
        elif (array[m] < t):
            l = m + 1
        else:
            h = m - 1

    return -1
print(binary_search([5,3,1,2,4],4))
print(binary_search([5,3,1,2,4],6))

# Linear search function for unsorted array.
def linear_search(arr,item):

    for i in range(len(arr)):
        if arr[i]==item:
            return True

    return False

# Linear search function for sorted array
