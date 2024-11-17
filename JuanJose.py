# -------------------------------------
# Taller de Python: Conceptos de Listas
# Nombre: Juan Jose Rodriguez Bermudez 
# Fecha de creación: Noviembre 17, 2024
# Descripción: Este archivo contiene ejercicios prácticos para dominar el uso de listas en Python.
# -------------------------------------

# Ejercicio 1: Crear una lista con los nombres de 5 frutas colombianas favoritas y mostrarla por pantalla.
# ------------------------------------------------------------

# Creación de la lista con 5 frutas colombianas favoritas
frutas_colombianas = ["guama", "Guanábana", "Maracuyá", "mangostino", "Guayaba"]

# Imprime la lista completa de frutas
print("Lista de frutas colombianas favoritas:", frutas_colombianas)

# Ejercicio 2: Acceder al segundo y cuarto elemento de la lista anterior e imprimirlos.
# ------------------------------------------------------------

# Acceder al segundo elemento (índice 1) y cuarto elemento (índice 3)
segundo = frutas_colombianas[1]
cuarto = frutas_colombianas[3]

# Imprimir los elementos seleccionados
print("Segundo elemento:", segundo)
print("Cuarto elemento:", cuarto)

# Ejercicio 3: Crear una lista con los números del 1 al 10 y mostrar su longitud.
# ------------------------------------------------------------

# Crear la lista con números del 1 al 10
numeros = [1,2,3,4,5,6,7,8,9,10]

# Mostrar la longitud de la lista
print("Lista de números del 1 al 10:", numeros)
print("Longitud de la lista:", len(numeros))

# Ejercicio 4: Concatenar las dos listas creadas en los ejercicios 1 y 3.
# ------------------------------------------------------------

# Concatenar las dos listas
lista_concatenada = frutas_colombianas + numeros

# Imprimir la lista resultante
print("Lista concatenada:", lista_concatenada)

# Ejercicio 5: Modificar el tercer elemento de la lista del ejercicio 4 al valor 100.
# ------------------------------------------------------------

# Modificar el tercer elemento (índice 2) de la lista concatenada
lista_concatenada[2] = 777

# Imprimir la lista actualizada
print("Lista después de modificar el tercer elemento:", lista_concatenada)

# ------------------------------------------------------------
# Ejercicio 6: Borrar el último elemento de la lista del ejercicio 4.
lista_concatenada.pop()
print("Lista después de borrar el último elemento:", lista_concatenada)

# ------------------------------------------------------------

# Ejercicio 7: Crear una lista con 3 números enteros y multiplicar cada elemento por 5.
numeros_pequenos = [2, 4, 6]
multiplicados = [x * 5 for x in numeros_pequenos]
print("Lista original:", numeros_pequenos)
print("Lista multiplicada por 5:", multiplicados)

# ------------------------------------------------------------

# Ejercicio 8: Crear dos listas con 5 números enteros cada una y multiplicar los elementos correspondientes.
lista_a = [1, 2, 3, 4, 5]
lista_b = [11, 12, 13, 14, 15]
producto = [a * b for a, b in zip(lista_a, lista_b)]
print("Producto de elementos correspondientes:", producto)

# ------------------------------------------------------------

# Ejercicio 9: Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista.
listas_anidadas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
segundo_elemento = listas_anidadas[1][1]
print("Segundo elemento de la segunda lista:", segundo_elemento)

# ------------------------------------------------------------

# Ejercicio 10: Crear una lista a partir de la lista del ejercicio 3, tomando los elementos del índice 2 al 6.
sublista = numeros[2:7]
print("Sublista del índice 2 al 6:", sublista)

# ------------------------------------------------------------

# Ejercicio 11: Usar `.append()` para agregar un nuevo elemento a la lista del ejercicio 1.
frutas_colombianas.append("Papaya")
print("Lista de frutas después de agregar un elemento:", frutas_colombianas)

# ------------------------------------------------------------

# Ejercicio 12: Usar `.insert()` para agregar un nuevo elemento en la posición 2 de la lista del ejercicio 3.
numeros.insert(2, 99)
print("Lista de números después de insertar en posición 2:", numeros)

# ------------------------------------------------------------

# Ejercicio 13: Usar `.remove()` para eliminar un elemento específico de la lista del ejercicio 7.
multiplicados.remove(20)
print("Lista después de eliminar el número 20:", multiplicados)

# ------------------------------------------------------------

# Ejercicio 14: Usar `.reverse()` para invertir el orden de la lista del ejercicio 4.
lista_concatenada.reverse()
print("Lista concatenada invertida:", lista_concatenada)

# ------------------------------------------------------------

# Ejercicio 15: Usar `.sort()` para ordenar de forma ascendente la lista del ejercicio 7.
multiplicados.sort()
print("Lista ordenada de forma ascendente:", multiplicados)

# ------------------------------------------------------------

# Ejercicio 16: Usar `.pop()` para eliminar y obtener el último elemento de la lista del ejercicio 4.
ultimo_elemento = lista_concatenada.pop()
print("Último elemento eliminado:", ultimo_elemento)
print("Lista después de eliminar el último elemento:", lista_concatenada)

# ------------------------------------------------------------

# Ejercicio 17: Usar `.count()` para contar cuántas veces aparece un elemento en la lista del ejercicio 7.
veces = multiplicados.count(10)
print("El número 10 aparece:", veces, "veces en la lista.")

# ------------------------------------------------------------
# Ejercicio 18: Usar `.index()` para obtener el índice de un elemento específico en la lista del ejercicio 4.
if 777 in lista_concatenada:
    indice = lista_concatenada.index(777)
    print("Índice del elemento 777 en la lista:", indice)
else:
    print("El elemento 777 no está en la lista.")

    # ------------------------------------------------------------

# Ejercicio 19: Usar `.clear()` para eliminar todos los elementos de la lista del ejercicio 1.
frutas_colombianas.clear()
print("Lista de frutas después de usar .clear():", frutas_colombianas)

# ------------------------------------------------------------

# Ejercicio 20: Crear una lista vacía y usar un bucle `for` para agregar los números del 1 al 10.
lista_vacia = []
for i in range(1, 11):
    lista_vacia.append(i)
print("Lista con números del 1 al 10:", lista_vacia)

# ------------------------------------------------------------

# Ejercicio 21: Crear una lista de números enteros y usar un bucle `while` para eliminar los elementos impares.
numeros_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
indice = 0
while indice < len(numeros_enteros):
    if numeros_enteros[indice] % 2 != 0:
        numeros_enteros.pop(indice)
    else:
        indice += 1
print("Lista después de eliminar los números impares:", numeros_enteros)

# ------------------------------------------------------------

# Ejercicio 22: Crear una lista con los nombres de 5 materias favoritas y ordenarlas alfabéticamente.
materias_favoritas = ["Matemáticas", "Tecnologia", "ingles", "Biología", "Edu.fisica"]
materias_favoritas.sort()
print("Materias ordenadas alfabéticamente:", materias_favoritas)

# ------------------------------------------------------------

# Ejercicio 23: Crear una lista con los números del 1 al 15 y mostrar solo los múltiplos de 3.
numeros_quince = list(range(1, 16))
multiplos_tres = [x for x in numeros_quince if x % 3 == 0]
print("Múltiplos de 3:", multiplos_tres)

# ------------------------------------------------------------

# Ejercicio 24: Crear una lista con los nombres de 10 artistas favoritos y usar un bucle `for` para imprimirlos en mayúsculas.
artistas = ["Shakira", "Blesdd", "J Balvin", "Maluma", "Badbunny", "Ryan castro", "Feid", "DFZM", "Eladio", "Myke towers"]
for artista in artistas:
    print(artista.upper())

# ------------------------------------------------------------

# Ejercicio 25: Crear una lista con los números del 1 al 20 y usar una comprensión de listas para obtener solo los pares.
numeros_veinte = list(range(1, 21))
pares = [x for x in numeros_veinte if x % 2 == 0]
print("Números pares:", pares)

# ------------------------------------------------------------

# Ejercicio 26: Crear una lista con los nombres de los municipios del departamento de Arauca y usar un bucle `for` para imprimirlos en orden inverso.
municipios = ["Arauca", "Arauquita", "Saravena", "Tame", "Fortul", "Cravo Norte", "Puerto Rondón"]
for municipio in reversed(municipios):
    print(municipio)

# ------------------------------------------------------------

# Ejercicio 27: Crear una lista con los números del 1 al 12 y usar una comprensión de listas para obtener sus cuadrados.
numeros_cuadrados = [x ** 2 for x in range(1, 13)]
print("Cuadrados de los números del 1 al 12:", numeros_cuadrados)

# ------------------------------------------------------------

# Ejercicio 28: Crear una lista con los meses del año y usar `.index()` para obtener el índice del mes "Junio".

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
indice_junio = meses.index("Junio")
print("Índice del mes 'Junio':", indice_junio)

# ------------------------------------------------------------
# Ejercicio 29: Crear una lista con nombres de mascotas y usar `.remove()` para eliminar una mascota específica.
# ------------------------------------------------------------
mascotas = ["Firulais", "Luna", "Max", "Bruno", "Rocky", "Killer"]
mascotas.remove("Luna")
print("Lista después de eliminar 'Luna':", mascotas)

# ------------------------------------------------------------
# Ejercicio 30: Crear una lista con los números del 1 al 20 y usar `.sort(reverse=True)` para ordenarla en forma descendente.

numeros_descendente = list(range(1, 21))
numeros_descendente.sort(reverse=True)
print("Lista ordenada en forma descendente:", numeros_descendente)

# ------------------------------------------------------------
# Ejercicio 31: Crear una lista con nombres de 4 libros favoritos y usar `.append()` para agregar un nuevo libro.

libros_favoritos = ["Cien Años de Soledad", "Don Quijote", "El Principito", "Padre rico padre pobre"]
libros_favoritos.append("Harry potter")
print("Lista de libros después de agregar uno:", libros_favoritos)

# ------------------------------------------------------------
# Ejercicio 32: Crear una lista con los números del 1 al 15 y usar una comprensión de listas para obtener los impares.

numeros_impares = [x for x in range(1, 16) if x % 2 != 0]
print("Números impares del 1 al 15:", numeros_impares)

# ------------------------------------------------------------
# Ejercicio 33: Crear una lista con nombres de 7 comidas favoritas y usar `.insert()` para agregar una nueva comida en la posición 3.

comidas_favoritas = ["Pizza", "Hamburguesa", "Tacos", "Asado", "Ceviche", "Arepa", "Arroz con pollo"]
comidas_favoritas.insert(3, "Salchipapa")
print("Lista después de insertar 'salchipapa':", comidas_favoritas)

# ------------------------------------------------------------
# Ejercicio 34: Crear una lista con los números del 1 al 10 y usar `.extend()` para agregar números del 11 al 15.

numeros_base = list(range(1, 11))
numeros_base.extend(range(11, 16))
print("Lista extendida con números del 11 al 15:", numeros_base)

# ------------------------------------------------------------
# Ejercicio 35: Crear una lista con nombres de 6 compañeros y usar `.count()` para contar un nombre específico.

companeros = ["Juan", "Luis", "Daniel", "Juan", "Sebastian", "Valentina"]
veces_juan = companeros.count("Juan")
print("El nombre 'Juan' aparece:", veces_juan, "veces.")

# ------------------------------------------------------------
# Ejercicio 36: Crear una lista con los números del 1 al 12 y usar una comprensión para obtener números divisibles por 3.

divisibles_por_tres = [x for x in range(1, 13) if x % 3 == 0]
print("Números divisibles por 3 del 1 al 12:", divisibles_por_tres)

# ------------------------------------------------------------
# Ejercicio 37: Crear una lista con 5 artistas musicales favoritos y usar `.reverse()` para invertir el orden.

artistas_favoritos = ["Blessd", "Ryan", "Badbunny", "Karol G", "J Balvin"]
artistas_favoritos.reverse()
print("Lista de artistas en orden inverso:", artistas_favoritos)

# ------------------------------------------------------------
# Ejercicio 38: Crear una lista con números del 1 al 20 y usar una función lambda para ordenarla en forma descendente.

numeros_lambda = list(range(1, 21))
numeros_lambda.sort(key=lambda x: -x)
print("Lista ordenada en forma descendente usando lambda:", numeros_lambda)

# ------------------------------------------------------------
# Ejercicio 39: Crear una lista con materias de la universidad y usar `.pop()` para eliminar y obtener el último elemento.

materias_uni = ["Estadistica", "Bases de datos", "Programación", "Formulacion de proyectos", "Gestion de proyectos"]
ultima_materia = materias_uni.pop()
print("Última materia eliminada:", ultima_materia)
print("Lista después de eliminar la última materia:", materias_uni)

# ------------------------------------------------------------
# Ejercicio 40: Crear una lista con números del 1 al 25 y usar una comprensión para obtener los múltiplos de 5.

multiplos_de_cinco = [x for x in range(1, 26) if x % 5 == 0]
print("Múltiplos de 5 del 1 al 25:", multiplos_de_cinco)

# ------------------------------------------------------------
# Ejercicio 41: Crear una lista con 8 deportes y usar una función lambda para ordenarlos alfabéticamente.

deportes = ["Fútbol", "Baloncesto", "Tenis", "Natación", "Ciclismo", "Atletismo", "Voleibol", "Rugby"]
deportes.sort(key=lambda x: x)
print("Deportes ordenados alfabéticamente:", deportes)

# ------------------------------------------------------------
# Ejercicio 42: Crear una lista con los números del 1 al 15 y usar `.clear()` para eliminar todos los elementos.

numeros_a_borrar = list(range(1, 16))
numeros_a_borrar.clear()
print("Lista después de usar .clear():", numeros_a_borrar)

# ------------------------------------------------------------
# Ejercicio 43: Crear una lista con nombres de 6 países y usar un bucle `for` para imprimirlos en minúsculas.

paises = ["Colombia", "Brasil", "Argentina", "Ecuador", "México", "EEUU"]
for pais in paises:
    print(pais.lower())

# ------------------------------------------------------------
# Ejercicio 44: Crear una lista con números del 1 al 20 y usar una comprensión para obtener los cuadrados de los pares.

cuadrados_pares = [x ** 2 for x in range(1, 21) if x % 2 == 0]
print("Cuadrados de números pares del 1 al 20:", cuadrados_pares)

# ------------------------------------------------------------
# Ejercicio 45: Crear una lista con 10 videojuegos y usar `.index()` para obtener el índice de un juego específico.

videojuegos = ["Minecraft", "FIFA", "Call of Duty", "Zelda", "Mario Kart", "Among Us", "Fortnite", "Clah royale", "Tetris", "Pac-Man"]
indice_juego = videojuegos.index("FIFA")
print("Índice del videojuego 'FIFA':", indice_juego)

# ------------------------------------------------------------
# Ejercicio 46: Crear una lista con números del 1 al 12 y usar `.remove()` para eliminar un número específico.

numeros_para_remover = list(range(1, 13))
numeros_para_remover.remove(7)
print("Lista después de eliminar el número 7:", numeros_para_remover)

# ------------------------------------------------------------
# Ejercicio 47: Crear una lista con nombres de 7 monumentos colombianos y ordenarlos por longitud con lambda.

monumentos = ["Cristo Rey", "La Popa", "La Catedral de Sal", "Santuario de Las Lajas", "Parque Tayrona", "Caño Cristales", "Ciudad Perdida"]
monumentos.sort(key=lambda x: len(x))
print("Monumentos ordenados por longitud de nombre:", monumentos)

# ------------------------------------------------------------
# Ejercicio 48: Crear una lista con números del 1 al 18 y usar una comprensión para obtener múltiplos de 3 y 5.

multiplos_tres_cinco = [x for x in range(1, 19) if x % 3 == 0 and x % 5 == 0]
print("Múltiplos de 3 y 5:", multiplos_tres_cinco)

# ------------------------------------------------------------
# Ejercicio 49: Crear una lista con 6 asignaturas interesantes y usar `.append()` para agregar otra asignatura.

asignaturas = ["Programación", "IA", "Estadistica", "Redes", "Física", "Lectura critica"]
asignaturas.append("Big Data")
print("Lista de asignaturas después de agregar una:", asignaturas)

# ------------------------------------------------------------
# Ejercicio 50: Crear una lista con números del 1 al 25 y usar `.pop()` para eliminar el elemento en la posición 7.

numeros_finales = list(range(1, 26))
eliminado = numeros_finales.pop(7)
print("Elemento eliminado de la posición 7:", eliminado)
print("Lista después de eliminar el elemento:", numeros_finales)
# ------------------------------------------------------------

