# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start > end:
        return -1
    else:
        mid_point = (start + end) // 2
        if arr[mid_point] == target:
            return mid_point
        elif arr[mid_point] < target:
            mid_point = mid_point - 1
            return binary_search(arr, target, mid_point, end)
        else:
            mid_point = mid_point + 1
            return binary_search(arr, target, start, mid_point)
