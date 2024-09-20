import math
def task1(n, m,):
    k = 1
    V = n * m * k                                   #Находим объем памяти данного изображения
    return int (V)

def task2(before, after,):
    result = after / before                         #Находим во сколько раз увеличился объем памяти
    return int (result)

def task3(nn, mm, vv):
    vv = vv * 1024 * 8                              #Перевод Килобайтов в биты
    k = vv / (nn * mm)                              #определение кол-во цветов
    return int (k)

def task4 (k, vvv):
    vvv = vvv * 8                                   #перевод из байтов в бит
    k = math.log2 (k)                               #узнаём кол-во бит в одной точке
    mn = vvv / k                                    #кол-во точек на экране
    return int (mn)
    




if __name__ == "__main__" :
    #n = int (input("Ширина: "))
    #m = int (input("Высота: "))
    #print (task1(n, m))
    #before = int (input("кол-во цветов до: "))
    #after = int (input("кол-во цветов после: "))
    #print (task2(before, after))
    #nn = int (input("Ширина: "))
    #mm = int (input("Высота: "))
    #vv = int (input("Объем памати: "))
    #print (task3(nn, mm, vv))
    k = int (input("кол-во цветов: "))
    vvv = int (input("объем памяти: "))
    print (task4(k, vvv))