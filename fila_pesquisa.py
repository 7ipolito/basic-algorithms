from collections import deque

# Grafo representando conexões entre pessoas
grafo = {
    "allan": ["bob", "claire", "alice"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "alice": ["peggy"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'


def pesquisa(nome):
    fila_de_pesquisa= deque()
    fila_de_pesquisa += grafo[nome]
    verificadas =[]

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if pessoa not in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(f"{pessoa} é um vendedor de mangas")
                return True
            else:
                fila_de_pesquisa += grafo(pessoa)
                verificadas.append(pessoa)
    print("Nenhum vendedor de mangas foi encontrado!")
    return False

pesquisa("allan")