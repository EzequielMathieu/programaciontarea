# 1. Con los nombres de su familia.
familia = ["Padre", "Madre", "Hermano", "Tía"]

# 2. Con los valores de la temperatura de un mes entero (mes a elección, pero definirlo).
temperaturas = [25, 26, 28, 30, 32, 34, 33, 31, 29, 27, 26, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]

# 3. Con los nombres de ciudades que hayan visitado.
ciudades_visitadas = ["Nueva York", "París", "Tokio", "Londres", "Roma"]

# 4. Con las fechas y nombres de eventos importantes de su vida.
eventos_importantes = [
    ("2022-03-15", "Graduación universitaria"),
    ("2023-06-20", "Boda de amigo"),
    ("2024-01-05", "Viaje a Bali")
]

# 1. Ordenar alfabéticamente la lista de los nombres de familia.
familia.sort()

# 2. Ordenar ascendentemente la lista de temperaturas.
temperaturas.sort()

# 3. Agregar en la lista de temperaturas, las temperaturas de los 15 días del mes siguiente.
temperaturas_siguiente_mes = [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
temperaturas.extend(temperaturas_siguiente_mes)

# 4. Quitar de la lista de los nombres de familia, a tus abuelos.
familia.remove("Abuelo")
familia.remove("Abuela")

# 5. Quitar de la lista de ciudades la ciudad menos linda que hayas visitado.
ciudades_visitadas.remove("CiudadMenosLinda")

# 6. Mostrar todas las listas.
print("Lista de Familia:", familia)
print("Lista de Temperaturas:", temperaturas)
print("Lista de Ciudades Visitadas:", ciudades_visitadas)
print("Lista de Eventos Importantes:", eventos_importantes)

# Crear tres tuplas con datos random.
tupla1 = (1, "A", True)
tupla2 = ("apple", 3.14, False)
tupla3 = (42, "banana", True)

# Crear una lista que las contenga y mostrarla.
lista_de_tuplas = [tupla1, tupla2, tupla3]
print("Lista de Tuplas:", lista_de_tuplas)

# Crear el diccionario del núcleo familiar
familia_diccionario = {
    "11111111A": "Padre",
    "22222222B": "Madre",
    "33333333C": "Hermano",
    "44444444D": "Tía"
}

# Añadir datos de familia ampliada al diccionario
familia_diccionario.update({
    "55555555E": "Abuelo",
    "66666666F": "Abuela",
    "77777777G": "Suegra"
})

# Crear un nuevo diccionario con claves autogeneradas y valores de números de teléfono
telefonos_diccionario = {
    "11111111A": "123-456-7890",
    "22222222B": "987-654-3210",
    "33333333C": "555-555-5555",
    "44444444D": "111-222-3333",
    "55555555E": "444-444-4444",
    "66666666F": "777-777-7777",
    "77777777G": "999-999-9999"
}

# Mostrar ambos diccionarios
print("Diccionario del Núcleo Familiar:", familia_diccionario)
print("Diccionario de Teléfonos:", telefonos_diccionario)
