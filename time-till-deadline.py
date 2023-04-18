from datetime import date,time,datetime
str  = input("enter your goal with a deadline separated by colon\n")
list = str.split(":")
goal = list[0]
deadline = list[1]
d2 = datetime.strptime(deadline,"%d.%m.%Y")
delta  = d2 - datetime.today()

print(f"Dear user! Time remaining for you goal: {goal} is {delta.days} days")