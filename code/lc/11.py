# 3：47
'''给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

 

示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。'''
nums = [1,5,11,5]
target = sum(nums) // 2
print(target)
# bag,dp[件数][容量]
n = len(nums)
dp = [[0] * (target+1) for _ in range(n)]
print(dp)
print(len(dp))
print(len(dp[0]))