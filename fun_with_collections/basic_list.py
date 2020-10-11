
def make_list():
    list = []
    for x in range(0, 3):
        userInput = int(get_input())
        list.insert(x, userInput)
    return list


def get_input():
    userInput = input("Enter Value")
    return userInput

if __name__ == '__main__':
    print(make_list())

