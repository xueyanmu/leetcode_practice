class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.ret = [nums]
        self.used = [0*nums]
        self.dfs(nums, self.ret, [], 0)
        return self.ret

    def dfs(self, nums, ret, path, index):
        if not nums:
            res.append(path)