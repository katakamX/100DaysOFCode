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
        
get_numbers()
    
        