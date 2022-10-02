import operator

dict_operadores ={
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

print("Digite o primeiro número:")
n1 = int(input())

print("Digite o operador:")
operador = input()

print("Digite o segundo número:")
n2 = int(input())

print(dict_operadores[operador](n1,n2))