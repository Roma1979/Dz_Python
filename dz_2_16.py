#Задайте список из n чисел последовательности 〖(1+1/n)〗^n 
# и выведите на экран их сумму.
num = int(input('ВВедите число: ')) 

def sequence(num):

    return[round((1 + 1 / x)**x, 2) for x in range (1, num + 1)]   
        
print(sequence(num))
print(round(sum(sequence(num))))