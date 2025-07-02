def manual_sort(lst):
    # Bubble Sort (ascending order)
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def analyze_list(numbers):
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers:
        total += num
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    average = total / len(numbers)

    return {
        "Sum": total,
        "Average": round(average, 2),
        "Minimum": minimum,
        "Maximum": maximum,
        "Sorted List": manual_sort(numbers[:])  # Pass a copy to avoid changing original
    }


def display_statistics(stats):
    print("\n List Analysis Summary:")
    for index, (key, value) in enumerate(stats.items(), start=1):
        print(f"{index}. {key}: {value}")


def get_valid_input():
    while True:
        raw_input = input(" Enter numbers separated by spaces: ")
        try:
            numbers = [int(x) for x in raw_input.strip().split()]
            if not numbers:
                print(" Please enter at least one number.")
                continue
            return numbers
        except ValueError:
            print(" Invalid input! Please enter only integers.")


# Main Program
if __name__ == "__main__":
    print(" Smart List Analyzer (Manual Mode)")
    user_numbers = get_valid_input()
    results = analyze_list(user_numbers)
    display_statistics(results)
