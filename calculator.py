def get_numbers():
    numbers = []
    print("keep entering your numbers or enter \"finished\" when done with entering your numbers")
    while True:
        user_input= input("enter:").strip()
        
        if user_input.lower() == 'finished':
            break
        try:
            
            number = float(user_input)
            numbers.append(number)
        
        except ValueError:
            print("invalid input")
            
    return numbers
        
def calculator():

    print("Calculator Prog" )
    print("enter 1 for Addition")
    print("enter 2 for substraction")
    print("enter 3 for division")
    print("enter 4 for multiplication")
    
    while True:
        choice = input("enter the option")
        
        if choice in ['1', '2', '3', '4']:
            numbers = get_numbers()
            
            if len(numbers) < 2:
                print("enter atleast 2 numbers")
                
                continue
            if choice == '1':
                result =  sum(numbers)
                print("the result is: " , result)
                            
            elif choice == '2':
                result = numbers[0]
                for num in numbers[1:]:
                    result = result-num
                    print("the result is :", result)
                    
            elif choice == '3':
                result = numbers[0]
                for num in numbers[1:]:
                    result = result * num
                    print("the result is:", result)
                    
            elif choice == '4':
                result = numbers[0]
                for num in numbers[1:]:
                    result = result / num
                    print("result is: ", result)
                    
        else: 
            print("invalid response")
            
        next_calc = input("do you wish to perform another calculation? type yes/no")
             
        if next_calc == 'yes':
            calculator()
            
        else:
            print("goodbye")
            break
        

calculator()
            
                
                       
    
        