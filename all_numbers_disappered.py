# My wrong solution working oly in 1 case
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#
#         nums.sort()
#
#         for i, v in enumerate(nums):
#             aux = i + 1
#             if i + 1 != v:
#                 if i + 1 == len(nums):
#                     return [i + 1]
#                 else:
#
#                     return [i + 1, aux + 1]



    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

    # Better solution
    #     set_nums = set(nums)
    #
    #     ret = []
    #
    #     for i in range(1, len(nums) + 1):
    #         if i not in set_nums:
    #             ret.append(i)
    #     return ret