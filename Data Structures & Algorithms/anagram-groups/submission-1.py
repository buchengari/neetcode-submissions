from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Solution

        * Build HashMap

        - store the sorted version of word as a tuple in the dictionary key
        - and then add the actual word to the list of values
        - loop through the map and fetch all values in the map
        '''
        aMap = defaultdict(list)
        result = []

        for word in strs:
            sortedWord = tuple(sorted(word))
            aMap[sortedWord].append(word)

        for v in aMap.values():
            result.append(v)

        return result