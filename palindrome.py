string=input("Enter the string:")
if(string == string[::-1]):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
print("The reverse of ",string," is ",string[::-1])
