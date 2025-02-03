def get_numbers():
    numbers = []
    print("Keep entering your numbers or enter \"finished\" when done.")
    while True:
        user_input = input("Enter: ").strip()
        
        if user_input.lower() == 'finished':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input, please enter a number.")
            
    return numbers
        
def calculator():
    print("Calculator Program")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Division")
    print("4: Multiplication")

    while True:
        choice = input("Enter the option: ").strip()
        
        if choice in ['1', '2', '3', '4']:
            numbers = get_numbers()
            
            if len(numbers) < 2:
                print("Enter at least 2 numbers.")
                continue
            
            if choice == '1':  # Addition
                result = sum(numbers)

            elif choice == '2':  # Subtraction
                result = numbers[0]
                for num in numbers[1:]:
                    result -= num

            elif choice == '3':  # Division
                result = numbers[0]
                for num in numbers[1:]:
                    if num == 0:
                        print("Error: Division by zero is not allowed.")
                        break
                    result /= num

            elif choice == '4':  # Multiplication
                result = 1
                for num in numbers:
                    result *= num
            
            print("The result is:", result)

        else: 
            print("Invalid response. Please enter a valid option.")

        next_calc = input("Do you wish to perform another calculation? (yes/no): ").strip().lower()
        
        if next_calc != 'yes':
            print("Goodbye!")
            break

calculator()
