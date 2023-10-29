import random

cordas = ['mizão', 'la', 're', 'sol', 'si', 'miziha']
notas_sus = ['do', 'do#', 're', 're#', 'mi', 'fa', 'fa#', 'sol', 'sol#', 'la', 'la#', 'si']
notas_mol = ['do', 're b', 're', 'mi b', 'mi', 'fa', 'sol b', 'sol', 'la b', 'la', 'si b', 'si']
perguntas = ["posição de cordas", "posição de notas"]
numero_pergunta = 0
def formar_pergunta():

    global numero_pergunta
    numero_pergunta += 1
    x = 0
    e_pergunta = random.choice(perguntas)

    # posição das cordas
    if (e_pergunta == perguntas[0]):
        e_pergunta = f'{numero_pergunta} {e_pergunta}'
        corda_s = random.choice(cordas)
        if corda_s == cordas[0]:
            corpo_pergunta = f"{numero_pergunta} qual corda vem abaixo da {corda_s}"
            resposta_certa = 'la'
        elif corda_s == cordas[5]:
            corpo_pergunta = f"qual corda vem acima da {corda_s}"
            resposta_certa = 'si'
        else:
            op_enum = [f'qual corda vem abaixo da {corda_s}: ', f'qual corda vem acima da {corda_s}: ']
            enum = random.choice(op_enum)
            corpo_pergunta = enum
            if enum == f'qual corda vem abaixo da {corda_s}: ':
                for indice in range(len(cordas)):
                    if cordas[indice] == corda_s:
                        resposta_certa = cordas[indice + 1]
            else:
                for indice in range(len(cordas)):
                    if cordas[indice] == corda_s:
                        resposta_certa = cordas[indice - 1]

        alternativas = criador_alternativas(resposta_certa, cordas)

        return [e_pergunta, corpo_pergunta, resposta_certa, alternativas]

    # posição das notas
    elif e_pergunta == perguntas[1]:
        e_pergunta = f'{numero_pergunta} {e_pergunta}'
        qual_tipo = [notas_mol, notas_sus]
        notas = random.choice(qual_tipo)
        nota_s = random.choice(notas)

        if nota_s == notas[0]:
            anterior = [1, len(notas) - 1]
            resposta_certa = notas[random.choice(anterior)]
            if resposta_certa == notas[1]:
                corpo_pergunta = f"qual nota vem depois da {nota_s}"
            else:
                corpo_pergunta = f"qual nota vem antes da {nota_s}"

        elif nota_s == notas[len(notas) - 1]:
            anterior = [0, -2]
            resposta_certa = notas[random.choice(anterior)]
            if resposta_certa == notas[0]:
                corpo_pergunta = f"qual nota vem depois da {nota_s}"
            else:
                corpo_pergunta = f"qual nota vem antes da {nota_s}"
        else:
            op_enum = [f'qual nota vem antes da {nota_s}: ', f'qual nota vem depois da {nota_s}: ']
            enum = random.choice(op_enum)
            corpo_pergunta = enum
            if enum == f'qual corda vem antes da {nota_s}: ':
                for indice in range(len(notas)):
                    if notas[indice] == nota_s:
                        resposta_certa = notas[indice - 1]
            else:
                for indice in range(len(notas)):
                    if notas[indice] == nota_s:
                        resposta_certa = notas[indice + 1]

        alternativas = criador_alternativas(resposta_certa, notas)

        return [e_pergunta, corpo_pergunta, resposta_certa, alternativas]


def criador_alternativas(resposta_certa, array):
    alternativas = []
    x = 0
    while x <= 3:
        alternativa_s = random.choice(array)
        if alternativa_s != resposta_certa:
            unica = True
            if alternativas == []:
                alternativas.append(alternativa_s)
                x += 1
            else:
                for indice in range(len(alternativas)):
                    if alternativas[indice] == alternativa_s:
                        unica = False
                if unica:
                    alternativas.append(alternativa_s)
                    x += 1

    opçoes = [f'1 ({alternativas[0]}) | 2 ({alternativas[1]}) | 3 ({alternativas[2]}) | 4 ({alternativas[3]}) | 5 (nenhuma das anteriores) : ',
    f'1 ({resposta_certa}) | 2 ({alternativas[1]}) | 3 ({alternativas[2]}) | 4 ({alternativas[3]}) | 5 (nenhuma das anteriores) : ',
    f'1 ({alternativas[0]}) | 2 ({resposta_certa}) | 3 ({alternativas[2]}) | 4 ({alternativas[3]}) | 5 (nenhuma das anteriores) : ',
    f'1 ({alternativas[0]}) | 2 ({alternativas[1]}) | 3 ({resposta_certa}) | 4 ({alternativas[3]}) | 5 (nenhuma das anteriores) : ',
    f'1 ({alternativas[0]}) | 2 ({alternativas[1]}) | 3 ({alternativas[2]}) | 4 ({resposta_certa}) | 5 (nenhuma das anteriores) : ']
    opção_s = random.choice(opçoes)

    return alternativas
