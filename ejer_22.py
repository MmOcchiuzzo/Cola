# Ejercicio 22

cola_personajes = [
    ("Tony Stark", "Iron Man", "M"),
    ("Steve Rogers", "Capitán América", "M"),
    ("Natasha Romanoff", "Black Widow", "F"),
    ("Carol Danvers", "Capitana Marvel", "F"),
    ("Scott Lang", "Ant-Man", "M")
]

#a) Determinar el nombre del personaje de la superhéroe Capitana Marvel
for personaje in cola_personajes:
    if personaje[1] == "Capitana Marvel":
        nombre_personaje = personaje[0]
        break
else:
    nombre_personaje = "No se encontró el personaje de Capitana Marvel"

print("a) Nombre del personaje de la superhéroe Capitana Marvel:", nombre_personaje)

#b) Mostrar los nombres de los superhéroes femeninos
superheroes_femeninos = [personaje[1] for personaje in cola_personajes if personaje[2] == "F"]
print("b) Nombres de los superhéroes femeninos:", superheroes_femeninos)

#c) Mostrar los nombres de los personajes masculinos
personajes_masculinos = [personaje[0] for personaje in cola_personajes if personaje[2] == "M"]
print("c) Nombres de los personajes masculinos:", personajes_masculinos)

#d) Determinar el nombre del superhéroe del personaje Scott Lang
for personaje in cola_personajes:
    if personaje[0] == "Scott Lang":
        nombre_superheroe = personaje[1]
        break
else:
    nombre_superheroe = "No se encontró el superhéroe del personaje Scott Lang"

print("d) Nombre del superhéroe del personaje Scott Lang:", nombre_superheroe)

#e) Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S
personajes_con_S = [personaje for personaje in cola_personajes if personaje[0][0] == "S"]
print("e) Datos de los superhéroes o personajes cuyos nombres comienzan con la letra S:")
for personaje in personajes_con_S:
    print("   - Nombre del personaje:", personaje[0])
    print("     Nombre del superhéroe:", personaje[1])
    print("     Género:", personaje[2])

#f) Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe
for personaje in cola_personajes:
    if personaje[0] == "Carol Danvers":
        nombre_superheroe_carol = personaje[1]
        break
else:
    nombre_superheroe_carol = "No se encontró el personaje Carol Danvers"

print("f) Carol Danvers se encuentra en la cola. Nombre de su superhéroe:", nombre_superheroe_carol)
