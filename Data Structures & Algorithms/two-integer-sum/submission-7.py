class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        # This is a bruteforce approach - o(n*2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        '''

        '''
        Solution
        - start from first element and check if target - first exists in a lookup
        - if not, add the first element to the lookup
        '''
        seen = {}

        for idx, val in enumerate(nums):
            complement = target - val
            if complement in seen:
                return [seen[complement], idx]
            seen[val] = idx
            

        