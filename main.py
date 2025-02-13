def create_number_list():
    numbers = []
    while True:
        try:
            n = int(input("Enter the number of elements in the list: "))
            if n < 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    for i in range(n):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
    return numbers

def display_menu():
    print("\nSearch Menu:")
    print("1. Exact match search")
    print("2. Search for numbers greater than")
    print("3. Search for numbers less than")
    print("4. Search for numbers within a range")
    print("5. Exit")

def search_exact(numbers):
    if not numbers:
        print("The list is empty. Please add numbers first.")
        return
    try:
        target = int(input("Enter the number to search for: "))
        if target in numbers:
            print(f"{target} found in the list.")
        else:
            print(f"{target} not found in the list.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def search_greater_than(numbers):
    if not numbers:
        print("The list is empty. Please add numbers first.")
        return
    try:
        target = int(input("Enter the number to search for greater than: "))
        result = [num for num in numbers if num > target]
        if result:
            print(f"Numbers greater than {target}: {result}")
        else:
            print(f"No numbers greater than {target} found.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def search_less_than(numbers):
    if not numbers:
        print("The list is empty. Please add numbers first.")
        return
    try:
        target = int(input("Enter the number to search for less than: "))
        result = [num for num in numbers if num < target]
        if result:
            print(f"Numbers less than {target}: {result}")
        else:
            print(f"No numbers less than {target} found.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def search_within_range(numbers):
    if not numbers:
        print("The list is empty. Please add numbers first.")
        return
    try:
        start = int(input("Enter the starting number of the range: "))
        end = int(input("Enter the ending number of the range: "))
        if start > end:
            print("Invalid range! The starting number should be less than or equal to the ending number.")
            return
        result = [num for num in numbers if start <= num <= end]
        if result:
            print(f"Numbers within the range {start} to {end}: {result}")
        else:
            print(f"No numbers found in the range {start} to {end}.")
    except ValueError:
        print("Invalid input! Please enter valid integers.")

def main():
    numbers = create_number_list()
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            search_exact(numbers)
        elif choice == '2':
            search_greater_than(numbers)
        elif choice == '3':
            search_less_than(numbers)
        elif choice == '4':
            search_within_range(numbers)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
