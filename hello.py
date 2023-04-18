print("200 is a great no")
print(2.3)
print(1900)
print(20 * 24 * 60)
name = "saurabh"
print("his name is " + name + " bisht")
print("saurabh is " + str(24) + " year old")
print(f"saurabh is {24} years old ")
time = 24*60*60
print(f"20 days are {20 * time} seconds")
#function


def factorial(num):
    sum = 1
    for i in range(1,num+1):
        sum = sum * i
    print(sum)

factorial(9)
