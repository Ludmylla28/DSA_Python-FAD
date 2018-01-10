print("Python Debugger")
print("---------------")
a = [4,5,6]
b = 2
c = 3

resultado = b + c
print(resultado)

resultado2 = a + b
print(resultado2)

import pdb
a = [4,5,6]
b = 2
c = 3

resultado = b + c
print (resultado)

pdb.set_trace()

resultado2 = a + b
print(resultado2)
