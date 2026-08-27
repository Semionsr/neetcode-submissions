class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        arr = [[]for i in range(len(nums) + 1)]
        for n in nums:
            elements[n] = 1 + elements.get(n,0)
        for n, c in elements.items():
            arr[c].append(n)
        
        res = []
        for i in range(len(arr) - 1, 0 , -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
