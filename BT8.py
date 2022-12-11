import random
def matran():
    x = [random.randint(-10,10) for i in range(15)]
    z = []
    while x != []:
        z.append(x[:3])
        x = x [3:]
    print (z)
    print ("Phần tử ở hàng 2 cột 3 là : ",(z[1][2]))
matran()
