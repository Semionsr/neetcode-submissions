class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        max_l = height[l]
        max_r = height[r]

        while l < r:
            max_l = max(max_l, height[l])
            max_r = max(max_r, height[r])
            if max_l <= max_r:
                l += 1
                if max_l - height[l] > 0:
                    res += max_l - height[l]
                    
            if max_l > max_r: 
                r -= 1
                if max_r - height[r] > 0:
                    res += max_r - height[r]
                    
        return res