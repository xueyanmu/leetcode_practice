from typing import List

"""
STATUS:
I understand most of it
I don't understand why java and python have different backtracking methods
i.e. concatenation using one line vs. add and remove using multiple lines.
I suspect they do the same
things but I haven't seen anything in python use add and remove and vv.
I haven't coded it into another language yet for this reason
"""


class Solution:

    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ret = []
        candidates.sort()
        self.candidates = candidates
        self.backtrack([], target, 0)
        return self.ret

    def backtrack(self, path, target, start):
        """
        :param path: a new array that will store potential arrays results
        :param target: our target number
        :param start: the index to start at, which prevents double-counting
        :return: nothing
        """
        if target < 0:
            return

        elif target == 0:
            list.append(path)
            return

        else:
            for i in range(start, len(self.candidates)):
                """
                why is there add and remove, when you could simply modify the path
                TODO: are these interchangeable- the add/remove vs the path modification?
    
                append/pop trick may save some time and space complexity? but actually in python it
                doesnt really work. in java it does... why               
                
                path.append(self.candidates[i])  # why? we are trying out a new option here
                self.backtrack(path...
                path.pop()  # why? we are removing the last option to make room for the new one.
                
                
                """
                # we need to add self.candidates[i] because that is now the new option we are considering.
                self.backtrack(path + [self.candidates[i]], target - self.candidates[i], i)
