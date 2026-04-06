class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # return sorted(s) == sorted(t)
        s_f={}
        t_f={}
        for i in s:
            s_f[i]=s_f.get(i,0) +1
        for i in t:
            t_f[i]=t_f.get(i,0) +1
        return s_f==t_f
