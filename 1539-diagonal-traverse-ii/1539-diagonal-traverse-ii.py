import math

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        m = max(len(num) for num in nums)

        diag_order = {}

        for i in range(n-1, -1, -1):
            for j in range(m):
                if j >= len(nums[i]):
                    break

                if i+j not in diag_order:
                    diag_order[i+j] = []
                
                diag_order[i+j].append(nums[i][j])
            
        res = []

        for k in sorted(diag_order.keys()):
            res.extend(diag_order[k])

        return res
