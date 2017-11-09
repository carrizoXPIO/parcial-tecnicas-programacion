def soloTieneEspaciosEnBlanco(palabra):
    for letra in palabra:
        if letra != " ":
            return False

    return True


def ejercicio1(palabra):
    if len(palabra) == 0:
        return []

    if soloTieneEspaciosEnBlanco(palabra):
        return []

    palabrasRotadas = [palabra]

    vueltas = len(palabra)
    ultimaLetra = -1
    rotaciones = []
    for valor in range(len(palabra)):
        rotada = palabra[ultimaLetra:] + palabra[:ultimaLetra]
        rotaciones.append(rotada)
        ultimaLetra = ultimaLetra - 1
    rotaciones = rotaciones [:: -1]

    return rotaciones



assert (ejercicio1("") == [])
assert (ejercicio1("     ") == [])
assert (ejercicio1("a") == ['a'])

assert (ejercicio1("ab") == ['ab', 'ba'])


assert (ejercicio1("paz") == ['paz','azp','zpa'])
assert (ejercicio1("so l") == ['so l','o ls',' lso','lso '])
assert (ejercicio1("rotar") == ['rotar','otarr','tarro','arrot','rrota'])


