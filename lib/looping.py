#!/usr/bin/env python3

def happy_new_year():
    number = 10
    while number >= 1:
        print(number)
        number -= 1
    print("Happy New Year!")



def square_integers(int_list):
    return [int ** 2 for int in int_list]

def fizzbuzz():
    number = 1
    while number <= 100:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
        number += 1