import re

######################## Instruções

# * PALAVRAS RESERVADAS: int, double, char, float, if, while, for.
# * IDENTIFICADORES: sempre começam com letras maiúsculas e só podem ser letras.
# * NÚMEROS FLUTUANTES: formados por vírgula e não ponto (estamos no Brasil).
# * COMENTARIOS: os mesmos do bash (#).

######################## Variaveis

i = 1
texto = ""
corta_comentario = []
corta_simbolo = []
partes = []
tabela = []
tokens = []

######################## Função Captador

def Captador():
    global texto
    print("Digite o código a ser analisado: (CRTL+Z para finalizar)")
    while True:
        try:
            linha = input()
            texto += linha + "\n"
        except EOFError:
            break

######################## Função Fragmentador

def Fragmentador():
    linhas = texto.splitlines() #divide linha
    for l in linhas:
        corta_comentario.append(l.split("#")[0]) #corta comentarios
    for c in corta_comentario:
        corta_simbolo.append(re.sub(r"([;=()<>])", r" \1 ", c)) #corta simbolos
    for s in corta_simbolo:
        partes.append(s.split()) #corta palavras

######################## Função Processador

def Processador(p, tipo):
        global i
        if not any(p == e[1] for e in tabela):
            tabela.append((i, p, tipo))
            tokens.append((tipo, i))
            i += 1 

######################## Função Comparador

def Comparador():
    for parte in partes:
        for p in parte:
            #################################### RESERVADA
            if re.match(r"^(int|double|char|float|if|while|for)$", p):
                Processador(p, "reservada")
            #################################### IDENTIFICADOR
            elif re.match(r"^[A-Z][a-zA-Z]*$", p):
                Processador(p, "identificador")
            #################################### FLOAT
            elif re.match(r"(^[0-9]+,[0-9]+$)", p):
                Processador(p, "float_number")
            #################################### INT
            elif re.match(r"(^[0-9]+$)", p):
                Processador(p, "int_number")

######################## Função Impressor

def Impressor():
    print("\n=============================")
    print("ENTRADA  |  VALOR  |  TIPO")
    for t in tabela:
        print(f"{t}")
    print("=============================\n")

    print(tokens)

######################### Função Main

def main():
    Captador()
    Fragmentador()
    Comparador()
    Impressor()

######################### Saída

main()