def multiply_nums(nums_list):
    """Return a new list where evens are doubled and odds are tripled."""
    return [num * 2 if num % 2 == 0 else num * 3 for num in nums_list]


def capitalize_fruits(fruits):
    """Return a space-separated string;
    longer words uppercased and shorter ones lowercased.
    """
    return " ".join(s.upper() if len(s) > 5 else s.lower() for s in fruits)


def main():
    # Example input data
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    # Process lists using helper functions
    processed_nums = multiply_nums(list1)
    processed_strings = capitalize_fruits(list2)

    #Display results
    print("Processed Numbers:", processed_nums)
    print("Processed Strings:", processed_strings)


# Run main() only if this file is executed directly
if __name__ == "__main__":
    main()



