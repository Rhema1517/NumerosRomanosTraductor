class RomanNumerals:
    @staticmethod
    def from_roman(s):
        X=[dict(zip('MDCLXVI',(1e3,500,100,50,10,5,1)))[x]for x in s]
        return int(sum((x,-x)[x<y]for x,y in zip(X,X[1:]))+X[-1])

    @staticmethod
    def to_roman(i,o= ' I II III IV V VI VII VIII IX' .split(' ')):
        r=lambda n:o[n]if n<10 else''.join(dict(zip('IVXLC' , 'XLCDM'))[c]for c in r(n//10))+o[n%10]
        return r( i )

#from_roman('MIV')

#to_roman(890)
P=RomanNumerals()
P.to_roman(890)
P.from_roman('MIV')
# que es lamda es para definir funciones sensillas a una variable 

#filter sirve para firltrar listas o lista en objetos, creando una nueva lista con los elementos filtrados, primero se crea un funcion con una condicion
#luego se le pasa la lista y la funcion lista(filter (funcionconcondicion,numeros)

#map seria muy parecido a filter pero hace un funcion dentro de una lista como puede ser multiplicar los numeros, o agregar un numero o asi

#zip es una funcion en el  namespace(que no es necesario importarla) 
a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b)

print(list(c))
# [(1, 'Uno'), (2, 'Dos')]

#zip hace una lista con las dos listas entrantes separando los elementos en tuplas segun en el orden que tenga primer elemento con el primer elemento
#en tupla y el segundo elemento con el semgundo elemento de la otras lista y asi con todos

numeros = [1, 2, 3, 4, 5]
espanol = ["Uno", "Dos"]

for n, e in zip(numeros, espanol):
    print(n, e)

# 1 Uno
# 2 Dos

zip()
''' con un argumento
Como cabría esperar, dado que zip está definido para un número arbitrario de parámetros de entrada, es posible también posible usar un único valor. El resultado son tuplas de un elemento.
'''
numeros = [1, 2, 3, 4, 5]
zz = zip(numeros)
print(list(zz))

# [(1,), (2,), (3,), (4,), (5,)]

zip()
'''con diccionarios
Hasta ahora nos hemos limitado a usar zip con listas, pero la función está definida para cualquier clase iterable. Por lo tanto podemos usarla también con diccionarios.

Si realizamos lo siguiente, a,b toman los valores de las key del diccionario. Tal vez algo no demasiado interesante.
'''
esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}

for a, b in zip(esp, eng):
    print(a, b)

# 1 1
# 2 2
# 3 3
#Sin embargo, si hacemos uso de la función items, podemos acceder al key y value de cada elemento.

esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}

for (k1, v1), (k2, v2) in zip(esp.items(), eng.items()):
    print(k1, v1, v2)

# 1 Uno One
# 2 Dos Two
# 3 Tres Three
'''Nótese que en este caso ambas key k1 y k2 son iguales.
Deshacer el zip()
Con un pequeño truco, es posible deshacer el zip en una sola línea de código. Supongamos que hemos usado zip para obtener c.
'''
a = [1, 2, 3]
b = ["One", "Two", "Three"]
c = zip(a, b)

print(list(c))
# [(1, 'One'), (2, 'Two'), (3, 'Three')]
#¿Es posible obtener a y b desde c? Sí, tan sencillo como:

c = [(1, 'One'), (2, 'Two'), (3, 'Three')]
a, b = zip(*c)

print(a)  # (1, 2, 3)
print(b)  # ('One', 'Two', 'Three')
#Nótese el uso de *c, lo que es conocido como unpacking en Python.
#dict crea un diccionario

''' c=zip('MDCLXVI',(1e3,500,100,50,10,5,1))
list(c)
s = 'IV'
X=[dict(zip('MDCLXVI',(1e3,500,100,50,10,5,1)))[x]for x in s] #hace un diccionario donde la clave son los numeros romanos y los valores los valores 
#en numeros normal, luego con el for lo que hace es iteral cada elemento del numero en romano que se le pone y cuentra el valor en el diccionario
#X #es  [1, 5] # si s es s = 'IV'
#dict(zip('MDCLXVI',(1e3,500,100,50,10,5,1)))  = {'M': 1000.0, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}'''

'''Z=[dict(zip('MDCLXVI',(1e3,500,100,50,10,5,1)))['V']]#owww estraño si una lista con el valor si le pasas la calve al final resiltado [5]
Z # respuesta [5]
r=lambda n:o[n]if n<10 else''.join(dict(zip('IVXLC' , 'XLCDM'))[c]for c in r(n//10))+o[n%10]
list(r)
 '''
#p =lambda n:n*2
#print(p(10))

#def to_roman(i,o= ' I II III IV V VI VII VIII IX' .split(' ')):
 #   print(i,o)
#to_roman(8) #respuesta 8 ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
'''
def to_roman(i,o= ' I II III IV V VI VII VIII IX' .split(' ')):
    r=lambda n:o[n]if n<10 else''.join(dict(zip('IVXLC' , 'XLCDM'))[c]for c in r(n//10))+o[n%10]
    return r( i )'''
'''
frutas = ['manzana', 'banana', 'cereza']
separador = " : "
frutas_concatenadas = separador.join(frutas)

print(frutas_concatenadas)
separador.join(frutas)
#join sive para hacer una cadena de caracter apartir de otras cadenas, puede hacer union estas cadenas apartir de un separador que este caso es :
'''