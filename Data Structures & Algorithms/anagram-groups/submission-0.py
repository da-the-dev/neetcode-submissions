class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(s)) for s in strs]

        d = {}
        for s, c in zip(strs, sorted_strs):
            d.setdefault(c, []).append(s)

        return list(d.values())


            


        