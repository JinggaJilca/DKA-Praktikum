
def Fibonacci(n):  
    if n < 0:
        print("Input Salah")
        return 0
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def cetak(n):
    for i in range(n + 1):
        print(Fibonacci(i))


n = int(input("Masukkan nilai n: "))
cetak(n)


