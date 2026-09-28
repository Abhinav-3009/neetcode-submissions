class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # s = sorted(s)
        # t = sorted(t)
        # return s == t
        freq = {}
        for c in s:
            freq[c] = freq.get(c,0)+1
        for c in t:
            freq[c] = freq.get(c,0)-1
        for value in freq.values():
            if value is not 0:
                return False
        return True
        