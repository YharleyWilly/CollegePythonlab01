#Dinâmicamente tipada
#Você pode alterar o tipo de uma variável durante a execução do código e o Python não lançará nenhuma Exception.

name = 'Eleven'     # a string
age = 12            # a int
power = 42.0        # a float

type_format = '{} is a {}'

print(type_format.format(name, type(name)))
print(type_format.format(age, type(age)))
print(type_format.format(power, type(power)))

name = 11           # now name is a int

print(type_format.format(name, type(name)))
print('This is a stranger thing!')

