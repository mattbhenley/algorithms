def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f"Pass {i+1}: {arr}")
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    numbers = [9, 5, 3, 8, 20, 1, 11, 2, 7, 15]
    print("Before:", numbers)
    bubble_sort(numbers)
    print("After :", numbers)
