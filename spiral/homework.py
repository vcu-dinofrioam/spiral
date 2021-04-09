def spiralize(number):
    return_value = 1
    number*=number
    num=1
    add=2
    result=1
    while num<number:
        for i in range(4):
            num+=add
            result+=num
        add+=2
    return result
print (spiralize(501))

    return return_value
