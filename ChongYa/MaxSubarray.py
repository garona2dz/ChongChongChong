def maxsubarray(nums):  # 这种时间复杂度O(n2)很大
    sum_list = [0] * len(nums)
    result = 0
    s = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] <= 0:
            count += 1
            continue
        else:
            for j in range(i, len(nums)):
                s += nums[j]
                if s > result:
                    result = s
                if s <= 0:
                    break
            sum_list[i] = result
            result = 0
            s = 0
    print(max(sum_list) if count != len(nums) else max(nums))
    return max(sum_list) if count != len(nums) else max(nums)


x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxsubarray(x)


def maxSubArray(nums):  # leetcode上解法，很巧妙，利用前面和的正负来判断是否叠加
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)


