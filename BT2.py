import random
num = int(input("Nhập số phần tử của vector : "))
def sinh_vector_so_nguyen():
  x = [random.randint(-10,10) for i in range(num)]
  print (x)
def main():
  sinh_vector_so_nguyen()
if __name__ == "__main__":
  main()