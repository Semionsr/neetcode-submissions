class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            my_dict[nums[i]] = 1 + my_dict.get(nums[i],0)

        freq = [[] for i in range(len(nums) + 1)]
        for n, c in my_dict.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

