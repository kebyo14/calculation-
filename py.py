a = input("What is your operation +, *, /, - ")
b = int(input("Give me the first index (for ex: 123)") )
c = int(input("Give me the second index (for ex: 123)") )
if a == "+":
    print(f"Your answer is {b + c}")
elif a == "-":
        print("Your answer is ", b - c)

elif a == "*":
        print("Your answer is ", b * c)
elif a == "/":
        print("Your answer is ", b / c)
else:
      print("U chose wrong operation, try again")     