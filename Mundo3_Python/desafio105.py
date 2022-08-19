
def notas(*num, sit=False):
    '''
    -> Função para analisar e informar a situação de vários alunos
    :param num: Nota do aluno (Aceita várias)
    :param sit: Valor opcional, adiciona ou não a situação do aluno
    :return: Dicionário com informações com base nas notas passada: maior nota, menor, média e situação da turma.
    '''
    results = {}
    total = 0
    soma = 0
    for c, v in enumerate(num):
        total += 1
        soma += v
        results["total"] = total
        if c == 0 or v > results["maior"]:
            results["maior"] = v
        if c == 0 or v < results["menor"]:
            results["menor"] = v
    media = soma / total
    results["média"] = media
    if sit != False:
        if media >= 7:
            results["situação"] = "Boa"
        elif 5 <= media < 7:
            results["situação"] = "Razoável"
        elif media < 5:
            results["situação"] = "Ruim"
        else:
            print('Parece que algo não ocorreu bem, tente novamente!')
    return results


resultados = notas(6.7, 5.5, 5.3, 2.5, sit=True)
print(resultados)

