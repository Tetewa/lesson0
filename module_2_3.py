my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

while index < len(my_list):
    number = my_list[index]
    if number == 42:
        print(number)
    elif number == 69:
        print(number)
    elif number == 322:
        print(number)
    elif number == 13:
        print(number)
    elif number == 99:
        print(number)
    index += 1

# Так же можно было просто сделать так, ведь все нужные нам цифры в начале, а после 99, отрицательное число

# while index < len(my_list):
#     number = my_list[index]
#     if number < 0:
#         break
#     if number > 0:
#         print(number)
#     index += 1



# Но, чтобы использовать и Continue, и Break в коде, можно сделать так

# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# index = 0
# while index < len(my_list):
#     number = my_list[index]
#     if number < 0:
#         break
#     if number == 0
#         index += 1
#         continue
#     print(number)
#     index += 1

