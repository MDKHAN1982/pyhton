# commented after testing
print("Hello, World!")
print("Enter value for x")
x = int(input())
if x % 3 == 0:
     if x % 5 == 0:
          print("Your number is divisible by 3 and 5 ")
     else:
          print("Your number is divisible by 3 and NOT 5")
elif x % 5 ==0:
    print("Your number is divisible by 5 and NOT  by 3")
else:
    print("Your number is NOT divisible by 3 & 5")
print ("End of program")
# committed from gitHUB to VScode
