class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        # This is a bruteforce approach - o(n*2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        '''
        seen = {}

        # nums=[-3,4,3,90]

        # print(abs(-3-0)) # 3

        for idx, val in enumerate(nums):
            complement = target - val
            if complement in seen:
                # print(target - val)
                # print("Yes")
                return [seen[complement], idx]
            seen[val] = idx

            # print(seen)
            

        