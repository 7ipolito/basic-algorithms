class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        valores=[]
        for i in range(1,len(nums)+1):
            valores.append(i)

        for i in range(len(valores)):
                if valores[i] not in nums:
                    return valores[i]

                # nums.sort()
                #
                # for i, v in enumerate(nums):
                #
                #     if (i != v):
                #         return v - 1
                #     if v == len(nums) - 1:
                #         return v + 1
                # Solution O(n)