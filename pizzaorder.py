print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size=="S":
    print("Prize for small pizza is $15")
    bill +=15
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill = bill+2
elif size=="M":
    print("Prize for medium size pizza is $20")
    bill +=20
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill = bill+3
elif size=="L":
    print("Prize for large pizza is $25")
    bill+=25
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill = bill + 3
else:
    print("OOOPS!!! you typed wrong input. TRY AGAIN!")

extra_cheese = input("Do you want extra cheese? y or no: ")
if extra_cheese=="y":
    bill = bill+1
print(f"Your total bill is ${bill}")
