
def print_increasing(num:int):
    for line in range(num):
        position = line % 3
        for space in range(position):
            print("", end=" ")
        print("*")


def print_decreasing(num: int):
    for line in range(num):
        position = line % num
        for space in range(num - position-1):
            print("", end=" ")
        print("*")


num = 6
print_increasing(num // 2)
print_decreasing(num - num // 2)




    
