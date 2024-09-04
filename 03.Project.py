f =float(input("Enter First Number:"))
o =(input("Enter Operator:+,-,*,/:"))
s =float(input("Enter Second Number"))
result=str(f)+(o)+str(s)+("=")
if o=="+":
    print (result, f+s)
elif o == "-":
    print (result,f-s)
elif o== '*':
    print (result,f*s)
elif o== "/": 
    print (result,f/s)
else: 
    print("Invalid Operator") 