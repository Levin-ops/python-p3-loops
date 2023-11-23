#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count-=1
    print("Happy New Year!")

    
def square_integers(int_list):
    return [i ** 2 for i in int_list]
    

def fizzbuzz():
    out_put = ""

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            out_put += "FizzBuzz\n"
        elif i % 3 == 0:
            out_put += "Fizz\n"
        elif i % 5 == 0:
            out_put += "Buzz\n"
        else:
            out_put += str(i) + "\n"

    print (out_put)

# fizzbuzz()
# code along
# while loop
# i = 0
# while i < 5:
#     print("Looping!")
#     i += 1

# for i in range(10):
#     print("Looping!")
#     print(f"I am loop number:{i}")


# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# before list comprehension
# inch_height = list()
# for height in player_heights:
#     inches_height = height * 7920
#     inch_height.append(inches_height)
    
# print(inch_height)

# After list comprehension

# inch_heights = [height * 7920 for height in player_heights]
# print(inch_heights)

# player_heights =[height * 7920 for height in player_heights]
# print(player_heights)