class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        checker = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            checker[num] = 1 + checker.get(num,0)

        for num,cnt in checker.items():
            freq[cnt].append(num)
        

        res = []

        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                if k > 0:
                    res.append(num)
                    k -= 1
        return res