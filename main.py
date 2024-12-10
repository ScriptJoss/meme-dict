meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta comun a algo gracioso",
    "XD": "Reirse de algo, como un Jajajaj",
    "CREEPY": "Algo realmente aterrador o siniestro"
}

word = input("Escribe una palabra que no entiendas").upper(  )

if word in meme_dict.keys():
    print("Lo que significa es: ", meme_dict[word])
else:
    print("La palabra que pusiste no existe, prueba con otra por favor.")
