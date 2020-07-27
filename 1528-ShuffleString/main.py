from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i, char in enumerate(s):
            res[indices[i]] = char

        return ''.join(res)


s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]

sol = Solution()
result = sol.restoreString(s, indices)
print(result)
