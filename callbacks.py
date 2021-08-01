def func_1(x):
    return x**2
def func_2(x):
    return x**3
callbacks=[func_1,func_2]
print('named functions:')
for func in callbacks:
    print('result:',func(3))
callbacks=[lambda x:x**2,lambda x:x**3]
print('results:')
for func in callbacks:
    print('result:',func(3))
