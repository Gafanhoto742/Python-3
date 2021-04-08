num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O \033[1;32mPRIMEIRO\033[m número é o maior')
elif num1 == num2:
    print('Os dois valores são \033[1;32mIGUAIS\033[m') 
else:
    print('O \033[1;32mSEGUNDO\033[m número é o maior') 

