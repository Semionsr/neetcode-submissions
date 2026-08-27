class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for strings in strs:
            count = [0] * 26
            for c in strings:
                count[ord(c) - ord("a")] += 1
            my_dict[tuple(count)].append(strings)
        return my_dict.values()
