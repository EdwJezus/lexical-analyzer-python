import re

# * PALAVRAS RESERVADAS: int, double, char, float, if, while, for.
# * IDENTIFICADORES: sempre começam com letras maiúsculas e só podem ser letras.
# * NÚMEROS FLUTUANTES: formados por vírgula e não ponto (estamos no Brasil).
# * COMENTARIOS: os mesmos do bash (#).

########################

i = 1
tabela = []
tokens = []
corta_comentario = []
partes = []
texto = '''int ab Ab AB Abbb AbbbB\n 
           43 12,45  # ##comment Pa Ab\n
           Cb TV float while 97'''

linhas = texto.splitlines()

for l in linhas:
    corta_comentario.append(l.split("#")[0])

for c in corta_comentario:
    partes.append(c.split())

for parte in partes:
    for p in parte:
        print(p) #debug

def Processador(p, tipo):
        global i
        if not any(p == e[1] for e in tabela):
            tabela.append((i, p, tipo))
            tokens.append((tipo, i))
            i += 1 
        else:
            print(f"{p} Já existe!") #debug

print("\n--------------- \n")

########################

for parte in partes:
    for p in parte:
        #################################### RESERVADA
        if re.match(r"^(int|double|char|float|if|while|for)$", p):
            print(f"É Palavra reservada: {p}") #debug
            Processador(p, "reservada")
        #################################### IDENTIFICADOR
        elif re.match(r"^([A-Z]+[a-z]*)+$", p):
            print(f"É Identificador: {p}") #debug
            Processador(p, "identificador")
        #################################### FLOAT
        elif re.match(r"(^[0-9]+,[0-9]+$)", p):
            print(f"É Numero Flutuante: {p}") #debug
            Processador(p, "float_number")
        #################################### INT
        elif re.match(r"(^[0-9]+$)", p):
            print(f"É Numero Inteiro: {p}") #debug
            Processador(p, "int_number")

#########################

print("\n=============================")
print("ENTRADA  |  VALOR  |  TIPO")
for t in tabela:
    print(f"{t}")
print("=============================\n")

#########################

print(tokens)