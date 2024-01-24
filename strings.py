def print_digits(value):
    digits = [] # lista
    while value >= 10:
        digits.append(value % 10) # metodo append ingresa al ultimo elemento de la lista
        value = value // 10
        # 1 [0]
        #2 [0, 2]
    digits.append(value) # [0, 2, 1]
    digits.reverse() # metodo reverse sorts la lista al reves
    print(digits) # [1, 2, 0]

cadena =  'palabra'
cadena2 = "palabra doble"

# p -> a -> l -> a -> b -> r -> a -> \0
# nulo: '\0' = 0 = null = None
# int = 32 bits, float = 64, char = 256, bool = 1 bit, double (coma flotante * 2 dimension 128), long (integer * 2)
# ['p', 'a', 'l', 'a', 'b', 'r', 'a', '\0'] 

print(cadena[6])
print(cadena[-1])

for letra in cadena:
    print(letra)

for i in range(10):
    print(i)

for value in range(100):
    if (value % 3) == 0: # logic operators '>', '<', '==', 
        continue
    print(value)

texto = "1234567"
value = 1234567

text = ""
while value > 0:
    digit = value % 10
    text =  str(digit) + text
    # if(value < 10):
    #     digit = value % 10
    #     text =  str(value) + text
    value = value // 10


print(text)

cadena3 = "otra"
cadena3[2] = 'l'

print(cadena3)
# N = 1000
# while N > 10:
#     print(N % 10)
#     N = N // 10
# print(N)
# print_digits(120)
# for each 
# por cada elemento en una coleccion, haz algo
'''
do 
{
    # bloque de codigo
} while(codicion) '''

# vector = {1, 4, 5, 8}  N = [4]
# 5, i3
'''
matriz = vector en R2 (dos dimensiones)
{
    {2, 5, 6, 7, 3},
    {9, 4, 5, 3, 3},
    {4, 4, 3, 1, 12},
    {0, 4, 6, 3, 32}
}
N x M
donde N = 4
donde M = 5
4 x 5
i,j
i = 3, j = 2 ???? = 4
'''

'''
funcion range es generador, regresa valores entre 0 y N
'''