a=int(input("Enter the first number:"))
b=input("Enter the second number:")
b=int(b)
if 100<=a<1000 or 100<=b<1000:
    print("One of these is greater than 100.")
elif a<=100 and b<=100:
    print("a and b are less than 101.")
elif(a>1000 and a<1000) or(b>1000 and b<10000):
    print("That is hue amount.")