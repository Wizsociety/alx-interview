#!/usr/bin/python3
"""
Determines if all boxes can be opened using keys stored inside boxes.
Each box may contain keys to other boxes.
A key with the same number as a box opens that box.
Box 0 is unlocked initially.
Returns True if all boxes can be opened, False otherwise.
"""


def canUnlockAll(boxes):
    """
    Method that determines if all boxes can be unlocked
    Args:
        boxes (list): list of lists where each inner list contains keys
    Returns:
        bool: True if all boxes can be opened, False otherwise
    """
    if not boxes or type(boxes) is not list:
        return False

    n = len(boxes)
    if n == 0:
        return False
    if n == 1:
        return True

    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    # Use a queue-like approach to process keys
    while keys:
        current_box = keys.pop(0)
        
        # Check each key in current box
        for key in boxes[current_box]:
            # Validate key is within valid range and box hasn't been unlocked
            if isinstance(key, int) and 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    # Check if all boxes are unlocked
    return all(unlocked)


if __name__ == "__main__":
    # Test cases
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]]
    print(canUnlockAll(boxes))  # True

    boxes = [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[0]]
    print(canUnlockAll(boxes))  # True

    boxes = [[10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], 
             [5, 1, 9, 1], [], [6, 6, 9, 4, 3, 2, 3, 8, 5], 
             [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6], [9, 5, 8, 8], 
             [6, 2, 8, 6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], 
             [7, 3], [7, 9, 10, 10, 8, 9, 2, 5],
             [7, 2, 2, 4, 4, 2, 4, 8, 7],
             [4, 2, 9, 6, 6, 5, 5]]
    print(canUnlockAll(boxes))  # True
