#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (54.94%)
# Likes:    1205
# Dislikes: 0
# Total Accepted:    289.1K
# Total Submissions: 526.1K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
#
# 注意：你不能在买入股票前卖出股票。
#
#
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#
#
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
#
#
from math import inf
# @lc code=start
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 2:
            return 0

        # i 表示天数，k 表示交易次数，k 只有在买的时候加1，s 表示是否持有股票
        # 0 <= i < len(prices), k <= 1, s in (0, 1)
        # 状态方程：
        # dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k - 1][1] + prices[i])
        # 解释：今天没有持有股票，有两种可能：
        # - 昨天也没有持有股票，今天休息；
        # - 昨天持有股票，今天卖了；
        # dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        # 解释：今天持有股票，有两种可能：
        # - 昨天持有股票，今天休息；
        # - 昨天没有持有股票，今天买了；
        # 由于最多只允许完成一笔交易，所以退化为二维
        # dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        # dp[i][1] = max(dp[i - 1][1], -prices[i])
        # dp = [[0, 0] for _ in range(len(prices))]
        # for i in range(len(prices)):
        #     if not i:
        #         dp[i][0] = 0
        #         dp[i][1] = -prices[i]
        #         continue
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        #     dp[i][1] = max(dp[i - 1][1], -prices[i])
        # return dp[-1][0]

        min_price, profit = inf, 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = max(profit, price - min_price)
        return profit
# @lc code=end
s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))
