class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, sum1):
            if sum1 == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or sum1 > target:
                return
            
            cur.append(nums[i])
            backtrack(i, cur, sum1 + nums[i])

            cur.pop()
            backtrack(i+1, cur, sum1)
        
        backtrack(0, [], 0)
        
        return res
    