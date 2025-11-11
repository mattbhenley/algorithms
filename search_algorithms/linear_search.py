def linear_search(items, target):
    for i, item in enumerate(items):
        print(f"Checking index {i}: {item}")  # to visualize
        if item == target:
            return i
    return -1


if __name__ == "__main__":
    baseball_players = ["Greg Maddux", "Ken Griffey Jr.", "Pete Rose", "Mike Piazza", "Barry Bonds", "Sammy Sosa", "Mark McGwire"]
    print("\nList:", baseball_players)

    result = linear_search(baseball_players, "Pete Rose")
    if result != -1:
        print(f"\nFound 'Pete Rose' at index {result}")
    else:
        print("\n'Player' not found")
