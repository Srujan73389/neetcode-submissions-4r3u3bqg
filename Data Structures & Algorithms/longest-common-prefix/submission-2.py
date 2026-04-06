class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base=strs[0]
        if base=="":
            return ""
        for i in range(len(base)):
            for word in strs[1:]:
                if (i==len(word) or word[i]!=base[i]):
                    return word[0:i]
        return base
        