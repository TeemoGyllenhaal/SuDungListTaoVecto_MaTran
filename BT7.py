import random
num = int(input("Nhập số phần tử của vecto : "))
def sinh_vector_so_thuc(num):
    a = -5.7
    b = 6.9
    x = [(b-a)*random.random()+ a for i in range (num)]
    print (x)
    return x
x = sinh_vector_so_thuc(num)
y = sinh_vector_so_thuc(num)
def tich_vo_huong(x,y):
    i = 0
    z = 0
    while i < len(x):
        z = z + (x[i]*y[i])
        i +=1 
    print ("Tích vô hướng : ",z)
    return z
tich_vo_huong(x,y)