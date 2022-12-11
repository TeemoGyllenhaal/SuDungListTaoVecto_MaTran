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
def nhan_2_vector(x,y):
    i = 0
    z = []
    while i < len(x):
        z.append(x[i]*y[i])
        i +=1 
    print ("Vector sau khi nhân : ",z)
    return z
nhan_2_vector(x,y)