class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        tot_elements = m * n

        if tot_elements == 1:
            if matrix[0][0] == target:
                return True
            return False

        left = 0
        right = m * n - 1
        index = tot_elements // 2

        while left <= right and index > -1 and index < tot_elements:
            i = index // n
            j = index % n

            index_value = matrix[i][j]

            if index_value == target:
                return True

            # on left half
            elif index_value > target:
                right = index - 1

            # on right half
            elif index_value < target:
                left = index + 1

            index = (((right - left) // 2) + left)

        return False