class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       my_dict = {}
       my_dict_two = {}
       for i in range(len(t)):
        my_dict[t[i]] = 1 + my_dict.get(t[i], 0)
       for j in range(len(s)):
        my_dict_two[s[j]] = 1 + my_dict_two.get(s[j], 0)
       print(my_dict)
       print(my_dict_two)
       if my_dict == my_dict_two:
        return True
       return False