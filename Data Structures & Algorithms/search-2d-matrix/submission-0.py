import itertools

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatten_matrix = list(itertools.chain.from_iterable(matrix))

        l, r = 0, len(flatten_matrix) - 1

        while l <= r:
            mid = (l + r) // 2

            t = flatten_matrix[mid]

            if t == target:
                return True
            elif t < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False