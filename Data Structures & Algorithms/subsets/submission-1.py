class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        def backtracking(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            backtracking(i+1)

            cur.pop()
            backtracking(i+1)

        
        backtracking(0)
        return res
