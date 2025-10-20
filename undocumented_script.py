def multiply_nums(nums_list):
    return [num * 2 if num % 2 == 0 else num * 3 for num in nums_list]


def capitalize_fruits(fruits):
    return " ".join(s.upper() if len(s) > 5 else s.lower() for s in fruits)


def main():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_nums = multiply_nums(list1)
    processed_strings = capitalize_fruits(list2)

    print("Processed Numbers:", processed_nums)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()


