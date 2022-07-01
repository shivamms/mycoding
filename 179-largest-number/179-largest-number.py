class compare(str):
    def __lt__(x, y):
        return x+y > y+x
    
class Solution:
    import functools
    def largestNumber(self, nums: List[int]) -> str:
        big_sum = ''.join(sorted(map(str,nums), key=compare))
        return '0' if big_sum[0] == '0' else big_sum
        

        
# import functools
# class Solution(object):
#     def largestNumber(self, arr):
#         for i,n in enumerate(arr):
#             arr[i]=str(n)
#         def comp(n1,n2):
#             if n1+n2>n2+n1:
#                 return -1
#             else:
#                 return 1
#         arr=sorted(arr,key=functools.cmp_to_key(comp))
#         return str(int(''.join(arr)))

        