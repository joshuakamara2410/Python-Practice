name = input("Name: ")
age = int(input("Age: "))
hasSubscription = input("Do you have a subscription? Y/N: ")
if age <= 12:
    price = 5
elif age >= 12:
    price = 10
elif age >= 18:
    price = 12
if hasSubscription == "Y":
    total = price - 2
elif hasSubscription == "N":
    total = price
print(f"{name}, your total is {total}")