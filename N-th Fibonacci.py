def fibonacci(n):
    a, b = 0, 1
    valores = []
    valores2 = []
    for _ in range(n):
        valores.append(a)
        # print(a, end=' ')
        a, b = b, a + b

    i = 0

    while i <= len(valores)  :
        print(i)
        if i == len(valores):
            valores2.append(valores[i -1])
        i  =  i + 1
        # print(variavel)

    # return valores[-2]
    print(valores2)
    return f"nth_fib({n}) = {valores2[0]}"

# Exemplo: exibe os 10 primeiros termos
print(fibonacci(2))


# Exemplo: exibe os 10 primeiros termos