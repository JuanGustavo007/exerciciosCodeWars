
def split_pairs(s):
    pares = []
    for i in range(0, len(s), 2):
        par = s[i:i+2]
        if len(par) == 1:
            par += '_'
        pares.append(par)
    return pares


print(split_pairs('abcdef'))  # ['ab', 'cd', 'ef']
