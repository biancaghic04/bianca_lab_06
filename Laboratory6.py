import os


def insertion_sort(numbers):
    arr = numbers.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers.copy()

    middle = len(numbers) // 2

    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def main():
    filename = "date.txt"

    if not os.path.isfile(filename):
        print("Error: date.txt does not exist.")
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        if len(lines) < 2:
            print("Error: The file must contain two input lines.")
            return

        numbers_line = lines[0].strip()
        algorithm = lines[1].strip()

        if not numbers_line:
            print("Error: No numbers provided.")
            return

        try:
            numbers = [int(x) for x in numbers_line.split()]
        except ValueError:
            print("Error: Invalid numbers in date.txt.")
            return

        if algorithm == "Insertion":
            sorted_numbers = insertion_sort(numbers)
        elif algorithm == "Merge":
            sorted_numbers = merge_sort(numbers)
        else:
            print("Error: Unknown sorting algorithm.")
            print("Available algorithms: Insertion, Merge")
            return

        result = algorithm + ": " + " ".join(
            str(x) for x in sorted_numbers
        )

        with open(filename, "w", encoding="utf-8") as file:
            file.write(lines[0].rstrip("\r\n") + "\n")
            file.write(lines[1].rstrip("\r\n") + "\n")
            file.write(result + "\n")

        print("Sorting completed successfully!")
        print(result)

    except OSError as error:
        print("File error:", error)


if __name__ == "__main__":
    main()
