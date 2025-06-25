#def average(a=3,b=6):
 #   print("the average i s", (a+b)/2)
    
#average()

def name(fname="aditya", mname="", lname="katakam"):
    print("your name is = ", fname,mname,lname)
    
#name(mname= "putty")
# name("Aditya")

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)  # Return the average

c = average(1,2,3)   
print(c)

