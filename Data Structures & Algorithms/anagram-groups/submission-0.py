from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aMap = defaultdict(list)
        result = []

        for word in strs:
            sortedWord = tuple(sorted(word))

            aMap[sortedWord].append(word)

        for v in aMap.values():
            result.append(v)

        return result