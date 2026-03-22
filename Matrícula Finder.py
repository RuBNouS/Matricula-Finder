import random
import string
import itertools
import sys

def gerar_matricula_aleatoria():
    formatos = [ #guarda os 4 formatos
        "{L}{L}-{N}{N}-{N}{N}", #1937-1992
        "{N}{N}-{N}{N}-{L}{L}", #1992-2005
        "{N}{N}-{L}{L}-{N}{N}", #2005-2020
        "{L}{L}-{N}{N}-{L}{L}"  #2020-presente
    ]

    formato = random.choice(formatos) #escolhe um formato

    #gera 4 letras e 4 números
    letras = random.choices(string.ascii_uppercase, k=4)
    numeros = random.choices(string.digits, k=4)

    #subtitui o espaço da letra/número por uma letras/números que esta na lista de 4 letras e 4 números
    matricula = formato
    for l in letras:
        matricula = matricula.replace("{L}", l, 1)
    for n in numeros:
        matricula = matricula.replace("{N}", n, 1)
    return matricula #devolve a matrícula gerada

def completar_matricula_parcial():
    padrao = input("\nIntroduz a matrícula parcial (XX-XX-XX): ").upper().strip() #tudo em maiúsculas e tira espaços (o .strip)
    blocos_input = padrao.split('-') #ex: 12-__-ab -> ["12, "__", "AB"]

    if len(blocos_input) != 3 or any(len(b) != 2 for b in blocos_input):
        print("\nFormato inválido. Deves usar o formato XX-XX-XX (ex: 38-__-45).")
        return

    #os 4 formatos possíveis em Portugal
    formatos_validos = [
        ("L", "N", "N"), #AA-00-00
        ("N", "N", "L"), #00-00-AA
        ("N", "L", "N"), #00-AA-00
        ("L", "N", "L")  #AA-00-AA
    ]

    formatos_compativeis = []

    #==================== Lógica para completar a matrícula parcial ====================

    #1-descobrir se o input do utilizador usa um formato válido
    for fmt in formatos_validos:
        compativel = True
        for i in range(3):
            bloco_fmt = fmt[i]
            bloco_inp = blocos_input[i]

            if bloco_fmt == 'L' and any(c.isdigit() for c in bloco_inp):
                compativel = False
            elif bloco_fmt == 'N' and any(c.isalpha() for c in bloco_inp):
                compativel = False

        if compativel:
            formatos_compativeis.append(fmt)

    if not formatos_compativeis:
        print("\nPadrão impossível. Em Portugal não se misturam letras e números no mesmo bloco.")
        return

    todas_matriculas = []

    #2-gerar combinações válidas
    for fmt in formatos_compativeis:
        caracteres_por_posicao = []
        for i in range(3):
            bloco_fmt = fmt[i]
            bloco_inp = blocos_input[i]
            for char in bloco_inp:
                if char == '_':
                    if bloco_fmt == 'L':
                        caracteres_por_posicao.append(string.ascii_uppercase)
                    else:
                        caracteres_por_posicao.append(string.digits)
                else:
                    caracteres_por_posicao.append([char])

        #"junta" as listas que geramos
        combinacoes = itertools.product(*caracteres_por_posicao)
        for combo in combinacoes:
            mat_str = f"{combo[0]}{combo[1]}-{combo[2]}{combo[3]}-{combo[4]}{combo[5]}"
            todas_matriculas.append(mat_str)

    #3-verificar se existem duplicados
    matriculas_unicas = list(set(todas_matriculas))
    matriculas_unicas.sort() #ordenar por ordem alfabética

    #criar e escreve as matrículas possíveis
    nome_ficheiro = f"possibilidades_{padrao.replace('_', 'X')}.txt"
    with open(nome_ficheiro, 'w') as ficheiro:
        for m in matriculas_unicas:
            ficheiro.write(m + "\n")

    print(f"\nForam geradas {len(matriculas_unicas)} combinações possíveis.")
    print(f"Guardadas no ficheiro: {nome_ficheiro}")

    #===================================================================================

#menu
def como_funciona():
    print ("\n=== Como Funciona ? ===")
    print ("Opção 1: Gera uma matrícula portuguesa aleatória usando um dos 4 formatos históricos válidos.")
    print ("Opção 2: Insere uma matrícula incompleta. Ex: _1-__-BG.")
    print ("         O programa detecta os _ e os números/letras que inserir para descobrir o formato.")
    print ("         Depois, gera apenas combinações possíveis em Portugal e guarda num ficheiro.txt")
    print ("Opção 3: Mostra este texto de ajuda. (lol)")
    print ("Opção 4: Encerra o programa.")
    print ("=======================")

def menu():
    while True:
        print("\n" + "="*10 + " Matrícula Finder " + "="*10)
        print("1. Gerar matrícula aleatória")
        print("2. Completar matrícula parcial")
        print("3. Como funciona")
        print("4. Sair")
        print("="*38)
        escolha = input("Escolhe uma opção (1-4): ")
       
        if escolha == '1':
            nova_matricula = gerar_matricula_aleatoria()
            print(f"\nMatrícula Gerada: {nova_matricula}")
        elif escolha == '2':
            completar_matricula_parcial()
        elif escolha == '3':
            como_funciona()
        elif escolha == '4':
            print("\nA fechar o programa...")
            sys.exit()
        else:
            print("\nOpção inválida. Por favor, escolhe um número de 1 a 4.")

if __name__ == "__main__":
    menu()