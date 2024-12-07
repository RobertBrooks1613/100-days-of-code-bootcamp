try:
    age = int(input("How old are you?"))
except ValueError:
    print("Invalid option, use numerical values only ")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You can not drive at age {age}.")
