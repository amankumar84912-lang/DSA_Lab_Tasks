def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


n = int(input("Enter number of elements: "))

arr = []

print("Enter array elements:")
for i in range(n):
    arr.append(int(input()))

sorted_arr = quick_sort(arr)

print("Sorted array in ascending order:")
print(sorted_arr)
