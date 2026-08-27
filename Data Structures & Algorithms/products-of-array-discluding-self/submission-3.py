class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        pre = 1
        suf = len(nums) -1

        total = 1

        for pre in range(len(nums)):
            if pre != 0:
                total *= nums[pre -1]
                res.append(total)
            else:
                res.append(total)
            #print(res)
            
        total2 = 1
        for suf in range(len(nums) - 1, -1, -1):
            if suf != len(nums) - 1:
                total2 *= nums[suf+1]
                res[suf] *= total2
            else:
                continue
            print(res)
        
        
        
        return res

