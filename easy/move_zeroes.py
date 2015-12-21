"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

"""

def move_zeroes(nums):
    """
    Runtime: 236 ms
    The delete operation is O(n) time complexity.
    Append is still O(1)
    """
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)


def move_zeroes_better(nums):
    """
    Runtime:68ms
    It has better runtimes because the for list operations
    get_item and set_item are O(1) operations.
    """
    pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos  = pos + 1

    for i in range(pos,len(nums)):
        nums[i] = 0
