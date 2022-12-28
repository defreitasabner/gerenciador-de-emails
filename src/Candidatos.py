from typing import List, Dict, Union

from Candidato import Candidato

from constantes import COLUNAS_ESPERADAS_PLANILHA_PS

class Candidatos:

    def __init__(self, dados_planilha_ps: List[Dict[str,str]]) -> None:
        """
        Classe responsável por conter e administrar todos os candidatos participantes do processo seletivo.
        """
        self.__lista_candidatos: List[Candidato] = []
        self.__adicionar_candidatos(dados_planilha_ps)

    """
    Métodos Getters e Setters
    ===
    Os métodos abaixo servem apenas para acessarmos (getters) e alterarmos (setters) os valores dos atributos privados da classe.
    """

    @property
    def lista_candidatos(self) -> List[Candidato]:
        return self.__lista_candidatos

    def __adicionar_candidato(self, novo_candidato: Dict[str,str]) -> None:
        """
        Método privado que recebe um dicionário (`Dict[str,str]`) e adiciona um objeto `Candidato` ao atributo privado `__lista_candidatos`.
        """
        # verifica se o dicionário possui as chaves iguais aos campos esperados pela Planilha de PS
        if list(novo_candidato.keys()) == COLUNAS_ESPERADAS_PLANILHA_PS:
            self.__lista_candidatos.append(
                Candidato(
                    id = novo_candidato['id'],
                    nome = novo_candidato['nome'],
                    email = novo_candidato['email'],
                    formulario = novo_candidato['formulario'],
                    dinamica = novo_candidato['dinamica'],
                    entrevista = novo_candidato['entrevista'],
                    capacitacao = novo_candidato['capacitacao'],
                    trainee = novo_candidato['trainee']
                )
            )
        
        else:
            # Retorna um erro caso o campo do dicionário não correspondam as colunas esperadas numa Planilha de PS
            raise Exception('Ocorreu um erro adicionando o novo candidato...')

    def __adicionar_candidatos(self, dados_planilha_ps: List[Dict[str,str]]) -> None:
        """
        Método privado responsável por receber os dados de um objeto `Planilha` de PS (`List[Dict[str,str]]`), transformar cada dado de candidato num objeto `Candidato` e adicionar numa lista de um grande objeto `Candidatos`.
        """
        for dado in dados_planilha_ps:
            self.__adicionar_candidato(dado)
