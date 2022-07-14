sum = 0
num1 = 0 
num2 = 1 
#fibo = []
while num2 < 4000000:
    temp = num1
    num1 = num2
    num2 = num2 + temp 
    #fibo.append(num2)
    if num2 % 2 == 0:
        sum += num2
print(sum)

