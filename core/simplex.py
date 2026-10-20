import numpy as np

def ler_entrada(nomearquivo):
    with open(nomearquivo, 'r') as f:
        linhas = [linha.strip() for linha in f if linha.strip()]
    resultado = {}
    # n é o número de variáveis e m é o número de restrições
    resultado["n"] = int(linhas[0])
    resultado["m"] = int(linhas[1])
    
    # lidando com as restrições de sinal
    temp = linhas[2].split()
    alvo = []

    for c in temp:
        alvo.append(int(c))

    resultado["sinal"] = alvo

    # função objetivo
    temp = linhas[3].split()
    alvo = []

    for c in temp:
        alvo.append(float(c))
    z = np.array(alvo, dtype=float)
    resultado["z"] = z 

    # matriz de restrições 
    m = resultado["m"]
    k = 4

    alvao = []
    b = []
    relacoes = []

    for _ in range(m):

        temp = linhas[k].split() 
        k += 1
        a = temp[:-2]
        r = temp[-2]
        bzin = float(temp[-1])
        alvo = []
        
        for c in a:
            alvo.append(float(c))
        alvao.append(alvo)
        b.append(bzin)
        relacoes.append(r)

    resultado["A"] = np.array(alvao, dtype=float)
    resultado["relacoes"] = relacoes 
    resultado["b"] = np.array(b, dtype=float)

    return resultado

x = ler_entrada("exemplo.txt")
print(x)

