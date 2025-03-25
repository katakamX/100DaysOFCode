a,b=9,10
def gmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
gmean(a,b)

def isgreater(a,b):
    if(a<b):
        print("a is greater")
    elif(b>a):
        print("b is the greater number of the two")
        
isgreater(a,b)

def nameprint(fname,mname = "aditya" , lname = "katakam" ):
    print(fname , mname, lname)
nameprint("aditya", "katakam")