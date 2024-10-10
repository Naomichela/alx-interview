#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

# Test case 1
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 2
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 3
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected output: False

