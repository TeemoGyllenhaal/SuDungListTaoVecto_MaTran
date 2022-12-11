import random
def matran1(m,k):
    x = [random.randint(-10,10) for i in range(m)]
    z = []
    while x != []:
        z.append(x[:k])
        x = x [k:]
    print (z)
    return z
def matran2(k,n):
    x = [random.randint(-10,10) for i in range(k)]
    z = []
    while x != []:
        z.append(x[:n])
        x = x [n:]
    print (z)
    return z
k = int(input("Nhập k (cột của ma trận 1 hoặc hàng của ma trận 2): "))
n = int(input("Nhập n(cột của ma trận 2): "))
m = int(input("Nhập m(hàng của ma trận 1): "))
tich1 = int(input("Nhập tích m*k: "))
tich2 = int(input("Nhập tích k*n: "))
x = matran1(tich1,k)
y = matran2(tich2,n)
def nhan_2_ma_tran(x,y,k,m,n):
    z = 0
    for i in range (m):
        for j in range (n):
            for k in range (k):
                z = z + (x[i][k] * y[k][j])
                k += 1
            j += 1
        i += 1
    print("Tích vô hướng ma trận: ",z)
    return y
nhan_2_ma_tran(x,y,k,m,n)
# k = 4 ; n = 5 ; m = 3 ; m*k = 12 ; k*n = 20

