def calculator(operation,n1,n2):
 return operation(n1,n2)
result = calculator(lambda n1,n2:n1*n2,10,20)
print(result)
print(calculator(lambda n1,n2:n1+n2,10,20))
