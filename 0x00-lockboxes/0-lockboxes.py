#!/usr/bin/python3
"""
You have n number of locked boxes in front of you
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes
"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened"""
    isOpen = [0]
    for key in isOpen:
        for k_box in boxes[key]:
            if k_box not in isOpen:
                if k_box < len(boxes):
                    isOpen.append(k_box)
    if len(isOpen) == len(boxes):
        return True
    return False
