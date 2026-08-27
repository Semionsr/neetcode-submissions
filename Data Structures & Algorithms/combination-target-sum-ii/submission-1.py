class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, cur, sum1):
            if sum1 == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or target < sum1:
                return
            
            cur.append(candidates[i])

            backtrack(i+1, cur, sum1 + candidates[i])
            cur.pop()


            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(i+1, cur, sum1)
            

        backtrack(0,[], 0)
        return res


