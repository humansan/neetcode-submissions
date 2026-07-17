class Solution:
    def trap(self, height: List[int]) -> int:
        
        min_height = 0
        temp_water = 0
        held_water = 0
        
        for h in height:
            if h >= min_height:
                min_height = h
                held_water += temp_water
                temp_water = 0
            else:
                temp_water += min_height - h

        min_height = 0
        temp_water = 0

        for i in range(len(height)-1, -1, -1):
            h = height[i]

            if h > min_height:
                min_height = h
                held_water += temp_water
                temp_water = 0
            else:
                temp_water += min_height - h
        
        return held_water