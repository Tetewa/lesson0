import random

def generate_password(n):
    result = ""
    for i in range(1, n):
        for j in range(i + 1, n): 
            if (i + j) % n == 0:
                result += str(i) + str(j)              
    return result
n = random.randint(3, 20)
print("Случайное число:", n)
print("Пароль:", generate_password(n))

#Проверка
#def generate_password(n):
#    result = ""  
#    for i in range(1, n):
#        for j in range(i + 1, n): 
#            if n % (i + j) == 0:
#                result += str(i) + str(j)            
#    return result
#for n in range(3, 21):
#    print(f"{n} {generate_password(n)}")