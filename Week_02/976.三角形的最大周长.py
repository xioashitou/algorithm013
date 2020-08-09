#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#
# https://leetcode-cn.com/problems/largest-perimeter-triangle/description/
#
# algorithms
# Easy (55.40%)
# Likes:    71
# Dislikes: 0
# Total Accepted:    18.7K
# Total Submissions: 33.8K
# Testcase Example:  '[2,1,2]'
#
# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
# 
# 如果不能形成任何面积不为零的三角形，返回 0。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：[2,1,2]
# 输出：5
# 
# 
# 示例 2：
# 
# 输入：[1,2,1]
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：[3,2,3,4]
# 输出：10
# 
# 
# 示例 4：
# 
# 输入：[3,6,2,3]
# 输出：8
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= A.length <= 10000
# 1 <= A[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        l = 0
        if len(A) < 3:
            return l

        A.sort()
        for index in range(len(A)-2):
            if abs(A[index]+A[index+1]) > A[index+2]:
                l = max(l, sum([A[index], A[index+1], A[index+2]]))
        return l
# @lc code=end

