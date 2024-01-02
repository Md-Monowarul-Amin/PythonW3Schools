num_list = [1, 2, 3, 4, 5, 10, 55, 44, 11, 30, 12]

even_nums = 0
odd_nums = 0

for i in range(len(num_list)):
    if num_list[i] % 2 == 0:
        even_nums += 1
    else:
        odd_nums += 1

print("Total even numbers: ", even_nums)
print("Total Odd Numbers: ", odd_nums)
