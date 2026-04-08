import re

# * PALAVRAS RESERVADAS: int, double, char, float, if, while, for.
# * IDENTIFICADORES: sempre começam com letras maiúsculas e só podem ser letras.
# * NÚMEROS FLUTUANTES: formados por vírgula e não ponto (estamos no Brasil).
# * COMENTARIOS: os mesmos do bash (#).

######################## Variaveis

i = 1
tabela = []
tokens = []
corta_comentario = []
corta_simbolo = []
partes = []
texto = '''int Ab;\n
            # int Xb poderia\n 
            doble teste\n
            float Exemplo # sera minha variavel de exemplo\n
            # double Exemplo2 seria melhor?\n
            Exemplo = 3456,567\n
            while (Ab < 500)'''

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

######################### Função Main

def main():
    Fragmentador()
    Comparador()

    print("\n=============================")
    print("ENTRADA  |  VALOR  |  TIPO")
    for t in tabela:
        print(f"{t}")
    print("=============================\n")

    print(tokens)

######################### Saída

main()