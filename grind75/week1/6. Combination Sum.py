class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def ric(templist, target, start, lista):
            if (0 == target):
                lista.append(templist)
                return
            if (target < 0 or len(templist) > 150):
                return
            for i in range(start, len(candidates)):
                ric(templist + [candidates[i]], target - candidates[i], i, lista)

        lista = []
        ric([], target, 0, lista)
        return lista