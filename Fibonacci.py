n = int(input("Enter the size of the series : "))
n1 = 0
n2 = 1
f = []
f.append(n1)
f.append(n2)
for x in range(3,n):
    fib = n1+n2;
    f.append(fib)
    n1 = n2
    n2 = fib
print('Fibonacci Series : ',f)


# Enter the size of the series : 10
# Fibonacci Series :  [0, 1, 1, 2, 3, 5, 8, 13, 21]
