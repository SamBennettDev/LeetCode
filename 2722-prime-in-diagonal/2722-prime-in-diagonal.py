class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(num):
            if num == 1:
                return False

            if num == 2:
                return True

            for i in range(2, ceil(sqrt(num) + 1)):
                if num % i == 0:
                    return False

            return True

        dim = len(nums)
        diag_nums = []

        for i in range(dim):
            diag_nums.append(nums[i][i])
            diag_nums.append(nums[i][(dim-1) - i])

        diag_nums.sort(reverse=True)

        for num in diag_nums:
            if is_prime(num):
                return num

        return 0