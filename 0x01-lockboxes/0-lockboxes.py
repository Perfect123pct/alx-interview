#!/usr/bin/python3

"""Module for lockboxes problem."""


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened."""
    if len(boxes) == 0:
        return False

    keys = [0]  # Start with the first box
    visited = set()

    while keys:
        box_index = keys.pop()
        visited.add(box_index)

        for key in boxes[box_index]:
            if key not in visited and key < len(boxes):
                keys.append(key)

    return len(visited) == len(boxes)


if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False
