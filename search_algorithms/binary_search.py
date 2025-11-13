def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = items[mid]
        print(f"low={low}, high={high}, mid={mid}, guess={guess}")

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13]
    print("\nSorted list:", numbers)

    result = binary_search(numbers, 9)
    if result != -1:
        print(f"\nFound 9 at index {result}")
    else:
        print("\n9 not found")
