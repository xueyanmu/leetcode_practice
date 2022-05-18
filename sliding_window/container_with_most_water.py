class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        * write the algo in english points before coding
        """
        i, j = 0, len(height) - 1
        area = 0

        """
        * dont include if statement; 
            the constraints & while loop already cover them.
        """
        while i <= j:
            """
            * move dist calculation to INSIDE the while loop, 
                instead of decrementing each time.
            """
            dist = j - i
            temp_height = min(height[i], height[j])

            area = max(area, temp_height * dist)

            # move the shorter side forward

            """
            * instead of height[i + 1] < height[j - 1]
            * instead of height[i] > height[j]
            """
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return area


