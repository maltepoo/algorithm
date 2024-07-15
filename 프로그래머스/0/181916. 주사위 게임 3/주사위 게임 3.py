def solution(a, b, c, d):
    answer = 1
    
    nums = sorted([a, b, c, d])
    distinct_nums = set(nums)
    
    if len(distinct_nums) == 1:
        answer = 1111 * a
    elif len(distinct_nums) == 2:
        if nums.count(nums[0]) == 1:
            answer = (10 * nums[3] + nums[0])**2
        elif nums.count(nums[3]) == 1:
            answer = (10 * nums[0] + nums[3])**2
        else:
            answer = (nums[0] + nums[2]) * abs(nums[0] - nums[2])
    elif len(distinct_nums) == 3:
        for i in distinct_nums:
            if nums.count(i) == 1:
                answer *= i
    elif len(distinct_nums) == 4:
        answer = min(nums)
    return answer