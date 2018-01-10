print("Dicionários")
print("-----------")
# Isso é uma lista
estudantes_lst = ["Pedro", 24, "Fernando", 22, "Tania", 26, "Cris", 25]
print(estudantes_lst)
# Isso é um dicionário
estudantes_dict = {"Pedro":24, "Fernando":22, "Tania":26, "Cris":25}
print(estudantes_dict)
print(estudantes_dict["Pedro"])
estudantes_dict["Pedro"] = 23
print(estudantes_dict["Pedro"])
print(estudantes_dict["Tania"])
estudantes_dict.clear()
print(estudantes_dict)
del estudantes_dict
# print(estudantes_dict)

estudantes = {"Pedro":24, "Fernando":22, "Tania":26, "Cris":25}
print(estudantes)
print(len(estudantes))
print(estudantes.keys())
print(estudantes.values())
print(estudantes.items())

estudantes2 = {"Maria":27, "Erika":28, "Milton":26}
print(estudantes2)
estudantes.update(estudantes2)
print(estudantes)

dic1 = {}
print(dic1)
dic1["key_one"] = 2
print(dic1)
dic1[10] = 5
print(dic1)
dic1[8.2] = "Olá"
print(dic1)
dic1["teste"] = 5
print(dic1)
dict1 = {}
print(dict1)
dict1["teste"] = 10
dict1["key"] = "teste"
# Atenção, pois chave e valor podem ser iguais, mas representam coisas diferentes.
print(dict1)

dict2 = {}
dict2["key1"] = "Big Data"
dict2["key2"] = 10
dict2["key3"] = 5.6
print(dict2)
a = dict2["key1"]
b = dict2["key2"]
c = dict2["key3"]
print(a, b, c)

# Dicionário de listas
dict3 = {'key1':1230,'key2':[22,453,73.4],'key3':['leite','maça','batata']}
print(dict3)
print(dict3['key2'])
# Acessando um item da lista, dentro do dicionário
print(dict3['key3'][0].upper())
# Operações com itens da lista, dentro do dicionário
var1 = dict3['key2'][0] - 2
print(var1)
# Duas operações no mesmo comando, para atualizar um item dentro da lista
dict3['key2'][0] -= 2
print(dict3)

print("\nCriando dicionários aninhados")
print("---------------------------")
# Criando dicionários aninhados
dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhado em Python'}}}
print(dict_aninhado)
print(dict_aninhado['key1']['key2_aninhada']['key3_aninhada'])