def isPal(number):
    strNumber = str(number)
    for i in range(0 , int(len(strNumber)/2 +1 )):
        if strNumber[i] != strNumber[-i -1]:
            return False
    return True
            

maxProduct = 0
for i in range(99, 999):
    for j in range(99, 999):
        result = i * j
        if isPal(result):
            if result > maxProduct:
                maxProduct = result

print(maxProduct)

