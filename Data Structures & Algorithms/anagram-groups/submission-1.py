class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        b = {}
        for i in strs:
            c = "".join(sorted(i))
            if c in b:
                b[c].append(i)
            else:
                b[c] = [i]
        return list(b.values())