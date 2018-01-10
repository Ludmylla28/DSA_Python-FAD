print("List Comprehension")
print("------------------")
# Retornar cada caracter em uma sequência de caracteres
lst = [x for x in 'python']
# Check
print(lst)
print(type(lst))

# Raiz quadrada e um range de números e retornar uma lista
lst = [x**2 for x in range(0,11)]
print(lst)
# Verificar os números pares em um range de números
lst = [x for x in range(11) if x % 2 == 0]
print(lst)

# Converter Celsius para Fahrenheit
celsius = [0,10,20.1,34.5]
fahrenheit = [ ((float(9)/5)*temp + 32) for temp in celsius ]
print(fahrenheit)

# Operações aninhadas
lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)
