# check whether the number is armstrong or not
num = int(input("enter a number: "))
length = len(str(num))
temp = num
sum = 0

while temp > 0:
    remainder = temp % 10
    sum = sum + remainder ** length
    temp = temp // 10  

if num == sum:
    print("armstrong")
else:
    print("not armstrong")