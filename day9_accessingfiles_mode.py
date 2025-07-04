def read_student_marks(file_path):
    student_marks = {}
    skipped_entries = 0

    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                try:
                    name, mark = line.strip().split(',')

                    name = name.strip().title()
                    mark = mark.strip()

                    if not name or not mark:
                        raise ValueError("Missing name or mark.")

                    mark = int(mark)  # Will raise ValueError if not a number

                    student_marks[name] = mark

                except ValueError as ve:
                    print(f" Skipping invalid entry at line {line_num}: {line.strip()} | Reason: {ve}")
                    skipped_entries += 1

    except FileNotFoundError:
        raise FileNotFoundError(" File not found. Please check the path.")

    return student_marks, skipped_entries


def print_summary(student_marks):
    print("\n Student Marks Summary:")
    try:
        if not student_marks:
            raise ZeroDivisionError("No valid student data to display.")

        total = 0
        for i, (name, mark) in enumerate(student_marks.items(), start=1):
            print(f"{i}. {name}: {mark}")
            total += mark

        average = total / len(student_marks)
        print(f"\n Average Mark: {round(average, 2)}")

    except ZeroDivisionError as zde:
        print(f" {zde}")


# Main Program
if __name__ == "__main__":
    while True:
        path = input(" Enter path to the marks file (e.g., marks.txt): ").strip()
        try:
            marks_dict, skipped = read_student_marks(path)
            print_summary(marks_dict)
            print(f"\n Total Valid Entries: {len(marks_dict)}")
            print(f" Skipped Entries Due to Errors: {skipped}")
            break
        except FileNotFoundError as fnf:
            print(fnf)
            print(" Please try again.")
