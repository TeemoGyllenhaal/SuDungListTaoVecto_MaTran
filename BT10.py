import random
def matran():
    x = [random.randint(-10,10) for i in range(15)]
    z = []
    while x != []:
        z.append(x[:3])
        x = x [3:]
    print (z)
    return z
x = matran()
y = matran()
def cong_ma_tran(x,y):
    for i in range (5):
        for j in range (3):
            x[i][j] += y[i][j] 
            j += 1
        i += 1
    print("ma trận sau khi cộng: ",x)
    return x
cong_ma_tran(x,y)
