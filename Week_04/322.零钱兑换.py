#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (40.82%)
# Likes:    776
# Dislikes: 0
# Total Accepted:    123.1K
# Total Submissions: 300.3K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
#
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
#
# 示例 2:
#
# 输入: coins = [2], amount = 3
# 输出: -1
#
#
#
# 说明:
# 你可以认为每种硬币的数量是无限的。
#
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        res = -1

        def helper(coins, amount, num):
            nonlocal res
            if not amount:
                res = num if res == -1 else min(res, num)
                return

            if not coins:
                return
            coin = coins[-1]
            count = amount // coin
            for i in range(count, -1, -1):
                if res != -1 and num + i > res:
                    return
                helper(coins[:-1], amount - coin * i, num + i)

        helper(coins, amount, 0)
        return res
# @lc code=end

