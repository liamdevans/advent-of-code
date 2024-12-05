from pathlib import Path
from icecream import ic

def read_input(filepath: Path) -> str:
    with open(filepath, "r") as file:
        text = [[int(num) for num in nums.split(" ")] for nums in file.readlines()]
    return text

MAX_DIFF = 3
input = read_input(Path(__file__).parent / "input.txt")


def is_steadily_increasing(nums: list[int]) -> bool:
    curr = nums[0]
    for num in nums[1:]:
        if num <= curr:
            return False
        if num > curr + MAX_DIFF:
            return False
        curr = num
    return True

def is_steadily_decreasing(nums: list[int]) -> bool:
    curr = nums[0]
    for num in nums[1:]:
        if num >= curr:
            return False
        if num < curr - MAX_DIFF:
            return False
        curr = num
    return True


def part_1():
    count = 0
    for nums in input:
        if is_steadily_increasing(nums):
            count += 1
        elif is_steadily_decreasing(nums):
            count += 1
    
    return count


def count_increasing_errors(nums: list[int]) -> tuple[list[int], list[int, list[int]]]:
    errors = [0, []]
    curr = nums[0]
    for idx, num in enumerate(nums[1:], start=1):
        if num <= curr:
            errors[0] += 1
            errors[1].append(idx)
        elif num > curr + MAX_DIFF:
            errors[0] += 1
            errors[1].append(idx)
        curr = num
    return nums, errors

def count_decreasing_errors(nums: list[int]) -> tuple[list[int], list[int, list[int]]]:
    errors = [0, []]
    curr = nums[0]
    for idx, num in enumerate(nums[1:], start=1):
        if num >= curr:
            errors[0] += 1
            errors[1].append(idx)
        elif num < curr - MAX_DIFF:
            errors[0] += 1
            errors[1].append(idx)
        curr = num
    return nums, errors

def list_subset_generator(input_list: list):
    for idx in range(len(input_list)):
        yield input_list[:idx] + input_list[idx + 1:]

def part_2():
    count_no_errors = part_1()

    count_with_errors = 0
    input_errors_only = [nums for nums in input if not is_steadily_increasing(nums) and not is_steadily_decreasing(nums)]
    for nums in input_errors_only:
        for subset in list_subset_generator(nums):
            if is_steadily_increasing(subset) or is_steadily_decreasing(subset):
                count_with_errors += 1
                break

    return count_no_errors + count_with_errors

ic(part_1())
ic(part_2())