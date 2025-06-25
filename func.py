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
        #print("the average is", sum/len(numbers))
    return sum / len(numbers)

c = average(5,6,7)
print(c)
a = 5
b = 6   
c = 7
d = average(a, b, c)
print(d)