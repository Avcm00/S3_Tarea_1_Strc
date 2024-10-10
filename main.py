#1. Imprime "Hola Mundo"
print("Hola Mundo")

#2. Crea una variable llamada nombre y asigna tu nombre como su valor. Luego imprime nombre.
nombre = input("Ingrese su nombre ")
print(f'su nombre es {nombre}')

#3. Realiza una operación que sume dos números y almacena el resultado en una variable. Imprime el resultado.
num1= int(input("ingrese un numero "))
num2= int(input("ingrese otro numero "))
print(f'la suma de  ambos numeros es {num1+num2}')

#4. Utiliza un if para verificar si un número es positivo, negativo o cero e imprime el resultado
numero = int(input('Igrese un numero'))
print('el valor es mayor a cero') if numero >= 1 else print('el numero es negativo') if numero <= -1 else print('el numero es cero')

#5. Crea una variable para cada tipo de dato básico en Python: int, float, str, y bool.
#Imprime el tipo de cada variable.
var_int = 8
var_float = 1.2
var_str = 'hola'
var_bool = True

#6. Escribir un programa que pregunte al usuario su edad y muestre por pantalla
#todos los años que ha cumplido (desde 1 hasta su edad).
edad = int(input('ingrese su edad '))

for i in range(edad):
    print(i+1)

#7. Convierte un ‘float’ a ‘int’ y viceversa. Imprime ambos valores.
print(f'el valor float {var_float} cambia a {int(var_float)}')
print(f'el valor float {var_int} cambia a {float(var_int)} ')

#8. Concatena dos strings utilizando el operador ‘+’ y luego utilizando la función format.
cadena_1 = input('Ingrese una cadena ')
cadena_2 = input('Ingrese otra cadena ')

concatenar = cadena_1 +' '+ cadena_2
print(concatenar)
print('{} {}'.format(cadena_1,cadena_2))

#9. Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario 
# por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada 
# en la variable sin tener en cuenta mayúsculas y minúsculas.
contrasenia = 'Esta es la contrasenia'

ver_contrasenia = input("ingrese la contrasenia ")

print("la contrasenia es la correcta") if ver_contrasenia == contrasenia else print('la contrasenia ingresada es incorrecta')

#10. Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o
#  superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y
#  muestre por pantalla si el usuario tiene que tributar o no.
edad_ = int(input('ingrese su edad '))
ingresos_mes = int(input('ingrese sus ingresos al mes '))

print("usted cumple con los requisitos para tributar") if edad_> 16 and ingresos_mes > 1000 else print('usted no tiene que atribuir, aun')

#11. Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
#  quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar
#  al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis,
#  si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad_cliente = int(input('ingrese su edad '))

print('su entrada es gratis') if edad_cliente < 4 else print('debe pagar 10€ ') if edad_cliente > 18 else print('debe pagar 5€')

#12. Verifica si un valor está presente en una lista usando ‘in’.
lista = [1,2,3,4,5,6,7,8,9]
numero_ = 10

if numero_ in lista:
    print(f'el numero {numero_} esta en la lista')
else:
    print(f'el numero {numero_} no esta en la lista')

#13. Crea una lista con al menos 5 elementos y luego imprime toda la lista.

for elementos in lista:
    print(elementos)

#14. Accede al primer y último elemento de una lista.

primer_ele = lista[0]

ultimo_ele = lista[len(lista)-1]

print(f'el primer elemento de la lista es {primer_ele} y el ultimo es {ultimo_ele}')

#15. Añade un elemento al final de la lista y otro en una posición específica.

def agregar(lista, posicion, ele):
    lista.insert(posicion, ele)
    return lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.append(12)  
x = agregar(lista, 2, 22)  
print(x)

#16. Elimina un elemento de la lista por su valor y otro por su índice.


def eliminarPorEle(lista, ele):
    if ele in lista:
        lista.remove(ele)
    return lista

def eliminarPorInd(lista, i):
    if 0 <= i < len(lista):  
        del lista[i]
    return lista

x = eliminarPorEle(lista, 9)
y = eliminarPorInd(lista, 0)

print(x)  
print(y)  

#17. Usa list comprehension para crear una lista de los cuadrados de los números del 1 al 10.

numeros_al_cuadrado = [i**2 for i in range(1,11)]
print(numeros_al_cuadrado)

#18. Crea una lista de los números impares de una lista existente de números del 1 al 20.


numeroHastaEl20 = [i for i in range(1, 21)]

lista_de_impares = [element for element in numeroHastaEl20 if element % 2 != 0]

print(lista_de_impares) 

#19. Usa list comprehension para convertir una lista de temperaturas en Celsius a Fahrenheit.

lista_temperaturasCelcius = [32,28,29,30.3,26,25]

lista_temperaturasFahrenheit = [element *1.8 +32 for element in lista_temperaturasCelcius ]

print(lista_temperaturasFahrenheit)

#20. Filtra todos los números mayores a 10 en una lista usando list comprehension

nueva_listanum = [element for element in numeroHastaEl20 if element > 10]

print (nueva_listanum)
#21. Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

res_usuario = input('Ingrese una divisa ')

print(f'ha selecionado la divisa {res_usuario}') if diccionario.get(res_usuario) else print(f'la divisa {res_usuario} no esta en el diccionario')
#22. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
#  pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
#  Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

diccionario_frutas = {'Papaya': 2.75 ,'Manzana':4.25,'Pera':3.30,'Sandia': 0.90,'Uvas':4.0,'Granadillas':6.0}

fruta = input('Ingrese el nombre de la fruta que esta buscando ')
kilos = float(input('Ingrese la cnatidad en kilos que va ha llevar '))
resultado = float
print(f'el costo de {kilos} de {fruta} es de {diccionario_frutas[fruta] * kilos }') if fruta in diccionario_frutas else print(f'La fruta {fruta} no se encuentra en el diccionario')

#23. Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar 
# el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe
#  mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

def diccionario_articulos():
    cesta_compra = {}
    agregarmas = True
    total = 0
    while agregarmas :
        articulo = input('Agrege un el nombre de un articulo ')
        precio = int(input('Agrege el precio de el articulo '))
        cesta_compra[articulo]=precio
        agregaotro = (input('agregar otros productos (si/no) '))
        agregarmas = agregaotro=='si'

    print('LISTA DE PRODUCTOS:')
    for articulo,precio in cesta_compra.items():
        print(f'{articulo } : {precio}')
        total += precio

    print(f'el precio total es {total}')


diccionario_articulos()



      