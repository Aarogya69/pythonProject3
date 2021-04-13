str_name=str(input("Enter the name"))
leng=len(str_name)
print(leng)
if leng < 3:
    print("Name must be 3 character")
elif leng>50:
    print("Name must be maximum of 50 character")
else:
    print("Name looks good")
