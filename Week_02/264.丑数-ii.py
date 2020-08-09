#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (53.29%)
# Likes:    350
# Dislikes: 0
# Total Accepted:    31.3K
# Total Submissions: 58.8K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
# 
# 丑数就是质因数只包含 2, 3, 5 的正整数。
# 
# 示例:
# 
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 
# 说明:  
# 
# 
# 1 是丑数。
# n 不超过1690。
# 
# 
#
import heapq
# @lc code=start
class Ugly:
    def __init__(self):
        # self.seen = {1,}  # just for heap
        self.nums = [1]
        # self.heap = [1]  # just for heap

        self.caculate()

    def caculate(self):
        # 1、heap
        # weights = [2,3,5]

        # for _ in range(1690):
        #     cur_ugly = heapq.heappop(self.heap)
        #     self.nums.append(cur_ugly)
        #     for weight in weights:
        #         new_ugly = cur_ugly * weight
        #         if new_ugly not in self.seen:
        #             self.seen.add(new_ugly)
        #             heapq.heappush(self.heap, new_ugly)

        # 2、dynamic programming
        weight_2, weight_3, weight_5 = 0 ,0, 0

        for _ in range(1690):
            new_ugly = min(self.nums[weight_2]*2, self.nums[weight_3]*3, self.nums[weight_5]*5)
            self.nums.append(new_ugly)

            # !ATTENTION! use if but not elif, because different weight may get same result 
            if new_ugly == self.nums[weight_2]*2:
                weight_2 += 1
            if new_ugly == self.nums[weight_3]*3:
                weight_3 += 1
            if new_ugly == self.nums[weight_5]*5:
                weight_5 += 1

class Solution:
    uglys = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        # 1、dumb solution
        # def is_ugly(num):
        #     while num:
        #         if num == 1:
        #             return True
        #         elif num % 2 == 0:
        #             num //= 2
        #         elif num % 3 == 0:
        #             num //= 3
        #         elif num % 5 == 0:
        #             num //= 5
        #         else:
        #             return False

        # count = 0
        # num = 1
        # while num:
        #     if is_ugly(num):
        #         count += 1

        #     if count == n:
        #         return num
            
        #     num += 1

        # pre caculate, define a new class
        return self.uglys.nums[n-1]
# @lc code=end

s = Solution()
print(s.nthUglyNumber(10))

