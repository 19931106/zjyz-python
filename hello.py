# class Solution:
#     # 暴力匹配（超时)
#     def longestPalindrome(self, s: str) -> str:
#         if len(s)<2:
#             return s
#         max_len = 1
#         res = s[0]
#         for i in range(len(s)-1):
#             for j in range(i+1,len(s)):
#                 if j-i+1 > max_len and self._valid(s,i,j):
#                     max_len = j-i+1
#                     res = s[i:j+1]
#         return  res
#
#
#     #判断字串s是否是回文
#     def _valid(self,s,i,j):
#         while i<j:
#             if s[i]!=s[j]:
#                 return False
#             i+=1
#             j-=1
#         return True
#
# a = Solution()
# a_value = a.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# print(a_value)

#动态规划方法１
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         size = len(s)
#         if size < 2:
#             return s
#
#         dp = [[False for _ in range(size)] for _ in range(size)]
#
#         max_len = 1
#         start = 0
#
#         for i in range(size):
#             dp[i][i] = True
#
#         for j in range(1, size):
#             for i in range(0, j):
#                 if s[i] == s[j]:
#                     if j - i < 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i + 1][j - 1]
#                 else:
#                     dp[i][j] = False
#
#                 if dp[i][j]:
#                     cur_len = j - i + 1
#                     if cur_len > max_len:
#                         max_len = cur_len
#                         start = i
#         return s[start:start + max_len]

# strstr()

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle == "":
#             return 0
#         needle_len = len(needle)
#         haystack_len = len(haystack)
#         for i in range(haystack_len-needle_len+1):
#             print(haystack[i:i+needle_len])
#             if haystack[i:i + needle_len] == needle:
#                 return i
#                 break
#         return -1
#
#
# a = Solution()
# b = a.strStr('hello','lle')
# print(b)
# strstr()
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         len_haystack,len_needle = len(haystack),len(needle)
#         if len_needle == 0:
#             return 0
#
#         pn = 0
#         while pn < len_haystack-len_needle+1:
#             while pn < len_haystack-len_needle+1 and haystack[pn]!=needle[0]:
#                 pn += 1
#
#             cur_len = pl = 0
#             while pl < len_needle and pn < len_haystack and haystack[pn] == needle[pl]:
#                 pn+=1
#                 pl+=1
#                 cur_len+=1
#             if cur_len == len_needle:
#                 return pn-len_needle
#
#             pn = pn-cur_len+1
#         return -1



