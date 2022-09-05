
def notas(*num, sit=False):
    '''
    -> Função para analisar e informar a situação de vários alunos
    :param num: Nota do aluno (Aceita várias)
    :param sit: Valor opcional, adiciona ou não a situação do aluno
    :return: Dicionário com informações com base nas notas passada: maior nota, menor, média e situação da turma.
    '''
    results = {}
    results["Total"] = len(num)
    results["Maior"] = max(num)
    results["Menor"] = min(num)
    results["Média"] = sum(num)/len(num)
    if sit != False:
        if results["Média"] >= 7:
            results["situação"] = "Boa"
        elif results["Média"] >= 5:
            results["situação"] = "Razoável"
        elif results["Média"] < 5:
            results["situação"] = "Ruim"
        else:
            print('Parece que algo não ocorreu bem, tente novamente!')
    return results


resultados = notas(6.7, 5.5, 5.3, 2.5, sit=False)
print(resultados)

