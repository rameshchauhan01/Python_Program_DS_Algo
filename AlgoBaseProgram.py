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

# Binary Search function and unit test class to test the function
# Print the search value index in the sequence
import unittest

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

class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search([], 3), -1)
        self.assertEqual(binary_search([1, 2], 3), -1)
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4], 4), 3)

# Linear search function and unit test class for testing the linear search function.
def linear_search(arr,item):

    for i in range(len(arr)):
        if arr[i]==item:
            return True

    return False

# Linear search Driver code
'''printing the linear_search function retuns values on sample test data'''
arrlist=[3,2,78,34,23]
item=78
print(linear_search(arrlist,item))
'''unit test cases in one function for the linear_search function'''
# Linear search unit test
class TestLinearSearch(unittest.TestCase):

    def test_linear_search(self):
        self.assertEqual(linear_search([], 3), False)
        self.assertEqual(linear_search([1, 2], 3), False)
        self.assertEqual(linear_search([1, 2, 3, 4], 3), True)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 5), True)

if __name__ == '__main__':
    unittest.main()
