eng=int(input("Enter the number you got in English:"))
sci=int(input("Enter the number you got in Science:"))
nep=int(input("Enter the number you got in Nepali:"))
soc=int(input("Enter the number you got in Social:"))
Tot_mark=eng+sci+nep+soc
print(f"Total mark you got is {Tot_mark}")
Per=Tot_mark/4
print(f"Percentage you got is {Per}")
if(Per>70):
    print("You have got Distinction")
elif(Per>60):
    print("You have got First Division")
elif(Per>50):
    print("You have got Second Division")
elif(Per>40):
    print("You have been Pass")
else:
    print("You have failed")
