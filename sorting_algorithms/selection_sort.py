def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i+1}: {arr}")


if __name__ == "__main__":
    nums = [7, 11, 4, 9, 5, 13, 2, 15, 21]
    print("Before:", nums)
    selection_sort(nums)
    print("After :", nums)
