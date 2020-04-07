# class Solution:
#     def longestPalindrom(self,s:str)->str:
#         size = len(s)
#         max_len = 0
#         start = 0
#         dp = [[False for _ in range(size) for _ in range(size)]]
#
#         if size < 2 :
#             return s
#
#         for j in range(1,size):
#             for i in range(0,j):
#                 if s[i] == s[j]:
#                     if j-i < 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i+1][j-1]
#                 else:
#                     dp[i][j] = False
#
#                 if dp[i][j]:
#                     cur_len = j-i+1
#                     if cur_len > max_len:
#                         max_len = cur_len
#                         start = i
#         return s[start:start+max_len]
a = 0
for i in range(1,101):
    for j in range(1,101):
        if str(3^i+7^j)[-1] == '8':
            a += 1
print(a)


