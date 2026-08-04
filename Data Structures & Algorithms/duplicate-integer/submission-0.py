class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Solution
        - loop through the given list and add them to a set
        - while doing this, check if the element already exists in the set
        - if it does, it contains duplicates
        '''
        # use a set instead of list because lookup is faster
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False