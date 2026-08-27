class Solution:

    def encode(self, strs: List[str]) -> str:
        arr = ""
        for i in strs:
            arr += str(len(i)) + "#" + i
        return arr
        
    def decode(self, s: str) -> List[str]:
        arr, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])
            arr.append(s[j + 1 : j+ 1 + length])
            i = j + 1 + length
        return arr

