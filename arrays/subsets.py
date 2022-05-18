"""
STATUS:
I understand backtracking through this
"""


class Solution:

    def subset(self, nums):
        # todo: why is this backtracking and not regular recursion
        """
        basically in backtracking we attempt solving a
        subproblem, and if we don't reach the desired solution,
         then undo whatever we did for solving that subproblem,
          and try solving another subproblem.

          Backtracking: remove the last option we tried and replace it with
          another option.

        :param nums:
        :return:
        """
        self.res = []
        self.dfs(sorted(nums), 0, [], self.res)
        return self.res

    def dfs(self, nums, index, path, res):
        # in backtracking, there is no need for a base case. we are simply exploring all
        # the possibilities building from the ground up.
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, index + 1, path + [nums[index]], res)
