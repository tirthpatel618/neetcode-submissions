class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group by number of each char in the string 
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())        