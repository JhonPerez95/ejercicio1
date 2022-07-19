# Se crea un dicionario de python con los datos del grupo de personas

grupoPersonas = {
    "carlos": {"edad": 40, "estrato": 5, "genero": "M"},
    "Jhon": {"edad": 20, "estrato": 1, "genero": "M"},
    "Juan": {"edad": 30, "estrato": 2, "genero": "M"},
    "Luis": {"edad": 25, "estrato": 2, "genero": "M"},
    "Luisa": {"edad": 25, "estrato": 2, "genero": "F"},
    "Alejandra": {"edad": 25, "estrato": 1, "genero": "F"},
    "Valeria": {"edad": 30, "estrato": 2, "genero": "F"},
    "Andrea": {"edad": 31, "estrato": 1, "genero": "F"},
}

contadorMujer = 0
contadorHombre = 0
acomuladorEdadHombre = 0
acomuladorEdadMujer = 0

for persona in grupoPersonas:
    # Para Hombres
    if grupoPersonas[persona]["genero"] == "M" and grupoPersonas[persona][
            "edad"] <= 35 and grupoPersonas[persona]["estrato"] <= 2:
        contadorHombre = contadorHombre + 1
        acomuladorEdadHombre = acomuladorEdadHombre + grupoPersonas[persona][
            "edad"] 

    # Para Mujeres
    elif grupoPersonas[persona]["genero"] == "F" and grupoPersonas[persona][
            "edad"] <= 30 and grupoPersonas[persona]["estrato"] <= 2:
        contadorMujer = contadorMujer + 1
        acomuladorEdadMujer = acomuladorEdadMujer + grupoPersonas[persona][
            "edad"]
    else:
      print('La persona '+ persona+ ' no es beneficiado')

# Cuantos hombres  son beneficiados
print('La cantidad de hombres beneficiados fue: ' + str(contadorHombre))

# Cuantas mujeres  son beneficiadas
print('La cantidad de mujeres beneficiados fue: ' + str(contadorMujer))

# Mostrar el promedio de edad de hombres beneficiados
print('Edad Promedio de hombres beneficiados fue: ' +
      str(round(acomuladorEdadHombre / contadorHombre, 1)))

# Mostrar el promedio de edad de mujeres beneficiadas
print('Edad Promedio de mujeres beneficiados fue: ' +
      str(round(acomuladorEdadMujer / contadorMujer, 1)))
