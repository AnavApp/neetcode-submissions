class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):   
            return False
        s_list = list(s)
        t_list = list(t)
        list.sort(s_list)
        list.sort(t_list)
        if s_list==t_list:
            return True
        return False