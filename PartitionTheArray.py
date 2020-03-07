#Print the Yes and No  for checking the array length with given value
def arrtPartition(arr, k):
    if k >= len(arr):
        return False
    return True

arr = [1, 2, 3]
k = 2
ans = arrtPartition(arr, k)
if ans == 0:
    print("Yes")
else:
    print("No")


# Python program to print all sublist from a given list

# function to generate all the sub lists
def sub_lists(list1):
    # store all the sublists
    sublist = []

    # first loop
    for i in range(len(list1) + 1):

        # second loop
        for j in range(i + 1, len(list1) + 1):
            # slice the subarray
            sub = list1[i:j]
            sublist.append(sub)

    return sublist


# driver code
l1 = [1, 2, 3]
print(sub_lists(l1))
