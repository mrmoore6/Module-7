from array import array
def sort_array(arr):
        arr.sort()
        return arr
def search_array(num):
    try:
        number = int(input("Enter Value"))
        num = num.index(number)
    except ValueError:
        raise ValueError
    return num

if __name__ == '__main__':
    first_array = [2,4,5,5,6]
    print(sort_array(first_array))
    print(search_array(first_array))


