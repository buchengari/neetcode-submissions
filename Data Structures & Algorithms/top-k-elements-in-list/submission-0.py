from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntrMap = Counter(nums)
        sortResult = sorted(cntrMap.items(), key=lambda x:x[1], reverse=True)

        result = [res[0] for res in sortResult[:k]]
        return result