list=[]
print("Enter the size of the list")
n= int(input())

for i in range(0,n):
    print("Enter a number in list")
    num=int(input())
    list.append(num)

print('The list created is ',list)


# OUTPUT:
# Enter the size of the list
# 3
# Enter a number in list
# 324
# Enter a number in list
# 555
# Enter a number in list
# 666
# The list created is  [324, 555, 666]
