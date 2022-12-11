import random
num = int(input("Nhập số phần tử của vecto : "))
def sinh_vector_so_thuc(num):
    a = -5.7
    b = 6.9
    x = [(b-a)*random.random()+ a for i in range (num)]
    print (x)
def main():
  sinh_vector_so_thuc(num)
if __name__ == "__main__":
  main()
    