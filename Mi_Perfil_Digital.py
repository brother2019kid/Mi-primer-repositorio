#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Nicolás Enrique Prada Villareal"
edad = 14
estatura = 1.80
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("cuenta de Github:" "brother2019kid", " cuenta de instagram:" "sukuna_heian8")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "Jane!", "artista": "The Long Faces", "duracion": "3:06"},
{"titulo": "Dazzle", "artista": "Cheetah Mobile", "duracion": "1:31"},
{"titulo": "washing machine heart", "artista": "Mitski", "duracion": "2:08"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")
