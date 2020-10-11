"""
Author: Michael Moore
Program: basic_list.py
Date: 10/11/20

This program takes
"""
def make_list():
    list = []
    try:

        for x in range(0, 3):
            userInput = int(get_input())
            if userInput < 50 and userInput > 1:
                list.insert(x, userInput)
            else:
                raise ValueError

    except ValueError:
        raise ValueError
    return list


def get_input():
    userInput = input("Enter Value")
    return userInput

if __name__ == '__main__':
    print(make_list())

