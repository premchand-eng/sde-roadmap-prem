# My standalone version of Two Sum
def twoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[num] = i

# Example run
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
