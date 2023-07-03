#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened.
"""
from collections import deque


def canUnlockAll(boxes):
    """Return all boxes that can be opened, else false"""
    num_boxes = len(boxes)
    visited = [False] * num_boxes  # Track visited boxes
    visited[0] = True  # Mark the first box as visited
    queue = deque([0])  # Start the bfs queue with the first box

    while queue:
        current_box = queue.popleft()

        """Check all keys in the current box"""
        for key in boxes[current_box]:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    """If all boxes have been visited, return True
       otherwise, return False
    """
    return all(visited)
