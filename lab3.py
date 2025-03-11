# Funcion para hacer las combinaciones
def combinacionLetras(digitos):
    if not digitos:
        return []

    letrasNumeros = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    resultado = []

    def backtrack(indice, combinacion):
        if indice == len(digitos):
            resultado.append(combinacion)
            return

        current_digit = digitos[indice]
        for letra in letrasNumeros[current_digit]:
            backtrack(indice + 1, combinacion + letra)

    backtrack(0, "")
    return resultado

# Punto de entrada del script
if __name__ == "__main__":
    digitos = "23"  # Digitos de prueba de acuerdo a lo pedido
    combinaciones = combinacionLetras(digitos)
    print("Combinaciones:", combinaciones)