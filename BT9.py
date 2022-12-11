import random
def matran():
    x = [random.randint(-10,10) for i in range(15)]
    z = []
    while x != []:
        z.append(x[:3])
        x = x [3:]
    print (z)
    return z
def nhan_vector(z,c):
    y = 0
    for i in range (5):
        for j in range (3):
            y = y + (c * z[i][j])
            j += 1
        i += 1
    print("Tích vô hướng ma trận: ",y)
    return y
z = matran()
n = float(input("Nhập giá trị n: "))
nhan_vector(z,n)
