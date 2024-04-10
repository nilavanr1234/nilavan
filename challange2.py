from collections import Counter


def third_highest_frequency(nums):
    # Count the occurrences of each integer in the list
    count_dict = Counter(nums)

    # Sort the dictionary by values in descending order
    sorted_counts = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    # Find the third highest frequency
    third_highest_freq = None
    for _, freq in sorted_counts:
        if freq > 1:
            third_highest_freq = freq
            break

    # If there are fewer than three unique frequencies, return None
    if third_highest_freq is None:
        return None

    # Find the integer(s) with the third highest frequency
    third_highest_nums = [num for num, freq in count_dict.items() if freq == third_highest_freq]

    # If there's only one integer with the third highest frequency, return it
    if len(third_highest_nums) == 1:
        return third_highest_nums[0]
    # Otherwise, return all integers with the third highest frequency
    else:
        return third_highest_nums


# Example usage
nums = [1, 2, 3, 2, 2, 3, 4, 4, 5, 5, 5]
result = third_highest_frequency(nums)
print("Integer(s) with the third highest frequency:", result)
