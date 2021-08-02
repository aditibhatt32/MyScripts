num= input('Enter a number:')
def square(num):
    if not num.isdigit():
     return 'invalid'
    num=int(num)
    return num*num+num
print('square:',square(num))
