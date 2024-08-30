from typing import List

def maxArea( height: List[int]) -> int:
    start, end = 0, len(height) - 1
    area = min(height[start], height[end]) * (end - start)
    while start < end:
        if height[start] < height[end]:
            start = start + 1
        else:
            end = end - 1
            # area = max(area, height[start] * (end - start))

        area = max(area, min(height[start], height[end]) * (end - start))
    return area
