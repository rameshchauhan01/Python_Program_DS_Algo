#Print the Yes and No  for checking the array length with given value
def arrtPartition(arr, k):
    if k >= len(arr):
        return True
    return False

arr = [1, 2, 3]
k = 2
ans = arrtPartition(arr, k)
if ans == 1:
    print("Yes")
else:
    print("No")