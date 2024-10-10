#!/usr/bin/python3
"""
Module 0-lockboxes
This module defines a function that determines if all the boxes can be opened
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    Args:
        boxes (list of lists): a list of lists where each sublist represents a box
        containing keys to other boxes
    Returns:
        bool: True if all boxes can be opened, else False
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # Box 0 is unlocked
    keys = boxes[0].copy()  # Start with the keys in the first box

    for key in keys:
        if 0 <= key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])  # Add keys from the unlocked box

    return all(unlocked)

