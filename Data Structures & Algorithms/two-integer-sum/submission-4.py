class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output_dict = {}
        for i in range(len(nums)):
            answer = target - nums[i]
            if answer in output_dict:
                #int new_num = output_dict[answer]
                #arr = [output_dict[answer], i]
                return [output_dict[answer], i]
            output_dict[nums[i]] = i