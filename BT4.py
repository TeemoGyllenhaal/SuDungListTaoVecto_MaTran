import random
num = int(input("Nhập số phần tử của vecto : "))
a = float(input("Nhập số thực a: "))
def nhan_vector(num,c):
    a = -5.7
    b = 6.9
    x = [(b-a)*random.random()+ a for i in range (num)]
    print (x)
    i = 0
    while i < len(x):
        x[i]= c*x[i]
        i +=1
    print(x)
    return x
def main():
  nhan_vector(num,a)
if __name__ == "__main__":
  main()