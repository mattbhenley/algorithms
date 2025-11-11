def linear_search(items, target):
    """
    Check each element until we find the target.
    Time complexity: O(n)
    """
    for i, item in enumerate(items):
        print(f"Checking index {i}: {item}")  # to visualize
        if item == target:
            return i
    return -1


if __name__ == "__main__":
    fruits = ["apple", "banana", "cherry", "mango", "pear"]
    print("\nList:", fruits)

    result = linear_search(fruits, "mango")
    if result != -1:
        print(f"\nFound 'mango' at index {result}")
    else:
        print("\n'mango' not found")
