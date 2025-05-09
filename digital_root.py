def digital_root(n):

    texto = str(n)
    valores = []
    valor_final = 0
    for i in texto:
        valores.append(int(i))

    for i in valores:
        valor_final = i + valor_final

    texto = str(valor_final)

    soma = 0
    for i in texto:
        soma  = int(i) + soma

    soma2 =  0
    if soma >= 10:
        soma_texto = str(soma)
        for i in soma_texto:
            soma2 = int(i) + soma2

        return soma2

    return soma

print(digital_root(74514317987550531907))