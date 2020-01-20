import unittest
#Linear search with for loop
def linear_search(arr,item):

    for i in range(len(arr)):
        if arr[i]==item:
            return True

    return False

#Driver code
'''printing the linear_search function retuns values on sample test data'''
arrlist=[3,2,78,34,23]
item=78
print(linear_search(arrlist,item))
'''unit test cases in one function for the linear_search function'''

class TestLinearSearch(unittest.TestCase):

    def test_linear_search(self):
        self.assertEqual(linear_search([], 3), False)
        self.assertEqual(linear_search([1, 2], 3), False)
        self.assertEqual(linear_search([1, 2, 3, 4], 3), True)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 5), True)


if __name__ == '__main__':
    unittest.main()
