class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        current = nums[0]
        twice = False

        for i in range(1 ,len(nums)):
            if current == nums[i] and not twice:
                nums[j] = nums[i]
                j += 1
                twice = True

            elif current != nums[i]:
                nums[j] = nums[i]
                j += 1
                twice = False
            
            current = nums[i]

        return j