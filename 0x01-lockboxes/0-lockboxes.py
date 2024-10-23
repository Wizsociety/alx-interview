#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Parameters:
    boxes (list of lists): A list containing keys in each box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    opened = [False] * len(boxes)  # Track opened boxes
    opened[0] = True  # The first box is unlocked
    keys = boxes[0]  # Start with the keys in the first box

    while keys:
        key = keys.pop()  # Get a key from the list
        if key < len(boxes) and not opened[key]:  # If the box can be opened
            opened[key] = True  # Mark the box as opened
            keys.extend(boxes[key])  # Add the keys from this box to the list

    return all(opened)  # Check if all boxes are opened

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False

