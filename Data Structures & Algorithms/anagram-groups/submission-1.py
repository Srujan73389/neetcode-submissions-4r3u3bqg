class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped={}
        for word in strs:
            sorted_w=''.join(sorted(word))
            if sorted_w in grouped:
                grouped[sorted_w].append(word)
            else:
                grouped[sorted_w]=[word]
        return list(grouped.values())

        