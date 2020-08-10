# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    LHS = 0
    RHS = 0
    # Your code here

    for i in range(0, len(merged_arr)):
        if LHS < len(arrA) and RHS < len(arrB):
            if arrA[LHS] < arrB[RHS]:
                merged_arr[i] = arrA[LHS]
                LHS = LHS + 1
            else:
                merged_arr[i] = arrB[RHS]
                RHS = RHS + 1
        elif LHS < len(arrA):
            merged_arr[i] = arrA[LHS]
            LHS = LHS + 1
        else:
            merged_arr[i] = arrB[RHS]
            RHS = RHS + 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively

# a = [1,3,5]
# b = [2,4,6]
# print(merge(a,b))


def merge_sort(arr):
    # Your code here
    low = 0
    high = len(arr)
    if len(arr) <= 1:
        return arr
    mid_point = (low + high) // 2
    temp_arr1 = arr[:mid_point]
    temp_arr2 = arr[mid_point:]
    left = merge_sort(temp_arr1)
    right = merge_sort(temp_arr2)
    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
