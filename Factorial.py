def fact(a):
  if a == 1 or a == 0:
    return 1
  else:
    return a*fact(a-1)  

n = int(input('Enter a number : '))
f = fact(n)
print(f'Factorial of {n} is {f}')
